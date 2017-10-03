# language_categorizer
THIS ARE ONLY HUMBLE BEGINNINGS OF AN APP. DEVELOPING IN PROGRESS.
By now it eats too much memory, and its less effective with very short texts.

App that detects language of given text. Database driven, with some cool features like machine learning etc.  

Instructions:

-- run language_loader to create language code table in database

-- next step may be skipped by downloading example database and putting it in 'database' folder. Base available at: http://drhans.vipserv.org/language_categorizer.db

-- run crawler to crawl Wikipedia for scikit-learn trainig data and save it to database
* IMPORTANT: crawler set this way do not violate Wikipedia rules (1 page per second).
* IMPORTANT: downloading data by crawler the way respecting Wikipedia rules takes hours or even days.
* IMPORTANT: changing crawler speed settings below 1art/s may result in IP ban from Wikipedia and it's just simply not cool. DONT DO THIS.
* crawler uses widely translated keywords for articles saved in keywords.txt (not complete)

-- run categorizer.py to enter text for classification (1-2 sentences should be enough).

-- enter number of data-train articles Number of articles to train data is 22000. The higher amount, the better results. 

WARNING: Optimal number for 4GB RAM is 1500-2000. Too high amount may result in freezing Your PC !!!

-- if You want to test overall accuracy. Run accuracy_test.py WARNING: Needs more memory/less articles than standard input.

language codes source: https://datahub.io/core/language-codes#resource-language-codes

example database: http://drhans.vipserv.org/language_categorizer.db 

Leave your advices/opinions :) Thanks!