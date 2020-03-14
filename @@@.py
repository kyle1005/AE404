# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 10:16:16 2020

@author: kylel
"""
from bs4 import BeautifulSoup
import requests
res = requests.get('https://www.books.com.tw/web/sys_saletopb/books')
soup = BeautifulSoup(res.text,'html.parser')
divs = soup.find_all("div",class_="type02_bd-a")

#for each_div in divs:
#   h4 = each_div.find('h4')
#   if h4:
#       a = h4.find('a')
#       if a:
#           bookName = a.text
#    print(h4)
            
#    ul = each_div.find('ul',class_="msg")
#    liz = ul.find('li',class_="price_a")
#    av = liz.text
#    print(av)
    
    
for index,each_div in enumerate(divs):
   h4 = each_div.find('h4')
   if not h4:
       continue
   a = h4.find('a')
   if not a:
       continue
   bookName = a.text
   print('排名'+str(index+1)+': '+bookName)
