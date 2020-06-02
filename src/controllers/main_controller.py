import connexion
import sys
import json
from bson.json_util import loads, dumps
from logbook import Logger , ERROR, WARNING, DEBUG, INFO
sys.path.append("..")
from services.db_connect import read_all , fetch_by_keyword
from services.content_scraper import scraping


log = Logger('logbook' , INFO)

## FUNCTION TO SCRAP AND STORE ARTICLES
def scrape_data ():
	log.info('Calling scraping data endpoint')

	if connexion.request.is_json:
		try:
			scraping()
			response = {} , 200
		except KeyError:
			response = {} , 404

	return response

## FUNCTION TO READ ALL ARTICLES
def read_data ():

	log.info('Calling read_all endpoint')
	if connexion.request.is_json:
		try:
			articles = dumps(read_all())
			response = {"news_articles" : articles} , 200
		except KeyError:
			response = {} , 404

	return response


## FUNCTION TO FETCH ARTICLES
def fetch_data ():

	log.info('Calling fetch data endpoint')
	if connexion.request.is_json:
		body = connexion.request.get_json()
		body_parse_keyword = body["keyword"]
		try:
			response = {"news_articles" : dumps(fetch_by_keyword(body_parse_keyword))} , 200
		except KeyError:
			response = {} , 404

	return response
