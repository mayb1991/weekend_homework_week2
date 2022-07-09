

from distutils import extension
import random


class Parking():
    def __init__(self, ticket, parking_spaces):
                self.ticket =  [i for i in (range(ticket + 1)[1:])]
                self.parking_spaces = [i for i in range(parking_spaces + 1) [1:]]
                self.in_use_spaces = {}
                self.ticket_number = None
#CHANGED TICKET_NUMBER TO  A VARIABLE IN PARKING () SO WE  CAN USE IT LATER
    def takeTicket(self):
        rand_ticket = input('Press enter to take a ticket: ') #ADDED THIS FOR  FLOW
        self.ticket_number = random.randint(1,15) # Program will select a ramdom number from 1-15 for the ticket number
        self.ticket.remove(self.ticket_number) #REPLACE POP WITH  .REMOVE(TICKET_NUMBER) SO IT REMMOVES THAT  SPECIFIC TICKET NUMBER
        self.parking_spaces.remove(self.ticket_number)#REPLACE POP WITH  .REMOVE(TICKET_NUMBER) SO IT REMMOVES THAT  SPECIFIC TICKET NUMBER
        self.in_use_spaces[self.ticket_number] = False
        print(f"Ticket #{self.ticket_number}")

    
    
    def payForParking(self):
        print_ticket = print("How many hours would you like to prepay for?")
        amount_time = {1: "$5.00", 2: "$7.00", 3: "$10.00", 4: "$15.00", "All Day": "$25.00"}
        for time, money in amount_time.items():
            print(f"{time}: {money}")
        choice = int(input("Make your selection 1-5: "))
        if choice == 1:   #I wanted to do this if statement in 2 lines but could not get it to work
                print("You have 1 hour remaining")
                self.in_use_spaces[self.ticket_number] = True #MADE SO SELF.TICKET_NUMBER DOESNT REMOVE KEY FROM THE DICT
        elif choice == 2:
            print("You have 2 hours remaining")
            self.in_use_spaces[self.ticket_number] = True #MADE SO SELF.TICKET_NUMBER DOESNT REMOVE KEY FROM THE DICT
        elif choice == 3:
            print("You have 3 hours remaining")
            self.in_use_spaces[self.ticket_number] = True #MADE SO SELF.TICKET_NUMBER DOESNT REMOVE KEY FROM THE DICT
        elif choice == 4:
            print("You have 4 hours remaining")
            self.in_use_spaces[self.ticket_number] = True #MADE SO SELF.TICKET_NUMBER DOESNT REMOVE KEY FROM THE DICT
        else:
            print("See you in 24 hours!")
            self.in_use_spaces[self.ticket_number] = True #MADE SO SELF.TICKET_NUMBER DOESNT REMOVE KEY FROM THE DICT

            

    def leavingGarage(self):
        parked = True
        while parked:
            extended = input("Would you like to extend your time? (Y/N)")
            if extended.upper() == "Y":
                more_time = int(input("Plase make a slection between 1-5: "))
            else:
                print("Thank you! Hope to see you again soon.")
                break
            
            if more_time == 1:  
                print("You have 1 hour remaining")
            elif more_time == 2:
                print("You have 2 hours remaining")
            elif more_time == 3:
                print("You have 3 hours remaining")
            elif more_time == 4:
                print("You have 4 hours remaining")
            else:
                print("See you in 24 hours!")
       # add_ticket = len(self.ticket) + 1 #REMOMVED BC SELF.TICKET_NUMBER
        self.ticket.append(self.ticket_number)
        self.parking_spaces.append(self.ticket_number)
        self.ticket_number = None #ADDED THIS SO AT THE END THERE  IS N0 SELF.TICKET_NUMBER
        self.in_use_spaces = {} #MOVED WHAT WAS HERE TO THE PAYFORPARKING  SECTION SO THAT WHEN THEY LEAVE THE GARAGE, PARKING_SPACES IS NOW EMPTY


car1 = Parking(15, 15)
print(car1.__dict__)
car1.takeTicket()
print(car1.__dict__)
car1.payForParking()
print(car1.__dict__)
car1.leavingGarage()
print(car1.__dict__)

