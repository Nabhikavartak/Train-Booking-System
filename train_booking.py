class train:

    def __init__(self,name, fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def getStatus(self):
        print('***************************')
        print(f"The name of the train is {self.name}")
        print(f"Number of seats available are {self.seats}")
        print('***************************')

    def getFare(self):
        print('                   ***************************')
        print(f"                  The fare for single seat :Rs.{self.fare}")
        print('                   ***************************')

    def BookTicket(self):
        if (self.seats>0):
            print(f"Your ticket has been booked!!! Your Seat Number is {self.seats}")
            self.seats=self.seats-1
        else:
            print("Sorry the train is Full!!You are in waiting list")


intersity=train("Intersity Express:14051",90,250)
intersity.getStatus()
intersity.BookTicket()
intersity.BookTicket()
intersity.getFare()
        
