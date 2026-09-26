class TwoDvector:
    def __init__(self ,i, j):
        self.i = i
        self.j = j
    def show(self):
        print(f"The vector is {self.i}i + {self.j}J")

class ThreeDvector(TwoDvector): #Inherit done otherwise error get
    def __init__(self, i, j, k):
        super().__init__(i,j) # set zala first cha reference varun
        self.k = k
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

a = TwoDvector(1,2)
a.show()
b = ThreeDvector(1,2,3,)
b.show()