#IndicWiki Summer Internship - Cities

##Cities:

The aim of this domain is to generate about 25k articles above the different cities across the world. Each and every individual who wants to explore the world will look into the cities. So we thought it is a domain which needs articles in any language. Wikipedia, a free encyclopedia, is rich in the content of english language. Even the data of cities is rich with english articles on wikipedia. As a branch of this IndicWiki project we are spreading the wings by generating about 25k articles in telugu language of wikipedia. As technical interns we would like to use our skills in this project to develop a python bot which will generate articles with sufficient accuracy and less human intervention. We would like to carry forward this as a data science project. It all starts with data collection, data cleaning, data analysis and then using the data for article generation. 

##Team
This batch is a group of 11 members, the teams are divided on the basis of the sections of the article. 5 teams are formed with 11 members. Team wise details and the respected domains are listed below:
*Team-1 :
Team will be working on the Demographics section.
Anusha Thodupunoori - anushathodupunoori123@msitprogram.net
Nikitha Penchala - nikithapenchala@gmail.com
*Team-2:
Will be working on the Governance Section.
Phaneendra - phaneendra622@msitprogram.net
Vamsi Krishna ramisetti - vk19999052563765@msitprogram.net
*Team-3 :
Will be working on the Introduction Section.
Suma Kola - sumakola1106@msitprogram.net
Rushikesh - rushikonganapalli2233@msitprogram.net
*Team-4:
Will be working on the Climate Section.
Saketh Reddy Regatte - sakethreddy1305@gmail.com
Sai Tanuja Thirupathi - tanujathirupathi624@gmail.com
Sairam Tamisetti - t.sathyasairam@gmail.com
*Team-5:
Will be working on the section of Notable places and the transport section.
Karthik Surineni - surinenikarthik122k@gmail.com
Chirasmayee Bhavaraju - chirasmayee1606@gmail.com
##Data Collection
Sources/ Sites 
*DBpedia:
A database of wikipedia data which has the data in the form of the key value pair attributes. Each and every entity of the wikipedia data entry is related to one another in the tree data structure.Many attributes for the city domain are collected from the dbpedia itself. Attributes collected from dbpedia are clearly stated in the dataSchema sheet attached in the resources section of this documentation.
*WOLFRAM ALPHA:
Excel 2019 featured a built-in datatype which treats cities as an entity possessing some of the geographic properties. Excel gets this data from a unified datasource - WOLFRAM Alpha. So this is one of the indirect sources for our data collection.
*Wikipedia:
English wikipedia also served as one of the major sources for data collection for this project. We used english Wikipedia article of the respective city for scrapping the weather boxes and infoboxes. We scraped the weather boxes to get data for the climate section from the existing english wikipedia articles.
*TripAdvisor 
Format of data available - List of notable places 
Tools used - googlesearch python package, BeautifulSoup web scraping
Attributes found - list of tourist attractions in a city
Planetware
Format of data available - List of notable places
Tools used - googlesearch python package, BeautifulSoup
Attributes found-  list of tourist attractions in a city

Holidify:
 Format of data available - List of notable places
Tools used - googlesearch python package,BeautifulSoup
Attributes found - list of tourist attractions in a city
    
TripHobo:
Format of data available - List of notable places
Tools used - googlesearch python package,BeautifulSoup
Attributes found - list of tourist attractions in a city

Wiki data items: 
Each country has a wiki data item code starting with Q. We have attribute code for every attribute starting with P. We write a SPARQL command to extract attribute data in a particular country. Then check if that attribute data is within a city or not. If it is within the city, we add attribute data to the city. 
We followed this procedure to extract airports, seaports, railway stations, bus stops, beaches and images of notable places in the city.   
Format of data available - RDF, Table containing all rows which satisfy SPARQL command
Tools used - rdflib python package, SPARQLWrapper, pprint python packages
Attributes found - airports,seaports,beaches,railway stations,bus stands,images of notable places
Tools used for Data collection 
SPARQL query language:
To access dbpedia we were supposed to learn a completely new and different language similar to SQL which is called SPARQL. The data sources in dbpedia and wikidata are stored in the form of graphs linked to many nodes. To access the data we need a special mechanism which is provided to us by the SPARQL. A querying language used to extract data from the dbpedia and wikidata.




Excel’s built in Datatypes:
Excel 2019 came with a new feature of defining some of the entities as data types like cities, hospitals,universities etc. We explored it and efficiently collected relevant data for some attributes like area, population,state name etc.

