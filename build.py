# -*- coding: utf-8 -*-
"""Genere le site statique du portfolio.

Usage :  python build.py

Ecrit index.html et un fichier par projet dans projets/. Les pages produites sont
du HTML pur, sans dependance : GitHub Pages les sert telles quelles.
"""
import html
import json
import pathlib
import re

import contenu

ICI = pathlib.Path(__file__).parent
IMG = ICI / "assets" / "img"
MANIFEST = json.loads((IMG / "manifest.json").read_text(encoding="utf-8")) if (IMG / "manifest.json").exists() else {}

SITE = contenu.SITE
PROJETS = contenu.PROJETS

# proportions connues, pour reserver la place et eviter les sauts de mise en page
def dims(name):
    d = MANIFEST.get(name)
    return f' width="{d["w"]}" height="{d["h"]}"' if d else ""

TALL = {"audit", "osint", "affiche", "garde"}
ICONS = {"lmc", "myme"}


def numero(p):
    """Numero d'ordre global, calcule : jamais desynchronise du contenu."""
    return f"{PROJETS.index(p) + 1:02d}"


def esc(t):
    return html.escape(t, quote=True)


# --------------------------------------------------------------------------- #
# Fragments communs
# --------------------------------------------------------------------------- #

def head(titre, description, base):
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(titre)}</title>
<meta name="description" content="{esc(description)}">
<meta name="author" content="{esc(SITE['nom'])}">
<meta property="og:title" content="{esc(titre)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#08090b">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%2308090b'/%3E%3Ccircle cx='16' cy='16' r='7' fill='%23e0a458'/%3E%3C/svg%3E">
<link rel="stylesheet" href="{base}assets/style.css">
</head>
<body>
<a class="skip" href="#contenu">Aller au contenu</a>
"""


def header(base):
    return f"""<header class="site-header" id="top">
  <div class="wrap site-header__inner">
    <a class="brand" href="{base}index.html"><span class="brand__dot"></span>{esc(SITE['nom'])}</a>
    <nav class="site-nav" aria-label="Navigation principale">
      <a href="{base}index.html#travaux">Travaux</a>
      <a href="{base}index.html#apropos" data-hide>À propos</a>
      <a href="{base}index.html#competences" data-hide>Compétences</a>
      <a href="#contact">Contact</a>
    </nav>
  </div>
</header>
"""


def footer(base):
    mail = SITE["email"]
    return f"""<footer class="footer" id="contact">
  <div class="wrap">
    <h2 class="footer__title">Travaillons ensemble</h2>
    <p class="footer__text">
      Je cherche une alternance ou un stage en cybersécurité, et je prends aussi des
      projets de design et d'automatisation. Écris-moi, je réponds vite.
    </p>
    <a class="mail" href="mailto:{mail}">{mail}</a>
    <p class="mail__hint">Ou copie l'adresse<span class="copy-zone">
      <button class="btn btn--copy" type="button" data-copy="{mail}">Copier</button>
    </span></p>
    <div class="footer__links">
      <a href="{SITE['linkedin']}" target="_blank" rel="noopener">LinkedIn</a>
      <a href="{SITE['github']}" target="_blank" rel="noopener">GitHub</a>
      <a href="mailto:{mail}">Envoyer un email</a>
    </div>
    <p class="footer__legal">
      <span>{esc(SITE['nom'])} · {esc(SITE['ville'])}</span>
      <span>Portfolio personnel, 2026</span>
    </p>
  </div>
</footer>
<script src="{base}assets/app.js" defer></script>
</body>
</html>
"""


# --------------------------------------------------------------------------- #
# Index
# --------------------------------------------------------------------------- #

def carte_work(p, i):
    flip = " work--flip" if i % 2 else ""
    if p.get("ext") == "svg":
        cls = "work__media work__media--diagram"
    elif p["img"] in ICONS:
        cls = "work__media work__media--icon"
    elif p["img"] in TALL:
        cls = "work__media work__media--tall"
    else:
        cls = "work__media work__media--wide"
    tags = "".join(f"<li>{esc(t)}</li>" for t in p["tags"])
    href = f"projets/{p['slug']}.html"
    return f"""<article class="work{flip} reveal">
  <a class="{cls}" href="{href}" tabindex="-1" aria-hidden="true">
    <img src="assets/img/{p['img']}.{p.get('ext', 'webp')}" alt="{esc(p['titre'])}"{dims(p['img'])} decoding="async">
  </a>
  <div class="work__body">
    <p class="work__meta"><b>{numero(p)}</b> <span>{esc(p['discipline'])}</span> <span>{p['annee']}</span></p>
    <h3 class="work__title"><a href="{href}">{esc(p['titre'])}</a></h3>
    <p class="work__lede">{esc(p['lede'])}</p>
    <ul class="tags">{tags}</ul>
    <a class="work__more" href="{href}">Lire la fiche</a>
  </div>
