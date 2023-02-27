Contrats et transactions de déneigement
Ensemble de données contenant les informations sur les contrats de déneigement de la Ville de Montréal ainsi que les données détaillées sur les transactions de transport de la neige par camion des souffleuses aux sites d'élimination de la neige. Plus spécifiquement, les transactions dénombrent les passages de camions chargés de neige accédant à un des sites d'élimination de neige de la Ville de Montréal lors des opérations de déneigement.

Les ensembles sur les secteurs de déneigement et les sites d'élimination de la neige sont également disponibles sur le portail.

https://www.donneesquebec.ca/recherche/dataset/vmtl-contrats-transaction-deneigement

Dernière modification (métadonnées ou ressources)	2023-02-27 01:20 EST
Diffusion initiale	2016-03-14 16:43 EDT
Identifiant	5bfbd75f-7531-48c2-b6b6-072284f7b9e7

Les données sont extraites à partir du système de gestion du transport de la neige utilisé par la Ville de Montréal. Les opérations de déneigement sont gérées en arrondissement.

Au niveau des transactions, les statistiques proviennent des sites d'élimination de la neige. Les camions qui y accédant transmettent à la guérite du site les données captées à la souffleuse.

Un contrat peut inclure plus d'un secteur de déneigement. La table des transactions permet de faire le lien entre les numéros de secteurs et le numéro de contrat.

Les transactions inclues des contrats/secteurs fictifs exécutés par la régie interne (NuméroContrat/NomSecteur = XXX-RE) et des contrats/secteur fictifs d'entités externes à la Ville (NuméroContrat/NomSecteur = EXT-XXX) qui n'ont pas d'associations aux géométries des secteurs puisque associés à l'ensemble de la Ville ou d'un arrondissement.

Note: Les données sur les transactions sont évolutives et en constantes validations, elles sont complétées et corrigées au fil de la saison de déneigement des informations colligées par les arrondissements. Il est donc possible d'y constater des différences mineures, particulièrement dans l'assignation des transactions aux contrats ou à l'ajout de transactions manquantes, entre les versions extraites automatiquement aux deux semaines.

Dictionnaires de données
Contrats

IdentifiantContrat: Identifiant numérique unique du contrat
NuméroContrat: Numéro du contrat, correspondant généralement au secteur de déneigement tel qu'identifié dans l'ensemble de données Secteur de déneigement (*Certains contrats inclus plus d'un secteur - la correspondance exacte entre les numéros de contrats et les secteurs se trouve dans l'ensemble des transactions de déneigement)
TypeContrat: Type de contrat, liste de valeur:

Déneigement: activités complètes de déblaiement, d'épandage trottoir, de chargement et de transport de la neige
Transport: activité de transport uniquement
Régie: Transport de la neige par les camions de la Ville
AnneeContrat: Période couverte par le contrat

IdentifiantArrondissement: Identifiant numérique unique de l'arrondissement
ArrondissementCode: Code de l'arrondissement
Arrondissement: Nom complet de l'arrondissement
DescriptionType: Description des activités incluses dans le contrat
Entreprise: Nom de l'entreprise réalisant le contrat



Transactions

TransactionID: Identifiant unique de la transaction
DateChargement: Date et heure du début du chargement du camion par la souffleuse
Idenfiantsecteur: Identifiant numérique du secteur de provenance de la neige (selon l'ensemble de données Secteur de déneigement). Ce champ prend la valeur NULL lorsqu'il s'agit d'un chargement de neige provenant d'un particulier ou d'un partenaire de la Ville et non des opérations de déneigement de la Ville de Montréal.
NomSecteur: Nom du secteur de provenance de la neige (selon l'ensemble de données Secteur de déneigement). Ce champ prend la valeur NULL lorsqu'il s'agit d'un chargement de neige provenant d'un particulier ou d'un partenaire de la Ville et non des opérations de déneigement de la Ville de Montréal
IdentifiantArrondissement: Identifiant de l'arrondissement de provenance (selon l'ensemble de données Secteur de déneigement)
ArrondissementCode: Identifiant de l'arrondissement de provenance (selon l'ensemble de données Secteur de déneigement)
Arrondissement: Nom de l'arrondissement de provenance (selon l'ensemble de données Secteur de déneigement)
IdentifiantDepot: Identifiant unique du dépôt utilisé (selon l'ensemble de données Dépôt de neige)
NomDepot: Nom du dépôt utilisé (selon l'ensemble de données Dépôt de neige)
DateDéchargement: Date et heure du passage du camion à la guérite du dépôt à neige
Volume: Volume de neige déposé en mètre cube, selon le volume du camion mesuré par les agents techniques de la Ville de Montréal
TypeTransaction: Indicateur d'une transaction autorisée (AUT), non-autorisée (N-AUT) ou en échange d'un coupon (BARCODE) par partenaire de la Ville ou un particulier
IdentifiantContrat: Identifiant du contrat (selon l'ensemble Contrats de déneigement)
NuméroContrat: Nom du contrat (selon l'ensemble Contrats de déneigement)
