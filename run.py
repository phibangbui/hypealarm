import sys

sys.path.append('scrapers/instagram/')
sys.path.append('emailer/')

from instagram import instagram_scrape
from emailer import send_email

hypelist = [] 

instagrams = [post.rstrip('\n') for post in open('instagrams.txt')]
hypelist += instagram_scrape(instagrams)

send_email(hypelist)
