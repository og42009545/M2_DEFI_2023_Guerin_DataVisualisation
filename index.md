# Le concours de l'Eurovision 
## Table des Matières

- [Présentation du sujet](#présentation-du-sujet)
- [Collecte des données](#collecte-des-données)
- [Nettoyage et enrichissement des données](#nettoyage-et-enrichissement-des-données)
- [Visualisations et editorialisations](#visualisations-et-editorialisations)
- [Conclusion](#conclusion)

# Présentation du sujet
J'ai décidé de travailler sur le **concours de l'Eurovision** (version adulte). En effet, je suis une grande fan de l'Eurovision, depuis petite, et je regarde chaque année le concours. Malheureusement, la France n'a pas gagné depuis **1977** avec la chanson de **Marie Myriam** *L'Oiseau et L'Enfant*, ce qui me chagrine énormément. De ce fait, j'aimerais estimer les chances de la France cette année, puisque notre représentant et notre chanson ont déjà été dévoilés. En effet, pour l'édition de 2024, c'est le chanteur **Slimane** qui va représenter la France, avec la chanson *Mon Amour*.

![Photo de Slimane, représentant de la France pour le concours de l'Eurovision en 2024](/images/Eurovision_2024_France_Slimane_MonAmour.jpg)

***Image** : Slimane, représentant de la France pour le concours de l'Eurovision en 2024* / [Source](https://www.francetelevisions.fr/et-vous/notre-tele/a-ne-pas-manquer/lartiste-slimane-portera-les-couleurs-de-la-france-a-leurovision-2024-21456)

[![Clip officiel de la chanson "Mon Amour" de Slimane](https://img.youtube.com/vi/bal8oESDH7s/0.jpg)](https://www.youtube.com/watch?v=bal8oESDH7s)

***Vidéo** : Clip officiel de la chanson "Mon Amour" de Slimane*

# Collecte des données
## Jeu de données utilisé
Pour ce sujet, j'ai décidé de m'appuyer sur le jeu de données de l'utilisatrice GitHub **Spijkervet** qui propose dans un repository *eurovision-dataset* un ensemble de données concernant le concours de 1956 à 2023.

J'ai décidé de me concentrer sur **la release de 2023**, la plus à jour. Je n'ai gardé que le fichier **contestants.csv**.

**Pourquoi ?**
Ce qui m'intéresse c'est d'évaluer les chances de Slimane au concours et donc pour cela, il me faut comparer notre représentant et notre chanson avec les autres participants (*contestants*). Mon but va être de voir ce qui fonctionne mieux à l'Eurovision (un chanteur homme ? un groupe ? une chanson en anglais ?).

J'ajouterai des informations directement sur OpenRefine via un enrichissement WikiData (par exemple, géolocalisation des pays).

### Liens :
* [Source du repository](https://github.com/Spijkervet/eurovision-dataset/)
* [Source du fichier contestants.csv](https://github.com/Spijkervet/eurovision-dataset/releases/)

*Remarque* : Le fichier contestants.csv peut être trouvé [également au sein de ce projet](/sources/contestants.csv).

## Contrôle qualité

Je réalise un contrôle qualité allégé (10 points) de ce jeu de données. 

|   Point de contrôle qualité   |   Problème observé et commentaire |   Correction : comment ? importance ? |
|---    |---    |---   |
| Le jeu de données est difficilement accessible (format “image”, PDF, HTML...), le fichier est mal formé   |   Le jeu de données est facilement accessible, puisqu’il est au format csv, format non-propriétaire.   | Rien à signaler. | 
| La licence est absente ou inhabituelle, le jeu de données n’est pas “open data”   |  Le jeu de données est open data : on n’a pas besoin de s’inscrire à Github pour accéder au fichier contestants.csv. De plus, il n’y a pas de licence puisque c’est une initiative de fans de l’Eurovision. En revanche, dans le readme du repository, il est notifié la source des données scrapées (« The metadata and voting data are provided by the EurovisionWorld fansite. ») et il est également possible de télécharger les fichiers python pour reproduire l’ensemble des jeux de données (« You can download the entire dataset using the scraping code included in this repository. »). Par contre, il est demandé de citer les auteurs du jeu de données.|   Ce n’est pas une plateforme d’open data, mais on voit qu’il y a une volonté de sérieux de la part des personnes à l’initiative du projet. |
| Le fichier fait peu appel aux standards répandu et aux données pivots   |  Ici on a du csv, ce qui correspond à ce qui est répandu et recommandé (format non-propriétaire).    |   Rien à signaler.|
| Le fichier est mal documenté  |    Le fichier est documenté : en effet, il est possible d'avoir une explication sur les champs du fichier dans le read me du repository. | Dans le cadre du projet, on remarque qu'il y a des colonnes qui seront à supprimer (par exemples, celles concernant les demi-finales puisque les pays comme les Big Five et le pays organisateur ne participent pas aux demi-finales). | 
| Il existe des problèmes de syntaxe  |  Il existe quelques problèmes de cohérence : tout d’abord, dans la colonne « to_country_id », on remarque qu’il y a parfois l’id (qui lui n’est pas documenté) du pays pour lequel le représentant concoure, ou le nom écrit directement. Au niveau des colonnes concernant les points obtenus et la place finale (que cela soit en demi-finale ou en finale), il y a aussi un souci de cohérence : parfois on a des nombres décimaux (15.0 pour 15ème place) et parfois on a des nombres entiers (15).  |   On supprimera la colonne « to_country_id » et on se basera sur la colonne « to_country ». On prendra des valeurs décimales pour les points, mais des valeurs entières pour la place obtenue. |
| Valeurs aberrantes, suspectes, inexplicables, pas crédibles   |  A part le fait qu’on aurait dû gagner avec Barbara Pravi, non rien d’aberrant. La seule colonne qui m’a fait tiquée est « sf_num » car je voyais pleins de 1.0 / 2.0 mais c’est en fait le numéro de la demi-finale à laquelle le participant a pris part et c’est expliqué dans la documentation. De plus, il y a eu parfois au début plusieurs gagnants et des ex-aequo donc il est normal d’avoir parfois plusieurs gagnants pour les premières éditions du concours. |  Rien à signaler. |
| Il manque des données et cela n’est pas documenté (trous, données tronquées, valeurs vides, granularité / fréquence / maillage / fraîcheur)  |  Oui, il y a beaucoup de trous et ce n’est pas expliqué. Cependant, si on connait un peu le principe de l’Eurovisions ces trous sont explicables. Par exemple, pour la colonne « sf_num », il y a des trous car pendant très longtemps il n’y a pas eu de demi-finales car il y avait très peu de pays qui participaient (surtout dans les premières années du concours). Concernant les colonnes « running_sf » et « running_final », il y a des trous car tous les pays ne prennent pas part aux demi-finales (c’est le cas des cinq pays fondateurs de l’Eurovision, les Big Five, dont fait partie la France mais aussi le pays organisateur qui échappe à la demi-finale) ni aux finales (si le pays perd en demi-finale, il ne peut pas participer en finale). Pour les colonnes liées aux points attribués par le jury et le télévote, les trous s’expliquent de différentes manières : le site qui sert pour la captation des données n’a pas toutes les données, notamment des premières années. Des plus, le télévote n’existait pas au départ. On voit aussi des écarts dans le nombre de points qu’obtiennent par exemple les gagnants : c’est parce qu’il y a entre autres maintenant beaucoup plus de pays participants qu’au début (il y a donc plus de points à distribuer). Les données sont fraîches car contiennent la dernière édition de mai 2023. | Ne pas se baser sur les colonnes relatives aux nombres de points et aux demi-finales. | 
| Trop de données : doublons, inutilement vieilles, précision / fréquence / maillage / fraîcheur  | Le fichier contient 1735 lignes. Il n’y a pas de doublons : par exemple, il y a des chanteurs (Mahmood, Sergey Lazarev etc.) qui ont participé à plusieurs éditions. |   N/A |
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
Pour l'enrichissement j'ai utilisé d'une part WikiData (directement via OpenRefine) pour récupérer le genre de l'artiste et le type d'artiste (groupe ou solo) et un Script Python pour détecter les langues de chaque chanson. Le processus est expliqué dans le document relatant toutes mes taches.

### Liens :
* [Explication des étapes de nettoyage et d'enrichissement via WIKIDATA/script Python](/autres/M2_DEFI_2023_Guerin_OpenRefineWikiData.pdf).
* [Script Python pour la détection de langues, conçu par moi-même](/sources/langue.py).
* [CSV d'export d'OpenRefine](/sources/M2_DEFI_2023_Guerin_Eurovision_ExportOpenRefine.csv).
* [Historique d'OpenRefine](/sources/M2_DEFI_2023_Guerin_Eurovision_Historique.json).
* [CSV final](/sources/M2_DEFI_2023_Guerin_Eurovision_PostOpenRefine.csv).


# Visualisations et editorialisations
## L'Eurovision en bref
### Les victoires par pays

J'ai réalisé une copie de mon CSV final afin de filter mes données pour réaliser ma première visualisation. 

En effet, je veux d'abord visualiser une carte des pays ayant remporté le concours, avec le nombre de victoires. Pour ce faire, je ne garde sur mon fichier que les lignes où le place_contest = 1, puis j'ajoute une colonne dans LibreOffice qui s'appelle "nbVictoires" ou je fais une fonction NBSI pour compter le nombre de fois où un pays apparait afin de déterminer le nombre de victoires. Je supprime d'autres colonnes (ex: coordonnées de géolocalisation car finalement DataWrapper va les trouver automatiquement). 

Sur Datawrapper je réalise une "Symbol Map".

<iframe title="Les pays qui ont gagné l'Eurovision" aria-label="Map" id="datawrapper-chart-azGjB" src="https://datawrapper.dwcdn.net/azGjB/2/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="810" data-external="1"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"]){var e=document.querySelectorAll("iframe");for(var t in a.data["datawrapper-height"])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data["datawrapper-height"][t]+"px";e[r].style.height=i}}}))}();
</script>

On s'aperçoit donc que la France n'est pas si mauvaise qu'elle ne prétend l'être puisque nous avons gagné 5 fois. Cependant, notre dernière victoire remonte à...1977. 

Concernant les données, la visualisation me permet de remarquer aussi une coquille : le code iso pour l'Ukraine devrait être ukr et non sk, ce qui peut me faire douter de l'efficacité de mon script python pour les langues slaves. De plus, comme expliqué sur la carte, la victoire de la Yougoslavie (1989) a été retirée car ce pays n'existe plus et ne peut plus être placée sur une carte contemporaine.

#### **Fichier utilisé pour cette première visualisation**
* [CSV de la première visualisation](/sources/M2_DEFI_2023_Guerin_Eurovision_PremiereVisualisation.csv).

### La France à l'Eurovision

Je décide donc de comparer la France aux autres grandes nations qui ont gagné minimum 5 fois l'Eurovision, à savoir : Le Luxembourg, La Suède, les Pays Bas, Le Royaume Uni et l'Irlande.

Je décide de réaliser une timeline sur Flourish afin de voir où terminent ces pays chaque année au concours. Pour ce faire j'ai dû réarranger mes données pour avoir en colonne les années et en ligne les places obtenues selon les pays. Je réalise cette transformation sur libreoffice via des copier/coller > "Transposer".

Mon seul soucis concernait les années où les pays n'ont pas participé à l'Eurovision : j'ai remplacé mes "non applicable" dans le fichier d'origine en case vide. Dans Flourish, j'ai créé une colonne "image" où j'ai ajouté le shortcode de chaque pays pour obtenir le drapeau de ce dernier. J'ai aussi ajouté le logo de l'Eurovision en bas, à droite.

<div class="flourish-embed flourish-chart" data-src="visualisation/16447744"><script src="https://public.flourish.studio/resources/embed.js"></script></div>

#### **Fichier utilisé pour cette deuxième visualisation**
* [CSV de la deuxième visualisation](/sources/M2_DEFI_2023_Guerin_Eurovision_DeuxiemeVisualisation.csv).
* [Source logo Eurovision](https://fr.wikipedia.org/wiki/Fichier:Eurovision_Song_Contest_logo_2015.svg).
  
## Comment gagner à l'Eurovision ?
### Zoom sur les dix derniers gagnants (2012-2023)

On voit donc au travers de la deuxième visualisation que la France connait une dégringolade depuis quelques années au concours (hormis la 2ème place de Barbara Pravi en 2021, et la 6ème place d'Amir en 2015) alors que d'autres pays, comme la Suède, a gagné de nombreuses fois ce dernier ces dernières années (2012, 2015 et 2023). Je décide donc de faire un panorama des dix derniers gagnants pour voir s'il y a une tendance qui émane (en termes de chanteurs : est-ce que ce sont des hommes qui ont plus gagné ? est-ce que ce sont des femmes ? est-ce que les gagnants sont des groupes ou des artistes solo en majorité ? etc.)

Pour ce faire, je réalise cette visualisation une nouvelle fois sur Flourish. J'y ajoute une nouvelle fois le logo de l'Eurovision et je place le lien de chaque chanson pour que l'utilisateur puisse aller écouter le titre remporté.

<div class="flourish-embed flourish-cards" data-src="visualisation/16447895"><script src="https://public.flourish.studio/resources/embed.js"></script></div>

On remarque que la Suède a gagné trois fois dont deux fois avec la même chanteuse, Loreen : c'était d'ailleurs la première fois qu'une femme remportait deux fois le concours. On s'aperçoit qu'à l'exception de la Suède et des Pays Bas, les grandes nations de l'Eurovision vues en deuxième visualisation ne sont pas représentés. On voit par ailleurs l'émergence d'autres nations, comme l'Italie et Israel qui ont 3 victoires à leur actif (cf. première visualisation).

On remarque aussi que ce sont en majorité des performances solo qui ont remporté cette dernière décennie le concours et que l'anglais est la langue majoritaire.

#### **Fichier utilisé pour cette troisième visualisation**
* [CSV de la troisième visualisation](/sources/M2_DEFI_2023_Guerin_Eurovision_TroisiemeVisualisation.csv).
* [Source logo Eurovision](https://fr.wikipedia.org/wiki/Fichier:Eurovision_Song_Contest_logo_2015.svg).

### Exploration de différentes pistes (le genre, la langue, artiste solo/groupe etc.) 

On va donc essayer d'estimer nos chances pour cette année avec les paramètres suivants : le genre de l'artiste, la langue de la chanson et si la performance est réalisée en groupe ou en solo.

Pour rappel, Slimane est un homme qui chante seul et en français.

J'utilise DatWrapper pour réaliser ces visualisations assez simples (donuts, bar charts etc.).

#### **Genre** :

Pour le genre, je fais une copie de mon CSV de base et j'utilise la fonction NB.SI pour avoir le nombre d'hommes, femmes etc. Je réalise des donuts via DataWrapper.

<iframe title="Le genre des candidats à l'Eurovision" aria-label="Multiple Donuts" id="datawrapper-chart-Po7Pd" src="https://datawrapper.dwcdn.net/Po7Pd/1/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="356" data-external="1"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"]){var e=document.querySelectorAll("iframe");for(var t in a.data["datawrapper-height"])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data["datawrapper-height"][t]+"px";e[r].style.height=i}}}))}();
</script>

On remarque que les hommes n'arrivent qu'en troisième position des gagnants et ce que sont les femmes qui gagnent le plus souvent le concours. Slimane partirait-il donc avec un désavantage ? Je remarque qu'une personne genderfluid aurait participé pour la France : en regardant mon jeu de donnée, il s'agit de Bilal Hassani. Cependant, à ma connaissance, Bilal Hassani s'est toujours revendiqué comme un homme. Bien que cela ne fausse que de très peu les résultats, il est important de prendre du recul sur les données.

#### **Artiste Solo** :

Pour le type de performance, même principe : j'ai construit mon fichier grâce à des NB.SI sur LibreOffice en partant du fichier Post-OpenRefine. Même chose que pour le genre : je réalise ma visualisation sur DataWrapper.

<iframe title="Part des performances solo &amp;amp; de groupe à l'Eurovision" aria-label="Multiple Pies" id="datawrapper-chart-OfMTk" src="https://datawrapper.dwcdn.net/OfMTk/1/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="339" data-external="1"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"]){var e=document.querySelectorAll("iframe");for(var t in a.data["datawrapper-height"])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data["datawrapper-height"][t]+"px";e[r].style.height=i}}}))}();
</script>

