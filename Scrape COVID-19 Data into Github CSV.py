#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as bs
import requests
import urllib.request
import time
import json
import csv
import pandas as pd
from IPython.display import Image 
import re
import xlsxwriter
from selenium import webdriver


# In[2]:


import base64
from github import Github
from github import InputGitTreeElement


# In[3]:


link="https://www.worldometers.info/coronavirus/#countries"
page=requests.get(link)
soup=bs(page.content,'html.parser')


# In[4]:


step1= soup.find_all('div',{'class':"tab-pane active"})[2]


# In[5]:


step2 = step1.find_all('table',{'class':"table"})[0]


# In[6]:


step3=step2.find_all('tr',{'class':""})


# In[7]:


field= step3[0].find_all('th') 
field_names=list()
for p in field:
    field_names.append(p.text)
    
file_csv=open('corona.csv','w',newline='')
thewriter=csv.DictWriter(file_csv,field_names)
thewriter.writeheader()
for pt in step3[1:]:
    step4 = pt.find_all('td')
    thewriter.writerow({field_names[0]:step4[0].text
    ,field_names[1]:step4[1].text
    ,field_names[2]:step4[2].text
    ,field_names[3]:step4[3].text
    ,field_names[4]:step4[4].text
    ,field_names[5]:step4[5].text
    ,field_names[6]:step4[6].text
    ,field_names[7]:step4[7].text
    ,field_names[8]:step4[8].text
    ,field_names[9]:step4[9].text
    ,field_names[10]:step4[10].text
    ,field_names[11]:step4[11].text
    ,field_names[12]:step4[12].text
    ,field_names[13]:step4[13].text
    ,field_names[14]:step4[14].text
    ,field_names[15]:step4[15].text
    ,field_names[16]:step4[16].text
    ,field_names[17]:step4[17].text
    ,field_names[18]:step4[18].text})
file_csv.close()


# In[8]:


total_tag=step2.find_all('tr',{'class':'total_row','style':''})[0]
total=total_tag.find_all('td')
filetotal_csv=open('corona_all.csv','w',newline='')
thewriter_total=csv.DictWriter(filetotal_csv,field_names)
thewriter_total.writeheader()
thewriter_total.writerow({field_names[0]:total[0].text
    ,field_names[1]:total[1].text
    ,field_names[2]:total[2].text
    ,field_names[3]:total[3].text
    ,field_names[4]:total[4].text
    ,field_names[5]:total[5].text
    ,field_names[6]:total[6].text
    ,field_names[7]:total[7].text
    ,field_names[8]:total[8].text
    ,field_names[9]:total[9].text
    ,field_names[10]:total[10].text
    ,field_names[11]:total[11].text
    ,field_names[12]:total[12].text
    ,field_names[13]:total[13].text
    ,field_names[14]:total[14].text
    ,field_names[15]:total[15].text
    ,field_names[16]:total[16].text
    ,field_names[17]:total[17].text
    ,field_names[18]:total[18].text})
filetotal_csv.close()


# In[9]:


from github import Github
g = Github("Abdelaziz-Nabil", "#Zezo20182023")


# In[10]:


repo = g.get_user().get_repo("Coronavirus-Cases")
all_files = []
contents = repo.get_contents("")


# In[11]:


while contents:
    file_content = contents.pop(0)
    if file_content.type == "dir":
        contents.extend(repo.get_contents(file_content.path))
    else:
        file = file_content
        all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))


# In[12]:


file_csv=open('corona.csv','r',newline='')
content_csv=file_csv.read()


# In[13]:


git_prefix = 'folder1/'
git_file = git_prefix + 'corona.csv'
if git_file in all_files:
    contents = repo.get_contents(git_file)
    repo.update_file(contents.path, "committing files", content_csv, contents.sha)
    print(git_file + ' UPDATED')
else:
    repo.create_file(git_file, "committing files", content_csv)
    print(git_file + ' CREATED')


# In[208]:


filetotal_csv=open('corona_all.csv','r',newline='')
contenttotal_csv=filetotal_csv.read()


# In[209]:


git_prefix_t = 'folder1/'
git_file_t = git_prefix_t + 'corona all world.csv'
if git_file_t in all_files:
    contents_t = repo.get_contents(git_file_t)
    repo.update_file(contents_t.path, "committing files", contenttotal_csv, contents_t.sha)
    print(git_file + ' UPDATED')
else:
    repo.create_file(git_file_t, "committing files", contenttotal_csv)
    print(git_file_t + ' CREATED')