BeautifulSoup:
This package was very useful and we did not face any errors during compilation or errors in the scraped data. But there was an issue of speed as we needed to collect data for nearly 29k cities. So we had to run our code from various notebooks
Issue: Takes nearly 10 seconds for each city → Run in more notebooks

Saving data in MongoDB
We realised when we were getting a list of tourist spots from at least 15 to 40 for each city that these cannot be saved in a Dataframe. With the number of attributes we used during scraping, it was confusing to write code that stored the list directly into a csv file.
Unable to save in CSV → Saving data as dictionary in MongoDB
We wanted to save data for each city in the form of a dictionary containing the attributes: _id,city_name,links,site,places
_id is id of the city
City_name is name of the city
Links are all the links extracted from google search
Site is a site chosen from {“TripAdvisor”,”Holidify”,”Planetware”,”TripHobo”} from which we extract the data.
All the list of tourist spots will be saved in places key
Saving data in MongoDB has helped us tremendously to analyse the data, to save and retrieve the data in lesser time and assurance of safe storage of data 
Planetware links issue: This issue was that for unpopular cities planetware site provided the city’s countries tourist spots. So, the output was wrong.
Workaround: This was resolved by identifying all the planetware links that were repeated and replacing them with the city’s extracted TripAdvisor link and output improved for nearly 10,000 cities
Wikidata query service:
This was a very important tool for extraction of data for a particular attribute. 
Issue: All the attribute data like airports, seaports, railway stations, stadiums, places images etc. data was accurate with regards to the country they were present in. These attribute data were not identified accurately for a city.
Workaround: 
We have then collected data for all the entities such as Airports, beaches etc for all the cities using Wikidata Query service(code for getting all the stadiums in India).
As we already have coordinates of all the cities that have been extracted from wikipedia articles, we have used coordinates for mapping the entities with their corresponding cities.
We have fixed a threshold for each entity(Ex: 50Km for Airports). We have considered a city and calculated the city’s distance with all the airports in the world. If the distance is less than the threshold, the airport is added to the data or else it discarded(code for calculating distance between  2 coordinates).

Some Issues of the tools explored for data collection:

Scraping (Beautifulsoup)
Wikipedia format is not same for articles ,it was little difficult to scrape the links
For some articles there were more than one climate table scraping the required one was an issue. After a few modifications we overcame the issue.
Extracting the source links of climate table was also difficult
Parsehub for scraping - it is an online tool
It is not efficient to scrape multiple pages at a time
Though the accuracy is pretty good but the time taken to scrape is more and manual work is also involved.
Wikidata
SPARQL language is used to extract data from wikidata
The language is somewhat difficult to understand at first
As it deals with id’s the extraction was difficult
Dbpedia
Understanding the database is difficult. 
BertAna 
Tried to use this NLP Question and Answering  model for feature extraction from text. But failed to use it as it is taking more time to train and each question needed to be framed separately and the model needed to be trained for each and every question with text.
Excel Data Types (Wolfram)
As the new version of excel provides us with datatypes it was helpful to a bit.
some cities are unidentified we need to do it manually but the count was very less

Images 
Wikidata query service (code for getting image of a particular object)
Issue: The query service returns urls of the images while we need to place the file name of the image in wiki code for proper workflow. So we have transformed the image url to file name. Actually the image name is encoded in the url. SO we have used a small set of code to extract the image file name.
Data Storing 
Format - MongoDB
Why - The amount of data extracted regarding notable places, airports,seaports,stadiums etc. for each city was very high and saving all that data to a csv file without analysing the data and its validity seemed risky. So we stored the data into MongoDB. We created a collection for each attribute like Cities collection for Notable places, EntitiesImages collection for mediawiki links of notable places images, Entities collection for other attributes like Transport (airports, seaports etc.) 
Data Cleaning
Cases taken care of 
Case
Planetware links issue: This issue was that for unpopular cities planetware site provided the city’s countries tourist spots. So, the output was wrong.
 Workaround: This was resolved by identifying all the planetware links that were       repeated and replacing them with the city’s extracted TripAdvisor link and output improved for nearly 10,000 cities

Case
TripAdvior -- missed link format: tripAdvisor/attractionsNear
When we had written code for extracting data from the tripadvisor link, we observed only two patterns: tripadvisor/Tourism and tripadvisor/Attractions. During data cleaning process, when we checked all the cities that has lists containing no tourist spots, most of the links were of the pattern tripadvisor/attractionsNear 
 Workaround: We wrote the scraping code for tripadvisor/attractionsNear and nearly 900 cities notable places were recovered.
