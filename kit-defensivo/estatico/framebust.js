/**
 * Frame-busting clássico — apenas para contraste didático.
 * Não substitui X-Frame-Options / CSP frame-ancestors.
 */
(function () {
  if (window.top === window.self) {
    return;
  }
  console.log("Esta página está dentro de um frame.");
  try {
    window.top.location = window.self.location;
  } catch (err) {
    console.warn("Não foi possível redirecionar o top frame:", err);
  }
})();
