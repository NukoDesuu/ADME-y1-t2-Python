date = input()

date_comp = date.split("/")
month_n = int(date_comp[1])

month_name = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

print(month_name[month_n - 1] + " " + str(date_comp[0]) + ", " + str(date_comp[2]))