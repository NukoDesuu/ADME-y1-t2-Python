def total(pocket):
    total = 0
    for bv, bn in pocket.items():
        total += bv * bn
    return total

def take(pocket, money_in):
    for ibv, ibn in money_in.items():
        if ibv not in pocket:
            pocket[ibv] = ibn
        else:
            pocket[ibv] += ibn

def pay(pocket, amt):
    payments = {}
    for bv, bn in pocket.items():
        v = bv
        n = bn
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

exec("def _a(p):\n print([(k,v) for k,v in sorted(p.items())])\np={100:3, 10:5, 5:10, 1:7};_a(pay(p, 68));_a(p)")