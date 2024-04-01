#Object Oriented Program in python.We deal with real time object and  its entities

class Room: #blue print of object.
    l = int(input("Enter Length: "))
    b = int(input("Enter Breadth: "))
    h = int(input("Enter height: "))

    def area(self):
        print("Area of room is:",self.l*self.b)

    def volume(self):
        print("Volume of room is:",self.l*self.b*self.h)


room = Room()
print(room.area())
print(room.volume())