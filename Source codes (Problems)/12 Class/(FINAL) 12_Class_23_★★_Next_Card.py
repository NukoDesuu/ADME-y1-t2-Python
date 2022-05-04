class Card:
    
    def __init__ (self, value, suit):
        self.v = value
        self.s = suit
    
    def getOrder (self):
        orders = ["3", "4", "5", "6", "7", "8", "9", "10",
                  "J", "Q", "K", "A", "2"]
        return orders.index(self.v)

    def getSuit (self):
        suits = ["club", "diamond", "heart", "spade"]
        return suits.index(self.s)
    
    def __str__ (self):
        num = range(20)
        if self.v in num and self.s in num:
            orders = ["3", "4", "5", "6", "7", "8", "9", "10",
                  "J", "Q", "K", "A", "2"]
            suits = ["club", "diamond", "heart", "spade"]
            return "(" + orders[self.v] + " " + suits[self.s] + ")"
        else:
            return "(" + self.v + " " + self.s + ")"

    def next1(self):
        num = range(20)
        if not(self.v in num and self.s in num):
            o = self.getOrder()
            s = self.getSuit()
        else:
            o = self.v
            s = self.s
        s += 1
        if s == 4:
            s = 0
            o += 1
        if o == 13:
            o = 0
        return Card(o, s)

    def next2(self):
        num = range(20)
        if not(self.v in num and self.s in num):
            o = self.getOrder()
            s = self.getSuit()
        else:
            o = self.v
            s = self.s
        s += 1
        if s == 4:
            s = 0
            o += 1
        if o == 13:
            o = 0
        self.v = o
        self.s = s
        return 
        

n = int(input())
cards = []

for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))

for i in range(n):
    print(cards[i].next1())

print("-" * 10)

for i in range(n):
    print(cards[i])

print("-" * 10)

for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])