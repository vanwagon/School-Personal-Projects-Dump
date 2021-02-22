from bs4 import BeautifulSoup
import requests
import lxml


#getting product title
def get_title(soup):
	try:
		#outer tag
		title = soup.find('span', attrs={"id":'productTitle'})

		#inner navigable string
		title_value = title.string
		title_string = title_value.strip()
		#printing product title
		#print(type(title))
		#print(type(title_value))
		#print(type(title_string))
		#print("Product Title = ", title_string)
		return title_string

	except AttributeError:
		title_string = "error in getting title"

		return title_string

def get_rating(soup):
	try:
		rating = soup.find("i", attrs={"data-hook":"rating-out-of-text"}).string.strip()

	except AttributeError:
		try:
			rating = soup.find("span", attrs={"data-hook":'rating-out-of-text'}).string.strip()
		except:
			rating = "error in getting rating"

	return rating


def get_review_count(soup):
	try:
		review_count = soup.find("span", attrs={"id":'acrCustomerReviewText'}).string.strip()
		return review_count

	except AttributeError:
		review_count ="error in getting review count"

	return review_count

if __name__ == '__main__':
	# Headers for request (agent) ***PUT YOUR OWN AGENT AFTER the first " and before the ,
	HEADERS = ({", 
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip', 
'DNT' : '1', 
'Connection' : 'close'})

	#PUT AN AMAZON URL IN BETWEEN THE ""
	URL = ""
	#HTTP REQUEST
	webpage = requests.get(URL, headers=HEADERS)

#soup object containing all above data
	soup = BeautifulSoup(webpage.content, 'lxml')

	print("Product Title =", get_title(soup))
	print("Product Rating =", get_rating(soup))
	print("Number of Product Reviews =", get_review_count(soup))
    
    
   # NOTE: MAY NOT WORK IF YOU'RE AGENT IS NOT BELIEVABLE AS A REAL USER, OR IF YOU DONT HAVE AN ACCESS TOKEN PROVIDED BY AMAZON, THIS IS ONLY A PERSONAL PROJECT
