#!/usr/bin/env python3
import sys
from sys import argv
import requests
from bs4 import BeautifulSoup

def finddeadlinks(url, depth):
    raw = requests.get(url)
    soup = BeautifulSoup(raw.content, features='html.parser')
    
    goodLinks=[]
    for Endtry in soup.find_all('a', href=True):
        link = Endtry.get("href")
        try:
            if link.startswith("/"):
                link = url+link
            if requests.get(link).status_code not in [200, 302]:
                print("That is a mighty bad link {", link,"}")
            else:
                goodLinks.append(link)        
        except:
            print("That is a mighty bad link {", link,"}")
    if depth == 0:
        pass
    else:
        for goodLink in goodLinks:
            finddeadlinks(goodLink, depth-1)


if __name__ == '__main__':
    from sys import argv
    progName = argv[0]
    depth = 0
    url = ""
    if len(argv) <= 2:
        print("error with the syntax of the command you typed. Please read the readme file")
        exit(1)
    if argv[1].startswith('-'):
        depth = int(argv[1][1:])
        url = argv[2]
    else:
        url = argv[1]
    finddeadlinks(url, depth)
    # just a test so I can run it in thonny
    #finddeadlinks("http://10.92.21.107:8080", -1)