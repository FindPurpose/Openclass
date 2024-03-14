import requests
from bs4 import BeautifulSoup


class extract_books():
    def __init__(self,url):
        self.url = url


    def get_html(self):
        page = requests.get(self.url)
        return BeautifulSoup(page.content, 'html.parser')


    def get_info(self):
        soup =  self.get_html()
        title = soup.find("li", class_="active")
        print(title.string)
        tables = soup.find_all("th")
        for table in tables:
            print(table.string)
        products = soup.find_all("td")
        for product in products:
            print(product.string)
        description = soup.find("p",class_="")
        print(description.string)
        categorys = soup.find_all("a")
        for category in categorys:
            print(category.string)
        if soup.find("p", class_="star-rating Three"):
            print("Three stars out of five")
        print (self.save_img())

    def get_img_url(self):
        soup =  self.get_html()
        image = soup.find("img")
        return image['src']
    
    def save_img(self):
        image = self.get_img_url()
        # url = self.url + image
        url = "https://books.toscrape.com/" + image
        return url






    
    

extract = extract_books("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
print (extract.get_info())

"""
class extract_cat():
    def __init__(self, url):
        self.url = url

    



url = "https://books.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
"""    


