# author timothy vitkin
import requests
import re
import json
from bs4 import BeautifulSoup

url = 'http://catalog.illinois.edu/courses-of-instruction/cs/'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
courses = soup.findAll("div", class_="courseblock")
course_descriptions = soup.findAll("p", class_="courseblockdesc")


data = []
i = 0
# TODO make the logic better (find next sibling
def get_params(courses):
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
        with open('courses.json', 'a') as the_file:
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

get_params(courses)

'''
for course, coursedesc in courses, course_descriptions:
    # department, course_number, course_name, course_description, course_prereqs =
    department = course.find()
    data.append({
        'department': department

    })
'''
'''

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})
'''



'''
original garbage:



department = url.split('/')[-2]
    print(department)
    current_course = str(current_course)
    current_course_description = str(current_course_description)

    print(current_course + '\n\n')
    print(current_course_description + '\n\n')


    # all text from the url onwards
    start_pos = current_course.find('href=')
    janky_ass_substring = current_course[start_pos+6:]  # get the url from 'href=' onwards, split it by '/

    # get course number
    course_number = int(janky_ass_substring.split('/')[6][:3])
    print(course_number)
    # get course name
    temp_arr = janky_ass_substring.split('\u2002')
    course_name = temp_arr[1].strip(' ')
    print(course_name)

'''