import extract
import pandas as pd

data = extract.extract_books("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
_data = data.get_info()
__data = pd.DataFrame(_data)
#Maybe use this? columns = ["product_page_url", "book_title", "universal_ product_code (upc)", "price_including_tax", "price_excluding_tax", "tax", "quantity_available", "delete", "product_description", "category", "review_rating", "image_url"]
"""
delete tax portion later
"""
print (__data)
