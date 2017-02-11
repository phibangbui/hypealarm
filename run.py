import sys
sys.path.insert(0, 'scrapers/instagram/')

from instagram import instagram_scrape

instagrams = [post.rstrip('\n') for post in open('instagrams.txt')]
instagram_scrape(instagrams)

