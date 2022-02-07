TICKETNAMES = ["One adult", "One child (an adult may bring up to two children)", "One senior", "family ticket (up to two adults or seniors, and three children)", "groups of six people or more, price per person"]
EXTRA = ["Lion feeding", "Penguin feeding", "Evening barbecue (two-day tickets only)"]
COSTONE = [20, 12, 16, 60, 15]
COSTTWO = [30, 18, 24, 90, 22.5] 
COSTEXTRA = [2.5, 2, 5.00]
#pretty much for printing usage maybe cal
uniqueID = []
totalCost = []

#task 1
def display():
    print("\nOne day  Two days   Ticket type")
    for i in range(len(TICKETNAMES)): #prints main list of ticket types
        print(f"${float(COSTONE[i])}    ${float(COSTTWO[i])}      {TICKETNAMES[i]}")
    print("\nCost per person  Extra attraction")
    for i in range(len(EXTRA)):
        print(f"${float(COSTEXTRA[i])}             {EXTRA[i]}")
#end of task 1: days available not neede because there are tickets for everyday :D
#dunno if i should add days into booking: mon, tue...
display()

booking = "y"
while booking == "y":
    #allocate unique id
    if len(uniqueID) == 0:
        uniqueID.append(0)
    else:
        uniqueID.append(uniqueID[-1]+1)

    visitLength = int(input("Visitng for 1 or 2 days?: "))
    while visitLength != 1 and visitLength != 2:
        print("Enter 1 or 2.")
        visitLength = int(input("Visiting for 1 or 2 days?: "))
    
    #tickets
    adult = int(input("Input number of adult tickets: "))
    while adult < 0: #validation: cannot be less than 0
        print("Number has to be greater than 0.")
        adult = int(input("Input number of adult tickets: "))

    child = int(input("Input number of child tickets: "))
    while child < 0:
        print("Number has to be greater than 0.")
        child = int(input("Input number of children tickets: "))

    senior = int(input("Input number of senior tickets: "))
    while senior < 0:
        print("Number has to be greater than 0.")
        senior = int(input("Input number of senior tickets: "))

    family = int(input("Input number of family tickets: "))
    while family < 0: 
        print("Number has to be greater than 0.")
        family = int(input("Input number of family tickets: "))

    group = int(input("Input number of people in group: "))
    while group < 6:
        if group == 0: #account for if they dont want group booking
            break
        print("Number has to be greater than 5.")
        group = int(input("Input number of group tickets: "))

    lion = int(input("Input number of lion feeding tickets: "))
    while lion < 0:
        print("Number has to be greater than 0.")
        lion = int(input("Input number of lion feeding tickets"))

    penguin = int(input("Input number of penguin feeding tickets: "))
    while penguin < 0:
        print("Number has to be greater than 0.")
        penguin = int(input("Input number of penguin feeding tickets"))

    if visitLength == 1: #splits off into if statement because the calculations depend on the length of visit
        totalNormal = (adult*COSTONE[0]) + (child*COSTONE[1]) + (senior*COSTONE[2]) 
        totalOthers = (family*COSTONE[3]) + (group*COSTONE[4]) 
        totalAttractions = (lion*COSTEXTRA[0]) + (penguin*COSTEXTRA[1]) #separating variables so weighting can be applied during discount calculations
        totalCost.append(totalNormal + totalOthers + totalAttractions)

        #checking for discount: task 3
        if (adult+child+senior) > 5 and totalNormal > (COSTONE[4]*(adult+child+senior)):
            print("\nIMPORTANT: A GROUP ticket would be cheaper.")
            print("---BEST VALUE discount---\nDear valued customer, you are qualified for a BEST VALUE discount.\nQuote your unique booking ID at the ticket office upon arrival.")

        if (adult+senior) > 1 and child > 2 and totalNormal > COSTONE[3]:
            print("\nIMPORTANT: A FAMILY ticket would be cheaper.")
            print("---BEST VALUE discount---\nDear valued customer, you are qualified for a BEST VALUE discount.\nQuote your unique booking ID at the ticket office upon arrival.")
        
    else:
        bbq = int(input("Input number of barbeque tickets: "))
        while bbq < 0:
            print("Number has to greater than 0.")
            bbq = int(input("Input number of bbq tickets: "))
        
        #can allow for booking cancellation here

        #it's fine to use this variable names because the look is an if loop so only one of conditional loop will run (variables will not clash with each other)
        totalNormal = (adult*COSTTWO[0]) + (child*COSTTWO[1]) + (senior*COSTTWO[2]) 
        totalOthers = (family*COSTTWO[3]) + (group*COSTTWO[4]) 
        totalAttractions = (lion*COSTEXTRA[0]) + (penguin*COSTEXTRA[1]) + (bbq*COSTEXTRA[2])
        totalCost.append(totalNormal + totalOthers + totalAttractions)

        #checking for discount: task 3
        if (adult+child+senior) > 5 and totalNormal > (COSTTWO[4]*(adult+child+senior)):
            print("\nIMPORTANT: A GROUP ticket would be cheaper.")
            print("---BEST VALUE discount---\nDear valued customer, you are qualified for a BEST VALUE discount.\nQuote your unique booking ID at the ticket office upon arrival.")

        if (adult+senior) > 1 and child > 2 and totalNormal > COSTTWO[3]:
            print("\nIMPORTANT: A FAMILY ticket would be cheaper.")
            print("---BEST VALUE discount---\nDear valued customer, you are qualified for a BEST VALUE discount.\nQuote your unique booking ID at the ticket office upon arrival.")
        
    print("BOOKING DETAILS")
    print(f"Unique booking ID: {uniqueID[-1]}\nTotal cost: ${totalCost[-1]}")

    booking = input("Press 'y' to start another booking, or press any other key to exit: ")

#program check
print("\n-----Bookings completed-----")
for i in range(len(uniqueID)):
    print(f"Unique booking ID: {uniqueID[i]} Booking cost: ${totalCost[i]}")

print("--END--")