</article>
"""


def index():
    strip = "".join(
        f"""<figure><img src="assets/img/{n}.webp" alt="{esc(c)}" decoding="async"><figcaption>{esc(c)}</figcaption></figure>"""
        for n, c in SITE["strip"]
    )
    facts = "".join(f"<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>" for k, v in SITE["facts"])
    cyber = "".join(carte_work(p, i) for i, p in enumerate(contenu.CYBER))
    apps = "".join(carte_work(p, i) for i, p in enumerate(contenu.APPS))
    crea = "".join(carte_work(p, i) for i, p in enumerate(contenu.CREA))

    return (
        head(SITE["titre"], SITE["description"], "")
        + header("")
        + f"""
<main id="contenu">

  <section class="hero">
    <div class="wrap">
      <p class="hero__kicker">{esc(SITE['kicker'])}</p>
      <h1 class="hero__title"><span>Benitho</span><span>Ntenda</span></h1>
      <div class="hero__body">
        <p class="hero__lede">{SITE['lede']}</p>
        <dl class="hero__facts">{facts}</dl>
      </div>
      <div class="hero__actions">
        <a class="btn btn--solid" href="#travaux">Voir les travaux</a>
        <a class="btn" href="mailto:{SITE['email']}">Écrire un email</a>
        <a class="btn" href="{SITE['github']}" target="_blank" rel="noopener">GitHub</a>
      </div>
    </div>
  </section>

  <div class="wrap">
    <div class="shot">{strip}</div>
  </div>

  <section class="section" id="travaux">
    <div class="wrap">
      <div class="section__head">
        <h2 class="section__title">Cybersécurité</h2>
        <p class="section__note">6 projets · 2026</p>
      </div>
      <p class="section__intro">
        Labs, audits et politiques de sécurité. Chaque fiche suit le même gabarit :
        contexte, ce que j'ai fait, résultat mesuré, limites assumées.
      </p>
      {cyber}
    </div>
  </section>

  <section class="section" id="applications">
    <div class="wrap">
      <div class="section__head">
        <h2 class="section__title">Applications</h2>
        <p class="section__note">3 projets · 2026</p>
      </div>
      <p class="section__intro">
        Des applications mobiles réelles, pas des maquettes : React Native et Expo, avec
        la conception, le code et l'identité visuelle.
      </p>
      {apps}
    </div>
  </section>

  <section class="section" id="creation">
    <div class="wrap">
      <div class="section__head">
        <h2 class="section__title">Création numérique</h2>
        <p class="section__note">5 projets · 2026</p>
      </div>
      <p class="section__intro">
        Design imprimé, direction artistique et développement web. Le
        versant visible du même travail : comprendre une contrainte et produire un
        livrable propre.
      </p>
      {crea}
    </div>
  </section>

  <section class="section" id="apropos">
    <div class="wrap">
      <div class="section__head">
        <h2 class="section__title">À propos</h2>
      </div>
      <div class="about">
        <div class="about__text">
          <p>
            Je suis étudiant en cybersécurité à <strong>Nexa Digital School</strong>, à
            Paris, et je suis en deuxième année de Bachelor (2026-2027).
            Originaire de la République démocratique du Congo, je suis arrivé en France
            en 2025.
          </p>
          <p>
            Ce qui m'intéresse, c'est le raisonnement derrière la faille. Un service
            qu'on publie sur le réseau Tor <strong>sans ouvrir un seul port</strong>. Un
            mail de phishing qui ne demande pas d'enfreindre la procédure, mais de
            l'appliquer correctement. Un rapport de reconnaissance dont la donnée la plus
            spectaculaire est justement celle qu'il faut écarter.
          </p>
          <p>
            Le reste vient du même endroit. Quand je ne fais pas de sécurité, je monte
            des visuels, des vidéos et des pages web, et j'applique la même exigence :
            que le livrable soit propre, utilisable et reproductible.
          </p>
          <p>
            Je cherche aujourd'hui une <strong>alternance ou un stage en
            cybersécurité</strong>. Les pistes qui m'attirent le plus sont l'analyse de
            risques et la gouvernance, la défense opérationnelle et le test d'intrusion.
          </p>
        </div>
        <div class="about__panel">
          <h3>En résumé</h3>
          <dl>
            <dt>Formation</dt>
            <dd>Bachelor Cybersécurité<small>Nexa Digital School, Paris · 2e année en cours (Bac+2, 2026-2027)</small></dd>
            <dt>Recherche</dt>
            <dd>Alternance ou stage<small>Sécurité opérationnelle, analyse de risques, gouvernance ou test d'intrusion</small></dd>
            <dt>Langues</dt>
            <dd>Français, lingala<small>Anglais technique</small></dd>
            <dt>Également</dt>
            <dd>Applications et design<small>React Native, identité visuelle, impression, automatisation</small></dd>
          </dl>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="competences">
    <div class="wrap">
      <div class="section__head">
        <h2 class="section__title">Compétences</h2>
        <p class="section__note">uniquement ce qui a servi dans un projet</p>
      </div>
      <div class="skills">
        <div class="skill">
          <h3>Systèmes et réseaux</h3>
          <ul><li>Linux Ubuntu</li><li>Bash</li><li>systemd</li><li>cron</li><li>TCP/IP</li><li>SSH</li><li>NAT</li><li>VirtualBox</li><li>Vagrant</li></ul>
        </div>
        <div class="skill">
          <h3>Sécurité offensive</h3>
          <ul><li>Tor et services cachés</li><li>GoPhish</li><li>Ingénierie sociale</li><li>Reconnaissance OSINT</li><li>WHOIS</li><li>dnstwist</li></ul>
        </div>
        <div class="skill">
          <h3>Défense et gouvernance</h3>
          <ul><li>ISO/IEC 27002</li><li>NIS 2</li><li>RGPD</li><li>RGS</li><li>Analyse de risque</li><li>SPF / DKIM / DMARC</li><li>MFA</li></ul>
        </div>
        <div class="skill">
          <h3>Développement mobile</h3>
          <ul><li>React Native</li><li>Expo</li><li>expo-router</li><li>TypeScript</li><li>Zustand</li><li>Jest</li><li>i18next</li></ul>
        </div>
        <div class="skill">
          <h3>Cryptographie appliquée</h3>
          <ul><li>Argon2id</li><li>Chiffrement authentifié</li><li>Stockage protégé</li><li>Biométrie</li><li>Signature sur courbe elliptique</li></ul>
        </div>
        <div class="skill">
          <h3>Création et développement</h3>
          <ul><li>Python</li><li>PowerShell</li><li>HTML / CSS</li><li>Three.js</li><li>Pillow</li><li>Montage vidéo</li><li>Design imprimé</li></ul>
        </div>
      </div>
    </div>
  </section>

