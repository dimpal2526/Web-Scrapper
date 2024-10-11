#If you want to scrap a website:
# Use the API 
# HTML web scraping using some tool like bs4

#Install all the requirements:
#pip install requests
#pip install bs4
#pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

#step 1: Get the HTML
r = requests.get(url)
htmlcontent = r.content
#print(htmlcontent)

# step 2: parse the HTML
soup = BeautifulSoup(htmlcontent, 'html.parser')
print(soup.prettify)

#step 3: HTML Tree traversal
#
#print(type(title)) #1.Tag
#print(type(title.string))  #2. Navigablestring  
#print(type(soup))  #3.Beautifulsoup
# # 4.comment

# markup = "<p><!-- this is a comment --></p>"
# soup2 = BeautifulSoup(markup)
# print(soup2.p)
# exit()
#print(type(soup2.p.string))

# Get the title of the HTML page
title = soup.title

# Get all the paragraphs from the page
paras = soup.find_all('p')
#print(paras)


#print(anchors)

#Get first element in the HTML page
print(soup.find('p'))

#Get classes of any element in the HTML page
print(soup.find('p')['class'])

#find all the elements woth class  lead
print(soup.find_all("p", class_="lead"))

# Get the text from the tags/soup
print(soup.find('p').get_text())
print(soup.get_text())

# Get all the anchor tag from the page
anchors = soup.find_all('a')
all_links = set()

# Get all the links on the page:
for link in anchors:
    if(link.get('href') !='#'):
        linkText= ("https://codewithharry.com" +link.get('href'))
        all_links.add(link)
        print(linkText)