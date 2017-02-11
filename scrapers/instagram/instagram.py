from bs4 import BeautifulSoup
from selenium import webdriver
import os.path

## keywords to look for
keywords = ['available', 'lookbook', 'EST', 'PST', 'drop', 'dropping']

def instagram_scrape(instgrams):
	driver = webdriver.Firefox()
	for instagram in instgrams: 
		url = "https://instagram.com/" + instagram
		driver.get(url)
		source_html = driver.page_source
		soup = BeautifulSoup(source_html)
		images = soup.find_all('img')

		check_hype(images, instagram)	
		update_visited(images, instagram)

	driver.close()

def check_hype(images, instagram):
	visited_file = 'scrapers/instagram/visited_' + instagram + '.txt'
	old_visited = []
	if os.path.exists(visited_file):
		old_visited = [post.rstrip('\n') for post in open(visited_file)]
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
			
def update_visited(images, instagram):
	visited_file = 'scrapers/instagram/visited_' + instagram + '.txt'
	new_visited = open(visited_file, 'w')
	for image in images:
		image_src = image.get('src')		
		print('writing ' + image_src + ' to visited file\n')
		new_visited.write("%s\n" % image_src)
