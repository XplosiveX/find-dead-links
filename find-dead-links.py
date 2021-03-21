import requests
from bs4 import BeautifulSoup
from sys import argv


def LinkFind(url, travel):
    ## list of links for future use
    foundLinks = []
    validLink = []
    try:
        req = requests.get(url)
    except requests.exceptions.ConnectionError:
        print( url, "Is not a valid pointer to a web address maybe you miss typed https://")
        return
    soup = BeautifulSoup(req.text, "html.parser")
    for elem in soup.find_all("a"):
        link = elem.get("href")
        if link.startswith("/"):
            if url.endswith("/"):
                link = url[:-1] + link
            else:
                link = url + link
        if link not in foundLinks:
            foundLinks.append(link)

    
    print("On page [" + url + "]:")
    for link in foundLinks:
        if not link.startswith("#"):
            try:
                newReq = requests.get(link)
                if newReq.status_code not in [200, 302]:
                    print("\t[" + link + "] is not valid")
                else:
                    validLinks.append(link)
            except:
                print("\t[" + link + "] is not valid")

    if travel > 0:
        for link in validLinks:
            LinkFind(link, travel-1)


if __name__ == "__main__":
    if len(argv) not in [2, 3]:
        print("please enter commands within the following format LinkFind <URL> [-<depth>]")
        exit(1)
    travel = 0
    for ounder in argv[1:]:
        if ounder.startswith("-"):
            try:
                travel = int(ounder[1:])
            except ValueError:
                print("Wrong value within travel depth".format(ounder[1:]))
                exit(1)
        else:
            url = ounder

    LinkFind(url, travel)
