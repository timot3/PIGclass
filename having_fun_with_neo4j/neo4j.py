import pandas as pd
import re  # regex

file = '2019-fa.csv'

classes  = []

class Class:
    def __init__(self, sub, num, name, title, desc, hours, preqs, attrs):
        self.subject = sub
        self.number = num

        if sub == "MCB":
            print(title)
            print(desc + '\n')

        self.name = name
        self.title = title
        self.desc = desc
        hours = re.findall(r"\d\.?\d?", hours)
        self.hours = hours
        dict = {}
        if ". See" in preqs:
            dict["cross_listed"] = re.search(r"/[A-Z]{2,5} [0-9]{1,3}", preqs)
        else:
            index = preqs.find("Prerequisite")
            preqs = preqs[index:]
            dict = get_rels(preqs)

        self.preqs = preqs
        self.attr = attrs

def get_rels(preqs):
    if "OR" in preqs:
        get_rels(preqs[:preqs.find("OR")-1])
        get_rels(preqs[preqs.find("OR")+3:])
        
def main():
    ca = pd.read_csv(file)
    for i, r in ca.iterrows():
        sub = r["Subject"]
        num = r["Number"]
        name = r["Name"]
        title = sub + " " + str(num)
        desc = r["Description"]
        hours = r["Credit Hours"]
        preqs = str(r["Section Info"]) # as a string
        attrs = r["Degree Attributes"]
        c = Class(sub, num, name, title, desc, hours, preqs, attrs)
        classes.append(c)



if __name__ == '__main__':
    main()


# Year	Term	YearTerm	Subject	Number	Name	Description	Credit Hours	Section Info	Degree Attributes	Schedule Information
