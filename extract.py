import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlsplit
data = []

class extract_books():
    def __init__(self,url):
        self.url = url


    def get_html(self):
        page = requests.get(self.url)
        return BeautifulSoup(page.content, 'html.parser')


    def get_info(self):
        global data
        soup =  self.get_html()
        data.append(self.url)
        title = soup.find("h1")
        # print(title.string)
        data.append(title.string)
        products = soup.find_all("td")
        for product in products:
            if product.string != "Books":
                data.append(product.string)
        description = soup.find("p",class_=False)
        data.append(description.string)
        categorys = soup.find_all("a")
        for category in categorys:
            if category.string != "Books to Scrape" and category.string != "Home" and category.string != "Books":
                data.append(category.string)
        
        if soup.find("p", class_="star-rating Five"):
            data.append("Five stars out of Five")
        elif soup.find("p", class_="star-rating Four"):
            data.append("Three stars out of Five")
        elif soup.find("p", class_="star-rating Three"):
            data.append("Three stars out of Five")   
        elif soup.find("p", class_="star-rating Two"):
            data.append("Two stars out of Five")  
        elif soup.find("p", class_="star-rating One"):
            data.append("One stars out of Five")   
        data.append(self.save_img())

        return data

    def get_img_url(self):
        soup =  self.get_html()
        image = soup.find("img")
        return image['src']
    
    def save_img(self):
        image = self.get_img_url()
        # url = self.url + image
        url = "https://books.toscrape.com/" + image
        return url
    

class extract_cat():
    def __init__(self, url):
        self.url = url

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
                    r1 = urlsplit(self.url)
                    print(r1.geturl())
                    url = urljoin(self.url, book_url)
                    print(url)
                    self.extract_book(url)
                    
        
        self.next_page()
        """
        This thing has to book because it there is another one it should be able to loop the pages.
        """


    def extract_book(self, url):
        extract = extract_books(url)
        return (extract.get_info())
    
    def next_page(self):
        soup =  self.get_html()
        if soup.find("li", class_="next"):
            page_url = soup.find("li", class_="next").findChild().get("href")
            return urljoin(self.url, page_url)
        else:
            return self.url
        
"""
the original url has index.html. But you actually dont need that part for the website to go through. So would it be better to take of index.html or just try to take it off everytime?
"""



def main():
    extract = extract_cat("https://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html")
    print (extract.extract_url_book())

"""
useful for finding the url for the catergory 
        categorys = soup.find_all("a")
        for category in categorys:
            print(category['href'])
"""


"""
Get the list, unlock the list, then get a href.
class extract_cat():
    def __init__(self, url):
        self.url = url

    



url = "https://books.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
"""    

if __name__ == "__main__":
    main()