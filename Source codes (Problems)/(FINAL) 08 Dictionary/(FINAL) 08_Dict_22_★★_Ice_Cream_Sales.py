def keys(d, v):
    matches = []
    for dk,dv in d.items():
        if dv == v:
            matches.append(dk)
    return matches

n = int(input())

i = 0
iceCreamsStock = {}

while i < n:
    Entries = input().split()
    iceCreamsName = Entries[0]
    iceCreamsPrice = int(Entries[1])

    iceCreamsStock[iceCreamsName] = iceCreamsPrice
    i += 1

m = int(input())

j = 0
productSales = {}

while j < m:
    solds = input().split()
    productName = solds[0]
    productAmount = int(solds[1])
    if productName not in productSales:
        productSales[productName] = productAmount
    else:
        productSales[productName] += productAmount
    j += 1

totalSales = float(0)
uniqueSales = {}

for pn, pa in productSales.items():
    if pn in iceCreamsStock:
        add = float((pa * iceCreamsStock[pn]))
        if pn not in uniqueSales:
            uniqueSales[pn] = add
        else:
            uniqueSales[pn] += add

### OUTPUT ###

if len(uniqueSales) > 0:
    max_sale = max(uniqueSales.values())
    total_sale = float(sum(uniqueSales.values()))
    top_sale = sorted(keys(uniqueSales, max_sale))

    if len(top_sale) > 1:
        top_sale = sorted(top_sale)
    
    print("Total ice cream sales: " + str(total_sale))
    print("Top sales: " + ", ".join(top_sale))
else:
    print("No ice cream sales")
