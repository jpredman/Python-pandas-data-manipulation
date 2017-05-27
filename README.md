# Python-pandas-data-manipulation
manipulation of web-scrapped data in Pandas

Working on a project taking data from a website and transforming it into a PostrgreSQL database to be used in a mapping tool. This is the transforming process of the data that has been web-scraped from http://www.airlinepilotcentral.com/. 

I'm using the Pandas datset in Python to transform the data so it is in the proper schema to load into the PostgreSQL database.

THE CODE--
The web-scraped files for each airline are in "myFolderPath" and include the Fleet information, captian pay scale, and first officer pay scale. The data needs to be manipulated a bit before transforming it into the PostgreSQL database. 
Funcitions include: csv reader (the web-scraped files are in .csv), string replace, and writing to a csv. 
