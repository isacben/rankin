#! python3

# title           : rankin.py
# description     : This scirpt googles a keyword and tries to find a blog post from a given website in the search results
# author          : Isaac Benitez Sandoval
# date            : 2018-11-27
# version         : 1.0
# usage           : python3 pyscript.py yourwebsite.com search query
# notes           : The website name string must have the correct format as displayed by Google. 
#                   Use the command 'site:yourwebsite.com' on Google to know how it is displayed.
# python_version  : 3.4 


import requests
import bs4
import sys
import logging
import time

logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')

if len(sys.argv) == 1:
    print('Provide a target website. Check the readme file for instructions.\nUsage: python3 ranking.py yourwebsite.com keyword phrase')
    sys.exit()

if len(sys.argv) == 2:
    print('Give Google a keyword.\nUsage: python3 ranking.py yourwebsite.com keyword phrase')
    sys.exit()

website = sys.argv[1]
query = ' '.join(sys.argv[2:])

print('Target website: ' + website)
print('Googling \'' + query + '\'...')

res = requests.get('http://google.com/search?q=' + query + '&start=0')
res.raise_for_status()
logging.debug('First google page url: %s' % res.url)

soup = bs4.BeautifulSoup(res.text, features='html.parser')
elems = soup.select('cite')

found = False
for i in range(len(elems)):
    link = elems[i].getText()
    if link[0:len(website)] == website:
        print('\033[92m' + 'I found ' + link + ' in position %i' %i + '\033[0m')
        found = True
    logging.debug('Found url %s' %link)

if not found: print('No post was found...')
