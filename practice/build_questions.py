"""Build data/questions.json from the GKV4 master workbook.

Strips ALL scoring: no point values, no answer-option weights, no section totals.
Keeps: question text, KPA, documentation requirement, answer options, Core Criteria flag.
"""
import json
import re
import openpyxl

SRC = "/mnt/project/GKV4_QA_Master_English_20260424.xlsx"

KPA = {
    "Corporate": ("CORP", "Corporate Environmental Management", False),
    "Housekeeping": ("HK", "Housekeeping", False),
    "Conference": ("CONF", "Conference & Meeting Services", True),
    "F&B": ("FB", "Food & Beverage", True),
    "Engineering": ("ENG", "Engineering & Maintenance", False),
}


def clean(v):
    if v is None:
        return ""
    s = str(v).replace("\u2013", "-").replace("\u2014", "-")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def main():
    wb = openpyxl.load_workbook(SRC, data_only=True)
    out = []
    core_total = 0

    for sheet, (code, label, optional) in KPA.items():
        ws = wb[sheet]
        current = None

        for row in ws.iter_rows(min_row=3, values_only=True):
            num = row[0]
            text = clean(row[1])
            rtype = clean(row[3]) if len(row) > 3 else ""
            docreq = clean(row[4]) if len(row) > 4 else ""

            qid = ""
            if isinstance(num, (int, float)):
                qid = str(int(num))
            elif isinstance(num, str) and re.fullmatch(r"\d+[a-z]?", num.strip(), re.I):
                qid = num.strip().lower()
            is_question = bool(qid) and bool(text)

            if is_question:
                # The badge already says Core Criteria, so a trailing
                # "(mandatory)" in the question text is duplicate noise.
                text = re.sub(r"\s*\(mandatory\)\s*$", "", text, flags=re.I).strip()
                current = {
                    "id": f"{code}-{qid}",
                    "kpa": code,
                    "kpaLabel": label,
                    "n": qid,
                    "text": text,
                    "format": rtype or "Radio",
                    "documentation": docreq.lower().startswith("y"),
                    "optionalSection": optional,
                    "core": False,
                    "options": [],
                }
                out.append(current)
                continue

            # answer option row
            if current and text and text.lower() != "none":
                mandatory = "mandator" in rtype.lower() or "mandator" in text.lower()
                label_text = re.sub(
                    r"\s*\(mandatory\)\s*", "", text, flags=re.I
                ).strip()
                if label_text:
                    current["options"].append(
                        {"label": label_text, "mandatory": mandatory}
                    )
                if mandatory:
                    if not current["core"]:
                        core_total += 1
                    current["core"] = True

    # de-duplicate identical consecutive options (workbook artifacts)
    for q in out:
        seen = set()
        uniq = []
        for o in q["options"]:
            k = o["label"].lower()
            if k not in seen:
                seen.add(k)
                uniq.append(o)
        q["options"] = uniq

    meta = {
        "version": "V4",
        "sourceFile": "GKV4_QA_Master_English_20260424.xlsx",
        "questionCount": len(out),
        "coreCount": core_total,
        "kpas": [
            {"code": c, "label": l, "optional": o, "count": sum(1 for q in out if q["kpa"] == c)}
            for c, l, o in KPA.values()
        ],
    }

    with open("data/questions.json", "w", encoding="utf-8") as f:
        json.dump({"meta": meta, "questions": out}, f, indent=1, ensure_ascii=False)

    print(json.dumps(meta, indent=2))
    print("\nsample:", json.dumps(out[0], indent=1)[:400])


if __name__ == "__main__":
    main()
