#scraping E-Commerce Website product title, price and reviews
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#collecting the details from the url
text1 = soup.find_all(class_="_1AtVbE col-12-12")
for line in text1:
    try:
        name=line.find(class_="_4rR01T")
        price=line.find(class_="_30jeq3 _1_WHN1")
        rating= line.find(class_="_2_R_DZ")

#printing the details
        print("NAME      : "+name.get_text())
        print("PRICE     : "+price.get_text())
        print("RATING    : "+rating.get_text())
        print()
        print()
    except:
        pass
