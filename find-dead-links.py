import requests 
from pathlib import Path
import sys
from sys import argv
from bs4 import BeautifulSoup
Statemanage = Path(argv[0]).stem
AllLinks= []
deadLinks= []


def searchLink(url, linkDepth=0):
    try:
        r = requests.get(url)
        searchedLinks.append(url)
        soup = BeautifulSoup(r.text, features='html.parser')
        for link in AllLinks:
            if r.status_code not in [200,302]:
                deadLinks.append(url)
                print(deadLinks[-1])
                print('That is a very bad looking link')
            else:
                print('That is a mighty fine looking link')
    except:
        deadLinks.append(url)
if __name__ == '__main__':
    depth = 0
    url = ''
    if len(argv) in [2,3]:
        pass
    else:
        print("incorrect ussage syntax, please read the readme file")
        exit(1)
    for arg in argv:
        if "-" in arg:
            try:
                depth = int(arg[1:])
            except:
                print("Invalid usage, please read the readme file for help with documentation.")
        else:
            url = arg
    searchLink(url, linkDepth=0)
