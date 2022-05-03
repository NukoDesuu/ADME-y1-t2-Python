class Card:
    def __init__ (self, value, suit):
        self.v = value
        self.s = suit

    def __str__ (self):
        return "(" + self.v + " " + self.s + ")"

    def getScore(self):
        pairs = {"A": 1, "2": 2, "3": 3, "4": 4,
                 "5": 5, "6": 6, "7": 7, "8": 8,
                 "9": 9, "10": 10}
        if self.v in ["J", "Q", "K"]:
            return pairs["10"]
        return pairs[self.v]

    def sum(self, other):
        return (self.getScore() + other.getScore()) % 10

    def __lt__ (self, rhs):
        faces = {"3": 10, "4": 20, "5": 30, "6": 40,
                 "7": 50, "8": 60, "9": 70, "10": 80,
                 "J": 90, "Q": 100, "K" : 110, "A": 120,
                 "2": 130}
        suits = {"club": 1, "diamond": 2, "heart": 3,
                 "spade": 4}
        return (faces[self.v] + suits[self.s]) < (faces[rhs.v] + suits[rhs.s])

n = int(input())

cards = []

for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))

for i in range(n):
    print(cards[i].getScore())
    
print("-" * 10)

for i in range(n - 1):
    print(Card.sum(cards[i], cards[i+1]))

print("-" * 10)

cards.sort()

for i in range(n):
    print(cards[i])