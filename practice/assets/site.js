// Nav toggle. Progressive enhancement only: nav links work without JS.
(function () {
  var btn = document.querySelector('.navtoggle');
  var nav = document.querySelector('.nav');
  if (!btn || !nav) return;
  btn.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
})();

// Partner logo slots degrade to their alt text when no image file is present,
// so the credibility bar always reads correctly while artwork is pending.
(function () {
  function toText(img) {
    if (!img.parentNode) return;
    var span = document.createElement('span');
    span.className = 'txt';
    span.textContent = img.alt;
    img.replaceWith(span);
  }
  document.querySelectorAll('.creds-logos img').forEach(function (img) {
    // Already finished loading and failed before this script ran.
    if (img.complete && img.naturalWidth === 0) {
      toText(img);
      return;
    }
    img.addEventListener('error', function () { toText(img); });
  });
})();
