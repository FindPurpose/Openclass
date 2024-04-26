import extract
import pandas as pd
import urllib.request 
from PIL import Image 
from time import perf_counter


class csv_file():
    t1_start = perf_counter() 
    _datas = extract.get_all_books("https://books.toscrape.com/index.html")
    re = 0
    for i in _datas.extract_category():
        data = pd.DataFrame(i, columns = ["product_page_url", "book_title", "universal_product_code(upc)", "price_including_tax", "price_excluding_tax", "tax", "quantity_available", "delete", "product_description", "category", "review_rating", "image_url"])
        data = data.to_csv(f"{extract.cat_list[re]}.csv", index=False)
        re += 1
    t1_stop = perf_counter()
    print("Elapsed time:", t1_stop, t1_start) 
 
    print("Elapsed time during the whole program in seconds:",
                                        t1_stop-t1_start)
"""    for i in datas.index:
        #cat_data = datas.copy()
        datas.iloc[i]
        #data = pd.DataFrame(datas.extract_category(), columns = ["product_page_url", "book_title", "universal_product_code(upc)", "price_including_tax", "price_excluding_tax", "tax", "quantity_available", "delete", "product_description", "category", "review_rating", "image_url"])
        datas.iloc[i].columns = ["product_page_url", "book_title", "universal_product_code(upc)", "price_including_tax", "price_excluding_tax", "tax", "quantity_available", "delete", "product_description", "category", "review_rating", "image_url"]
        datas.iloc[i] = datas.iloc[i].drop("delete", axis=1)
        datas.iloc[i] =  datas.iloc[i].drop("tax", axis=1)
        for j in extract.category_list:
            data = data.to_csv(f"{j}.csv", index=False)"""
    #can put it into parent
    #urllib.request.urlretrieve( name, file_name)
    #img = Image.open("gfg.png") 
    #img.show()


"""
Get the own columns and pass it.
"""