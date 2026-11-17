/* Comportements du site : en-tête, apparition au défilement, copie de l'email.
   Aucune dépendance. Tout est neutralisé si le navigateur ne suit pas. */
(function () {
  "use strict";

  /* En-tête : bordure dès que la page défile */
  var header = document.querySelector(".site-header");
  if (header) {
    var stick = function () {
      header.classList.toggle("is-stuck", window.scrollY > 8);
    };
    stick();
    window.addEventListener("scroll", stick, { passive: true });
  }

  /* Apparition au défilement, une seule fois par élément */
  var cibles = document.querySelectorAll(".reveal");
  if (cibles.length) {
    var reduit = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (reduit || !("IntersectionObserver" in window)) {
      cibles.forEach(function (el) {
        el.classList.add("is-in");
      });
    } else {
      var obs = new IntersectionObserver(
        function (entrees) {
          entrees.forEach(function (e) {
            if (!e.isIntersecting) return;
            var el = e.target;
            var rang = Array.prototype.indexOf.call(el.parentNode.children, el);
            el.style.transitionDelay = Math.min(rang, 4) * 60 + "ms";
            el.classList.add("is-in");
            obs.unobserve(el);
          });
        },
        { rootMargin: "0px 0px -12% 0px", threshold: 0.08 }
      );
      cibles.forEach(function (el) {
        obs.observe(el);
      });
    }
  }

  /* Copie de l'adresse email, avec repli pour les contextes non sécurisés */
  document.querySelectorAll("[data-copy]").forEach(function (btn) {
    var texte = btn.dataset.copy;
    var initial = btn.textContent;
    btn.addEventListener("click", function () {
      var fini = function (ok) {
        btn.textContent = ok ? "Copié" : texte;
        clearTimeout(btn._t);
        btn._t = setTimeout(function () {
          btn.textContent = initial;
        }, 2000);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(texte).then(
          function () {
            fini(true);
          },
          function () {
            fini(false);
          }
        );
      } else {
        var zone = document.createElement("textarea");
        zone.value = texte;
        zone.setAttribute("readonly", "");
        zone.style.position = "fixed";
        zone.style.opacity = "0";
        document.body.appendChild(zone);
        zone.select();
        var ok = false;
        try {
          ok = document.execCommand("copy");
        } catch (e) {
          ok = false;
        }
        document.body.removeChild(zone);
        fini(ok);
      }
    });
  });
})();
