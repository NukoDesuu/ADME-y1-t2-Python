### GET INPUT FROM THE USER ###
courses_file = input()
lecturers_file = input()
pairs_file = input()


### GET DATA FROM THE DATABASE ###
# keep data from courses_file in terms of DICTIONARY
courses_key_value = {}
cf = open(courses_file, "r")

line = cf.readline()
while len(line) > 0:
    contents = line.replace("\n",'').split(",")
    key = contents[0]
    value = contents[1]
    courses_key_value[key] = value
    line = cf.readline()

cf.close()

# keep data from lecturers_file in terms of DICTIONARY
lecturers_key_value = {}
lf = open(lecturers_file, "r")

line = lf.readline()
while len(line) > 0:
    contents = line.replace("\n",'').split(",")
    key = contents[0]
    value = contents[1]
    lecturers_key_value[key] = value
    line = lf.readline()

lf.close()

# keep data from pairs_file in terms of LIST
pairs = []
pf = open(pairs_file, "r")

line = pf.readline()
while len(line) > 0:
    contents = line.replace("\n",'').split(",")
    pairs.append([contents[0], contents[1]])
    line = pf.readline()

pf.close()

### MATCH DATA FROM BOTH FILE WITH ONE FROM DATABASE (WHILE CHECKING FOR ERROR) ###
## Data sets :
## courses_key_value (dictionary, member : {index: course})
## lecturers_key_value (dictionary, member : {index: lecturer})
## pairs (list, member : [course_index, lecturer_index])
err_out = "record error"

for p in pairs:
    course_index = p[0]
    lecturer_index = p[1]
    if course_index not in courses_key_value or lecturer_index not in lecturers_key_value:
        print(err_out)
    else:
        print(",".join([courses_key_value[course_index], lecturers_key_value[lecturer_index]]))