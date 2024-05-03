import extract
import pandas as pd
import urllib.request 
from PIL import Image 
from time import perf_counter
from pathlib import Path


class csv_file():
    t1_start = perf_counter() 
    # CAT_BOOK_PATH = Path() / "Category" / "Books"
    # CAT_BOOK_PATH.mkdir(parents=True, exist_ok=True)
    _datas = extract.get_all_books("https://books.toscrape.com/index.html")
    re = 0
    for i in _datas.extract_category():
        data = pd.DataFrame(i, columns = ["product_page_url", "book_title", "universal_product_code(upc)", "price_including_tax", "price_excluding_tax", "tax", "quantity_available", "delete", "product_description", "category", "review_rating", "image_url"])
        data = data.to_csv(f"{extract.cat_list[re]}.csv", index=False)
        # with open(CAT_BOOK_PATH , "wb") as file:
        #     file.write(data)
        re += 1
    t1_stop = perf_counter()
    print("Elapsed time:", t1_stop, t1_start) 
 
    print("Elapsed time during the whole program in seconds:",
                                        t1_stop-t1_start)
    """Send email after submitting"""
