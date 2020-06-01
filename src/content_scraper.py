### PACKAGES
from urllib.request import urlopen , Request, urlretrieve
from bs4 import BeautifulSoup
import ssl
import time
import requests
from io import BytesIO
import tqdm


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

	### DEFINE LISTS TO CAPTURE DATA [LINK, CATEGORY , AUTHOR , ARTICLE , TITLE]
	list_categories = list()
	list_links = list()
	list_titles = list()
	list_authors = list()
	list_articles = list()
	wrong = list()



	for link in soup.find_all('a', { 'class': 'gs-c-promo-heading' }):
		### GET CATEGORY ARTICLE
		category = link['href'].split("/")[1]
		# print(category)
		list_categories.append(category)

		### GET LINK
		if 'https' in link['href']:
			link = link['href']
		else:
			link = "https://www.bbc.com"+link['href']
		# print(link)
		list_links.append(link)

		print("====> <====")
		try:
			req = Request(url= link, headers=headers) 
			document = urlopen(req)
			html = document.read()
			soup_article = BeautifulSoup(html , 'html.parser')

			core_article = soup_article.find('div' , class_ = "story-body")

			### GET TITLE
			title = core_article.find('h1' , class_ = "story-body__h1").text
			# print(title)
			list_titles.append(title)

			## GET AUTHOR
			try:
				author = core_article.find('span' , class_ = "byline__name").text
				if author == None:
					author = "unknown"
				else:
					author = author.split(" ")[1]
				# print(author)
				list_authors.append(author)
			except:
				author = core_article.find('span' , class_ = "byline__name")
				if author == None:
					author = "unknown"
				else:
					author = author.split(" ")[1]
				# print(author)
				list_authors.append(author)

			## GET ARTICLE
			article = core_article.find('div' , class_ = "story-body__inner").find_all('p')
			article = [x.text for x in article]
			article = ' '.join(article)
			# print(article)
			list_articles.append(article)

		except KeyboardInterrupt:
			print("Program interrupted by user ...")
			exit()
		except :
			print("SOMETHING WENT WRONG ")
			continue
			


	
except KeyboardInterrupt:
	print("Program interrupted by user ...")
	exit()
except:
	print("SOMETHING WENT WRONG ")



				
print("SCRAPING LINKS DONE !!")				

end = time.time()

print ('Time taken: {} seconds'.format(end-start_process))
