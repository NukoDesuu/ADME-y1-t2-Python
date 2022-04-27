import numpy as np

def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data

def report_lower_than_mean(weight, data):
    student_ID = data[::, 0]
    grades = data[::, 1:]
    weighted_grades = grades * weight
    n_grades = weighted_grades.shape[0]
    s = np.ndarray((n_grades, 1), int)
    for i in range(n_grades):
        s[i] = np.sum(weighted_grades[i])
    m = np.mean(s)
    low_scores = list()
    for i in range(n_grades):
        cur_s = np.sum(weighted_grades[i])
        if cur_s < m:
            low_scores.append(str(student_ID[i]))
    print(", ".join(low_scores))

w,d = read_data(); report_lower_than_mean(w,d)
