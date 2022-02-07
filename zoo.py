TICKETNAMES = ["One adult", "One child (an adult may bring up to two children)", "One senior", "family ticket (up to two adult or seniors, and three children)", "groups of six people or more, price per person"]
EXTRA = ["Lion feeding", "Penguin feeding", "Evening barbecue (two-day tickets only)"]
COSTONE = [20, 12, 16, 60, 15]
COSTTWO = [30, 18, 24, 90, 22.5] #list has int and float
COSTEXTRA = [2.5, 2, 5.00]
uniqueID = [] #non-constants; editable vars

#task 1
def display():
    print("\nOne day  Two days   Ticket type")
    for i in range(len(TICKETNAMES)): #prints main list of ticket types
        print(f"${float(COSTONE[i])}    ${float(COSTTWO[i])}      {TICKETNAMES[i]}")
    print("\nCost per person  Extra attraction")
    for i in range(len(EXTRA)):
        print(f"${float(COSTEXTRA[i])}             {EXTRA[i]}")
#end of task 1: days available not neede because there are tickets for everyday :D

#for one booking: need to reset global vars when new booking
#input what ticket they want to buy; eg. 0 ask how many adult
def purchasing():
    global totalCost #declaring as global because python thinks when im calling totalCost += adult is reassignment and says i havent assigned it in the local function
    day = int(input("One day or two days? (1 or 2): ")) # might move day outside the function and put it into function as a parameter
    while day != 1 and day != 2:
        print("Input must be 1 or 2.")
        day = int(input("One day or two days? (1 or 2): "))
    if day == 1:
        day = COSTONE
    else:
        day = COSTTWO
    
    rawAdult = int(input("Input number of adult tickets: "))
    while rawAdult < 0: #validation: cannot be less than 0
        print("Number has to be greater than 0.")
        rawAdult = int(input("Input number of adult tickets: "))
    totalAdult = rawAdult
    totalCost += rawAdult * day[0]

    rawChild = int(input("Input number of children tickets: "))
    while rawChild < 0:
        print("Number has to be greater than 0.")
        rawChild = int(input("Input number of children tickets: "))
    totalChild = rawChild
    totalCost += rawChild * day[1]

    rawSenior = int(input("Input number of senior tickets: "))
    while rawSenior < 0:
        print("Number has to be greater than 0.")
        rawSenior = int(input("Input number of senior tickets: "))
    totalSenior = rawSenior
    totalCost += rawSenior * day[2]

    #family tickets
    familyReject = False
    accepted = 0
    familyTicket = int(input("Input number of family tickets: "))
    while familyTicket < 0: #familyTicket validating
        print("Amount cannot be less than 0.")
        familyTicket = int(input("Input number of family tickets: "))
    while accepted != familyTicket:
        adult = int(input("Input number of adult in family package: "))
        while adult < 0:
            print("Number has to be greater than 0.")
            adult = int(input("Input number of adult in family package: "))
        senior = int(input("Input number of seniors in family package:"))
        while senior < 0:
            print("Number has to be greater than 0.")
            senior = int(input("Input number of seniors in family package:"))
        child = int(input("Input number of children in family package: "))
        while child < 0:
            print("Number has to be greater than 0.")
            child = int(input("Input number of children in family package: "))

        #family ticket validation
        if adult + senior > 2:
            print("Only up to 2 adult or seniors.")
            familyReject = True #tell if cancel calculation and assignment
        if child > 3:
            print("Cannot have more than 3 chidlren.")
            familyReject == True
        
        if familyReject == False:
            accepted += 1
            totalAdult += adult
            totalChild += child
            totalSenior += senior
            totalCost += day[3]
    
    #group tickets
    group = input("Do you need a group ticket? (Y/N): ")
    group.upper() #formatting input
    while group != "Y" and group != "N": #validating input
        print("Please input Y or N.")
        group = (input("Do you need a group ticket? (Y/N): "))
        group.upper()

    if group == "Y":
        adult = int(input("Input number of adult in group package: "))
        while adult < 0:
            print("Number has to be greater than 0.")
            adult = int(input("Input number of adult in group package: "))

        senior = int(input("Input number of seniors in group package:"))
        while senior < 0:
            print("Number has to be greater than 0.")
            senior = int(input("Input number of seniors in group package:"))
        
        child = int(input("Input number of children in group package: "))
        while child < 0:
            print("Number has to be greater than 0.")
            child = int(input("Input number of children in group package: "))

        totalAdult += adult
        totalChild += child
        totalSenior += senior
        totalCost += day[4] * (adult + senior + child)

    #generates unique booking number
    if len(uniqueID) == 0:
        uniqueID.append(0)
    else:
        a = uniqueID[-1] + 1
        uniqueID.append(a)
    
    print(adult)

    #displaying booking details
    print(f"Total price: ${totalCost}\nUnique booking number: {uniqueID[-1]}\n Adult's ticket: {rawAdult}\nChildren's ticket: {rawChild}\nSenior's ticket: {rawSenior}")

#repeating process
booking = True
while booking == True:
    display()
    purchasing()
    totalAdult = totalChild = totalSenior = totalCost = 0 #resetting vars to 0
    booking = str(input("End booking? (Y to end booking, press anything to continue): "))
    if booking == "Y":
        booking = False
    else:
        booking = True