Ce sont les artistes solo qui ont le plus gagné le concours, et ce sont ce type d'artistes qui sont le plus envoyés par la France. Slimane a donc bien fait de redevenir artiste solo après son aventure musicale avec Vitaa puisqu'il semblerait que les groupes aient tendance à moins gagner. Par contre, ces dernières cinq années, il y a eu deux groupes qui ont gagné : Maneskin et Kalush Orchestra, donc la tendance va peut-être s'inverser dans le futur.

#### **Langue** :

Au niveau de la langue, j'ai décidé d'utiliser les fonctions SI, puis NB.SI sur LibreOffice : en effet, mon script Python n'est pas très performant sur certaines langues, par exemple les langues slaves (cf. commentaire sous ma première visualisation). Je pense que partir sur les chansons en anglais vs les chansons non anglais, ce qui amènera à moins d'erreurs. Je réalise une visualisation sur DataWrapper.

<iframe title="L'anglais à l'Eurovision" aria-label="Colonnes groupées" id="datawrapper-chart-Kcaiu" src="https://datawrapper.dwcdn.net/Kcaiu/1/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="400" data-external="1"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"]){var e=document.querySelectorAll("iframe");for(var t in a.data["datawrapper-height"])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data["datawrapper-height"][t]+"px";e[r].style.height=i}}}))}();
</script>

