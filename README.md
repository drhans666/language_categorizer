# language_categorizer
THIS ARE ONLY HUMBLE BEGINNINGS OF APP

In progress. App that detects language of given text. Database driven, with some cool features like machine learning etc.  

language codes source: https://datahub.io/core/language-codes#resource-language-codes

Instructions:

-- run language_loader to create language code table in database

-- READ BELOW, run crawler to crawl Wikipedia for scikit-learn trainig data 
* in couple of days there will be example database availabe. So no need to use crawler unnecessary
* crawler set this way do not violate Wikipedia rules (1 page per second).
* downloading data by crawler the way respecting Wikipedia rules takes hours or even days
* changing crawler speed settings below 1art/s may result in IP ban from Wikipedia and it's just simply not cool. DONT DO THIS.
* crawler uses widely translated keywords for articles saved in keywords.txt (not complete)

-- all key features like language categorization or maybe django app version in near future.