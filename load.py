import extract
import pandas as pd

data = extract.extract_cat("https://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html")
data = pd.DataFrame(data.extract_url_book(), columns = ["product_page_url", "book_title", "universal_product_code(upc)", "price_including_tax", "price_excluding_tax", "tax", "quantity_available", "delete", "product_description", "category", "review_rating", "image_url"])
#Maybe use this? columns = ["product_page_url", "book_title", "universal_ product_code (upc)", "price_including_tax", "price_excluding_tax", "tax", "quantity_available", "delete", "product_description", "category", "review_rating", "image_url"]
"""
delete tax portion later
"""
# _data = _data.drop("index",axis=1)
data = data.drop("delete", axis=1)
data = data.drop("tax", axis=1)
data = data.to_csv("test.csv", index=False)
