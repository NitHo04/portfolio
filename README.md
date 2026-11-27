# Portfolio de Benitho Ntenda

Site statique, sans dépendance, sans serveur. Quatorze projets en trois volets :
cybersécurité, applications mobiles, création numérique.

## Voir le site

Double-cliquer sur `index.html`. Tout fonctionne hors ligne, y compris les polices,
qui sont hébergées dans le dossier.

## Ce qu'il y a dedans

```
portfolio/
├── index.html              accueil, travaux, à propos, compétences, contact
├── contenu.py              tout le texte du site, un dictionnaire par projet
├── build.py                génère index.html et les fiches à partir de contenu.py
├── assets/
│   ├── style.css           feuille de style unique, thème sombre
│   ├── app.js              apparition au défilement, copie de l'email
│   ├── fonts/              Baloo 2, Archivo et JetBrains Mono en woff2, hébergées ici
│   └── img/                visuels en WebP, un schéma en SVG
├── projets/                12 fiches générées, ne pas modifier à la main
└── .nojekyll               empêche GitHub Pages de traiter le site avec Jekyll
```

Les fichiers dans `projets/` sont générés. Pour changer un texte, modifier `contenu.py`
puis relancer :

```bash
python build.py
```

Aucune dépendance à un service tiers n'est nécessaire à l'affichage : ni police, ni
script, ni bibliothèque. C'est volontaire, un portfolio doit s'ouvrir même sur un
réseau filtré.

## Les quatorze projets

| # | Projet | Volet |
|---|--------|-------|
| 01 | Audit d'ingénierie sociale, Brévanne Industrie | Cybersécurité |
| 02 | Service onion auto-hébergé | Cybersécurité |
| 03 | Campagne de phishing avec GoPhish | Cybersécurité |
| 04 | PSSI de la Métropole de Valmont | Cybersécurité |
| 05 | Atelier d'automatisation Linux | Cybersécurité |
| 06 | Fiche outil Have I Been Pwned | Cybersécurité |
| 07 | YokaSon, lecteur de musique et ambiances | Applications |
| 08 | Le Millionnaire Congolais, jeu de quiz | Applications |
| 09 | MyMe, espace privé chiffré | Applications |
| 10 | Affiche et déclinaisons, premier anniversaire | Création |
| 11 | Série de fonds d'écran | Création |
| 12 | Runner 3D, jeu de course dans une page | Création |
| 13 | BOJJ Boutique, boutique de maillots en ligne | Création |
| 14 | Kessy Noire, personnage IA pour récits à suspense | Création |

## Modifier le contenu

Tout le texte est dans `contenu.py`.

- `SITE` : nom, email, liens, phrase d'accueil, colonne de droite, bandeau visuel
- `CYBER`, `APPS`, `CREA` : les trois volets. Chaque projet a un titre, un résumé, une
  image, des étiquettes, des caractéristiques et une suite de blocs
- Un bloc est un couple `(titre, html)`. L'ordre des blocs est l'ordre d'affichage

Pour ajouter un projet : copier un dictionnaire, changer le `slug`, le texte, ajouter
l'image dans `assets/img/`, puis relancer `build.py`. La numérotation, le sommaire, les
liens de navigation entre fiches et les compteurs se mettent à jour tout seuls. Le champ
`num` n'est plus lu, il reste à titre indicatif.

Pour ajouter une image : la placer dans `assets/img/`, en WebP si possible, puis
régénérer `assets/img/manifest.json` avec les dimensions réelles. Ce manifeste sert à
réserver la place de l'image et évite que la page saute au chargement.

## Remplacer les polices

Les deux fichiers `assets/fonts/*.woff2` sont des polices variables : un seul fichier
couvre toutes les graisses. Pour en changer, modifier les `@font-face` en haut de
`assets/style.css`, puis les variables `--font` et `--mono`.

## Mettre le site en ligne sur GitHub Pages

### 1. Créer le dépôt

Sur GitHub, bouton **New repository**.

- Nom : `portfolio` (le nom détermine l'adresse du site)
- Visibilité : **Public**, obligatoire pour GitHub Pages en offre gratuite
- Ne rien cocher d'autre, puis **Create repository**

### 2. Envoyer les fichiers

Ce dossier est déjà un dépôt Git avec un commit prêt. Il ne manque que la cible :

```bash
git remote add origin https://github.com/NitHo04/portfolio.git
git push -u origin main
```

Sans Git, dans le navigateur : sur la page du dépôt vide, cliquer sur
**uploading an existing file**, glisser le contenu du dossier `portfolio` (pas le
dossier lui même), puis **Commit changes**. `index.html` doit se retrouver à la racine.

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
   enfant. Vérifier l'accord des personnes concernées, ou recadrer sur la partie
   typographique.
3. **Aucune affirmation non vérifiable.** Les chiffres des fiches viennent des dépôts
   réels. La fiche de l'atelier Linux indique explicitement ce qui n'était pas encore
   exécuté, celle de MyMe indique le point bloquant. Une limite assumée vaut mieux qu'un
   résultat inventé.

## Vérifier le site

Un script de contrôle existe hors du dossier : `../out/test_site.py`. Il ouvre chaque page
dans Chrome, en desktop et en mobile, et signale les débordements, les images non
chargées et les erreurs JavaScript.

```bash
python ../out/test_site.py
```

## Version PDF

Ouvrir une page dans le navigateur, puis Ctrl+P et **Enregistrer au format PDF**. La
feuille de style contient un bloc `@media print` qui retire la navigation, force un fond
blanc et évite les coupures.

## Reste à faire

- [ ] Créer le dépôt et publier le site
- [ ] Confirmer l'adresse LinkedIn exacte
- [ ] Ajouter des captures d'écran des trois applications, l'icône seule est juste
- [ ] Décider pour la photo de l'affiche (accord ou recadrage)
- [ ] Rédiger un CV, le portfolio ne le remplace pas
- [ ] Mettre à jour la section formation au fil de l'année
