# digit_upper_lower
student_ID = input("Please input your student ID : ")
digit = '0123456789'.split()

if len(student_ID) != 10 and student_ID.split() not in digit :
  print("Your input is invalid.")
  

fc = student_ID[-1:-3:-1]
_2xcode = ['', 'ENGINEERING', 'ARTS' ,'SCIENCE', 'POLITICAL SCIENCE', 'ARCHITECTURE', 'COMMERCE AND ACCOUNTANCY', 'EDUCATION', 'COMMUNICATION ARTS', 'ECONOMICS']
_3xcode = ['MEDICINE', 'VETERINARY SCIENCE', 'DENTISTRY', 'PHARMACEUTICAL SCIENCES', 'LAW', 'FINE AND APPLIED ARTS', 'NURSING', 'ALLIED HEALTH SCIENCES', 'PSYCHOLOGY', 'SPORTS SCIENCE']

if fc[0] == '2':
  pass