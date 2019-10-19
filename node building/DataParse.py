# author timothy vitkin
import requests
import re
import json
from bs4 import BeautifulSoup


data = []
i = 0
# TODO make the logic better (find next sibling
def get_params(courses, filename):
    for course in courses:
        dep = course.p.strong.a.get_text().split("\xa0")[0]
        number = course.p.strong.a.get_text().split("\xa0")[1]
        name = course.p.strong.a.get_text().split(" ")[0]
        title = course.p.strong.a.get_text().split("\u2002")[1]
        ptag = course.findAll("p", {"class": "courseblockdesc"})[0].get_text()
        alias = ""
        preqs = []

        j_dump = json.dumps({
            'name': name,
            'ptag': ptag
        })
        with open(filename, 'a') as the_file:
            the_file.write(j_dump+',\n')

        if "Same as" in ptag:
            alias = ptag.split("See ")[-1]

        elif "Prerequisite: " in ptag:
            print(ptag)
            for x in re.finditer("[A-Z]+ \d{3}", ptag.split("Prerequisite: ")[-1]):
                val = max(x.span()[0]-6, 0)
                print(ptag.split("Prerequisite: ")[-1])
                preq = ptag.split("Prerequisite: ")[-1][val:x.span()[1]]
                if(len(preq) > 0):
                    preq = preq.split(" ")[1:]
                    preq_n = [x.replace("\xa0", " ") for x in preq]
                    preqs += preq_n
        print(name, preqs)
        hours = re.search('[0-9]+', course.p.strong.a.get_text().split("\u2002")[-1]).group()


def write_to_json(url, filename):
    url = 'http://catalog.illinois.edu/courses-of-instruction/ece/'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    courses = soup.findAll("div", class_="courseblock")
    course_descriptions = soup.findAll("p", class_="courseblockdesc")

    get_params(courses, filename)


write_to_json('http://catalog.illinois.edu/courses-of-instruction/ece/', 'courses_ece.json')
write_to_json('http://catalog.illinois.edu/courses-of-instruction/cs/', 'courses_cs.json')
