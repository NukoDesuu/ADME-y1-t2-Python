inp = input()
length = len(inp)

print(length)

char_list = 'abcdefghijklmnopqrstuvwxyz' * 2
remain_code_list = ['01', '02', '51', '53', '55', '58']
faculty_list = ['The Sirindhorn Thai Language Institute', 'General Education Center', 'Graduate School', 'School of Agricultural',
                'College of Population Studies', 'College of Public Health Sciences', 'Language Institute',
                'Sasin Graduate Institute of Business', 'Administration of Chulalongkorn University']
faculty_branches = ['Engineering', 'Arts', 'Science', 'Political Science', 'Architecture', 'Commerce and Accountancy',
                    'Education', 'Communication Arts', 'Economics', 'Medicine', 'Veterinary Science', 'Dentistry',
                    'Pharmaceutical Sciences', 'Law', 'Fine and Applied Arts', 'Nursing', 'Allied Health Sciences',
                    'Psychology', 'Sports Science']

print(char_list)
print(inp)

if length == 2:
    if inp in char_list:
        print("Error")
    else:
        x = int(inp)
