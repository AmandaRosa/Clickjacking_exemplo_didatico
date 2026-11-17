/*
 * EXEMPLO DIDÁTICO — frame-busting em JavaScript (defesa FRÁGIL).
 * Pode ser contornado (ex.: iframe com sandbox). A defesa recomendada
 * são os headers HTTP — veja headers_flask.py.
 */

if (window.top !== window.self) {
    console.log("Esta página está dentro de um frame.");
}

if (window.top !== window.self) {
    window.top.location = window.self.location;
}