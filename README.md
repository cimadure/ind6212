# Polytechnique Montréal - IND6212 - H23

Data Mining School Project

## Problématique

Français:  

* Par Quartiers similaires, quelle est la meilleure stratégie à adopter?  
(si on à du temps, descendre au niveau des secteurs [nettroyage des faux contrats])
* nombre de trajets, unités utilisées / volume, temps, temps déneigement par fenetre temporelle de neige tombée

Anglais:

* Per similar neigorhood, what would be the best snow removal strategy?  
(if we have time, go to sector hierarchy )

## TO-DO

When possible consider the area to normalize data

 0. [ ] table: row:year, columns: #transactions, #transactions/TypeTransaction| #unique secteur, | #depots, #depots/strategy,| #contrats  
  {columns level 0: source (transaction|secteur|contract|...)}
 0. [ ] table: probably a truncate table of ABBREVIATION and Arrondissement name 
 0. [ ] graph: database schema (links between data files)
 0. [ ] graph: x:week; y1:total volume/area ;y2:total snowfall(cm) {from weather}; hue:strategy    {y2 can be made later on}
 0. [ ] table: row:year, column: strategy, value: total volume ?! or [graph (horizontal stacked bars, with volume value inside the bar)](https://docs.bokeh.org/en/latest/docs/examples/topics/hierarchical/crosstab.html) 
 0. [ ] graph: Scatter plot; xy:clustering space; size=volume/area; label=arrondissement; hue:cluster; marker=strategy with best total volume 
     {will help us choose the best data manifold}
 0. [ ] map: arrondissement; color: number of sectors; mark: depot location; annotation=arrondissement  {color: heatmap gradiant}
 0. [ ] map: arrondissement; color: best strategy over years; annotation=arrondissement
 0. [ ] figure: data transformation pipeline


## Back-Up Ideas

### Français:

1. Dépendament du débit de chute de neige, quelle est la meilleur stratégie par quartier?
1. Quels sont les caractéristiques des meilleurs contracteurs selection par strategie et par secteur ?
1. Les secteurs qui se ressemblent ?
1. Qu’est ce qui influence le volume?
1. Les quartiers qui se ressemblent ?
1. Nombre de strategies de déneigement ?

### Anglais:

1. Depend on the snow 'debit' , what best strategy per neighborhoods ?
1. What are the attributes of the best contractors per strategy per sector? 
1. Which sectors are similar?
1. What influences volume?
1. Neighborhoods that look alike?
1. Number of snow removal strategies?


## Data

* [Depots](data/depot/readme.md)
* [Contrats](data/contrat/readme.md)
* [Transactions](data/transaction/readme.md)
* [Limites administratives](data/limite_administrative/readme.md)
* [Secteur](data/secteur/readme.md)

---

## Setup

In the Terminal, having installed Anaconda, execute the following lines.  
Create the environment:
> conda env create --file environment.yml  

Use the environment:
> conda activate ind6212

Launch the notebook to start working:
> jupyter notebook




## Knowledge

- Geospacial
  * https://geopandas.org/en/stable/gallery/choropleths.html
  * https://geopandas.org/en/stable/gallery/polygon_plotting_with_folium.html
  * https://osmnx.readthedocs.io/en/stable/osmnx.html#module-osmnx.stats
- Scikit Learn
  * https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html
  * AMAZING !! https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_set_output.html
- MarkDown 
  * https://www.markdownguide.org/basic-syntax/
  * https://www.w3schools.io/file/markdown-cheatsheet/
  * https://ia.net/writer/support/general/markdown-guide
  * https://www.mkdocs.org/getting-started/
- Visualize
  * https://seaborn.pydata.org/examples/index.html
  * https://docs.bokeh.org/en/latest/docs/gallery.html
  * [QGIS](https://www.qgis.org/en/site/about/screenshots.html#screenshots)
- Anaconda
  * Updating an environment
``conda env update --prefix ./env --file environment.yml  --prune``
  * Generate environment independent of the operating system
``conda env export --name ind6212 --from-history --file environment_gen.yml``
  * Rebuilding a Conda environment from scratch ``conda env create --file environment.yml --force``
  * Remove environment: ``conda env remove --name ind6212``
  * List environments: ``conda info --envs``  

---
## Evaluation
Par équipe de 3, vous devez vous procurer une base de données industrielle et appliquer
judicieusement les méthodes de fouille de données vues en classe.  
Pour chaque fouille, vous devrez préciser : 
 - le but recherché
 - les transformations éventuellement nécessaires à la mise en œuvre de la méthode
 - le réglage de différents paramètres
 - l’analyse critique des résultats 

Le rapport doit faire: 
- 6 pages 
- en français
- Times new Roman, 12pt
- interlignes simples
- simple colonne
- marges de 2cm tout autour
- Dépôt en pdf  

2 points en moins par jour de retard entamé.  
4 points en moins par page supplémentaire entamée.  
Remarque : ne rien trouver dans la base de données avec une méthode particulière est un résultat ! Il faut l’expliquer. Parfois le résultat peut être qu’il n’y a pas de relations de tel type entre tel et tel paramètres.  

**La base de données ET votre analyse devront être déposées avant le 27 avril à 16h.**
 
### Grille
* Nombre de pages
* respecté format (police, langue, propreté)
* Problématique
* description des données (taille, format)
* source des données
* préparation des données
* Choix des outils vs problématique
* Formatage des données vs outil
* Choix et justification des paramêtres outil
* Analyse des résultats
* Critique des résultats vs outils / paramètres
* Critique des résultats vs problématique
* Conclusion
