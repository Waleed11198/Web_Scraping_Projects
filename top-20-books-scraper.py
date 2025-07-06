import requests
from bs4 import BeautifulSoup
import csv

#سنستدعي الرابط لجلب الصفحة المرادة
page=requests.get("https://books.toscrape.com/catalogue/category/books_1")

def main(page):
 #content ترجع الصفحة بشكل (byte code)
 src=page.content
 
 
 #lxml اقوى محلل لل html
 soup=BeautifulSoup(src,"lxml")
 library_books=[]
 library=soup.find_all("ol",{"row"})
 

 for books in library:
  all_books=books.find_all("li")
  number_of_book=len(all_books)
  print(number_of_book)
 
 
  for i in range(number_of_book):
   
   #اسم الكتاب
   name_book=all_books[i].find("h3").text.strip()
   
   
   # تقيم الكتاب
   rating_book=all_books[i].find("p",class_="star-rating")
   if  rating_book and "class" in rating_book.attrs: 
    rating_classes=rating_book["class"]  #يعني عطيني جميع ال li
    if len(rating_classes)>1:
     rating=rating_classes[1]
     print(f" تقيم الكتاب رقم{i+1}:{rating}")
    else:
     print(f"تقيم الكتاب رقم {i+1}:لايوجد قيم")

   
   #السعر
    price_name=all_books[i].find("p",{"class":"price_color"}).text.strip()
    print(price_name)
   
   
   #حفظ الاستنتاج ضمن مكتبة
    library_books.append({"اسم الكتاب":name_book,"السعر":price_name,"التقيم":rating})
   
    
    keys=library_books[0].keys()                   #يأخذ اسماء الاعمدة ليضعها اول سطر
    with open(r"C:\Users\User\Desktop\web_scraping1\scraping1.csv","w",newline="",encoding="utf-8") as myfile:
     dict_writer=csv.DictWriter(myfile,keys)       #يجهز كاتب csv حسب المفاتيح
     dict_writer.writeheader()                     #يكتب اول سطر عناوين المكتبة
     dict_writer.writerows(library_books)          #يكتب جميع الصفوف دفعة واحدة من قائمة القواميس   
     print("file created")

main(page) 
import os
file=r"C:\Users\User\Desktop\web_scraping1\scraping1.csv"
os.startfile(file)
