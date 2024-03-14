import requests
from bs4 import BeautifulSoup

class extract_books():
    def __init__(self,url):
        self.url = url

    @staticmethod
    def split_html(self, url):
        page = requests.get(url)
        return BeautifulSoup(page.content, 'html.parser') 
    

extract = extract_books("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
print (extract.split_html)

"""
class extract_cat():
    def __init__(self, url):
        self.url = url

    



url = "https://books.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
"""    