Je remarque qu'à l'echelle du concours, ce sont les chansons qui ne sont pas en anglais qui ont le plus gagné mais je pense que ce n'est qu'une réalité mathématique vu qu'on assemble l'ensemble des langues ensemble : peut-être il aurait été plus pertinent de le faire par type de familles de langues (langues slaves, langues romanes, langues germaniques etc.). D'ailleurs, si on regarde ne serait-ce que ma deuxième visualisation, on s'aperçoit qu'au cours de la dernière décennie, les chansons ayant remporté le concours sont le plus souvent chantées en anglais.

De plus, pour la France, je relève des erreurs : pour la chanson "Roi" de Bilal Hassani, on me l'a classe en anglais alors que ce n'est que le refrain qui n'est en anglais. Cela prouve une fois que le script python, bien que permettant d'aller vite, n'est pas aussi fiable que je l'aurais voulu.

Une chose est sûre : l'anglais reste la langue de référence si on souhaite mettre toutes les chances de son côté. La France aime donc les challenges puisqu'elle envoie majoritairement des chansons qui ne sont pas en anglais (français surtout, mais aussi corse et breton).

#### Fichier utilisé pour ces visualisations
* [CSV du genre](/sources/M2_DEFI_2023_Guerin_Eurovision_genre.csv).
* [CSV sur le type de performance](/sources/M2_DEFI_2023_Guerin_Eurovision_performertype.csv).
* [CSV de la langue](/sources/M2_DEFI_2023_Guerin_Eurovision_langue.csv).

