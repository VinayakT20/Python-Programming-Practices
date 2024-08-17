class A1():
    def fruit(self):
        print("Watermelon is my favourite fruit.")

    def colour(self):
        print("Watermelon has a bright red colour.")

class B1():
    def fruit(self):
        print("I don't like chickoo.")

    def colour(self):
        print("Chickoo is brown in colour.")


ob1 = A1()
ob2 = B1()
for i in (ob1,ob2):
    i.fruit()
    i.colour()
