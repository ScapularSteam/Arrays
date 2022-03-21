# Define Variables #

length = 0
width = 0
yesOno = str('Hi')

area = 0
# Create a function to ask the User for Measurements

def findArea():

    length = float(input(print('Please enter the Length of your Rectangle')))
    width = float(input(print('Please enter the Width of your Rectangle')))

    print('You picked ', length ,'for your length, and ', width ,'for your width, is this correct? y/n')

# Create a function to ask the user what they would like to do #

def introduction():

    print('Hi, Welcome to the Area Calculator!')
    yesOno = str(input(print('What would you like to do, "c" to calculate an area, "l" to list all previous areas')))

# Create a function to read a file #

def readFile():

    # Will output the contents line by line
    f = open("previousAreas.txt", "r")
    for line in f:
        print(line)
# Decide if the User wants to continue #

while True:

    introduction()

    if yesOno == 'c':
        findArea()
        yesOno = str(input)

        if yesOno == 'n':
            print('Ok, please re-enter the data')
            continue
        else:
            break
        
        # Calculate the Area #

        area = length * width
        print('The area is ', area ,)

        # Writing to text files #


        textToWrite = ('Your area is ' + str(area) + '\n') # As the write function only takes 1 argument, we have to merge our strings now

        # Creates a file named by the Input of the User #

        f = open("previousAreas.txt", "a")
        f.write(textToWrite)
        f.close()
    else:
        