import random
import numpy as np
import sys

"""
@author Amir Lavi
@date   December 8th, 2017
Description: The event class will generate random amount
    of tickets with random prices. Random location will
    be sent through the main method
"""

class Event(object):

    def __init__(self, iD, loc):
        self.tickets = list()
        self.id = iD
        self.location = loc #location is a tuple of (x,y)

        # Call private functions
        self.__generateRandomTickets()

    def __generateRandomTickets(self):
        #randomizing not more than tickets 500 per event
        #because it makes a nicer spread of ticket prices
        tickets = random.randint(0,500)
        list_of_tickets = [None]*tickets

        for ticket in range(tickets):
            list_of_tickets[ticket] = round(random.uniform(1.0,1000.0),2)

        list_of_tickets.sort()
        self.tickets = list_of_tickets

    def PrintEvent(self,distance):
        print ("Event ", str(self.id).zfill(3), " - $", self.tickets[0] ,
            " Distance ", distance)
# VARIABLES #######################################################

"""
The map helps with verification that two events don't
overlap in location.
However, it's nice for visualizing purposes.
"""
COORDINATE_MAP = np.full((21,21),0)

###################################################################

# FUNCTIONS #######################################################
def printMap():
    ##how to print this array nicely was taken from stack overflow
    print ('\n'.join(' '.join(str(cell) for cell in row) for row in COORDINATE_MAP))

def generateEventList():
    event_ids  = random.randint(6,100)
    event_dict = {}

    for event in range(1, event_ids):
        x,y = gereateRandomLocation()
        event_dict[event] = Event(event, (x,y))

    return event_dict

def gereateRandomLocation():
    flag = True

    while(flag):
        x = random.randint(0,20)
        y = random.randint(0,20)
        if(COORDINATE_MAP[x][y] == 0):
                flag = False
                COORDINATE_MAP[x][y] = 1

    return (x-10,y-10)

#Calculating using manhattan distance
def calculate_Distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def getClosestEvents(events):
    close_keys = [(41,0)]*5

    for key in events:
        dist = (calculate_Distance(events[key].location, coordinate))
        if (dist < close_keys[4][0]):
            close_keys[4] = (dist, events[key].id)
        close_keys.sort()

    return close_keys


###################################################################
# Main
###################################################################
if __name__ == '__main__':
    print("Please Input Coordinates:")

    # Error handeling - bad input mainly
    while(1):
        try:
            coordinate = tuple(int(x.strip()) for x in input().split(','))
            while(not(-10 <= coordinate[0] <= 10 and -10 <= coordinate[1] <= 10)):
                print("please input a real coordinate between <-10,-10> to <10,10>")
                coordinate = tuple(int(x.strip()) for x in input().split(','))
            break
        except KeyboardInterrupt:
            print('\ninterrupted!')
            sys.exit(1)
        except:
            print("make sure to print tuple form <e.g (10,5)>")

    COORDINATE_MAP[coordinate[0]+10][coordinate[1]+10] = 2
    events = generateEventList()
    print("Closest Event to",coordinate,":")
    closest_event_list = getClosestEvents(events)

    for event in closest_event_list:
        events[event[1]].PrintEvent(event[0])


    """
    If you want to print the map and visualize how it looks
    like - uncomment the printMap() method below.
    Please advise the point (-10,-10) is on the top right since
    it is printed from the lowest index to the top index.
    """
    # printMap()
