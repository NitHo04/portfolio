# -*- coding: utf-8 -*-
"""Contenu du portfolio de Benitho Ntenda.

Chaque projet est un dictionnaire. Les blocs sont du HTML brut, dans l'ordre
d'affichage. Le generateur (build.py) se charge de la mise en page.
"""

SITE = {
    "nom": "Benitho Ntenda",
    "titre": "Benitho Ntenda, portfolio",
    "role": "Étudiant en cybersécurité et créateur numérique",
    "ville": "Paris",
    "email": "benithooff04@icloud.com",
    "linkedin": "https://www.linkedin.com/in/benitho-ntenda-43b680398",
    "github": "https://github.com/NitHo04",
    "description": (
        "Portfolio de Benitho Ntenda, étudiant en cybersécurité à Nexa Digital School. "
        "Projets documentés : audit de risque, lab Tor, simulation de phishing, PSSI, "
        "OSINT, applications mobiles React Native, cryptographie appliquée, design."
    ),
    "kicker": "Portfolio 2026 · Paris",
    "lede": (
        "Je documente ce que je construis, méthode comprise. "
        "<em>Onze projets</em>, du lab réseau jusqu'à la boutique en ligne."
    ),
    "facts": [
        ("Statut", "Alternance ou stage"),
        ("Formation", "Nexa Digital School"),
        ("Niveau", "2e année de Bachelor (2026-2027)"),
        ("Basé à", "Paris, France"),
    ],
    "strip": [("jeu", "Runner 3D, jeu de course jouable dans le navigateur")],
}

# --------------------------------------------------------------------------- #
# Cybersécurité
# --------------------------------------------------------------------------- #

