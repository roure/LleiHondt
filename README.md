# Càlcul Llei Hondt

Hi trobarem tres fitxers:
* scraper.py : crawler per cercar els resultats oficials de la Generalitat
* barcelona_result.json : el resultat del crawler
* llei_Hondt.py : calcula el nombre d'escons segons els vots (llegeix el fitxer json)


### scraper.py
Agafa els resultats de la demarcació  de Barcelona de les Eleccions al parlament de Catalunya del 2015 de la web oficial de
la Generalitat: http://www.gencat.cat/governacio/resultatsparlament2015/resu/09AU/DAU09089CI_L2.htm

Es pot extendre fàcilment per a que agafi els resultats de totes les demarcacions

**Comanda d'execució:** scrapy runspider scraper.py -t json -o barcelona_result.json

## llei_Hondt.py
Crec que el codi es força autoexplicatiu. Preparat per calcular només els escons de la demarcació de Barcelona. S'hauria
de generalitzar amb dos paràmetres: el fitxer a processar i el nombre d'escons total de la demarcació a calcular