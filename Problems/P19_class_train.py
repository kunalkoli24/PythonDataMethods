# train class which which shows train no. , status and fare. 
from random import randint

class train():
    
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, start, end):
        print(f"ticket is booked in train no: {self.trainNo} from {start} to {end}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self,start,end):
        print(f"Ticket fare in Train no: {self.trainNo} from {start} to {end} is {randint(222,444)}")

t= train(14554)
t.book("Pune","Pandharpur")
t.getStatus()
t.getFare("Pune","Pandharpur")