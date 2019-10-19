import urllib.request
from bs4 import BeautifulSoup

def addProfessor(subSoup):
    print(subSoup.a['href'])


def parseURL(query):

    url = f'https://www.ratemyprofessors.com/search.jsp?query={query}'

    fp = urllib.request.urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(fp, 'html.parser')

    mydivs = soup.findAll("li", {"class": "listing PROFESSOR"})
    for professor in mydivs:  # TODO support for multiple pages
        subSoup = BeautifulSoup(str(professor), 'html.parser')
        school = subSoup.find("span", {"class": "sub"}).get_text()
        if "University Of Illinois at Urbana - Champaign" in school:
            addProfessor(subSoup)

parseURL("Chen%2C+Yuting")


