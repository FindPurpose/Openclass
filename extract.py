import requests
from bs4 import BeautifulSoup


class extract_books():
    def __init__(self,url):
        self.url = url


    def get_html(self):
        page = requests.get(self.url)
        return BeautifulSoup(page.content, 'html.parser')


    def get_info(self):
        data = []
        soup =  self.get_html()
        title = soup.find("li", class_="active")
        data.append(title.string)
        products = soup.find_all("td")
        for product in products:
            data.append(product.string)
        description = soup.find("p",class_="")
        data.append(description.string)
        categorys = soup.find_all("a")
        for category in categorys:
            if category.string != "Books to Scrape" and category.string != "Home":
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
        #It does return but doesn't retun what I want
        #returns in string in a tuple
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
    

def main():
    extract = extract_books("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
    print (extract.get_info())

"""
useful for finding the url for the catergory 
        categorys = soup.find_all("a")
        for category in categorys:
            print(category['href'])
"""


"""
class extract_cat():
    def __init__(self, url):
        self.url = url

    



url = "https://books.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
"""    

if __name__ == "__main__":
    main()