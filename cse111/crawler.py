import requests
from bs4 import BeautifulSoup

urls = ["https://stephanie-reed.com/?gad_source=1&gclid=Cj0KCQiAy8K8BhCZARIsAKJ8sfSdl-sNw4ciJiOxgkbH4TogWczpqQj2RapwQJO7iC5hn7Ne2184ltYaAl52EALw_wcB"]

while len(urls) !=0:
    current_url = urls.pop()
    # crawling logic... 
    response = requests.get("https://www.scrapingcourse.com/ecommerce/")
    soup = BeautifulSoup(response.content, "html.parser")
    link_elements = soup.select("a[href]")
    for link_element in link_elements:
        url = link_element['href']
        if "https://stephanie-reed.com/?gad_source=1&gclid=Cj0KCQiAy8K8BhCZARIsAKJ8sfSdl-sNw4ciJiOxgkbH4TogWczpqQj2RapwQJO7iC5hn7Ne2184ltYaAl52EALw_wcB" in url:
            urls.append(url)
    product = {}
    product["url"] = current_url 
    product["image"] = soup.select_one(".wp-post-image")["src"]
    product["title"] = soup.select_one(".product_title").text() 
        
    products.push(product)

    print(product)