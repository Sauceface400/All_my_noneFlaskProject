class character():
    def __init__(self, name, age, weight):
        self.name = name
        self.age =  age
        self.weight = weight

    def intro(self):
        print(self.name, self.age, self.weight)


#char1 = character()
#char1.name = "Jane"
 
char1 = character("Jane" , 21, "52kg")

char1.intro()