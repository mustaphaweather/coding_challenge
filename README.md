# BBC NEWS WEBSITE SCRAPING API

# OVERVIEW
This API was is a scraping tool , it gives us the ability to scrape all the news from the BBC website and, it has cnnection with a mongodb database to store the the articles and its metadata (category , author , link, title after the scraping is done.
You can access the database and read all the articles at once and, you can also fetch articles using a keyword.
The previous API ablilities are presented in the following endpoints:
- ```v1/scrape_data : [GET METHOD] endpoint responsible for scraping and storing data in mongodb database.```
- ```v1/read_data : [GET METHOD] endpoint responsible for reading all data from mongodb database.```
- ```v1/fetch_data : [POST METHOD] endpoint responsible for fetching and reading data from mongodb database based on keyword.```

# Requirements
* Python 3.6
* Conda 4.8 (for virtual environement)

# Setup
### To run the project Please follow the instructions below :</br>
#### 1 - Clone the project
```
$ git clone https://github.com/mustaphaweather/coding_challenge.git
cd coding_challenge
```

#### 2 - create a conda virtual environement using the bbc_scraper.yml file 
```
Create the environment from the bbc_scraper.yml file
```

#### 3 - activate the virtual environement
```
conda activate codding_challenge
or
activate codding_challenge
```

#### 4 - associate the wsgi.py app luncher file with the enviroenemtn variable flask_env and set developement env
```
cd src
set flask_app=wsgy.py
set FLASK_ENV='developement'
```

#### 5 - Run the application
```
flask run
```

#### 6 - Run scraper endpoint
``` v1/scrape_data```

#### 7 - Run read all data endpoint
``` v1/read_data```

#### 6 - Run read using fetch by keyword
This endpoint takes us requestbody {"keyword":"your_keyword"} </br>
-``` v1/fetch_data```



# Purpose of the project
The aim of this project is to complete Data Engineering Coding Challenge .


