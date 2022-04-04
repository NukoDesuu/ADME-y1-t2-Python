#answer reading system : retrives n id-answers input (returns ID-ANSWERS LIST)
def id_ans_read(n):
    ia_list = []
    for k in range(n):
        ia_list.append(input().split())
    return ia_list

#grading system : grade letter from given point p (returns LETTER GRADE)
def grade(p):
    g = [ [80, "A"], [70, "B"], [60, "C"], [50, "D"] ]
    for n,l in g:
        if p >= n:
            return l
    return "F"

#marking system : percentage score according to the answers[], solutions[] (returns PERCENTAGE)
#global variable applied : sol
def perc_mark(a):
    cur = 0
    full = len(sol)
    for i in range(full):
        if a[i] == sol[i]:
            cur += 1
    perc = (cur / full) * 100
    return perc

#mark with reporting system : do marking for percent and grade, then report in list style
def ans_mark(li):
    out = []
    for e in li:
        mark = perc_mark(e[1])
        out.append([e[0], mark, grade(mark)])
    return out

#sorting system : sorts student entries according to percentage performance (performs operations within oneself)
def perf_sort(us_list):
    s_list = []
    for l in us_list:
        s_list.append( [ l[1], l[0], l[2] ] )
    s_list.sort(reverse=True)
    o_list = []
    for sl in s_list:
        o_list.append( [ sl[1], sl[0], sl[2] ] )
    return o_list

sol = input()
count = int(input())
id_ans = id_ans_read(count)

p_list = ans_mark(id_ans)
s_p_list = perf_sort(p_list)
for l in s_p_list:
    print(l[0], l[1], l[2])