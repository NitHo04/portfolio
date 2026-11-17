# Portfolio de Benitho Ntenda

Site statique, sans dépendance, sans serveur. Onze projets documentés en deux volets :
cybersécurité et création numérique.

## Voir le site

Double-cliquer sur `index.html`. Tout fonctionne hors ligne, sans installation.

## Ce qu'il y a dedans

```
portfolio/
├── index.html              page d'accueil : accueil, travaux, à propos, compétences, contact
├── contenu.py              tout le texte du site, un dictionnaire par projet
├── build.py                génère index.html et les fiches à partir de contenu.py
├── assets/
│   ├── style.css           feuille de style unique, thème sombre
│   ├── app.js              apparition au défilement, copie de l'email (aucune dépendance)
│   └── img/                visuels en WebP, un schéma en SVG
├── projets/                11 fiches générées, ne pas modifier à la main
└── .nojekyll               empêche GitHub Pages de traiter le site avec Jekyll
```

Les fichiers dans `projets/` sont générés. Pour changer un texte, modifier `contenu.py`
puis relancer :

```bash
python build.py
```

## Les onze projets

| # | Projet | Volet |
|---|--------|-------|
| 01 | Audit d'ingénierie sociale, Brévanne Industrie | Cybersécurité |
| 02 | Service onion auto-hébergé | Cybersécurité |
| 03 | Campagne de phishing avec GoPhish | Cybersécurité |
| 04 | PSSI de la Métropole de Valmont | Cybersécurité |
| 05 | Atelier d'automatisation Linux | Cybersécurité |
| 06 | Fiche outil Have I Been Pwned | Cybersécurité |
| 07 | Affiche et déclinaisons, premier anniversaire | Création |
| 08 | Série de fonds d'écran | Création |
| 09 | Montage vidéo d'un événement familial | Création |
| 10 | Page de garde universitaire générée par script | Création |
| 11 | Runner 3D, jeu de course dans une page | Création |

## Modifier le contenu

Tout le texte est dans `contenu.py`.

- `SITE` : nom, email, liens, phrase d'accueil, faits de la colonne de droite
- `CYBER` et `CREA` : la liste des projets. Chaque projet a un titre, un résumé, une
  image, des étiquettes, des lignes de caractéristiques et une suite de blocs
- Un bloc est un couple `(titre, html)`. L'ordre des blocs est l'ordre d'affichage

Pour ajouter un projet : copier un dictionnaire existant, changer le `slug`, le `num`,
le texte, ajouter l'image dans `assets/img/`, puis relancer `build.py`. Le sommaire,
les liens de navigation entre fiches et les compteurs de la page d'accueil se mettent à
jour tout seuls.

Pour changer une couleur ou un espacement : `assets/style.css`, blocs `:root` en haut.

## Mettre le site en ligne sur GitHub Pages

### 1. Créer le dépôt

Sur GitHub, bouton **New repository**.

- Nom : `portfolio` (le nom détermine l'adresse du site)
- Visibilité : **Public**, obligatoire pour GitHub Pages en offre gratuite
- Ne rien cocher d'autre, puis **Create repository**

### 2. Envoyer les fichiers

Méthode sans installation, dans le navigateur : sur la page du dépôt vide, cliquer sur
**uploading an existing file**, glisser le contenu du dossier `portfolio` (pas le dossier
lui même), puis **Commit changes**. `index.html` doit se retrouver à la racine du dépôt.

Méthode avec Git :

```bash
cd portfolio
git init
git add .
git commit -m "Portfolio"
git branch -M main
git remote add origin https://github.com/NitHo04/portfolio.git
git push -u origin main
```

### 3. Activer Pages

1. Onglet **Settings** du dépôt
2. Menu de gauche : **Pages**
3. Source : **Deploy from a branch**
4. Branch : **main**, dossier : **/ (root)**
5. **Save**

Une à deux minutes plus tard, l'adresse s'affiche en haut de la même page :

```
https://nitho04.github.io/portfolio/
```

Si la page renvoie une erreur 404, c'est presque toujours que `index.html` se trouve dans
un sous-dossier au lieu de la racine du dépôt.

## Règles de publication

Ce site est public et indexable. Trois règles valent d'être écrites pour un portfolio de
cybersécurité plus que pour un autre.

1. **Aucune adresse `.onion` active, aucun identifiant, aucune clé.** Le lab Tor est
   reproductible, sa documentation suffit. Le schéma d'architecture est publié, pas l'accès.
2. **Aucun visage de proche sans accord.** L'affiche du premier anniversaire montre un
   enfant, le montage montre des invités. Vérifier que les personnes concernées sont
   d'accord avant de publier, ou recadrer sur la partie typographique.
3. **Aucune affirmation non vérifiable.** « J'ai exécuté les huit tâches » se dit seulement
   si les sorties existent. La fiche de l'atelier Linux indique explicitement l'état réel.

## Vérifier le site

Un script de contrôle existe hors du dossier : `../out/test_site.py`. Il ouvre chaque page
dans Chrome en desktop et en mobile et signale les débordements, les images non chargées
et les erreurs JavaScript.

```bash
python ../out/test_site.py
```

## Version PDF

Pour joindre un document à une candidature : ouvrir une page dans le navigateur, puis
Ctrl+P et **Enregistrer au format PDF**. La feuille de style contient un bloc `@media print`
qui retire la navigation, force un fond blanc et évite les coupures.

## Reste à faire

- [ ] Créer le dépôt et publier le site
- [ ] Confirmer l'adresse LinkedIn exacte
- [ ] Rédiger un CV, le portfolio ne le remplace pas
- [ ] Décider pour les photos de proches (accord ou recadrage)
- [ ] Mettre à jour la section formation au fil de l'année
