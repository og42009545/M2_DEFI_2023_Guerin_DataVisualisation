# Le concours de l'Eurovision 
## Table des Matières

- [Présentation du sujet](#présentation-du-sujet)
- [Collecte des données](#collecte-des-données)
- [Nettoyage et enrichissement des données](#nettoyage-et-enrichissement-des-données)
- [Visualisations et editorialisations](#visualisations-et-editorialisations)
- [Conclusion](#conclusion)

# Présentation du sujet
J'ai décidé de travailler sur le **concours de l'Eurovision** (version adulte). En effet, je suis une grande fan de l'Eurovision, depuis petite, que je regarde chaque année. Malheureusement, la France n'a pas gagné depuis **1977** avec la chanson de **Marie Myriam** *L'Oiseau et L'Enfant* ce qui me chagrine énormément. De ce fait, j'aimerais estimer les chances de la France cette année, puisque notre représentant et notre chanson ont déjà été dévoilés. En effet, pour l'édition de 2024, c'est le chanteur **Slimane** qui va représenter la France, avec la chanson *Mon Amour*.

![Photo de Slimane, représentant de la France pour le concours de l'Eurovision en 2024](/images/Eurovision_2024_France_Slimane_MonAmour.jpg)

***Image** : Slimane, représentant de la France pour le concours de l'Eurovision en 2024*

[![Clip officiel de la chanson "Mon Amour" de Slimane](https://img.youtube.com/vi/bal8oESDH7s/0.jpg)](https://www.youtube.com/watch?v=bal8oESDH7s)

***Vidéo** : Clip officiel de la chanson "Mon Amour" de Slimane*

# Collecte des données
## Jeu de données utilisé
Pour ce sujet, j'ai décidé de m'appuyer sur le jeu de données de l'utilisatrice GitHub **Spijkervet** qui propose dans un repository *eurovision-dataset* un ensemble de données concernant le concours de 1956 à 2023.

J'ai décidé de me concentrer sur **la release de 2023**, la plus à jour. Je n'ai gardé que le fichier **contestants.csv**.

**Pourquoi?**
Ce qui m'intéresse c'est d'évaluer les chances de Slimane au concours et donc pour cela, il me faut comparer notre représentant et notre chanson avec les autres participants (*contestants*). Mon but va être de voir ce qui fonctionne mieux à l'Eurovision en analysant notamment les vainqueurs pour voir si notre représentant et notre chanson rentrent dans les critères.

J'ajouterai des informations via WIKIDATA (par exemple, géolocalisation des pays).

### Liens :
* [Source du repository](https://github.com/Spijkervet/eurovision-dataset/)
* [Source du fichier contestants.csv](https://github.com/Spijkervet/eurovision-dataset/releases/)

*Remarque* : Le fichier contestants.csv peut être trouvé [également au sein de ce projet](/sources/contestants.csv).

## Contrôle qualité

Je réalise un contrôle qualité allégé (10 points) de ce jeu de données. 

|   Point de contrôle qualité   |   Problème observé et commentaire |   Correction : comment ? importance ? |
|---    |---    |---   |
| Le jeu de données est difficilement accessible (format “image”, PDF, HTML...), le fichier est mal formé   |   Le jeu de données est facilement accessible, puis qu’il est au format csv, format non-propriétaire.   | Rien à signaler. | 
| La licence est absente ou inhabituelle, le jeu de données n’est pas “open data”   |  Le jeu de données est open data : on n’a pas besoin de s’inscrire à Github pour accéder au fichier contestants.csv. Cependant, il n’y a pas de licence puisque c’est une initiative de fans de l’Eurovision. En revanche, dans le readme du repository, il est notifié la source des données scrapées (« The metadata and voting data are provided by the EurovisionWorld fansite. ») et il est également possible de télécharger les fichiers python pour reproduire l’ensemble des jeux de données (« You can download the entire dataset using the scraping code included in this repository. »). Par contre, il est demandé de citer les auteurs du jeu de données.|   Ce n’est pas une plateforme d’open data, mais on voit qu’il y a une volonté de sérieux de la part des personnes à l’initiative du projet. |
| Le fichier fait peu appel aux standards répandu et aux données pivots   |  Ici on a du csv, ce qui correspond à ce qui est répandu et recommandé (format non-propriétaire).    |   Rien à signaler.|
| Le fichier est mal documenté  |    Le fichier est documenté : en effet, il est possible d'avoir une explication sur les champs du fichier dans le read me du repository. | Dans le cadre du projet, on remarque qu'il y a des colonnes qui seront à supprimer (par exemples, celles concernant les demi-finales puisque les pays comme les Big Five et le pays organisateur ne participent pas aux demi-finales). | 
| Il existe des problèmes de syntaxe  |  Il existe quelques problèmes de cohérence : tout d’abord, dans la colonne « to_country_id », on remarque qu’il y a parfois l’id (qui lui n’est pas documenté) du pays pour lequel le représentant concoure, ou le nom écrit directement. Au niveau des colonnes concernant les points obtenus et la place finale (que cela soit en demi-finale ou en finale), il y a aussi un souci de cohérence : parfois on a des nombres décimaux (15.0 pour 15ème place) et parfois on a des nombres entiers (15).  |   On supprimera cette colonne et on se basera sur la colonne « to_country ». On prendra des valeurs décimales pour les points, mais des valeurs entières pour la place obtenue. |
| Valeurs aberrantes, suspectes, inexplicables, pas crédibles   |  A part le fait qu’on aurait dû gagner avec Barbara Pravi, non rien d’aberrant. La seule colonne qui m’a fait tiquée est « sf_num » car je voyais pleins de 1.0 / 2.0 mais c’est en fait le numéro de la demi-finale à laquelle le participant a pris part et c’est expliqué dans la documentation. De plus, il y a eu parfois au début plusieurs gagnants et des ex-aequo donc il est normal d’avoir parfois plusieurs gagnants pour les premières éditions du concours. |  Rien à signaler. |
| Il manque des données et cela n’est pas documenté (trous, données tronquées, valeurs vides, granularité / fréquence / maillage / fraîcheur)  |  Oui, il y a beaucoup de trous et ce n’est pas expliqué. Cependant, si on connait un peu le principe de l’Eurovisions ces trous sont explicables.Pour la colonne « sf_num », il y a des trous car pendant très longtemps il n’y a pas eu de demi-finales car il y avait très peu de pays qui participaient (surtout dans les premières années du concours).Pour « running_sf » et « running_final », il y a des trous car tous les pays ne prennent pas part aux demi-finales (c’est le cas des cinq pays fondateurs de l’Eurovision, les Big Five, dont fait partie la France mais aussi du pays organisateur) ni aux finales (si le pays perd en demi-finale, il ne peut pas participer en finale).Pour les colonnes liées aux points attribués par le jury et le télévote, les trous s’expliquent de différentes manières : le site qui sert pour la captation des données n’a pas toutes les données, notamment des premières années. Des plus, le télévote n’existait pas au départ. On voit aussi des écarts dans le nombre de points qu’obtiennent par exemple les gagnants : c’est parce qu’il y a entre autres maintenant beaucoup plus de pays participants qu’au début. Les données sont fraîches car contiennent la dernière édition de mai 2023. | Ne pas se baser sur les colonnes relatives aux nombres de points et aux demi-finales. | 
| Trop de données : doublons, inutilement vieilles, précision / fréquence / maillage / fraîcheur  | Le fichier contient 1735 lignes. Il n’y a pas de doublons : par exemple, il y a des chanteurs (Mahmood, Sergey Lazarev etc.) qui ont participé à plusieurs éditions. Par contre il y a des données inutiles, type lyrics (paroles) : à part si on étudie les chansons gagnantes et qu’elles seraient dans la même langue (ce qui n’est pas le cas, donc il faudrait les traduire), les paroles sont difficilement exploitables. Idem pour la colonne sur l'url youtube. |   Supprimer la colonne lyrics et youtube. |
| Données posant problème avec la réglementation (données perso, relatives à la santé, la religion..., propriété littéraire et artistique, etc.)   |    Les informations dans ce jeu de données sont publiques : le nom des chanteurs, de la chanson, les paroles, les données liées à l’ordre de passage, les points etc… sont fournis par le concours de l’Eurovision lui-même.  |  Rien à signaler. |
| Les contenus posent problèmes : synonymies, non traduits (USA), cryptique (DAECPP), utilisation du 0 au lieu du “null”...  |    Le seul souci repose sur les id des pays qui n’est pas défini, mais on peut se passer de cette colonne grâce à la colonne « to_country ».  | Utiliser la colonne « to_country ».  |

***Tableau** : Contrôle qualité du jeu de données contestants.csv*

### Liens :
* [Source du readme du repository](https://github.com/Spijkervet/eurovision-dataset?tab=readme-ov-file#data-description)
* [Contrôle qualité au format PDF](/autres/M2_DEFI_2023_Guerin_SprintQualite.pdf).


# Nettoyage et enrichissement des données
## Nettoyage via OpenRefine 

Je procède au data-wrangling de mon fichier contestants.csv via OpenRefine. 
Pour ce faire, j'ai rédigé un document relatant toutes mes taches (enrichissement inclus).

## Enrichissement via WikiData
Pour l'enrichissement j'ai utilisé d'une part WikiData (directement via OpenRefine) pour récupérer le genre de l'artiste et le type d'artiste (groupe ou solo) et un Script Python pour détecter les langues de chaque chanson.

### Liens :
* [Explication des étapes de nettoyage et d'enrichissement via WIKIDATA/script Python](/autres/M2_DEFI_2023_Guerin_OpenRefineWikiData.pdf).
* [Script Python pour la détection de langues, conçu par moi-même](/sources/langue.py).
* [CSV d'export d'OpenRefine](/sources/M2_DEFI_2023_Guerin_Eurovision_ExportOpenRefine.csv).
* [Historique d'OpenRefine](/sources/M2_DEFI_2023_Guerin_Eurovision_Historique.json).
* [CSV final](/sources/M2_DEFI_2023_Guerin_Eurovision_PostOpenRefine.csv).


# Visualisations et editorialisations
## L'Eurovision en bref
### Les victoires par pays

J'ai réalisé une copie de mon CSV final afin de filter mes données pour réaliser ma première visualisation. En effet, je veux d'abord visualiser une carte des pays ayant remporté le concours, avec le nombre de victoires. Pour ce faire, je ne garde que les lignes où le place_contest = 1, puis j'ajoute une colonne dans LibreOffice qui s'appelle "nbVictoires" ou je fais une fonction NBSI pour compter le nombre de fois où un pays apparait afin de déterminer le nombre de victoires. Je supprime d'autres colonnes (ex: coordonnées de géolocalisation car finalement DataWrapper va les trouver automatiquement). Sur Datawrapper je réalise une "Symbol Map".

<iframe title="Les pays qui ont gagné l'Eurovision" aria-label="Map" id="datawrapper-chart-azGjB" src="https://datawrapper.dwcdn.net/azGjB/2/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="810" data-external="1"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"]){var e=document.querySelectorAll("iframe");for(var t in a.data["datawrapper-height"])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data["datawrapper-height"][t]+"px";e[r].style.height=i}}}))}();
</script>

On s'aperçoit donc que la France est une nation pas si mauvaise que l'on prétend être au concours puisque nous avons gagné 5 fois. Cependant, notre dernière victoire remonte à...1977.

#### Fichier utilisé pour cette première visualisation
* [CSV de la première visualisation](/sources/M2_DEFI_2023_Guerin_Eurovision_PremiereVisualisation.csv).

### La France à l'Eurovision

Je décide donc de comparer la France aux autres grandes nations qui ont gagné minimum 5 fois l'Eurovision, à savoir Le Luxembourg, La Suède, les Pays Bas, Le Royaume Uni et l'Irlande.

Je réalise une timeline sur Flourish. Pour ce faire j'ai dû réarranger mes données pour avoir en colonne les années et en ligne les places obtenues selon les pays. Je réalise cette transformation sur libreoffice via des copier/coller en "Transposer".

Mon seul soucis concernait les années où les pays n'ont pas participé à l'Eurovision : j'ai remplacé mes "non applicable" en case vide.

<div class="flourish-embed flourish-chart" data-src="visualisation/16447744"><script src="https://public.flourish.studio/resources/embed.js"></script></div>


## Comment ganger à l'Eurovision ?
### Zoom sur les dix derniers gagnants (2012-2023)
### Exploration de différentes pistes (le genre, la langue, artiste solo/groupe etc.)

# Conclusion
# Sources
