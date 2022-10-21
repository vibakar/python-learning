# Web Scraping Exercises
# Complete the Tasks Below
# TASK: Import any libraries you think you'll need to scrape a website.

import requests
from bs4 import BeautifulSoup
# import lxml

url = "http://quotes.toscrape.com/"

# TASK: Use requests library and BeautifulSoup to connect to http://quotes.toscrape.com/ and get the HMTL text from the homepage.

res = requests.get(url)
html = BeautifulSoup(res.text, 'lxml')
print(html)

# TASK: Get the names of all the authors on the first page.
print("##################")

authors = html.select(".author")
for author in authors:
    print(author.text)

# TASK: Create a list of all the quotes on the first page.
print("##################")

quotes = html.select(".quote")
for quote in quotes:
    print(quote.select(".text")[0].text)

# TASK: Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top right from the home page 
# (e.g Love,Inspirational,Life, etc...). HINT: Keep in mind there are also tags underneath each quote, 
# try to find a class only present in the top right tags, perhaps check the span.
print("##################")

top_ten_tags = html.select(".tags-box")[0].select(".tag")
for tags in top_ten_tags:
    print(tags.text)


# TASK: Notice how there is more than one page, and subsequent pages look like this http://quotes.toscrape.com/page/2/. 
# Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors on the website. 
# Keep in mind there are many ways to achieve this, also note that you will need to somehow figure out how to check that your loop is on the last page with quotes. 
# For debugging purposes, I will let you know that there are only 10 pages, so the last page is http://quotes.toscrape.com/page/10/, 
# but try to create a loop that is robust enough that it wouldn't matter to know the amount of pages beforehand, perhaps use try/except for this, its up to you!

print("##################")
unique_authors = []
base_url = "http://quotes.toscrape.com/page/{}"
page_exists = True
page_no = 1

while page_exists == True:
    print(f"Scrapping Page {page_no}")

    res = requests.get(base_url.format(page_no))
    html = BeautifulSoup(res.text, "lxml")
    authors = html.select(".author")
    if len(authors) != 0:
        for author in authors:
            if author not in unique_authors:
                unique_authors.append(author.text)
        page_no += 1
    else:
        print("Page doesn't exists")
        page_exists = False
        break

print(len(unique_authors))
print(unique_authors)