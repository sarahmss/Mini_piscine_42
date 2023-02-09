import sys
import requests
from bs4 import BeautifulSoup #pulling data out of HTML

# pip install -r requirement.txt
"""
    Clicking on the first link in the main text of an English Wikipedia article, and then repeating the process for subsequent articles
    usually leads to the Philosophy article
    1. Clicking on the first non-parenthesized, non-italicized link
    2. Ignoring external links, links to the current page, or red links (links to non-existent pages)
    3. Stopping when reaching "Philosophy", a page with no links or a page that does not exist, or when a loop occurs

    find(): search for an specified id
        * firstHeading
        * mw-content-text
    select(): used to run a CSS selector against a parsed document and return all the matching elements. 
        * 'p > a': <a> inside of <p> 

"""

class WikipediaCrawler:
    def __init__(self):
        self.visited = list()
        self.article_path = '/wiki/' + sys.argv[1]

    def search(self):
        self.url = f'https://en.wikipedia.org{self.article_path}'
        try:
            result = requests.get(url=self.url)
            if result.status_code == 404:
                return print("It leads to a dead end !.")
        except requests.HTTPError as exception:
            return print(exception)
        soup = BeautifulSoup(result.text, 'html.parser')
        title = soup.find(id='firstHeading').text
        if title in self.visited:
            return print("It leads to an infinite loop !")
        self.visited.append(title)
        print(title)
        if title == 'Philosophy':
            if len(self.visited) > 0:
                return(print(f"{len(self.visited)} roads from {self.visited[0]} to Philosophy"))
            else:
                return(print(f"{len(self.visited)} roads from Philosophy to Philosophy"))
        content = soup.find(id='mw-content-text')
        links = content.select('p > a') 
        for element in links:
            if element.get('href') != None and element['href'].startswith('/wiki/') \
                        and not element['href'].startswith('/wiki/wikipedia:') \
                        and not element['href'].startswith('/wiki/Help:'):
                self.article_path = element['href']
                return self.search()



def roads_to_philosophy():
    if (len(sys.argv) != 2):
        sys.exit("Wrong Usage [python3 roads_to_philosophy.py <title>]")
    WikipediaCrawler().search()

if __name__ == '__main__':
    roads_to_philosophy()