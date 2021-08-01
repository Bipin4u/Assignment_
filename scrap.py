import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import textwrap
list = []


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#connect to web
url = 'https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters'
html = urllib.request.urlopen(url, context=ctx).read()
soupa = BeautifulSoup(html, 'html.parser')

# collect all the linkd of the url(https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters) and store it in the list
text1 = soupa.find_all(class_="_2kHMtA")
for line in text1:
    tags=line('a')
    for tag in tags:
        urllink = tag.get("href",None)
        weblink = "https://www.flipkart.com"+urllink
        list.append(weblink)


#ittreating through all the links to collect produuct details
for link in list:
    try:


        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        url = link
        html = urllib.request.urlopen(url, context=ctx).read()
        soupa = BeautifulSoup(html, 'html.parser')

#collecting the details of product
        text=soupa.find(class_="_1YokD2 _2GoDe3")
        name=text.find(class_="B_NuCI")
        price=text.find(class_="_30jeq3 _16Jk6d")
        reviues= text.find_all(class_="col _2wzgFH")

#printing the details
        print("PRODUCT TITLE  : "+name.get_text())
        print("PRICE          : "+price.get_text())
        print("REVIEWS        :")
        n=1

#since there r many reviues , therefore applying for loop
        for reviue in reviues:

            pr =reviue.get_text()
            indent = "         Review  "+str(n)+ ":               "
            wrapper = textwrap.TextWrapper(initial_indent=indent, width=100,
                                           subsequent_indent=' '*15)

            print(wrapper.fill(pr))
            n=n+1
            print()

        print()
        print()
    except():
        pass
