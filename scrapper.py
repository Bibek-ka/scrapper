import requests
from bs4 import BeautifulSoup

import json

URL = "http://books.toscrape.com/"

def scrape_books(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the page")
        return
    
    #set encoding explicity to handle special character
    response.encoding = response.apparent_encoding
    
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    
    book_list = []
    
    for book in books:
        title = (book.h3.a['title'])
        price_text = book.find("p", class_="price_color").text
        currency = price_text[0]
        price = price_text[1:]
        print(title, currency, price)
        
        book_list.append({"title":title, "currency": currency, "price":price})
        
    with open("books.json", "w", encoding = "utf-8") as f:
        json.dump(book_list, f, indent=4, ensure_ascii=False)
        
    print("Data saved to book.json")
            
    
scrape_books(URL)




# install git
# create reprository in github
# go to gitbash
# git config --global user.name "Bibek kandel"
# git config --global user.email "bibekkandeell@gmail.com"

# git init
# git status =>if you want to check what are the status of Files
# git diff => if you want to check what are change


# git add. => track files and folder
# git commit -m "your message"
# git push => upload changes to github
# copy paste git code from github