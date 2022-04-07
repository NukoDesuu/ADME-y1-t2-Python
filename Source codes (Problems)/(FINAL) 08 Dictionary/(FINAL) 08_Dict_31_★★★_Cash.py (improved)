# def total(pocket):
#     total = 0
#     for bv, bn in pocket.items():
#         total += bv * bn
#     return total

# def take(pocket, money_in):
#     for ibv, ibn in money_in.items():
#         if ibv not in pocket:
#             pocket[ibv] = ibn
#         else:
#             pocket[ibv] += ibn

def pay(pocket, amt):
    payments = {}
    arranged_pocket = []
    for a, b in pocket.items():
        arranged_pocket.append([a,b])
    arranged_pocket = sorted(arranged_pocket, reverse=True)
    for banknote in arranged_pocket:
        v = banknote[0]
        n = banknote[1]
        while n > 0 and amt // v > 0:
            amt -= v
            if v not in payments:
                payments[v] = 1
            else:
                payments[v] += 1
            n -= 1
    if amt > 0:
        return {}
    else:
        for pv, pn in payments.items():
            pocket[pv] -= pn
        return payments

exec("def _a(p):\n print([(k,v) for k,v in sorted(p.items())])\np={10:5, 1:7};_a(pay(p, 42));_a(p)")