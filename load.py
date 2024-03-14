import extract
import pandas as pd

data = extract.extract_books("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
data_ = []
data_.append(data.get_info()) 
_data = pd.DataFrame(data_, columns = ["product_page_url", "book_title", "universal_ product_code (upc)", "price_including_tax", "price_excluding_tax", "tax", "quantity_available", "delete2", "product_description", "category", "review_rating", "image_url"])
#Maybe use this? columns = ["product_page_url", "book_title", "universal_ product_code (upc)", "price_including_tax", "price_excluding_tax", "tax", "quantity_available", "delete", "product_description", "category", "review_rating", "image_url"]
"""
delete tax portion later
"""
# _data = _data.drop("index",axis=1)
_data = _data.drop("delete2", axis=1)
_data = _data.drop("tax", axis=1)
_data = _data.to_csv("test.csv", index=False)
