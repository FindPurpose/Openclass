import extract

data = extract.extract_books("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
data2 = data.get_info()
print (data2)