# Conclusion

A l'évidence, bien que la France soit toujours dans le top des nations avec le plus de victoires (cf. première visualisation), il est évident que nous sommes depuis plusieurs années à la traîne dans le classement en comparaison avec les autres nations victorieuses (cf. deuxième visualisation). En regardant les dix derniers gagnants (cf. troisième visualisation), il est évident qu'une ère nouvelle souffle sur le concours avec la montée de nouvelles nations (Pays-Bas, Ukraine et Italie par exemple). 

La France, représentée en 2024 avec Slimane, n'a sur le papier que très peu de chances de s'en sortir : bien que la performance soit celle d'un artiste seul sur scène, la chanson est en français et est chantée par un homme. Or, si on regarde les statistiques générales sur le concours (cf. dernières visualisations) il aurait fallu envoyer une femme chantant en anglais...

Malgré tout, d'autres paramètres rentrent en compte : les chansons et voix concurrentes (il y a des années de grand cru quand d'autres sont plus faciles d'accès), la position de la chanson (je vous laisse vous renseigner sur la malédiction de la position 2...), la mise en scène etc.

Slimane a d'autres atouts : une voix magnifique, des paroles touchantes et un charisme indéniable. Nul doute qu'il nous rapportera une très belle place, et pourquoi pas la victoire (cela ne coûte rien de rêver).
