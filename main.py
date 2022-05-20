import requests
from bs4 import BeautifulSoup

def scrape(query):
    url = "https://www.google.com/search?q=" + query.replace(" ", "+")
    r = requests.get(url)
    content = BeautifulSoup(r.content, "html.parser")
    try:
        print(content.find("div", class_=["xpc"]).find("div", class_=["kCrYT"]).text)
    except:
        pass
    try:
        print(content.find("div", class_=["Ey4n2"]).text)
    except:
        pass
    try:
        print(content.find_all("div", class_=["ZINbbc"])[1].text)
    except:
        pass

    f = open("google.html", "w+")
    f.write(str(content))

q = ""

while q != "quit":
    q = input("Enter query: ")
    if(q == "quit"):
        print("Quitting...")
        break
    scrape(q)
    input("")
    print("\n\n--------------------------------\n\n")