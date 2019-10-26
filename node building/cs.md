README for cs.csv/ece.csv

name is course node.
Following course node is a list of n tuples of (course, type) where n can be = 0.
If type = -c, it is a or relationship with n other prereq tuples of type -c.
If type = 0, it is a requirement (preq)
If type = 1, it is a coreq with the current node
If type = 2, credit is not given for both course and current node
If type = 3, it is cross-listed as the course where course is the main course listed
If type = 4, it has special prerequisites and course is a string that tries to explain. CUSTOM, CONSENT are big ones
If type = 5, the course is a class standing (Fr, So, Ju, Sr). All caps, can have multiple
If type = 6 the course is recommended
If type = 7, the course is locked to the major in course, had to do two NOT_ECE, just btw. rest are ECE/CS
Type -5 is reserved to a list of COREQs with OR (type 1, but or)
If type = 8, it is an overriding or. So if the person has this they can take the class reguardless of past ands
Some high level grad classes have no preqs. This is correct, if you are a grad, you can take them.