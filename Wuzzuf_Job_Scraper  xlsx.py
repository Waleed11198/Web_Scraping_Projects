import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from itertools import zip_longest
#getيرسل طلب لجلب الصفحة
page=requests.get("https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=python")
filelist=[]
#content (ك بايتات يعطيك بيانات خام كما وصلتك من الصفحة  )يعرض محتوى الصفحة 
#text (يعطيك كنص )(نص الصفحة بعد فك الترميز) ) 
src=page.content
#print(name2)

#lxml (محرك تحليل لل htmlاسرع من العادي)
#lxml(تحليل ملفات)
soup=BeautifulSoup(src ,"lxml")
#print(soup)
#find()(يعيد اول عنصر مطابق)
#find_all()(يعيد جميع العناصر المطابقة)


#اسم المهمة
job_titels=soup.find_all("h2",{"class":"css-m604qf"})

#اسم الشركة
company_names=soup.find_all("a",{"class":"css-17s97q8"})

#عنوان
locations_names=soup.find_all("span",{"class":"css-5wys0k"})

#شرح
job_skills=soup.find_all("div",{"class":"css-y4udm8"})

#print(job_skills)
job_titel=[]
company_name=[]
locations_name=[]
skills=[]
#text (للحصول على النص داخل العنصر )

for i in range(len(job_titels)):
 job_titel.append(job_titels[i].text)
 company_name.append(company_names[i].text)
 locations_name.append(locations_names[i].text)
 skills.append(job_skills[i].text)

#zip_longest تستخدم لكي يتم اخذ من كل اسم صفة ويتم ترتيبها ضمن الملف
filelist=[job_titel,company_name,locations_name,skills]
exported=zip_longest(*filelist,fillvalue="")

# تحويل البيانات الى DataFrame 
df = pd.DataFrame(exported, columns=["اسم المهمة", "اسم الشركة", "الموقع", "المهارات"])

# حفظ البيانات في ملف Excel
excel_path = r"C:\Users\User\Desktop\scraping\ping2.xlsx"
df.to_excel(excel_path, index=False)
print("✔️ تم إنشاء الملف بنجاح")

# فتح الملف تلقائيًا
os.startfile(excel_path)
