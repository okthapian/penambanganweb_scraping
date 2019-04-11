#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re


# In[2]:


req = Request("https://www.suara.com/news/news-category/internasional")
html_page = urlopen(req)
soup = BeautifulSoup(html_page, "lxml")


# In[3]:



html=urlopen("https://www.suara.com/news/news-category/internasional").read()
soup=BeautifulSoup(html,"lxml")
ar= soup.find_all("li","item-outer")
i=1
judul=[]
for j in ar:
    dapat_judul=j.find('h4','post-title').get_text().replace("\n","")
    judul.append(dapat_judul)
print(judul)


# In[ ]:





# In[4]:


links = []
deskripsifull=[]
for link in soup.findAll('a','ellipsis2'):
    links.append(link.get('href')) #menyimpan link
print(links)
des=[]
for i in links: 
    deslink=urlopen(i).read() #membuka link 1per1
    soup1=BeautifulSoup(deslink,"lxml")
    ketdes= soup1.find_all("article")
    da=[]
    for j in ketdes:
        desk=""
        konten= soup1.find_all('article','content-article')
        for i in soup1.find('article','content-article').find_all('p'):
            desk=desk+i.text
        if(not desk in des):
            des.append(desk)
            
print(len(des))
for j in des:
    print(j.replace('"',' ').replace('.',' ').replace('/',' ').replace(',',' ').replace('""',' '))
    print("==========================================")
 

import pandas as pd
import numpy as np 
artikel = {'judul':judul,'deskripsi':des}
df=pd.DataFrame(artikel,columns=['judul','deskripsi'])
# print(df)
df.to_csv("dataku.csv",sep=',')
df.sort_values('judul',ascending=True)

per_kata=[]
for kt in des:
    per_kata.append(kt.split())

print(per_kata)
print(len(des))


# # 

# In[7]:


import pandas as pd 
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
data = pd.read_csv("dataku.csv") 
# Preview the first 5 lines of the loaded data 
deskr=[]
for i in data['deskripsi']:
    deskr.append(i)
    
print(deskr)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