Issue → Workaround
Data Merging
Primary key for the data collected from different sources/ for different subdomains, is the wikipedia Qid collected from wiki data.
Used the Vlookup library in the Excel sheet to map the data collected between various subdomains.
FinalKB format is a CSV file or Excel sheet
Final KB rows X columns - 27853 rows X 85 columns (along with the translated/Transliterated attributes) 
Final KB link - [IIIT github link is appreciated]
Initially we had two data sets one containing around 17K cities and the other containing around 11k cities. While merging both of them into one dataset, there was an issue in the ordering of attributes in both the datasets → We merged the dataset after thoroughly checking the column names in both of the datasets.

Version control
Github is our primary version control tool. Since our project is more around data collection we used different version control systems like google sheets’ version control, google docs’ version control in the process of data collection and sample article creation. Collaboration is the strength of this project and we can strongly say that we are able to efficiently collaborate with the help of above mentioned tools.
Sample article 
Link - [IIIT github link is appreciated]
Sections 
Cities being a geographic location on first impression we get some attributes like country, state, population, area, etc…
All the basic necessities which define a city are listed and pushed into the Introduction section.
A Demographics section is included which describes the facts of the city.
Governance of the city is included as the third section which describes the type of government in the city.
When we plan to go to a city we open an article and search for the climatic conditions of the city to pack our bags accordingly and to plan the trip.Hence we found that Climate is one such essential section. We added it as the fourth section.
Climate section is subdivided into two parts. Climate data and climate table. Climate data has the description of the climatic conditions of the city. It is basically an analysis of the climate table.
Climate table has the recorded values of temperatures and other measures in the city.The data of weather boxes is basically extracted from the weather boxes of the english wikipedia.

Next we continued this article with some places of attractions named the section as “Notable Places”. This section consists of the list of places in the city which are very notable whether it be a historic location or any kind of place which has registered a trademark.This section also has the list of famous Stadiums and Beaches in the city 
Next section is Transport. We look for transportation facilities for the city when we are new to it. So the transportation facilities are listed in this section like - Airports, Railways, Bus Stands & Sea Ports. Each of the subsections will have a scrollable lis of names of the respective transport facility. 2 of the images for each subsection are also included in the scroll so that one can get an idea of the location.
We concluded the article with attractive images of the city locations. We called this section Gallery.
Jinja template creation 
Link - [IIIT github link is appreciated]
Edge cases
All the empty cells in the database are filled with None string if it is a string data type or a number data type otherwise they are filled with empty array if it is a list datatype.
Categories, References 
As our domain is cities, we basically took ground level categories like to which state the city belongs to and to which country does the country belong to and also if the population is above one lakh then terming the city into a populous city with population above 100000.
[[వర్గం:నగరాలు]]
[[వర్గం:{{country_name}} లో నగరాలు]]
[[వర్గం:{{state_name}} లో నగరాలు]] 
Coming to references, our major source of data is wikipedia or its data sources like wikidata and dbpedia,which doesn't need any citation. Only source we need to cite is the site where we extracted the tourist spots of a particular city.Some of the websites like planetware, tripadvisor and holidify are cited depending on where the information is extracted.

Infobox
For cities' domains we have a default infobox template designed by Wikipedia named as “Infobox Settlement”.
We planned to use the same infobox template of wikipedia.
 When the project is in the research stage , there is a huge amount of data for a particular city in the particular city’s article of english wikipedia.
Unfortunately we are not able to extract the data from the infobox because each of the infobox is dynamic and has different views.
We almost found that it is impossible to scrape the infoboxes and its data as a key-value pair.
Hence we decided to get the source code of the infobox by mediawiki api so that when incorporated in te.wikipedia , most of the english attributes are by default translated to telugu. 
So a python program is built which creates a request to mediawiki to get the source code of the article from which infoboxes are taken out by balancing the parenthesis.
All the infoboxes so retrieved are stored as a .txt file with the name of the file being the unique id given to the city by the developers at the time of data collection. Unique ids are constant throughout the project and are never modified.
When a jinja template is called for other sections than the infoboxes are read by the render box and pushed to the source text.
Translation/ Transliteration
The data set is guided by a thorough knowledge of attributes which is clearly presented in the following spreadsheet:DataSchema

Tools used for each attribute are described clearly in the above report. Description of each tool explored is presented below:
Tools explored for Language Translation/Transliteration:

GOOGLETRANSLATE Formula of Google Spreadsheets.
		
Spreadsheets has this easy to use translator formula which can be applied to data in the cells like any other formula. Basic english words are translated.The google translator api is used by this formula for conversion. We are able to use it for some of our attributes which are having common english words like months of the year etc.
The syntax for the formula is shown below:
=GOOGLETRANSLATE(cell with text, “source language”, “target language”)

