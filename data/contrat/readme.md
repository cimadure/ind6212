# Contrats

### Dictionnaires de données

|Variable|Définition|
|:--- | :--- |
|IdentifiantContrat| Identifiant numérique unique du contrat|
|NuméroContrat| Numéro du contrat, correspondant généralement au secteur de déneigement tel qu'identifié dans l'ensemble de données Secteur de déneigement (*Certains contrats inclus plus d'un secteur - la correspondance exacte entre les numéros de contrats et les secteurs se trouve dans l'ensemble des transactions de déneigement)|
|TypeContrat| Type de contrat<br/>liste de valeur:<br/>- Déneigement: activités complètes de déblaiement, d'épandage trottoire, de chargement et de transport de la neige<br/> - Transport: activité de transport uniquement<br/> - Régie: Transport de la neige par les camions de la Ville|
|AnneeContrat| Période couverte par le contrat|
|IdentifiantArrondissement| Identifiant numérique unique de l'arrondissement|
|ArrondissementCode| Code de l'arrondissement|
|Arrondissement| Nom complet de l'arrondissement|
|DescriptionType| Description des activités incluses dans le contrat|
|Entreprise| Nom de l'entreprise réalisant le contrat|



## Contrats et transactions de déneigement

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