CYBER = [
    {
        "slug": "audit-brevanne",
        "num": "01",
        "discipline": "Analyse de risques",
        "annee": "2026",
        "titre": "Audit de vulnérabilité à l'ingénierie sociale",
        "lede": (
            "Prendre un rapport de reconnaissance OSINT, décider quelle donnée est "
            "vraiment exploitable, et construire l'attaque la plus crédible sans "
            "jamais l'exécuter."
        ),
        "img": "audit",
        "img_caption": "Dossier d'audit, synthèse pour la direction générale et cartographie de la surface d'attaque.",
        "tags": ["Tri de données", "Corroboration", "Analyse de risque", "Rédaction"],
        "specs": [
            ("Cadre", "Mandat fictif BRV-AUDIT-SE-01"),
            ("Rôle", "Analyste, rédaction du dossier"),
            ("Format", "Projet d'équipe"),
            ("Livrable", "Dossier classifié, synthèse direction"),
        ],
        "blocs": [
            ("Contexte", """
<p>
  Une entreprise fictive, un rapport de reconnaissance OSINT livré tel quel : neuf
  pièces, collecte passive horodatée, sites publics, registres de domaines, fuites
  de données. Le mandat ne demande pas de collecter, mais de <strong>lire</strong>.
  Aucune donnée hors dossier, aucun contact réel, scénario d'attaque interdit
  d'exécution.
</p>
<p>
  Contrainte supplémentaire : le dossier est destiné à une direction générale. Une
  page de conclusion doit suffire, sans jargon.
</p>
"""),
            ("La question posée", """
<p>
  Est-ce qu'un attaquant, avec seulement ce que le web public raconte, peut obtenir
  un virement de plus de 10 000 euros ?
</p>
"""),
            ("Ce que j'ai fait", """
<p>
  Le travail n'est pas la collecte, c'est le <strong>tri</strong>. Un rapport OSINT
  contient toujours plus de bruit que de signal, et un scénario bâti sur une donnée
  fausse s'effondre au premier contact avec la cible.
</p>
<ol class="steps">
  <li><strong>Datation et traçabilité.</strong> Chaque donnée est rattachée à sa pièce et à sa date. Une information sans source n'existe pas.</li>
  <li><strong>Quatre statuts.</strong> Fiable, périmé, leurre, impasse, avec le motif écrit de chaque écart.</li>
  <li><strong>Règle de corroboration.</strong> Une donnée n'est retenue que si deux sources indépendantes la confirment.</li>
  <li><strong>Cartographie.</strong> Onze éléments retenus, du domaine sosie au service distant exposé.</li>
  <li><strong>Choix de la cible prioritaire</strong> et construction du scénario en deux plans, avec le plan de repli.</li>
  <li><strong>Minimisation.</strong> Toute donnée personnelle sans lien avec l'objectif est écartée, même disponible.</li>
</ol>
<h3>Les écarts les plus instructifs</h3>
<div class="table-wrap">
  <table>
    <thead><tr><th>Donnée</th><th>Statut</th><th>Pourquoi elle est écartée</th></tr></thead>
    <tbody>
      <tr><td>Page « Équipe » désignant un autre directeur financier</td><td>Leurre</td><td>Page non mise à jour depuis 2021. Un scénario qui invoquerait ce nom se ferait démasquer immédiatement.</td></tr>
      <tr><td>Communiqué annonçant un partenariat stratégique</td><td>Périmé</td><td>Un article plus récent documente la rupture. Le prétexte déclencherait une vérification.</td></tr>
      <tr><td>Message de forum sur un bug du logiciel de paie</td><td>Impasse</td><td>Spectaculaire, invérifiable, sans rapport avec le circuit de paiement.</td></tr>
      <tr><td>Profil personnel de la cible, loisirs et animal</td><td>Exploitable, non utilisé</td><td>Donnée privée sans lien avec l'objectif. Un prétexte bâti dessus ferait basculer la cible dans la méfiance.</td></tr>
      <tr><td>Bannières présentées comme « à jour »</td><td>À recouper</td><td>Les versions citées datent de 2018 et 2020. À reclasser en vulnérabilité technique, hors du scénario humain.</td></tr>
    </tbody>
  </table>
</div>
"""),
            ("Résultat", """
<p>
  La conclusion est un renversement : l'entreprise n'est pas vulnérable par sa
  technique, elle l'est par la <strong>concentration de son pouvoir de décision sur
  une seule personne joignable et isolable</strong>. Trois faits se recoupent.
</p>
<ul>
  <li>Une procédure interne indexée publiquement réserve la validation des virements au dessus du seuil à la directrice financière. Le nom du seul décideur à convaincre est donc public, et le seuil aussi.</li>
  <li>Cette personne apparaît dans deux fuites qui exposent son email, un hash de mot de passe et surtout son <strong>numéro de téléphone</strong>. Un numéro connu, c'est ce qui rend un appel crédible.</li>
  <li>Son agenda public annonce son absence. La fenêtre où elle est seule, sans collègue pour contester une instruction, est connue à l'avance.</li>
  <li>Un domaine sosie enregistré sous identité masquée, trois semaines avant le rapport, montre que l'infrastructure d'usurpation existe déjà.</li>
</ul>
<dl class="kpis">
  <div><dt>Données triées</dt><dd>19</dd></div>
  <div><dt>Retenues / écartées</dt><dd>11 / 8</dd></div>
  <div><dt>Corroboration exigée</dt><dd>2 sources</dd></div>
</dl>
<div class="note">
  <p><strong>Recommandation principale :</strong> imposer un second regard humain sur tout virement dépassant le seuil, quel que soit le signataire, y compris quand le demandeur est la personne qui détient ce pouvoir.</p>
  <p><strong>Règle absolue :</strong> le contact indiqué dans une demande n'est jamais un canal de vérification. On raccroche et on rappelle sur un numéro connu par ailleurs.</p>
</div>
"""),
            ("Limites", """
<ul>
  <li>Scénario non exécuté, par construction du mandat. Sa crédibilité repose sur la lecture, pas sur un test réel.</li>
  <li>La fiabilité du rapport OSINT fourni n'a pas été auditée : deux sources issues de la même origine resteraient fausses.</li>
  <li>Aucun chiffrage du coût des mesures, ce qui limite leur portée décisionnelle.</li>
  <li>Analyse humaine et qualitative, qui ne remplace pas une revue de configuration.</li>
</ul>
"""),
            ("Ce que j'en retiens", """
<p>
  La donnée la plus spectaculaire est rarement la plus utile. Le bug de forum faisait
  une meilleure histoire que la procédure de virement indexée, et il ne servait à
  rien. Inversement, un document public ennuyeux a donné à la fois l'identité du
  décideur, le seuil et le contournement possible.
</p>
<p>
  Deuxième leçon : la piste la plus évidente était la plus fragile. Contourner un
  contrôle se referme en réécrivant une phrase. Convaincre la personne qui incarne
  le contrôle est beaucoup plus difficile à corriger.
</p>
"""),
        ],
    },
    {
        "slug": "tor-lab",
        "num": "02",
        "discipline": "Lab réseau",
        "annee": "2026",
        "titre": "Service onion auto-hébergé",
        "lede": (
            "Publier un service web sur le réseau Tor depuis une machine virtuelle, "
            "sans ouvrir un seul port entrant. Cinq pièges documentés, quatre qui "
            "m'ont coûté des heures."
        ),
        "img": "tor-schema",
        "ext": "svg",
        "img_caption": "Schéma de l'architecture : le service n'est joignable que parce que la VM ouvre le canal vers l'extérieur.",
        "tags": ["Tor", "Linux", "NAT", "Bash", "Documentation"],
        "specs": [
            ("Cadre", "Laboratoire personnel"),
            ("Rôle", "Conception et réalisation seul"),
            ("Environnement", "VirtualBox, Ubuntu Server, 4 Go, 2 vCPU"),
            ("Livrable", "Scripts, diagnostic, documentation"),
        ],
        "blocs": [
            ("Contexte", """
<p>
  Un service caché Tor est joignable sans que le serveur ait d'adresse IP publique
  ni de port entrant à exposer. La question de départ : est-ce que je peux publier
  quelque chose depuis ma machine, derrière une box qui ne redirige rien, sans coût,
  et le prouver ?
</p>
<p>
  La réponse intéresse la défense : un pare-feu entrant qui bloque tout ne suffit
  pas si les flux sortants sont libres. C'est exactement comme ça qu'un attaquant
  maintient un accès persistant.
</p>
"""),
            ("L'architecture", """
<p>
  Le mécanisme repose sur un renversement : le service n'est joignable que parce que
  c'est la machine qui sort vers le réseau Tor et maintient le canal ouvert.
</p>
<div class="note">
  <p>
    Navigateur Tor, puis réseau Tor (trois nœuds et un point de rendez-vous), puis
    connexion <strong>sortante</strong> initiée par la VM, puis Tor local, puis le
    service caché qui dirige le port 80 vers 127.0.0.1:8080, puis le serveur
    applicatif lié à la boucle locale uniquement.
  </p>
</div>
"""),
            ("Ce que j'ai fait", """
<ol class="steps">
  <li><strong>Machine virtuelle déclarative.</strong> Disque, mémoire et réseau définis par commandes, pour que le lab soit reproductible et pas cliqué.</li>
  <li><strong>Installation non supervisée</strong> d'Ubuntu Server avec une étape de configuration passée par l'installateur.</li>
  <li><strong>Script de publication.</strong> Installation de Tor, répertoire du site, configuration du service caché, redémarrage, affichage de l'adresse.</li>
  <li><strong>Service verrouillé.</strong> Le serveur HTTP écoute uniquement sur la boucle locale, jamais sur l'interface réseau.</li>
  <li><strong>Vérification.</strong> Requête à travers un proxy SOCKS Tor et contrôle du code de réponse.</li>
  <li><strong>Diagnostic.</strong> Un script séparé qui liste les ports en écoute, la configuration active et le journal.</li>
</ol>
"""),
            ("Résultat", """
<dl class="kpis">
  <div><dt>Ports ouverts sur l'hôte</dt><dd>0</dd></div>
  <div><dt>Coût</dt><dd>0 €</dd></div>
  <div><dt>Mise en place</dt><dd>environ 25 min</dd></div>
</dl>
<p>
  Le service est joignable depuis un navigateur Tor, confirmé par un code de réponse
  200 et par le contenu servi. Aucune redirection entrante, aucune règle de pare-feu
  assouplie, aucune IP publique révélée.
</p>
<div class="note">
  <p>
    <strong>Choix assumé :</strong> l'adresse onion et les identifiants du lab ne
    sont pas publiés. Le lab tourne encore, et exposer une adresse ou un accès dans
    un portfolio public revient à publier une porte ouverte en espérant que personne
    ne la remarque. La démarche est reproductible, c'est ce qui compte.
  </p>
</div>
"""),
            ("Les cinq pièges", """
<div class="table-wrap">
  <table>
    <thead><tr><th>Piège</th><th>Cause réelle</th></tr></thead>
    <tbody>
      <tr><td>Démarrer un service dans la post installation de l'installateur</td><td>La commande s'exécute dans un chroot. On ne démarre pas un service dans un chroot, donc l'installation échoue alors que le disque est complet. Une post installation doit rester de la configuration pure.</td></tr>
      <tr><td>Faire résoudre une adresse onion par le client lui-même</td><td>Les versions récentes refusent, conformément à la RFC 7686, et l'enveloppe proxy ne l'intercepte pas. Il faut laisser le proxy résoudre le nom.</td></tr>
      <tr><td>Passer une commande complexe à travers SSH depuis Windows</td><td>La couche de citation détruit les guillemets internes et le shell distant reçoit la commande coupée. Envoyer le script par l'entrée standard.</td></tr>
      <tr><td>Un script préparé sous Windows</td><td>Fins de ligne et locale française cassent tout : le retour chariot est interprété comme une commande. Écrire en LF.</td></tr>
      <tr><td>Tester un service par un simple test de port</td><td>La redirection NAT accepte la connexion avant que le service existe. Un port qui répond n'est pas une preuve.</td></tr>
    </tbody>
  </table>
</div>
"""),
            ("Limites", """
<ul>
  <li>Service statique : aucune surface d'authentification à durcir.</li>
  <li>Pas de durcissement système poussé, ni mise à jour automatique, ni filtrage applicatif.</li>
  <li>Aucune mesure de latence à travers le réseau Tor, alors qu'elle varie fortement.</li>
  <li>Le lab valide la publication d'un service, pas la sécurité d'une application.</li>
</ul>
"""),
            ("Ce que j'en retiens", """
<p>
  Le geste technique est simple, la compréhension du mécanisme l'est beaucoup moins.
  La question « pourquoi le NAT suffit ici et pas pour un site classique » force à
  regarder dans quel sens le flux s'établit, et c'est exactement le raisonnement
  qu'un pare-feu mal configuré laisse passer.
</p>
<p>
  Deuxième leçon : la documentation des erreurs vaut plus que le résultat. Un script
  qui marche une fois ne prouve pas la maîtrise. Une cause expliquée, si.
</p>
"""),
        ],
    },
    {
        "slug": "phishing-gophish",
        "num": "03",
        "discipline": "Simulation d'attaque",
        "annee": "2026",
        "titre": "Campagne de phishing avec GoPhish",
        "lede": (
            "Jouer l'attaquant et la victime dans la même machine virtuelle pour "
            "comprendre pourquoi une attaque aussi banale fonctionne encore. Rien "
            "n'est sorti du laboratoire."
        ),
        "img": "phish",
        "img_caption": "La page piège servie aux cibles, cohérente avec l'objet du mail envoyé.",
        "tags": ["GoPhish", "Ingénierie sociale", "SPF / DKIM / DMARC"],
        "specs": [
            ("Cadre", "TP encadré, groupe de trois"),
            ("Rôle", "Montage de la chaîne et rédaction"),
            ("Outils", "GoPhish, Mailpit, VirtualBox"),
            ("Livrable", "Rapport pas à pas avec captures"),
        ],
        "blocs": [
            ("Contexte", """
<p>
  Le scénario retenu est une <strong>fraude au président</strong> : l'attaquant se
  fait passer pour un dirigeant et obtient d'un employé un virement urgent. C'est
  l'une des arnaques les plus anciennes du répertoire, et l'une des plus rentables.
</p>
<p>
  L'objectif n'était pas de savoir cliquer sur envoyer, mais de voir chaque maillon
  de la chaîne, puis de comprendre quel maillon on peut réellement casser côté
  défense.
</p>
"""),
            ("Le scénario", """
<div class="table-wrap">
  <table>
    <tbody>
      <tr><th>Usurpé</th><td>La directrice administrative et financière</td></tr>
      <tr><th>Cible</th><td>L'assistante de direction, arrivée depuis quatre mois</td></tr>
      <tr><th>Prétexte</th><td>Un règlement fournisseur oublié, à régulariser avant 18 h à cause de la clôture comptable</td></tr>
      <tr><th>Leviers</th><td>L'autorité, l'urgence, la procédure interne, le secret</td></tr>
    </tbody>
  </table>
</div>
<div class="note">
  <p>
    Le détail qui rend ce mail dangereux : <strong>il ne demande pas d'enfreindre la
    procédure, il demande de l'appliquer</strong>. Une personne vigilante se méfie
    d'un message qui viole les règles. Beaucoup moins d'un message qui les respecte.
  </p>
</div>
"""),
            ("Ce que j'ai fait", """
<ol class="steps">
  <li><strong>Profil d'envoi.</strong> Par quel serveur les mails partent et sous quelle identité, validé par un envoi de test avant tout le reste.</li>
  <li><strong>Page piège.</strong> Un faux portail interne annonçant une opération en attente, cohérent avec l'objet du mail, avec collecte des données et des mots de passe activée.</li>
  <li><strong>Modèle de mail.</strong> Lien généré par l'outil et non écrit en dur, pour que chaque destinataire reçoive une adresse différente et qu'on sache qui clique.</li>
  <li><strong>Groupe de cibles</strong> rattaché à l'entreprise fictive.</li>
  <li><strong>Campagne</strong>, qui assemble les quatre objets. Avant elle, ce ne sont que des objets inertes.</li>
</ol>
<p>
  Détail d'architecture qui compte : l'outil lance <strong>deux serveurs
  distincts</strong>, l'administration d'un côté et les pages servies aux victimes de
  l'autre. Une victime ne doit jamais tomber sur l'interface d'administration, et se
  tromper de port fait échouer la campagne entière.
</p>
"""),
            ("Résultat", """
<p>Les quatre compteurs racontent chacun une étape franchie.</p>
<dl class="kpis">
  <div><dt>Mail envoyé</dt><dd>1</dd></div>
  <div><dt>Ouvert, lien cliqué</dt><dd>1 / 1</dd></div>
  <div><dt>Identifiants soumis</dt><dd>1</dd></div>
</dl>
<p>
  Jusqu'à la récupération du mot de passe, le parcours est complet. Les quatre
  erreurs rencontrées valent plus que le résultat : mauvais port dans l'URL de la
  campagne, format d'expéditeur refusé, campagne supprimée trop tôt ce qui détruit
  ses résultats et invalide les liens déjà envoyés, et groupe resté vide faute
  d'avoir validé la ligne du destinataire.
</p>
"""),
            ("Ce qui arrête réellement l'attaque", """
<ul>
  <li><strong>Deux valideurs au dessus du seuil, même quand le demandeur est le dirigeant.</strong> Aucune opération ne doit pouvoir être initiée et validée par la même personne. Cette règle détruit le scénario entier.</li>
  <li><strong>Ne jamais vérifier par le canal indiqué dans la demande.</strong> On raccroche et on rappelle sur un numéro connu par ailleurs.</li>
  <li><strong>Double authentification</strong> sur la messagerie et les outils bancaires : un mot de passe volé ne suffit plus.</li>
  <li><strong>SPF, DKIM et DMARC</strong> bien configurés, avec la limite que ce TP rend évidente : ces mécanismes authentifient un domaine, pas une intention. Un attaquant qui utilise un domaine sosie publie ses propres enregistrements et passe tous les contrôles.</li>
</ul>
"""),
            ("Limites", """
<ul>
  <li>Une seule cible, donc aucun enseignement statistique sur un taux de clic réel.</li>
  <li>Aucun filtre anti-spam sur le chemin : un vrai envoi externe aurait été arrêté avant la boîte.</li>
  <li>Environnement local uniquement, volontairement. Aucun message n'a quitté la VM.</li>
  <li>Page piège simple, sans comportement dynamique capable de résister à un utilisateur méfiant.</li>
</ul>
"""),
            ("Ce que j'en retiens", """
<p>
  En moins d'une heure, avec des outils gratuits, on obtient une attaque complète et
  chiffrée. La barrière technique n'existe pas. Ce qui protège, c'est une règle de
  gouvernance et une deuxième personne.
</p>
<p>
  Et une leçon de conception : la cohérence entre le message et la page vaut plus que
  la qualité graphique de la page. C'est là que se joue la crédibilité.
</p>
"""),
        ],
    },
    {
        "slug": "pssi-valmont",
        "num": "04",
        "discipline": "Gouvernance",
        "annee": "2026",
        "titre": "PSSI de la Métropole de Valmont",
        "lede": (
            "Écrire un document qui engage une collectivité de 6 000 agents, et le "
            "défendre en dix minutes devant une direction qui a trois décisions à prendre."
        ),
        "img": "pssi",
        "img_caption": "Slide d'ouverture de la soutenance direction, dix minutes chronométrées.",
        "tags": ["ISO/IEC 27002", "NIS 2", "RGPD", "Analyse de risque"],
        "specs": [
            ("Cadre", "Projet d'équipe, soutenance direction"),
            ("Rôle", "Co-rédaction et soutenance"),
            ("Référentiels", "ISO/IEC 27002, NIS 2, RGPD, RGS"),
            ("Livrable", "Document cadre et support de soutenance"),
        ],
        "blocs": [
            ("Contexte", """
<p>
  Une métropole fictive de <strong>6 000 agents, 40 communes et 25 sites</strong>,
  avec un système d'information hétérogène qui couvre aussi bien l'état civil que
  les automates d'eau et de transport. Deux éléments déclenchent l'urgence : une
  cyberattaque critique chez une commune voisine, et l'application imminente de la
  directive NIS 2, qui qualifie l'organisation d'entité essentielle.
</p>
<p>
  La difficulté n'est pas technique. C'est de produire un document lisible par une
  direction qui arbitre sur des risques cotés, pas sur une liste de bonnes pratiques
  sans hiérarchie.
</p>
"""),
            ("Ce que j'ai fait", """
<p>Cinq phases qui s'enchaînent.</p>
<ol class="steps">
  <li><strong>Contexte et valeurs métier.</strong> Cinq valeurs qualifiées par leurs besoins de disponibilité, intégrité, confidentialité et preuve, pour éviter de protéger « le SI » en général.</li>
  <li><strong>Registre de risques coté.</strong> Produit gravité par vraisemblance, seuil explicite, cible annoncée : ramener tous les risques sous huit.</li>
  <li><strong>Gouvernance.</strong> Quatre niveaux avec un rôle écrit, et chaque objectif rattaché à un responsable nommé.</li>
  <li><strong>Matrice de traçabilité.</strong> Chaque règle formulée avec son niveau d'exigence, rattachée à un risque, à une mesure du référentiel et à un indicateur mesurable.</li>
  <li><strong>Feuille de route et décisions.</strong> Trois horizons, cinq indicateurs trimestriels, trois décisions soumises au vote.</li>
</ol>
"""),
            ("Résultat", """
<p>Trois règles extraites de la matrice, pour montrer le principe.</p>
<div class="table-wrap">
  <table>
    <thead><tr><th>Règle</th><th>Exigence</th><th>Mesure</th><th>Indicateur</th></tr></thead>
    <tbody>
      <tr><td>ACC-01</td><td>Tout compte à privilèges doit utiliser la double authentification</td><td>5.17</td><td>Comptes couverts, cible 100 %</td></tr>
      <tr><td>RES-01</td><td>Le réseau d'administration doit être cloisonné des réseaux industriels</td><td>8.22</td><td>Flux non autorisés, cible 0</td></tr>
      <tr><td>EXP-02</td><td>Une sauvegarde hors ligne doit être testée chaque trimestre</td><td>8.13</td><td>Restaurations réussies, cible 100 %</td></tr>
    </tbody>
  </table>
</div>
<dl class="kpis">
  <div><dt>Périmètre</dt><dd>6 000 agents</dd></div>
  <div><dt>Risques cotés</dt><dd>5</dd></div>
  <div><dt>Indicateurs suivis</dt><dd>5 au trimestre</dd></div>
</dl>
"""),
            ("Limites", """
<ul>
  <li>Cas entièrement fictif : périmètre et hypothèses non validés sur le terrain.</li>
  <li>Aucun chiffrage détaillé du budget cyber, évoqué comme décision à voter sans estimation ligne à ligne.</li>
  <li>L'état de maturité initial est supposé, pas mesuré. Une vraie démarche commencerait par un diagnostic.</li>
  <li>Calendrier NIS 2 simplifié, articulation avec l'autorité nationale restée théorique.</li>
</ul>
"""),
            ("Ce que j'en retiens", """
<p>
  Une PSSI ne se vend pas à des techniciens, elle se vend à une direction. Ce qui la
  rend crédible n'est pas la qualité des mesures, mais la chaîne qui va du risque à
  la règle, de la règle à l'indicateur, et de l'indicateur à un responsable nommé.
</p>
<p>
  Deuxième leçon, très concrète : la différence entre « doit » et « devrait » n'est
  pas une nuance de style. Une règle impérative engage des sanctions, une
  recommandation n'engage rien. Écrire « doit » partout produit un document
  inapplicable, « devrait » partout produit un document décoratif.
</p>
"""),
        ],
    },
    {
        "slug": "atelier-linux",
        "num": "05",
        "discipline": "Systèmes",
        "annee": "2026",
        "titre": "Atelier d'automatisation Linux",
        "lede": (
            "Huit scripts qui surveillent l'hygiène d'un serveur, un laboratoire "
            "reproductible en une commande, et une planification pour que tout tourne "
            "sans intervention."
        ),
        "img": "linux",
        "img_caption": "Sortie réelle d'un script de contrôle : détection d'une alerte puis journalisation.",
        "tags": ["Bash", "systemd", "cron", "Vagrant", "Python"],
        "specs": [
            ("Cadre", "Module Bash et Shell, Nexa Digital School"),
            ("Rôle", "Scripts, laboratoire et rapports, seul"),
            ("Environnement", "Ubuntu, Vagrant, VirtualBox, SSH distant"),
            ("Livrable", "Dépôt de scripts et deux rapports générés"),
        ],
        "blocs": [
            ("Contexte", """
<p>
  Sur un serveur, les incidents graves viennent rarement d'une attaque sophistiquée.
  Ils viennent d'un disque plein, d'un service arrêté, d'une sauvegarde jamais
  testée, d'un compte sans mot de passe ou d'un fichier modifiable par tout le monde.
  Tout cela se détecte par script.
</p>
<p>
  J'ai traité le laboratoire avant les scripts, pour que chaque script soit écrit dans
  un environnement réel et pas dans le vide.
</p>
"""),
            ("Les huit contrôles", """
<div class="table-wrap">
  <table>
    <thead><tr><th>Script</th><th>Ce qu'il contrôle</th><th>Choix de conception</th></tr></thead>
    <tbody>
      <tr><td>Santé</td><td>Disque, mémoire, charge contre des seuils</td><td>Seuils en paramètres, pas codés en dur</td></tr>
      <tr><td>Services</td><td>État des services attendus</td><td>Alerte sans relance automatique : un service qui tombe en boucle doit être regardé</td></tr>
      <tr><td>Réseau</td><td>Réponse, résolution, ouverture de port</td><td>Garde-fou de périmètre : refuse de sortir de la cible autorisée</td></tr>
      <tr><td>Sauvegarde</td><td>Archive datée, vérifiée, rotation</td><td>Une sauvegarde non testée n'est pas une sauvegarde</td></tr>
      <tr><td>Mises à jour</td><td>Correctifs en attente, redémarrage requis</td><td>Le redémarrage requis est signalé, jamais déclenché</td></tr>
      <tr><td>Authentification</td><td>Échecs de connexion par source</td><td>Agrégation par adresse pour repérer une tentative répétée</td></tr>
      <tr><td>Comptes</td><td>Privilèges inattendus, permissions ouvertes</td><td>Détecter les dérives, pas seulement les intrusions</td></tr>
      <tr><td>Nettoyage</td><td>Fichiers temporaires anciens</td><td>Simulation par défaut, suppression sur demande explicite</td></tr>
    </tbody>
  </table>
</div>
"""),
            ("Résultat", """
<dl class="kpis">
  <div><dt>Scripts livrés</dt><dd>8 plus un bonus</dd></div>
  <div><dt>Laboratoire</dt><dd>validé, code 0</dd></div>
  <div><dt>Défis résolus</dt><dd>24</dd></div>
</dl>
<p>
  Le laboratoire est versionné et sa recette rend un code de sortie nul, ce qui est la
  définition d'un environnement conforme. Les huit scripts sont écrits, livrés et
  planifiés, et un journal d'atelier documente les difficultés au fil de l'exécution.
</p>
<p>
  Pour les rapports, j'ai écrit un générateur qui lit la source du document et y
  injecte les sorties réelles des scripts et les captures correspondantes. Aucune
  sortie n'est recopiée à la main.
</p>
<div class="note">
  <p>
    <strong>État exact, sans enjoliver :</strong> au dernier point d'avancement, le
    laboratoire était terminé et vérifié, les huit scripts écrits et livrés, mais
    l'exécution complète des huit tâches dans la machine virtuelle restait à
    finaliser. Les sorties montrées ici sont celles qui existent réellement.
  </p>
</div>
"""),
            ("Limites", """
<ul>
  <li>Tous les scripts n'avaient pas encore été exécutés sur la cible au dernier point, donc la robustesse en conditions réelles reste partiellement vérifiée.</li>
  <li>Gestion d'erreurs sommaire : si une dépendance manque, le comportement est prévisible mais peu explicite.</li>
  <li>Aucune remontée vers un outil de supervision, les alertes restent locales.</li>
  <li>Un seul système ciblé, Ubuntu. Les autres distributions demanderaient des adaptations.</li>
</ul>
"""),
            ("Ce que j'en retiens", """
<p>
  Un script de supervision qui corrige tout seul est plus dangereux qu'un script qui
  signale. Redémarrer automatiquement un service en échec masque un incident au lieu
  de le traiter. La même logique a guidé le garde-fou du script réseau et la
  simulation par défaut du nettoyage : par défaut, l'automatisation observe, elle
  n'agit pas.
</p>
<p>
  Deuxième leçon : faire générer les rapports par un script supprime une tentation.
  On ne peut pas inventer une sortie qui n'existe pas.
</p>
"""),
        ],
    },
    {
        "slug": "osint-hibp",
        "num": "06",
        "discipline": "OSINT",
        "annee": "2026",
        "titre": "Fiche outil : Have I Been Pwned",
        "lede": (
            "Un outil d'OSINT ne vaut pas par ce qu'il trouve, mais par la décision "
            "qu'il permet de prendre. Analyse complète, avec démonstration du "
            "mécanisme qui protège les mots de passe."
        ),
        "img": "osint",
        "img_caption": "La fiche outil, structurée autour de ce que l'outil ne peut pas révéler.",
        "tags": ["OSINT", "k-anonymat", "SHA-1", "PowerShell"],
        "specs": [
            ("Cadre", "TP outils OSINT, groupe de trois"),
            ("Rôle", "Analyse de l'outil et démonstration"),
            ("Outils", "API Have I Been Pwned, PowerShell, SHA-1"),
            ("Livrable", "Fiche outil et script de démonstration"),
        ],
        "blocs": [
            ("Contexte", """
<p>
  Le TP demandait de présenter un outil d'OSINT. Le piège de cet exercice est de
  recopier la page d'accueil de l'outil. J'ai pris l'angle inverse : partir de ce que
  l'outil <strong>ne peut pas</strong> révéler, parce que c'est cette limite qui
  détermine à quoi il sert vraiment.
</p>
<p>
  La démonstration a été faite sur un domaine public et connu, jamais sur une cible
  privée.
</p>
"""),
            ("Deux services à ne pas confondre", """
<div class="table-wrap">
  <table>
    <thead><tr><th>Service</th><th>Ce qu'on lui donne</th><th>Ce qu'il répond</th></tr></thead>
    <tbody>
      <tr><td>Fuites de comptes</td><td>Une adresse email ou un domaine</td><td>La liste datée des fuites concernées et les catégories de données exposées</td></tr>
      <tr><td>Mots de passe compromis</td><td>Les cinq premiers caractères d'une empreinte SHA-1</td><td>Un nombre d'occurrences dans le corpus</td></tr>
    </tbody>
  </table>
</div>
<p>
  Le nom d'une fuite est un renseignement à part entière : il indique quels services
  une personne utilise. Une adresse présente dans une fuite de forum de loisir ne
  raconte pas la même chose qu'une adresse présente dans une fuite bancaire.
</p>
"""),
            ("La démonstration du k-anonymat", """
<p>
  Le principe : le mot de passe ne quitte jamais la machine.
</p>
<ol class="steps">
  <li>Calcul de l'empreinte SHA-1 du mot de passe, en local.</li>
  <li>Envoi des cinq premiers caractères seulement.</li>
  <li>Réception d'une liste d'empreintes partageant ce préfixe.</li>
  <li>Recherche locale du suffixe exact et affichage du nombre d'occurrences.</li>
</ol>
<p>
  Conséquence directe : le service ne peut pas savoir quel mot de passe a été testé,
  puisqu'il ne reçoit qu'un fragment partagé par des milliers d'autres.
</p>
"""),
            ("Résultat", """
<dl class="kpis">
  <div><dt>Services distingués</dt><dd>2</dd></div>
  <div><dt>Caractères transmis</dt><dd>5</dd></div>
  <div><dt>Mot de passe en clair envoyé</dt><dd>0</dd></div>
</dl>
<p>Et ce que l'outil ne révèle pas, ce qui est la partie décisive.</p>
<ul>
  <li><strong>Jamais le mot de passe en clair</strong>, ni stocké ni servi sous cette forme.</li>
  <li><strong>Rien sur le système d'information</strong> : ni port, ni service, ni version, ni vulnérabilité. Ce n'est pas un moteur de recherche de services exposés.</li>
  <li><strong>Rien sur les fuites non publiées</strong>, qui sont justement les plus dangereuses : un volume interne, une vente sur un forum privé ou un vol par logiciel malveillant pas encore versé au corpus restent invisibles.</li>
</ul>
<p>
  Cette dernière limite change l'usage de l'outil : l'absence de résultat n'est pas
  une preuve d'innocuité, seulement une absence de preuve.
</p>
"""),
            ("Limites", """
<ul>
  <li>Analyse fondée sur la documentation publique et la démonstration, pas sur une évaluation indépendante du corpus.</li>
  <li>Le k-anonymat protège le secret du mot de passe, mais l'appel réseau reste observable dans sa forme et son volume.</li>
  <li>L'automatisation à l'échelle d'un parc n'est pas traitée, alors qu'elle soulève des questions de proportionnalité et de base légale.</li>
  <li>Aucune comparaison avec des outils concurrents.</li>
</ul>
"""),
            ("Ce que j'en retiens", """
<p>
  Un outil d'OSINT produit une donnée, pas une décision. Ce qui a de la valeur, c'est
  de savoir à quelle question il répond et à quelle question il ne répond pas. Ici,
  la question sans réponse est plus importante que celle avec réponse.
</p>
<p>
  Deuxième leçon : la fraîcheur fait l'outil. Un contrôle d'exposition fait une fois
  par an ne vaut presque rien, parce que le corpus bouge en permanence, surtout par
  l'ajout d'identifiants issus de vols par logiciels malveillants. C'est un contrôle
  à planifier, pas à cocher.
</p>
"""),
        ],
    },
]

