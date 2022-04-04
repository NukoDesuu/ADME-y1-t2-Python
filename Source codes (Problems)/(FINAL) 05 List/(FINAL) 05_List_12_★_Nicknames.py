n = int(input())

full_names = ['Robert', 'William', 'James', 'John', 'Margaret', 'Edward', 'Sarah', 'Andrew', 'Anthony', 'Deborah']
nick_names = ['Dick', 'Bill', 'Jim', 'Jack', 'Peggy', 'Ed', 'Sally', 'Andy', 'Tony', 'Debbie']

names = [''] * n

for i in range(n):
    names[i] = input()

pairs = []

for name in names:
    if name in full_names:
        pairs.append(nick_names[full_names.index(name)])
    elif name in nick_names:
        pairs.append(full_names[nick_names.index(name)])
    else:
        pairs.append('Not found')

for p in pairs:
    print(p)