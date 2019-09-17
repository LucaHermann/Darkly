import requests
import sys
from bs4 import BeautifulSoup


def urlScrapper(url):
    request = requests.get(url)
    page = request.content
    soup = BeautifulSoup(page, features="html.parser")
    for a in soup.find_all('a', href=True):
        path = a['href']
        if path == '../':
            continue
        elif path == 'README':
            reqReadme = requests.get(url + path)
            content = str(reqReadme.content)
            if " " not in content:
                print("Flag :", content)
                exit(0)
        else:
            urlScrapper(url + path)


if len(sys.argv) < 2:
    print("please give an IP adress as argument")
    exit(0)
else:
    ip = sys.argv[1]
    try:
        baseUrl = "http://" + ip + "/.hidden/"
        urlScrapper(baseUrl)
    except:
        print("nothing found")
