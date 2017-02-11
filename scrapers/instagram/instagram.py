from bs4 import BeautifulSoup
from selenium import webdriver

## keywords to look for
keywords = ['available', 'lookbook', 'EST', 'PST']

def scrape():
	driver = webdriver.Firefox()
	driver.get("https://instagram.com/phntmsrc")
	source_html = driver.page_source
	soup = BeautifulSoup(source_html)
	images = soup.find_all('img')

	check_hype(images)	
	update_visited(images)

	driver.close()

def check_hype(images):
	old_visited = [post.rstrip('\n') for post in open('visited.txt')]
	for image in images: 
		if image.get('src') not in old_visited:
			image_desc = image.get('alt', '')	
			image_words = image_desc.split()
			for image_word in image_words:
				if image_word in keywords:
					print('KEYWORD FOUND HYPE ALARM')
					print('IMAGE DESC IS: ' + image_desc)
					print('IMAGE LINK IS: ' + image.get('src'))
					break
			
def update_visited(images):
	new_visited = open('visited.txt', 'w')
	for image in images:
		image_src = image.get('src')		
		print('writing ' + image_src + ' to visited file\n')
		new_visited.write("%s\n" % image_src)

scrape()
