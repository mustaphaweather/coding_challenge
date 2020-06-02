### PACKAGES
from urllib.request import urlopen , Request, urlretrieve
from bs4 import BeautifulSoup
import ssl
import time
import requests
from io import BytesIO
from tqdm import tqdm
from db_connect import add_article 

### FUNCTION THAT SCRAPE AND ADD DATA TO MONGODB
def scraping():
	### MAIN URL
	main_url = "https://www.bbc.com/news"

	### IGNORE SSL CERTIFICATE ERRORS
	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE

	### FAKE BROWSER METADATA
	headers = {"User-Agent": "Mozilla/5.0"}

	### [1] SCRAPE ALL ARTICLES CORES

	### TIME TAKEN FOR THE PROCESS
	start_process = time.time()
	req = Request(url= main_url, headers=headers) 
	print("==============================")
	print(main_url)
	print("==============================")
	try:
		document = urlopen(req)
		html = document.read()
		soup = BeautifulSoup(html , 'html.parser')

		### DEFINE LIST OF DICTIONNARIES [LINK, CATEGORY , AUTHOR , ARTICLE , TITLE]
		articles = list()

		for link in tqdm(soup.find_all('a', { 'class': 'gs-c-promo-heading' })):
			### GET CATEGORY ARTICLE
			category = link['href'].split("/")[1]

			### GET LINK
			if 'https' in link['href']:
				link = link['href']
			else:
				link = "https://www.bbc.com"+link['href']

			try:
				req = Request(url= link, headers=headers) 
				document = urlopen(req)
				html = document.read()
				soup_article = BeautifulSoup(html , 'html.parser')

				core_article = soup_article.find('div' , class_ = "story-body")

				### GET TITLE
				title = core_article.find('h1' , class_ = "story-body__h1").text

				## GET AUTHOR
				try:
					author = core_article.find('span' , class_ = "byline__name").text
					if author == None:
						author = "unknown"
					else:
						author = author.split(" ")[1]
				except:
					author = core_article.find('span' , class_ = "byline__name")
					if author == None:
						author = "unknown"
					else:
						author = author.split(" ")[1]

				## GET ARTICLE
				article = core_article.find('div' , class_ = "story-body__inner").find_all('p')
				article = [x.text for x in article]
				article = ' '.join(article)
				
				new_article = {"category": category, "author": author, "link": link, "title": title, "article":article}
				articles.append(new_article)
			except KeyboardInterrupt:
				print("Program interrupted by user ...")
				exit()
			except :
				continue

		
	except KeyboardInterrupt:
		print("Program interrupted by user ...")
		exit()
	except:
		print("SOMETHING WENT WRONG ")
					
	print("SCRAPING  DONE !!")				

	end = time.time()

	print ('Time taken: {} seconds'.format(end-start_process))

	add_article(articles)