BING TRANSLATOR:
	Microsoft’s BING translator is explored for translation purposes. But we found that the translator is priced according to the usage. It is a cloud hosted platform hosted in Azure Cloud services. We are having our professional emails provided by our college which has access to Azure cloud service. Hence we figured out a way to use the resource.

There are two features of this resource:
Bing Translator
Bing Transliterator
	Transliterator is in the developing stage and conversion to telugu is still not developed hence we discarded it. But we found that the translator efficiency is amazing. It is able to understand the meaning behind the word then translating the word. We decided to use it anyway. But Cities domain has many attributes which is having data in the form of “Nouns”.
All nouns needed to be transliterated to retain the meaning.

Understand the below described scenario:
Bing translator is used for transliterating by "misleading" it .
All the city names are attached with a tag "City" which in turn convert the entire string into noun. Therefore translators do understand the parts of speech and Transliterate it. 
For Example, City Named "The Valley'' when send to translate it pushes the output as "లోయ" which is not expected. So when the city name is appended with a Tag "City" like "The Valley City" then translator transliterates it to "ది వాలీ నగరం" after getting the result "నగరం" is stripped and the desired output is obtained.  

This is how we mislead the translator to act as a transliterator. We have many attributes and tons of words to transliterate. The efficiency observed by using this is high compared to other resources. So we used this resource to the maximum to transliterate the data. Attributes transliterated by this BING Translator are providing more efficiency out of the available resources. But as it is a priced resource and as it is consuming much time we decided to use it only when we are in the need of more efficiency.

DEEP TRANSLIT :
 Deep translit module of the tensorflow library of python language is used in the local system for transliteration purposes. It is built by training the models and available in tensorflow module. English to Telugu conversion is very easy with this tool. The only thing this tool does is simply transliterating the given word based on the pronunciation of the word. It is not concerned with the internal meaning of the word. This is very useful for transliterating the nouns. So attributes like leaderName, Nicknames, demonyms etc which need absolute transliteration are transliterated using this tool.

Other Tools explored for language translation purposes “but Not Used”:
TEXT BLOB:
Textblob module of python uses NLP for translating the text from one language to another language. Its efficiency in translation is found to be pretty high but we could not use the tool as it is limiting the input stream. We are not able to use this translator to the fullest since it's consuming more time and a lot of manual task is included.
 
Google Trans New:
A translator api module of python which is also used for the purpose. The API calls are limited from an IP Address hence we discarded it from our checklist. The efficiency of the tool is pretty good but not as good as compared to those listed above.We tried using it but it failed in our training data set.

Manual analysis for efficient data translations:
We even used the replace function of excel for our translations:
Let me explain with an example we have an attribute - continent_name. We are all aware of the fact that there are about 8 continents in the entire world so by this we can say that around 30,000 entries of that attribute in our dataset we will have one of the 8 continents. So by manual conversion the 8 continents are efficiently converted to telugu language by a normal translator like google,the obtained results are stored in a map in the form of key value pair.Then with around 8 replacements of excel , the entire attribute is converted to telugu with 100% efficiency.
We applied this procedure for the summer and winter attribute which has data which is one of the 12 months. So those columns are converted with 100% efficiency by a small analysis.





COMMON ISSUES FACED IN TRANSLATION/TRANSLITERATION:
Time Consuming : It is found that the translation libraries are too time consuming. We are having tons of data which when fed to the tools took too much time to run the programs.It is estimated that an attribute took 8 hours to complete translation as per requirement.
Many Unwanted characters off Ascii Table:
Translators and transliterators are efficient in converting the english alphabets to telugu.But many tools failed to convert when they encountered any ascii characters for example ascii - ‘ü’ in the city name Düsseldorf. Transliterator failed to convert the ascents of those ascii values. Hence it became one of the problems for us which is to be addressed at 1st priority. We discussed the issue and came up with the solution of mapping those values with the equivalent english pronunciation. 
 
As seen above some all the special ascii are mapped and the entire database is mapped with this mapping function to get clean names.Now the transliteration efficiency is enormously increased.



Work Yet to be done:
Collect the data for all the Lakes in a city from the resources that are available with Radhika ma’am and provide the data regarding that in the article.
 If the list of values in the notable places or transport sections is too big, consider pointing that section to another article which contains the entire list of that particular section (For example, if the list of notable places is too big for Paris city, create an article on the Notable places in Paris city and point the Notable places section in the Paris city article, to the article containing all the notable places in Paris.)

