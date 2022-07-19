#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#-----------------------------------
#                                   #
# »Download Nohe as site«           # 
# programmer : Mohammad Lakzaee     #
# Version : 0.2                     #
#-----------------------------------#

import requests
import re
from bs4 import BeautifulSoup
import random

print("Start Downlaoding Nohe ....")
page = requests.get("https://nicmusic.net/%D9%85%D8%AF%D8%A7%D8%AD%DB%8C-%D8%AC%D8%AF%DB%8C%D8%AF/").content

soup = BeautifulSoup(page, 'html.parser')


for link in soup.find_all('a', attrs={'href': re.compile("mp3"), 'class': 'dl-320'}):
    nohe = link.get('href')
    dl = requests.get(nohe, stream=True)
    ran = str(random.randint(30, 400))
    f = open("nohes/{}.mp3".format(ran), "wb")
    f.write(dl.content)
    f.close()
    print(nohe)
    
    
print("End Download Nohe ...")