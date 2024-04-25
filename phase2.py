import pandas as pd
from extract import extract_cat
from time import perf_counter

t1_start = perf_counter() 
extract = extract_cat("https://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html")
    #print(extract.extract_url_book)
datas = pd.DataFrame(extract.extract_url_book(), columns = ["product_page_url", "book_title", "universal_product_code(upc)", "price_including_tax", "price_excluding_tax", "tax", "quantity_available", "delete", "product_description", "category", "review_rating", "image_url"])
datas = datas.drop("delete", axis=1)
datas = datas.drop("tax", axis=1)
datas = datas.to_csv("test1.csv", index=False)
t1_stop = perf_counter()
print("Elapsed time:", t1_stop, t1_start) 
 
 
print("Elapsed time during the whole program in seconds:",
                                        t1_stop-t1_start)