# --------------------------------------------------------------------------- #
# Création numérique
# --------------------------------------------------------------------------- #

CREA = [
    {
        "slug": "jeu-runner-3d",
        "num": "11",
        "discipline": "Développement web",
        "annee": "2026",
        "titre": "Runner 3D, un jeu de course dans une page",
        "lede": (
            "Un jeu de course sans fin en trois dimensions, jouable dans le navigateur, "
            "avec score, pièces, combo et effet de bloom."
        ),
        "img": "jeu",
        "img_caption": "Écran d'accueil du jeu, rendu trois dimensions et interface de score.",
        "tags": ["Three.js", "WebGL", "Game feel", "Un seul fichier"],
        "specs": [
            ("Cadre", "Projet personnel"),
            ("Rôle", "Conception et développement"),
            ("Moteur", "Three.js et post-traitement"),
            ("Format", "Une seule page, jouable au clavier"),
        ],
        "blocs": [
            ("Contexte", """
<p>
  L'objectif était de vérifier une intuition : est-ce qu'on peut obtenir une
  sensation de jeu correcte dans une simple page, sans moteur ni installation, et
  sans que ça rame ?
</p>
"""),
            ("Ce que j'ai fait", """
<ul>
  <li><strong>Route infinie en trois dimensions</strong>, trois voies, obstacles et pièces générés au fil de la course.</li>
  <li><strong>Sensation de vitesse</strong> par le brouillard, le défilement du décor et la position de caméra.</li>
  <li><strong>Interface de jeu</strong> : distance, record, pièces, indicateur de combo, avec des nombres à chasse fixe pour éviter que le compteur ne danse.</li>
  <li><strong>Post-traitement</strong> avec un effet de halo lumineux sur les éléments clairs, pour sortir du rendu brut.</li>
  <li><strong>Commandes clavier</strong> simples, plus pause et écran de fin, pour que la boucle de jeu soit complète.</li>
</ul>
"""),
            ("Résultat", """
<dl class="kpis">
  <div><dt>Livrable</dt><dd>1 page jouable</dd></div>
  <div><dt>Contrôles</dt><dd>clavier</dd></div>
  <div><dt>Boucle de jeu</dt><dd>complète</dd></div>
</dl>
<p>
  Le jeu se lance, se joue et se termine, avec un score conservé. Aucune
  installation, aucun compte, aucune publicité : le fichier s'ouvre et ça joue.
</p>
"""),
            ("Limites", """
<ul>
  <li>Les bibliothèques sont chargées depuis un réseau de diffusion, donc le jeu a besoin d'une connexion pour démarrer.</li>
  <li>Pas de version mobile : les commandes sont pensées pour un clavier.</li>
  <li>Pas d'optimisation poussée, la complexité de la scène reste volontairement basse.</li>
  <li>Le code est dans un seul fichier, pratique pour partager, moins pour faire évoluer.</li>
</ul>
"""),
            ("Ce que ça démontre", """
<p>
  Une boucle de jeu complète, de l'état d'accueil à l'écran de fin, avec les
  informations qui comptent affichées au bon endroit. Ce n'est pas du design
  d'interface de gestion, c'est du game feel : ce qui donne envie de relancer une
  partie.
</p>
"""),
        ],
    },
    {
        "slug": "bojj-boutique",
        "num": "13",
        "discipline": "Site e-commerce",
        "annee": "2026",
        "titre": "BOJJ Boutique, une boutique de maillots en ligne",
        "lede": (
            "Un site e-commerce complet en HTML, CSS et JavaScript vanilla : catalogue, "
            "fiche produit, panier, checkout simulé et compte client. 125 boutons câblés, "
            "aucun bouton mort, et le site est en ligne."
        ),
        "img": "bojj",
        "img_caption": "La page d'accueil de BOJJ Boutique, déployée sur Vercel.",
        "tags": ["HTML / CSS / JavaScript", "E-commerce", "UI", "Déploiement", "Audit"],
        "specs": [
            ("Cadre", "Projet personnel"),
            ("Rôle", "Design, développement et déploiement"),
            ("Pile", "HTML, CSS et JavaScript vanilla, une page, sans framework"),
            ("En ligne", "bojj-boutique.vercel.app"),
        ],
        "blocs": [
            ("Contexte", """
<p>
  Une boutique de maillots de clubs et de sélections, pensée pour le public de la
  RDC. Le design venait d'un brief importé ; le travail a été de l'implémenter
  vraiment, écran par écran, sans framework et sans backend, jusqu'à une version
  publique.
</p>
<p>
  La contrainte posée était simple à énoncer et exigeante à tenir : <strong>tous les
  boutons du site doivent faire quelque chose</strong>. Un site de démonstration où
  la moitié des liens ne répond pas ne démontre rien.
</p>
"""),
            ("Ce que j'ai fait", """
<ul>
  <li><strong>Dix pages fonctionnelles</strong> : accueil, catalogue, fiche produit, checkout, compte client, paiements, à propos, livraison, contact et les modales du pied de page.</li>
  <li><strong>Navigation et préférences</strong> : sélecteur de langue français/anglais, devises USD, CDF et EUR.</li>
  <li><strong>Catalogue</strong> : filtres par taille, pagination, neuf produits codés en dur.</li>
  <li><strong>Fiche produit</strong> : galerie, choix de la taille et de la version, quantité, onglets description, guide des tailles, livraison et avis, avec recalcul du total en temps réel.</li>
  <li><strong>Checkout</strong> : changement de pays, édition d'adresse, code promo, choix du moyen de paiement (carte, PayPal, Apple Pay, Mobile Money) et confirmation de commande.</li>
  <li><strong>Mini-panier et wishlist</strong> : ouverture, fermeture et compteur dynamique, cœur cliquable partout.</li>
  <li><strong>Validation automatique</strong> : HTML vérifié par parseur, JavaScript par node --check, et clic simulé sur tous les boutons avec jsdom (zéro erreur runtime).</li>
  <li><strong>Déploiement</strong> : en ligne sur Vercel.</li>
</ul>
"""),
            ("Résultat", """
<dl class="kpis">
  <div><dt>Boutons audités</dt><dd>125</dd></div>
  <div><dt>Boutons morts</dt><dd>0</dd></div>
  <div><dt>Produits au catalogue</dt><dd>9</dd></div>
</dl>
<p>
  Le site se parcourt de bout en bout, du catalogue à la confirmation de commande,
  avec un panier qui calcule, une wishlist qui mémorise la sélection pendant la
  visite et un checkout qui vérifie chaque étape.
</p>
"""),
            ("Limites", """
<ul>
  <li><strong>Aucun paiement réel</strong> : le bouton « Payer » simule une confirmation, aucune transaction bancaire n'a lieu.</li>
  <li>Catalogue statique de neuf produits, sans base de données ni administration.</li>
  <li>Le panier et la wishlist ne persistent pas entre les rechargements, faute de stockage local ou de backend.</li>
  <li>Pas de compte client réel : la page « Mon compte » est une maquette avec des données d'exemple.</li>
  <li>Newsletter et formulaire de contact valident la saisie mais n'envoient rien.</li>
  <li>Le contenu anglais n'est pas traduit : la bascule affiche un message.</li>
</ul>
"""),
            ("Ce que ça démontre", """
<p>
  Mener un site e-commerce complet jusqu'à une version en ligne : design, code,
  déploiement, et surtout la discipline de câbler chaque contrôle puis de le
  vérifier automatiquement.
</p>
<p>
  Et une leçon de produit : une démo e-commerce ne se juge pas sur la beauté du
  visuel, mais sur ce qui se passe quand on clique. Ici, tout se passe.
</p>
"""),
        ],
    },
]


