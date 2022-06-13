class Bio:
    def __init__ (self, height, weight):
        self.h = height
        self.w = weight
    
    def report(self):
        return str(self.h) + ", " + str(self.w)

Nono = Bio(165, 52)
print(Nono.report())