import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
from urllib.parse import urljoin, urlsplit, urlparse

class extract_books():
    def __init__(self,url):
        self.url = url
        self.data = []


    def get_html(self):
        page = requests.get(self.url)
        return BeautifulSoup(page.content, 'html.parser')


    def get_info(self):
        soup =  self.get_html()
        self.data.append(self.url)
        title = soup.find("h1")
        print(title.string)
        self.data.append(title.string)
        products = soup.find_all("td")
        for product in products:
            if product.string != "Books":
                self.data.append(product.string)
        description = soup.find("p",class_=False, href=False)
        if description is not None:
            self.data.append(description.string)
        else:
            self.data.append("No description")
        categorys = soup.find_all("li", class_=False, href=False)
        for category in categorys:
            if (category.findChild().string != "Home" and category.findChild().string != "Books"):
                self.data.append(category.findChild().string)
        
        if soup.find("p", class_="star-rating Five"):
            self.data.append("Five stars out of Five")
        elif soup.find("p", class_="star-rating Four"):
            self.data.append("Three stars out of Five")
        elif soup.find("p", class_="star-rating Three"):
            self.data.append("Three stars out of Five")   
        elif soup.find("p", class_="star-rating Two"):
            self.data.append("Two stars out of Five")  
        elif soup.find("p", class_="star-rating One"):
            self.data.append("One stars out of Five")   
        self.data.append(self.save_img())
        return self.data
    


    def get_img_url(self):
        soup =  self.get_html()
        image = soup.find("img")
        return image['src']
    
    def save_img(self):
        image = self.get_img_url()
        # url = self.url + image
        url = urljoin('https://books.toscrape.com/', image)
        return url
    

class extract_cat():
    def __init__(self, url):
        self.url = url
        self.total_books = []

    def get_html(self):
        page = requests.get(self.url)
        return BeautifulSoup(page.content, 'html.parser')

    def extract_url_book(self):
        soup =  self.get_html()
        books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
        for lists in books:
            for url in lists:
                anchor = url.find("a")
                if anchor != -1:
                    book_url = anchor.get("href")
                    urls = urljoin(self.url, book_url)
                    url_list = urls.split('\n')
                    for url in url_list:
                        self.total_books.append(self.extract_book(url))
                        
        next_page = self.next_page()     
        if (next_page):
            extract = extract_cat(next_page)
            self.total_books.extend(extract.extract_url_book())
        return self.total_books


    def extract_book(self, url):
        extract = extract_books(url)
        return (extract.get_info())
    
    def next_page(self):
        soup =  self.get_html()
        if soup.find("li", class_="next"):
            page_url = soup.find("li", class_="next").findChild().get("href")
            url = urljoin(self.url, page_url)
            return url


class get_all_books():
    def __init__(self, url):
        self.url = url
        self.total_cat = []

    def get_html(self):
        page = requests.get(self.url)
        return BeautifulSoup(page.content, 'html.parser')
    
    def extract_category(self):
        total_cat = []
        soup = self.get_html()
        categorys = soup.find_all("li", class_=False)
        for category in categorys:
            url_cats = category.find_all("a", class_=False)
            for url_cat in url_cats:
                if url_cat['href'] != "index.html" and url_cat['href'] != "catalogue/category/books_1/index.html":
                    url_cate = url_cat['href']
                    urls = urljoin(self.url, url_cate)
                    self.total_cat.append(self.extract_cat(urls))
        self.total_cat = list(OrderedDict.fromkeys(self.total_cat))
        return(self.total_cat)


    def extract_cat(self, url):
        extract = extract_cat(url)
        return extract.extract_url_book()

"""
useful for finding the url for the catergory 
        categorys = soup.find_all("a")
        for category in categorys:
            print(category['href'])

url = "https://books.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
"""    

def main():
    extract = get_all_books("https://books.toscrape.com/index.html")
    print(extract.extract_category())


if __name__ == "__main__":
    main()