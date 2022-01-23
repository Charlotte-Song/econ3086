# Project(Snearker)
The Porject is a simple try to get Sneaker price from differengt website set in different country, and through comparing the price comes from different source to do suggestion for the user（my expected achievement）.

## Main Content
### Source
* [StockX](https://www.area02.com/zh-CN)
* [KNCKFF(already renamed as AREA02)](https://stockx.com]

### Content
* STOCKX.py
    * Through request, ssl and beautiful4soup package to crawl data such as sneaker name size and corresponding price
    * Through the pandas to clwan the data
* KNCKFF.py
    * Almost Same way as STOCKX.py to crawl data form KNCKFF Website
* Search.py
    * Due to the difference of data format comes from different source we throught this part to match the snaeaker name 
    * Then though this part to complete the comparison
* sentmessage.py
    * Through the telepot package to interact with user
    * User sent message shoes name and size through telegram then get the corrsponding price and suggestion

### Limitation
* Person Technical knowledge limitation
    * Match Limitation: Just as what I mentioned in Search.py part, there are many different in naming the snearch. Thus I do not complete all type of comparsion but just limited in Yeezy(a hot shoes brand belong to Addidas)
    * Crawl Limitaiton: Because of the big website usually set the anit-crawl, thus sometimes the programme can not get the full data
    * Interact Limitation: do not complete the web interact, just through the telegram to show my point
    
### Expectation

* Crawl the data in daliy routing and sombine with the Machine learning to predict the price to improve the suggestion to the user.

## Authors

An Pyhton application Write duirng Mid Nov.2020 to Early Dec.2020 by Charlotte
Also part of the coding complete by my groupmate(KNCKFF.py),the release has been approved by him.
