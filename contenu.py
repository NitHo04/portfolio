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
        "Portfolio de Benitho Ntenda, étudiant en cybersécurité à Nexa Digital School "
        "et créateur numérique. Projets documentés : audit de risque, lab Tor, "
        "simulation de phishing, PSSI, automatisation Linux, OSINT, design imprimé."
    ),
    "kicker": "Portfolio 2026 · Paris",
    "lede": (
        "Je documente ce que je construis, méthode comprise. "
        "<em>Onze projets</em>, du lab réseau jusqu'à l'affiche imprimée en 300 dpi."
    ),
    "facts": [
        ("Statut", "Alternance ou stage"),
        ("Formation", "Nexa Digital School"),
        ("Niveau", "Bac+2 à la rentrée 2026"),
        ("Basé à", "Paris, France"),
    ],
    "strip": [("jeu", "Runner 3D, jeu de course jouable dans le navigateur")],
}

# --------------------------------------------------------------------------- #
# Blocs reutilisables
# --------------------------------------------------------------------------- #

def l(img, cap, cls=""):
    """Figure de fiche."""
    return (img, cap, cls)


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
        "slug": "affiche-atla-el-roi",
        "num": "07",
        "discipline": "Design imprimé",
        "annee": "2026",
        "titre": "Affiche et déclinaisons pour un premier anniversaire",
        "lede": (
            "Une affiche A4 imprimable en 300 dpi, déclinée en format vertical, en "
            "story et en version festive, avec la photo retouchée et détourée."
        ),
        "img": "affiche",
        "img_caption": "Affiche A4, 300 dpi, prête à imprimer. Photo détourée, étalonnée et intégrée.",
        "tags": ["Design imprimé", "Retouche", "Python", "Adobe alternatif"],
        "specs": [
            ("Cadre", "Commande familiale réelle"),
            ("Rôle", "Direction artistique et production"),
            ("Formats", "A4 300 dpi, story 9x16, 4x5"),
            ("Livrables", "10 fichiers finaux, PDF et JPG"),
        ],
        "blocs": [
            ("Contexte", """
<p>
  Un premier anniversaire, une photo de famille, et une demande simple : quelque
  chose de beau, à imprimer et à partager. C'est le type de projet où l'on juge le
  résultat sur l'impression, pas sur l'écran, et où une faute de résolution se voit
  tout de suite.
</p>
"""),
            ("Ce que j'ai fait", """
<ol class="steps">
  <li><strong>Direction artistique.</strong> Palette crème et brun, typographie à empattements, hiérarchie de l'information en quatre niveaux : événement, prénom, âge, citation.</li>
  <li><strong>Détourage et étalonnage.</strong> Sujet isolé de son arrière-plan, puis fondu dans un fond sombre avec des ballons et une texture de poussière lumineuse.</li>
  <li><strong>Composition.</strong> Cadre photo, filets typographiques, texte justifié centré, citation biblique et date.</li>
  <li><strong>Déclinaisons.</strong> Version A4 verticale, version story 9x16, format 4x5, et une variante festive. Même système, formats différents.</li>
  <li><strong>Production.</strong> Export 300 dpi, contrôle des polices et des glyphes, PDF prêt à imprimer et JPG pour le partage.</li>
  <li><strong>Automatisation.</strong> Le rendu est piloté par script plutôt qu'à la main, pour régénérer une variante en changeant un paramètre.</li>
</ol>
"""),
            ("Résultat", """
<dl class="kpis">
  <div><dt>Livrables finaux</dt><dd>10 fichiers</dd></div>
  <div><dt>Résolution</dt><dd>300 dpi</dd></div>
  <div><dt>Formats</dt><dd>A4, 9x16, 4x5</dd></div>
</dl>
<p>
  L'affiche existe en version imprimable et en version écran, avec la photo retouchée
  livrée séparément et sans texte, ce qui permet de la réutiliser. Les fichiers sont
  nommés et classés pour être retrouvés six mois plus tard.
</p>
"""),
            ("Limites", """
<ul>
  <li>Projet affectif, donc les arbitrages esthétiques ont été guidés par la demande familiale plus que par ma seule préférence.</li>
  <li>La photo est exposée ici avec l'accord implicite de publier ce travail ; elle reste une image privée.</li>
  <li>Pas de contrôle colorimétrique avec le profil de l'imprimeur, donc la fidélité en impression reste approximative.</li>
  <li>La chaîne de rendu par script gagnerait à être factorisée, plusieurs versions de scripts se sont succédé.</li>
</ul>
"""),
            ("Ce que ça démontre", """
<p>
  Tenir une direction artistique jusqu'au fichier imprimable, et pas seulement
  jusqu'à une image qui rend bien sur un écran. Comprendre qu'une déclinaison n'est
  pas un redimensionnement : le format vertical impose de recomposer.
</p>
<p>
  Et un réflexe d'automatisation : ce qui se répète d'un format à l'autre doit être
  produit par du code, pas refait à la main.
</p>
"""),
        ],
    },
    {
        "slug": "wallpapers",
        "num": "08",
        "discipline": "Direction artistique",
        "annee": "2026",
        "titre": "Série de fonds d'écran, un visuel et ses déclinaisons",
        "lede": (
            "Un même visuel décliné en dizaines de variantes et sur trois formats : 8K, "
            "4K et écran de téléphone. Un système de design, pas un one-shot."
        ),
        "img": "wallpaper",
        "img_caption": "Version 4K du fond d'écran, contraste élevé et zone sombre pour les icônes.",
        "tags": ["Direction artistique", "Composition", "Upscale", "Déclinaisons"],
        "specs": [
            ("Cadre", "Projet personnel"),
            ("Rôle", "Direction artistique et production"),
            ("Formats", "8K, 4K, téléphone 1206 x 2622"),
            ("Livrables", "Série de variantes nommées"),
        ],
        "blocs": [
            ("Contexte", """
<p>
  Un fond d'écran n'est pas une image qu'on regarde, c'est une image derrière des
  icônes. Le vrai problème n'est pas de faire joli, c'est de garder une zone calme
  là où le système pose ses éléments, et de tenir sur des formats très différents.
</p>
<p>
  L'illustration de départ n'est pas de moi. Le travail porte sur la composition, le
  traitement et le système de déclinaisons.
</p>
"""),
            ("Ce que j'ai fait", """
<ul>
  <li><strong>Composition autour des zones d'interface.</strong> Masse sombre à gauche, sujet à droite, dégradé latéral pour que les icônes restent lisibles.</li>
  <li><strong>Série de traitements.</strong> Sérigraphie une encre, sérigraphie deux encres, duotone, poster, pellicule, collage, glitch, noir mat, fond flou léger et moyen, version couleur en grand.</li>
  <li><strong>Déclinaison par format.</strong> 8K et 4K pour l'écran, format vertical pour téléphone, avec recadrage et recomposition à chaque fois, pas un simple redimensionnement.</li>
  <li><strong>Comparaison de pistes.</strong> Plusieurs propositions montrées côte à côte, puis une sélection argumentée plutôt qu'un choix au hasard.</li>
  <li><strong>Montée en résolution.</strong> Passage par un modèle d'augmentation de résolution pour tenir le 8K sans artefacts visibles.</li>
</ul>
"""),
            ("Résultat", """
<dl class="kpis">
  <div><dt>Variantes produites</dt><dd>des dizaines</dd></div>
  <div><dt>Formats</dt><dd>3</dd></div>
  <div><dt>Résolution max</dt><dd>8K</dd></div>
</dl>
<p>
  La série est nommée, donc retrouvable : chaque variante a un identifiant de
  traitement et de format. C'est ce qui transforme une collection d'images en
  système.
</p>
"""),
            ("Limites", """
<ul>
  <li>L'illustration de base appartient à une œuvre existante, le travail porte sur la composition et le traitement.</li>
  <li>La montée en résolution reste une interpolation : elle ne crée pas de détail absent de la source.</li>
  <li>Beaucoup de variantes explorées, peu sélectionnées et documentées. Le tri aurait dû venir plus tôt.</li>
  <li>Aucun test de lisibilité réelle sur téléphone avec les icônes du système par dessus.</li>
</ul>
"""),
            ("Ce que ça démontre", """
<p>
  Construire un système de déclinaisons cohérent plutôt qu'une image unique :
  identifiants de variante, contraintes par format, sélection argumentée.
</p>
<p>
  Et une compétence directement utile ailleurs : comprendre qu'une image d'interface
  doit être composée pour l'interface, pas pour elle même.
</p>
"""),
        ],
    },
    {
        "slug": "montage-video",
        "num": "09",
        "discipline": "Montage vidéo",
        "annee": "2026",
        "titre": "Montage vidéo d'un événement familial",
        "lede": (
            "Un diaporama animé de seize plans, habillé, sonorisé et rendu, avec des "
            "planches de contrôle avant livraison."
        ),
        "img": "video",
        "img_caption": "Carton de titre du montage, fond flouté et typographie centrée.",
        "tags": ["Montage", "Habillage", "Rythme", "Contrôle qualité"],
        "specs": [
            ("Cadre", "Commande familiale"),
            ("Rôle", "Montage et habillage"),
            ("Livrable", "Vidéo MP4, seize plans"),
            ("Contrôles", "Planches de vérification"),
        ],
        "blocs": [
            ("Contexte", """
<p>
  Un événement de famille, beaucoup de photos prises par plusieurs personnes, et une
  vidéo à produire pour que l'ensemble se regarde au lieu de se feuilleter. Le
  problème est un problème de rythme : trop lent on s'ennuie, trop rapide on ne
  reconnaît personne.
</p>
"""),
            ("Ce que j'ai fait", """
<ol class="steps">
  <li><strong>Sélection et ordre.</strong> Tri des photos et construction d'une progression : carton d'ouverture, portraits, scènes de groupe, moments, carton de clôture.</li>
  <li><strong>Habillage.</strong> Chaque photo posée dans un cadre, sur un fond flouté de la même image pour éviter les bandes noires et garder la cohérence chromatique.</li>
  <li><strong>Cartons typographiques.</strong> Ouverture et fermeture avec le nom de l'événement et du couple, typographie centrée, pas de fioriture.</li>
  <li><strong>Bande son.</strong> Piste audio montée à la durée, avec les points de coupe calés sur les changements de séquence.</li>
  <li><strong>Contrôle qualité.</strong> Planches de vignettes générées pour vérifier d'un coup d'œil l'ensemble des plans avant rendu final.</li>
  <li><strong>Rendu</strong> en MP4, avec vérification de la durée et de la synchronisation.</li>
</ol>
"""),
            ("Résultat", """
<dl class="kpis">
  <div><dt>Plans montés</dt><dd>16</dd></div>
  <div><dt>Livrable</dt><dd>1 vidéo MP4</dd></div>
  <div><dt>Contrôles</dt><dd>planches de vignettes</dd></div>
</dl>
<p>
  La vidéo existe en un fichier unique, prêt à être partagé tel quel, sans logiciel
  particulier pour la lire.
</p>
"""),
            ("Limites", """
<ul>
  <li>Seize plans pour un événement entier, c'est court : beaucoup de photos n'ont pas été retenues.</li>
  <li>Les photos n'ont pas toutes été prises dans les mêmes conditions de lumière, et l'étalonnage reste léger.</li>
  <li>Pas de sous-titres ni de version courte, qui auraient aidé au partage sur mobile.</li>
  <li>Le rendu n'a pas été vérifié sur plusieurs lecteurs, seulement sur le mien.</li>
</ul>
"""),
            ("Ce que ça démontre", """
<p>
  Monter, ce n'est pas aligner des images : c'est décider d'un rythme et d'un
  habillage qui rendent l'ensemble regardable. Et c'est accepter de couper beaucoup
  pour garder l'essentiel.
</p>
<p>
  Le réflexe de contrôle qualité compte autant : générer une planche de tous les
  plans permet de repérer une faute de cadrage avant le rendu, pas après.
</p>
"""),
        ],
    },
    {
        "slug": "page-de-garde",
        "num": "10",
        "discipline": "Automatisation documentaire",
        "annee": "2026",
        "titre": "Page de garde universitaire générée par script",
        "lede": (
            "Une page de garde conforme à une charte institutionnelle, produite par un "
            "script paramétrable plutôt que retapée à chaque travail."
        ),
        "img": "garde",
        "img_caption": "Page de garde générée, en-tête officiel, logo et bloc d'identification.",
        "tags": ["Python", "Document", "Charte", "Gabarit"],
        "specs": [
            ("Cadre", "Service rendu à une étudiante"),
            ("Rôle", "Script et gabarit"),
            ("Sortie", "Document échangeable et modifiable"),
            ("Paramètres", "Filière, cours, professeur"),
        ],
        "blocs": [
            ("Contexte", """
<p>
  Un travail universitaire doit commencer par une page de garde au format imposé :
  en-tête du ministère, nom de l'université, logo, filière, intitulé du cours,
  mention du travail, nom de l'étudiant, nom du professeur, année académique.
</p>
<p>
  Retapée à la main, cette page est une source d'erreurs et de perte de temps, et le
  format se dégrade d'un travail à l'autre. La demande était donc : la même page, en
  changeant seulement ce qui change.
</p>
"""),
            ("Ce que j'ai fait", """
<ul>
  <li><strong>Gabarit complet</strong> avec en-tête institutionnel, logo, filière, intitulé, bloc de réalisation et année, aligné sur le document d'origine.</li>
  <li><strong>Paramétrage.</strong> Les éléments variables sont regroupés en tête de script : changer de cours ou de professeur ne demande aucune retouche de mise en forme.</li>
  <li><strong>Sortie modifiable.</strong> Le document produit reste éditable, pour que l'étudiante puisse corriger un détail sans revenir au code.</li>
  <li><strong>Respect de la charte.</strong> Tailles, graisses et alignements reproduits à l'identique, y compris les cas où le document d'origine était approximatif.</li>
</ul>
"""),
            ("Résultat", """
<p>
  Une page de garde au format exact, régénérable en une commande pour n'importe quel
  cours. Le temps passé sur la mise en forme tombe à zéro, et le risque de faute de
  frappe dans un nom officiel aussi.
</p>
"""),
            ("Limites", """
<ul>
  <li>Le gabarit est fidèle à un document précis : une autre université demanderait un autre gabarit.</li>
  <li>Pas de vérification automatique du rendu, la page a été contrôlée visuellement.</li>
  <li>Le script ne gère qu'une page, pas la structure complète du document.</li>
</ul>
"""),
            ("Ce que ça démontre", """
<p>
  Repérer une tâche répétitive, la formaliser en gabarit, et rendre les variables
  explicites au lieu de les disperser dans la mise en forme.
</p>
<p>
  C'est la même logique que pour un rapport technique ou un runbook : ce qui se
  répète doit être écrit une fois, proprement.
</p>
"""),
        ],
    },
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
]

PROJETS = CYBER + CREA
