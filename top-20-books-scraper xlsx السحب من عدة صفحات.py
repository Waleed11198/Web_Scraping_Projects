import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
base_url=("https://books.toscrape.com/catalogue/category/books_1/")
page_num=1
all_books=[]
while True:
  url=(f"{base_url}page-{page_num}.html")
  response=requests.get(url)
  if response.status_code!=200:
    print(f"توقفت الطباعة عند الصفحة {page_num}")
    break
  src=response.content
  soup=BeautifulSoup(src,"lxml")
  library=soup.find_all("ol",{"class":"row"})
  for book in library:
    books=book.find_all("li")
    for i in range(len(books)):
      name_book=books[i].find("h3").text
      rating_book=books[i].find_all("p",{"class":"star-rating"})
      rating=books[i].p["class"][1]
      price_name=books[i].find("p",{"class":"price_color"}).text
      all_books.append({"أسم الكتاب":name_book,"تقيم الكتاب":rating,"السعر":price_name})
  page_num+=1
df=pd.DataFrame(all_books)
file=(r"C:\Users\User\Desktop\scraping\ping3.xlsx")
df.to_excel(file,index=False)
os .startfile(file)