# --------------------------------------------------------------------------- #
# Applications mobiles
# --------------------------------------------------------------------------- #

APPS = [
    {
        "slug": "yokason",
        "num": "07",
        "discipline": "Application mobile",
        "annee": "2026",
        "titre": "YokaSon, un lecteur de musique et ses ambiances",
        "lede": (
            "Une application musicale complète en React Native : cinquante-trois "
            "écrans, neuf ambiances illustrées et une identité de marque déclinée."
        ),
        "img": "yoka",
        "img_caption": "L'ambiance « nightdrive », l'une des neuf illustrations d'ambiance de l'application.",
        "tags": ["React Native", "Expo", "Audio", "Identité de marque"],
        "specs": [
            ("Cadre", "Projet personnel"),
            ("Rôle", "Conception, développement et identité visuelle"),
            ("Pile", "Expo 54, React Native 0.81, expo-router"),
            ("État", "En développement actif"),
        ],
        "blocs": [
            ("Contexte", """
<p>
  YokaSon est une application de musique pour Android et iOS. Le point de départ
  n'était pas d'ajouter un lecteur de plus, mais de répondre à une question simple :
  une application de musique peut-elle changer ce qu'on écoute selon le moment, sans
  demander à l'utilisateur de construire des playlists à la main ?
</p>
<p>
  D'où le choix des <strong>ambiances</strong> : étudier, se réveiller, rouler de nuit,
  faire la fête, se relaxer, dormir, faire du sport, voyager. Chacune a son
  illustration et son orientation musicale.
</p>
"""),
            ("Ce que j'ai fait", """
<ul>
  <li><strong>Architecture de navigation complète.</strong> Quatre onglets principaux, puis des écrans dédiés pour un album, un artiste, un genre et une playlist, tous adressables par URL avec le routeur d'Expo.</li>
  <li><strong>Moteur de lecture audio</strong> avec file d'attente, gestion de l'arrière-plan et contrôles système.</li>
  <li><strong>Recherche et bibliothèque</strong> sur des listes virtualisées, pour rester fluide avec de grands catalogues.</li>
  <li><strong>Réglages complets</strong> : apparence et thèmes, audio, compte, services connectés, catalogues avancés, couvertures animées, confidentialité publicitaire, mentions légales.</li>
  <li><strong>Neuf ambiances illustrées</strong>, chacune avec son visuel plein écran.</li>
  <li><strong>Identité de marque</strong> : logo égaliseur, déclinaisons de bannière comparées côte à côte, versions transparentes et monochromes.</li>
  <li><strong>Accès premium</strong> protégé par une clé signée sur courbe elliptique, plutôt qu'un simple booléen stocké sur l'appareil.</li>
</ul>
"""),
            ("Résultat", """
<dl class="kpis">
  <div><dt>Écrans</dt><dd>53</dd></div>
  <div><dt>Ambiances</dt><dd>9</dd></div>
  <div><dt>Fichiers de test</dt><dd>228</dd></div>
</dl>
<p>
  Le projet compte 56 fichiers d'écran dans son dossier de routes et 646 fichiers dans
  le dossier applicatif. C'est de loin le code le plus volumineux que j'aie écrit, et
  celui qui m'a le plus appris sur la structure d'une application réelle.
</p>
"""),
            ("Limites", """
<ul>
  <li>Surface de maintenance large : beaucoup de fonctionnalités dans une seule application.</li>
  <li>Les fichiers de test sont nombreux, mais je n'ai pas de mesure de couverture publiée.</li>
  <li>L'identité visuelle n'est pas arbitrée : plusieurs variantes de bannière cohabitent encore.</li>
  <li>Aucun test de performance sur un appareil d'entrée de gamme, alors que le rendu audio et les listes longues y sont sensibles.</li>
</ul>
"""),
            ("Ce que ça démontre", """
<p>
  Concevoir et tenir une application mobile complète : navigation imbriquée, gestion
  d'état, audio en arrière-plan, thèmes, internationalisation, et une identité
  visuelle qui tient sur neuf déclinaisons.
</p>
<p>
  Et une décision de sécurité que peu d'applications de cette taille prennent : un
  accès premium vérifié par signature cryptographique, pas par un indicateur local
  qu'un utilisateur curieux pourrait modifier.
</p>
"""),
        ],
    },
    {
        "slug": "millionnaire-congolais",
        "num": "08",
        "discipline": "Jeu mobile",
        "annee": "2026",
        "titre": "Le Millionnaire Congolais, jeu de quiz",
        "lede": (
            "Un jeu de culture générale congolaise : parcours d'accueil, quatre onglets, "
            "partie à niveaux, classement, badges et historique."
        ),
        "img": "lmc",
        "img_caption": "L'icône de l'application reprend la bande or et l'étoile du drapeau congolais.",
        "tags": ["React Native", "Expo", "Zustand", "Game design"],
        "specs": [
            ("Cadre", "Projet personnel"),
            ("Rôle", "Conception et développement"),
            ("Pile", "Expo 58, React Native 0.88, Zustand"),
            ("État", "Jouable, en développement"),
        ],
        "blocs": [
            ("Contexte", """
<p>
  Le quiz à niveaux est un format connu, presque usé. L'idée ici était de le
  réancrer : des questions sur la culture, l'histoire et les réalités congolaises, une
  progression qui récompense la régularité plutôt que la chance, et une identité
  visuelle qui ne ressemble pas à un jeu générique.
</p>
"""),
            ("Ce que j'ai fait", """
<ul>
  <li><strong>Parcours d'accueil en trois étapes</strong> : identité, niveau de départ, présentation. Il conditionne l'expérience et évite de poser les mêmes questions à tout le monde.</li>
  <li><strong>Quatre onglets</strong> : accueil, apprendre, jouer, classement, plus un profil.</li>
  <li><strong>Moteur de partie</strong> avec progression par paliers, écran de résultat, historique des parties et modes de jeu.</li>
  <li><strong>Contenu structuré en données</strong> : catégories et badges séparés du code d'affichage, pour pouvoir enrichir le jeu sans y toucher.</li>
  <li><strong>Identité visuelle</strong> dérivée du drapeau congolais : bleu ciel, bande or, étoile, avec une déclinaison en icône et écran de démarrage.</li>
</ul>
"""),
            ("Résultat", """
<dl class="kpis">
  <div><dt>Écrans</dt><dd>15</dd></div>
  <div><dt>Onglets</dt><dd>4</dd></div>
  <div><dt>Modules de données</dt><dd>catégories et badges</dd></div>
</dl>
<p>
  L'application se lance, se parcourt et se joue de bout en bout, avec un état global
  géré proprement et un historique persistant.
</p>
"""),
            ("Limites", """
<ul>
  <li>Le contenu des questions reste limité : la qualité d'un quiz tient à sa base de questions, pas à son interface.</li>
  <li>Le moteur de partie n'a pas de test automatisé, alors que c'est la partie la plus logique du projet.</li>
  <li>Pas de serveur, donc le classement reste local : il ne compare personne.</li>
  <li>Pas encore de build de distribution préparé pour les magasins.</li>
</ul>
"""),
            ("Ce que ça démontre", """
<p>
  Une boucle de jeu complète, du premier lancement à l'écran de résultat, avec un état
  partagé entre les onglets et un contenu séparé du code.
</p>
<p>
  Et le sens de l'identité : reprendre un symbole national et en faire un système
  graphique cohérent, plutôt que plaquer un thème par défaut.
</p>
"""),
        ],
    },
    {
        "slug": "myme",
        "num": "09",
        "discipline": "Application de sécurité",
        "annee": "2026",
        "titre": "MyMe, un espace privé chiffré dans une application ordinaire",
        "lede": (
            "Une application de confidentialité : interface publique banale, espace privé "
            "derrière un code secret et la biométrie, moteur cryptographique testé."
        ),
        "img": "myme",
        "img_caption": "L'icône de MyMe : un monogramme neutre, volontairement sans rapport avec la sécurité.",
        "tags": ["Cryptographie", "React Native", "Tests", "Sécurité mobile"],
        "specs": [
            ("Cadre", "Projet personnel"),
            ("Rôle", "Conception, cryptographie et développement"),
            ("Pile", "Expo 58, React Native 0.88, TypeScript strict"),
            ("État", "Étape 3, authentification en place"),
        ],
        "blocs": [
            ("Contexte", """
<p>
  Une application de confidentialité a un problème que les autres n'ont pas : son
  existence même est une information. Un téléphone qu'on ouvre volontairement devant
  quelqu'un ne doit rien laisser paraître.
</p>
<p>
  D'où le principe de MyMe : une interface publique ordinaire au premier regard, et un
  espace privé chiffré derrière une authentification. Le nom, l'icône et l'écran
  d'accueil sont volontairement neutres.
</p>
"""),
            ("Ce que j'ai fait", """
<ul>
  <li><strong>Moteur cryptographique</strong> bâti sur des bibliothèques auditées : chiffrement authentifié, dérivation de clé, hachage, aléa fourni par le système.</li>
  <li><strong>Espaces privés indépendants</strong> : plusieurs espaces étanches, chacun avec son code, sans qu'un espace puisse révéler l'existence d'un autre.</li>
  <li><strong>Authentification</strong> par code secret, biométrie adossée au stockage protégé de l'appareil, verrouillage automatique et limitation des tentatives.</li>
  <li><strong>259 tests automatisés</strong> sur le moteur, écrits avant l'interface, avec des vecteurs de test connus.</li>
  <li><strong>Documentation d'architecture et de sécurité</strong> : modèle de menace, choix cryptographiques, ce qui est protégé et ce qui ne l'est pas.</li>
  <li><strong>Internationalisation et thèmes</strong> dès le départ, pour ne pas les rétroficer après coup.</li>
</ul>
"""),
            ("Résultat", """
<dl class="kpis">
  <div><dt>Tests automatisés</dt><dd>259</dd></div>
  <div><dt>Fichiers sources</dt><dd>74</dd></div>
  <div><dt>Étape</dt><dd>3 sur 6</dd></div>
</dl>
<p>
  Le socle technique, l'identité visuelle, les thèmes, l'internationalisation et
  l'authentification sont en place, avec la création d'espaces privés et la biométrie.
</p>
<div class="note">
  <p>
    <strong>Un point bloquant, documenté plutôt que masqué :</strong> la dérivation de
    clé Argon2id en JavaScript pur coûte environ 35 secondes sur l'émulateur aux
    paramètres de production. Le calcul doit passer en natif. C'est le genre de mesure
    qu'on préfère trouver soi même avant qu'un utilisateur ne la trouve.
  </p>
</div>
"""),
            ("Limites", """
<ul>
  <li>Aucun coffre-fort de fichiers n'existe encore : c'est l'objet des étapes suivantes.</li>
  <li>La dérivation Argon2id reste trop lente en JavaScript, en attente du passage en natif.</li>
  <li>Le modèle de menace couvre la perte ou le vol de l'appareil, pas un appareil compromis avec privilèges système.</li>
  <li>Pas de build de production signé, donc aucune validation sur appareil physique pour l'instant.</li>
</ul>
"""),
            ("Ce que ça démontre", """
<p>
  Concevoir de la sécurité côté client pour de vrai : choisir des primitives éprouvées
  plutôt que les inventer, écrire les tests avant l'interface, mesurer ce qui coûte
  cher, et documenter ce qui ne marche pas encore.
</p>
<p>
  C'est le projet le plus proche du métier que je vise, et celui dont je parle le plus
  volontiers en entretien, précisément parce qu'il a des limites assumées.
</p>
"""),
        ],
    },
]

PROJETS = CYBER + APPS + CREA
