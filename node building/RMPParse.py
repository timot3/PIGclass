import urllib.request
from bs4 import BeautifulSoup

def addProfessor(subSoup, name):
    teacher_url = subSoup.a['href']
    url_base = "https://www.ratemyprofessors.com/"
    url = url_base+teacher_url
    print(teacher_url)
    uuid = teacher_url.split("=")[-1]

    teacher_page = urllib.request.urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(teacher_page, 'html.parser')

    grade = soup.find("div", {"class": "grade"}).get_text()

    print(uuid, grade, name.replace(r"%2C+", r", "))



def parseURL(query):

    url = f'https://www.ratemyprofessors.com/search.jsp?query={query}'

    fp = urllib.request.urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(fp, 'html.parser')

    mydivs = soup.findAll("li", {"class": "listing PROFESSOR"})
    for professor in mydivs:  # TODO support for multiple pages
        subSoup = BeautifulSoup(str(professor), 'html.parser')
        school = subSoup.find("span", {"class": "sub"}).get_text()
        if "University Of Illinois at Urbana - Champaign" in school:
            addProfessor(subSoup, query)

parseURL("Chen%2C+Yuting")