</main>
"""
        + footer("")
    )


# --------------------------------------------------------------------------- #
# Fiche projet
# --------------------------------------------------------------------------- #

def fiche(p):
    i = PROJETS.index(p)
    prec = PROJETS[i - 1] if i > 0 else None
    suiv = PROJETS[i + 1] if i < len(PROJETS) - 1 else None

    specs = "".join(f"<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>" for k, v in p["specs"])
    blocs = "".join(
        f"""<section class="block">
  <h2 class="block__title">{esc(t)}</h2>
  <div class="block__body">{corps}</div>
</section>"""
        for t, corps in p["blocs"]
    )
    tags = "".join(f"<li>{esc(t)}</li>" for t in p["tags"])
    if p.get("ext") == "svg":
        cls = "fiche__figure fiche__figure--diagram"
    elif p["img"] in ICONS:
        cls = "fiche__figure fiche__figure--icon"
    elif p["img"] in TALL:
        cls = "fiche__figure fiche__figure--tall"
    else:
        cls = "fiche__figure"
    nav = '<a href="../index.html#travaux">Tous les travaux</a>'
    if prec:
        nav = f'<a href="{prec["slug"]}.html">← {esc(prec["titre"])}</a>'
    nxt = ""
    if suiv:
        nxt = f'<a href="{suiv["slug"]}.html">{esc(suiv["titre"])} →</a>'

    titre_page = f"{p['titre']} · {SITE['nom']}"
    desc = p["lede"]

    return (
        head(titre_page, desc, "../")
        + header("../")
        + f"""
<main id="contenu" class="fiche">
  <div class="wrap">
    <div class="fiche__head">
      <div>
        <p class="fiche__kicker">{numero(p)} · {esc(p['discipline'])} · {p['annee']}</p>
        <h1 class="fiche__title">{esc(p['titre'])}</h1>
        <p class="fiche__lede">{esc(p['lede'])}</p>
      </div>
      <dl class="specs">{specs}</dl>
    </div>

    <figure class="{cls}">
      <img src="../assets/img/{p['img']}.{p.get('ext', 'webp')}" alt="{esc(p['img_caption'])}"{dims(p['img'])} decoding="async">
      <figcaption>{esc(p['img_caption'])}</figcaption>
    </figure>

    {blocs}

    <div class="block__body" style="padding-block:2rem 0">
      <ul class="tags">{tags}</ul>
    </div>

    <nav class="fiche__nav" aria-label="Navigation entre projets">
      {nav}
      {nxt}
    </nav>
  </div>
</main>
"""
        + footer("../")
    )


# --------------------------------------------------------------------------- #
# Ecriture
# --------------------------------------------------------------------------- #

def main():
    (ICI / "index.html").write_text(index(), encoding="utf-8")
    dossier = ICI / "projets"
    dossier.mkdir(exist_ok=True)
    for p in PROJETS:
        (dossier / f"{p['slug']}.html").write_text(fiche(p), encoding="utf-8")

    # nettoyage des anciennes fiches qui ne sont plus referencees
    slugs = {p["slug"] + ".html" for p in PROJETS}
    for f in dossier.glob("*.html"):
        if f.name not in slugs:
            f.unlink()
            print("supprime", f.name)

    print(f"index.html et {len(PROJETS)} fiches generees")
    for p in PROJETS:
        print(f"  {numero(p)}  projets/{p['slug']}.html")


if __name__ == "__main__":
    main()
