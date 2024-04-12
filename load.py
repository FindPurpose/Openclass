import extract
import pandas as pd

class csv_file():
    datas = extract.get_all_books("https://books.toscrape.com/index.html")
    data = pd.DataFrame(datas.extract_category(), columns = ["product_page_url", "book_title", "universal_product_code(upc)", "price_including_tax", "price_excluding_tax", "tax", "quantity_available", "delete", "product_description", "category", "review_rating", "image_url"])
    data = data.drop("delete", axis=1)
    data = data.drop("tax", axis=1)
    data = data.to_csv("first.csv", index=False)
    #can put it into parent

"""
Get the own columns and pass it.
"""