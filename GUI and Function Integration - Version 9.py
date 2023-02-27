"""
Author: Justin W Daily
Date written: 03/09/23
Assignment: DailyJustinWFinalProject
Version of Python: 3.11.1

Short Desc: 
"""

#Import module for checking file existence
from pathlib import Path

#Import tkinter module from tk
from tkinter import *
import tkinter as tk

#Instantiate window for output to user
outputWindow = tk.Tk()

#Instantiate textbox for output to user
#Pack textbox into output window
outputTextBox = tk.Text(outputWindow, width=100)
outputTextBox.pack()

#Intantiate window for input from user
inputWindow = tk.Tk()

#Define functions that are attached to buttons in input window

#Check for main file name validity with checkFile function
#Use decision for correct responses to validity check
#If the validity check has failed, output an error message
#Use fileErrorMessage for error message
#If the validity check has passed, use user input from file entry field
#Create a new file with user input value by opening the file with 'w'
#Close the new file after its creation
def newFile():
    """Create a new file"""
    isValid = checkFile()
    if isValid == False:
        fileErrorMessage()
    else:
        fileName = fileEntry.get()
        newFile = open(fileName + ".txt", 'w')
        newFile.close()

#Check for main file name validity with checkFile function
#Use decision for correct responses to validity check
#If the validity check has failed, output an error message
#Use fileErrorMessage function for error message
#Check for copy file name validity with checkCopy function
#If the validity check has failed, output an error message
#Use copyErrorMessage function for error message
#Use getInventoryDictionary function to obtain item dictionary from file
#Use sortInventoryDictionary function to sort the item dictionary by SKU
#Save the sorted inventory dictionary to main file with saveToFile function
#Save the sorted inventory dicitonary to copy file with saveToCopy function
def copyFile():
    """Copy file contents to a different file"""
    isValid = checkFile()
    if isValid == False:
        fileErrorMessage()
    else:
        inDirectory = checkDirectory()
        if inDirectory == False:
            notInDirectoryMessage()
        else:
            isValid = checkCopy()
            if isValid == False:
                copyErrorMessage()
            else:
                inventoryDictionary = getInventoryDictionary()
                inventoryDictionary = sortInventoryDictionary(inventoryDictionary)
                saveToFile(inventoryDictionary)
                saveToCopy(inventoryDictionary)

#Check for main file name validity with checkFile function
#Use decision for correct responses to validity check
#If the validity check has failed, output an error message
#Use fileErrorMessage function for error message
#If the validity check has passed, move on to the rest of the function
#Use getInventoryDictionary function to obtain item dictionary from file
#Use sortInventoryDictionary function to sort the item dictionary by SKU
#Save the sorted inventory dictionary to main file with saveToFile function
#Output sorted item inventory dictionary to user with outputInventory function
def openFile():
    """Output inventory from a file"""
    isValid = checkFile()
    if isValid == False:
        fileErrorMessage()
    else:
        inDirectory = checkDirectory()
        if inDirectory == False:
            notInDirectoryMessage()
        else:
            inventoryDictionary = getInventoryDictionary()
            inventoryDictionary = sortInventoryDictionary(inventoryDictionary)
            saveToFile(inventoryDictionary)
            outputInventory(inventoryDictionary)

#Check for main file name validity with checkFile function
#Use decision for correct responses to validity check
#If the validity check has failed, output an error message
#Use fileErrorMessage function for error message
#Check for item input field validity with checkEntry function
#If the validity check has failed, output an error message
#Use entryErrorMessage function for error message
#If the validity check has passed, move on to the rest of the function
#Use getInventoryDictionary function to obtain item dictionary from file
#Use sortInventoryDictionary function to sort the item dictionary by SKU
#Use getInventoryItem function to add new item to inventory dictionary
#Use sortInventoryDictionary function to sort the item dictionary by SKU
#Save the sorted inventory dictionary to main file with saveToFile function
#Output sorted item inventory dictionary to user with outputInventory function
def addToFile():
    """Add an inventory item to a file"""
    isValid = checkFile()
    if isValid == False:
        fileErrorMessage()
    else:
        isValid = checkEntry()
        if isValid == False:
            entryErrorMessage()
        else:
            inDirectory = checkDirectory()
            if inDirectory == False:
                notInDirectoryMessage()
            else:
                inventoryDictionary = getInventoryDictionary()
                inventoryDictionary = sortInventoryDictionary(inventoryDictionary)
                inventoryDictionary = getInventoryItem(inventoryDictionary)
                inventoryDictionary = sortInventoryDictionary(inventoryDictionary)
                saveToFile(inventoryDictionary)
                outputInventory(inventoryDictionary)

#Check for main file name validity with checkFile function
#Use decision for correct responses to validity check
#If the validity check has failed, output an error message
#Use fileErrorMessage function for error message
#Check for entry field SKU validity with checkSKU function
#If the validity check has failed, output an error message
#Use skuErrorMessage function for error message
#If the validity check has passed, move on to the rest of the function
#Use getInventoryItem function to add new item to inventory dictionary
#Use sortInventoryDictionary function to sort the item dictionary by SKU
#Check if user SKU is in inventory dictionary with checkIfFromFile function
#Use notInFileMessage function to output message if user SKU is not in file
#If user SKU is in the file, set inventorySKU to user SKU from SKU entry field
#Remove SKU entry from inventory dictionary
#Save the altered inventory dictionary to main file with saveToFile function
#Output altered item inventory dictionary to user with outputInventory function
def deleteFromFile():
    """Remove an inventory item from a file"""
    isValid = checkFile()
    if isValid == False:
        fileErrorMessage()
    else:
        inDirectory = checkDirectory()
        if inDirectory == False:
            notInDirectoryMessage()
        else:
            isValid == checkSKU()
            if isValid == False:
                skuErrorMessage()
            else:
                inventoryDictionary = getInventoryDictionary()
                inventoryDictionary = sortInventoryDictionary(inventoryDictionary)
                inFile = checkIfFromFile(inventoryDictionary)
                if inFile == False:
                    notInFileMessage()
                else:
                    inventorySKU = skuEntry.get()
                    inventoryDictionary.pop(inventorySKU)
                    saveToFile(inventoryDictionary)
                    outputInventory(inventoryDictionary)

def checkFile():
    """Check validity of main file name"""
    if fileEntry.get() == "":
        return False
    elif type(fileEntry.get()) != str:
        return False
    else:
        for key in ('/', '\\', '?', '%', '*', ':', '|', '"', '<', '>', '.', ',', ';', '=', ' '):
            if key in fileEntry.get():
                return False
        return True

def checkCopy():
    """Check validity of copy file name"""
    if fileCopyEntry.get() == "":
        return False
    elif type(fileCopyEntry.get()) != str:
        return False
    else:
        for key in ('/', '\\', '?', '%', '*', ':', '|', '"', '<', '>', '.', ',', ';', '=', ' '):
            if key in fileCopyEntry.get():
                return False
        return True

def checkDirectory():
    """Checks for existence of main file"""
    file = Path(fileEntry.get() + ".txt")
    if file.is_file():
        return True
    else:
        return False

#Use elif decision structure to check for validity of user input from
    #input entry fields
#All forms of invalid input return False for validity variable
#Return True for validity variable if all checks are passed
def checkEntry():
    """Check validity of input field values"""
    if skuEntry.get() == "":
        return False
    elif nameEntry.get() == "":
        return False
    elif departmentEntry.get() == "":
        return False
    elif quantityEntry.get() == "":
        return False
    elif priceEntry.get() == "":
        return False
    elif type(skuEntry.get()) != str:
        return False
    elif type(nameEntry.get()) != str:
        return False
    elif type(departmentEntry.get()) != str:
        return False
    elif quantityEntry.get().isdigit() == False:
        return False
    elif priceEntry.get().isdigit() == False:
        return False
    elif " " in skuEntry.get():
        return False
    elif " " in nameEntry.get():
        return False
    elif " " in departmentEntry.get():
        return False
    elif " " in quantityEntry.get():
        return False
    elif " " in priceEntry.get():
        return False
    elif len(skuEntry.get()) != 4:
        return False
    elif len(nameEntry.get()) > 13:
        return False
    elif len(departmentEntry.get()) > 13:
        return False
    elif len(quantityEntry.get()) > 15:
        return False
    elif len(priceEntry.get()) > 15:
        return False
    else:
        return True

#Us elif decision structure to check for validity of user input from
    #SKU entry field
#All forms of invalid input return False for validity variable
#Return True for validity variable if all checks are passed
def checkSKU():
    """Check validity of input field SKU"""
    if skuEntry.get() == "":
        return False
    elif type(skuEntry.get()) != str:
        return False
    elif " " in skuEntry.get():
        return False
    elif len(skuEntry.get()) != 4:
        return False
    else:
        return True

#Obtain list of inventory SKUs from inventory dictionary
#Use in to determine if value from SKU entry field is within the list of keys
#Return True for in file variable if SKU is in inventory dictionary
#Return False for in file variable if SKU is not in inventory dictionary
def checkIfFromFile(inventoryDictionary):
    """Check if SKU is in main file"""
    inventorySKUs = list(inventoryDictionary.keys())
    if skuEntry.get() in inventorySKUs:
        return True
    else:
        return False

#Output message for invalid main file name by inserting text into output textbox
def fileErrorMessage():
    """Output error message for invalid main file name"""
    outputTextBox.insert(tk.END, "Invalid main file name\n" + \
                                 "Main file name field must be filled\n" + \
                                 "Main file name must not contain spaces\n" + \
                                 "Main file name must not contain the following characters:\n" + \
                                 "/ \\ ? % * : | \" < > . , ; =\n" + "\n")

#Output message for invalid copy file name by inserting text into output textbox
def copyErrorMessage():
    """Output error message for invalid copy file name"""
    outputTextBox.insert(tk.END, "Invalid copy file name\n" + \
                         "\n")

def notInDirectoryMessage():
    outputTextBox.insert(tk.END, "File not in directory for main file name" + "\n")

#Output message for invalid entry field values by inserting text into output textbox
def entryErrorMessage():
    """Output error message for invalid input field values"""
    outputTextBox.insert(tk.END, "Invalid input\n" + \
                                 "All inventory input fields must be filled\n" + \
                                 "Inventory input must contain zero spaces\n" + \
                                 "SKU must contain four characters\n" + \
                                 "Name must be ten characters or fewer\n" + \
                                 "Department must be ten characters or fewer\n" + \
                                 "Quantity must be digits only\n" + \
                                 "Quantity must be ten digits or fewer\n" + \
                                 "Price must be digits only\n" + \
                                 "Price must be ten digits or fewer\n" + "\n")

#Output message for invalid SKU entry field value by inserting text into output textbox
def skuErrorMessage():
    """Output error message for invalid input field SKU"""
    outputTextBox.insert(tk.END, "Invalid input\n"\
                                 "SKU field must be filled\n" + \
                                 "SKU must contain four characters\n" + "\n")

#Output message for SKU entry field value not being in main file by inserting text into output textbox
def notInFileMessage():
    """Output message for SKU not being in main file"""
    outputTextBox.insert(tk.END, "SKU not found in inventory" + "\n")

#Initialize the iventory dictionary
#Set file name for main file to main file entry field value
#Set the input file variable to the contents of the main file
#Remove new line from each line in input file
#Create a list of values for each line with split function
#Insert the values that represent the major characteristics of the inventory item
    #into a new list
#Insert the new list into the inventory dictionary
#Use list value from the line that represents the SKU as the key value
#Return the completed inventory dictionary
def getInventoryDictionary():
    """Obtain inventory dictionary from main file"""
    inventoryDictionary = {}
    fileName = fileEntry.get()
    inputFile = open(fileName + ".txt", 'r')
    for line in inputFile:
        line = line.strip()
        line = line.split()
        itemDescriptors = [line[1], line[2], line[3], line[4], line[5]]
        inventoryDictionary[line[0]] = itemDescriptors
    return inventoryDictionary

#Inialize sorted inventory dictionary
#Obtain list of keys from inventory dictionary
#Sort the list of keys
#Add items to sorted inventory dictionary according to the order in the
    #sorted list of inventory dictionary keys
#Return the completed sorted inventory dictionary
def sortInventoryDictionary(inventoryDictionary):
    """Sort inventory dictionary by SKU"""
    sortedInventoryDictionary = {}
    sortedInventorySKUs = list(inventoryDictionary.keys())
    sortedInventorySKUs.sort()
    for key in sortedInventorySKUs:
        sortedInventoryDictionary[key] = inventoryDictionary[key]
    return sortedInventoryDictionary

#Set inventory item variables to appropriate entry field values
#Convert quantity and price to float
#Pass inventory item variables to addToInventoryDictionary function
    #Function adds inventory item to inventory dictionary
#Return the altered inventory dictionary
def getInventoryItem(inventoryDictionary):
    """Obtain inventory item values from input fields"""
    inventorySKU = skuEntry.get()
    inventoryName = nameEntry.get()
    inventoryDepartment = departmentEntry.get()
    inventoryQuantity = quantityEntry.get()
    inventoryQuantity = float(inventoryQuantity)
    inventoryPrice = priceEntry.get()
    inventoryPrice = float(inventoryPrice)
    inventoryDictionary = addToInventoryDictionary(inventoryDictionary, inventorySKU, inventoryName, inventoryDepartment, inventoryQuantity, inventoryPrice)
    return inventoryDictionary

#Initialize list for inventory item descriptors
#Calculate inventory value by multiplying inventory quantity by inventory price
#Append inventory item descriptor list with all inventory values except for SKU
#Add list to inventory dictionary with inventory SKU as key
#Return the altered inventory dictionary
def addToInventoryDictionary(inventoryDictionary, inventorySKU, inventoryName, inventoryDepartment, inventoryQuantity, inventoryPrice):
    """Add an inventory item to the inventory dictionary"""
    inventoryDescriptors = []
    inventoryValue = inventoryQuantity * inventoryPrice
    inventoryDescriptors.append(inventoryName)
    inventoryDescriptors.append(inventoryDepartment)
    inventoryDescriptors.append(inventoryQuantity)
    inventoryDescriptors.append(inventoryPrice)
    inventoryDescriptors.append(inventoryValue)
    inventoryDictionary[inventorySKU] = inventoryDescriptors
    return inventoryDictionary

#Set file name for main file to main file entry field value
#Set the output file variable to the contents of the main file
#Obtain list of inventory keys
#Sort the list of inventory dictionary keys
#For each key in the inventory dictionary key list, initialize a list for inventory item values
#Add the key and the value for an inventory item to the list
#Use the list of inventory item values to write the inventory item to the output file
#Format each line with a space between each inventory item value
#Add a new line at the end of each inventory item
#Close the output file
def saveToFile(inventoryDictionary):
    """Save the latest inventory dictionary to main file"""
    fileName = fileEntry.get()
    outputFile = open(fileName + ".txt", 'w')
    inventorySKUs = list(inventoryDictionary.keys())
    inventorySKUs.sort()
    for key in inventorySKUs:
        inventoryItem = []
        inventoryItem = [key] + inventoryDictionary[key]
        outputFile.write(str(inventoryItem[0]) + " " + \
                         str(inventoryItem[1]) + " " + \
                         str(inventoryItem[2]) + " " + \
                         str(inventoryItem[3]) + " " + \
                         str(inventoryItem[4]) + " " + \
                         str(inventoryItem[5]) + "\n")
    outputFile.close()

#Set file name for copy file to copy file entry field value
#Set the output file variable to the contents of the copy file
#Obtain list of inventory keys
#Sort the list of inventory dictionary keys
#For each key in the inventory dictionary key list, initialize a list for inventory item values
#Add the key and the value for an inventory item to the list
#Use the list of inventory item values to write the inventory item to the output file
#Convert each inventory item value to string
#Format each line with a space between each inventory item value
#Add a new line at the end of each inventory item
#Close the output file
def saveToCopy(inventoryDictionary):
    """Save the latest inventory dictionary to copy file"""
    fileName = fileCopyEntry.get()
    outputFile = open(fileName + ".txt", 'w')
    inventorySKUs = list(inventoryDictionary.keys())
    inventorySKUs.sort()
    for key in inventorySKUs:
        inventoryItem = []
        inventoryItem = [key] + inventoryDictionary[key]
        outputFile.write(str(inventoryItem[0]) + " " + \
                         str(inventoryItem[1]) + " " + \
                         str(inventoryItem[2]) + " " + \
                         str(inventoryItem[3]) + " " + \
                         str(inventoryItem[4]) + " " + \
                         str(inventoryItem[5]) + "\n")
    outputFile.close()

#Obtain list of inventory dictionary keys
#Output table header to output textbox
#For each key value in the list of inventory dictionary keys, initialize a list for inventory item values
#Add the key and the value for an inventory item to the list
#Convert each inventory value to the correct data type
#Use the list of inventory item values to produce a formatted line for output
#Output each line to the output textbox
#Add a new line to each line of output
#Use calculateTotal function to calculate the total value of the inventory
#Output the total value of the inventory as a formatted line
def outputInventory(inventoryDictionary):
    """Output the latest inventory dictionary to the user"""
    inventorySKUs = list(inventoryDictionary.keys())
    outputTextBox.insert(tk.END, "%-6s%-15s%-15s%-17s%-17s%-25s" % ("SKU", "Name", "Department", "Quantity", "Price", "Value") +"\n")
    for key in inventorySKUs:
        inventoryItem = []
        inventoryItem = [key] + inventoryDictionary[key]
        inventoryItem[0] = str(inventoryItem[0])
        inventoryItem[1] = str(inventoryItem[1])
        inventoryItem[2] = str(inventoryItem[2])
        inventoryItem[3] = float(inventoryItem[3])
        inventoryItem[4] = float(inventoryItem[4])
        inventoryItem[5] = float(inventoryItem[5])
        outputTextBox.insert(tk.END, "%-6s%-15s%-15s%-17d%-17d%-25d" % (inventoryItem[0], inventoryItem[1], \
                                                                                inventoryItem[2], inventoryItem[3], \
                                                                                inventoryItem[4], inventoryItem[5]) + "\n")
    totalInventoryValue = calculateTotal(inventoryDictionary)
    outputTextBox.insert(tk.END, "%-70s%-25d" % ("Total Inventory Value", totalInventoryValue) + "\n")

#Initialize total inventory value as zero
#Obtain list of inventory dictionary keys
#For each key in the list of inventory dictioary keys, add the inventory value to the total inventory value
#Return the total inventory value
def calculateTotal(inventoryDictionary):
    """Calculate the total value of inventory with cost of inventory items"""
    totalInventoryValue = 0
    inventorySKUs = list(inventoryDictionary.keys())
    for key in inventorySKUs:
        inventoryItem = []
        inventoryItem = [key] + inventoryDictionary[key]
        totalInventoryValue += float(inventoryItem[5])
    return totalInventoryValue

#Use destroy function to close both input window and output window
def closeProgram():
    """Close both windows of the program"""
    inputWindow.destroy()
    outputWindow.destroy()

fileLabel = tk.Label(inputWindow, text="Main File Name:")
fileLabel.grid(row=0, column=1)

fileEntry = tk.Entry(inputWindow, text="")
fileEntry.grid(row=0, column=2)

fileCopyLabel = tk.Label(inputWindow, text="Copy File Name:")
fileCopyLabel.grid(row=1, column=1)

fileCopyEntry = tk.Entry(inputWindow, text="")
fileCopyEntry.grid(row=1, column=2)

paddingFrame = tk.Frame(inputWindow)
paddingFrame.grid(row=2, column=0, columnspan=4)

paddingLabel = tk.Label(master=paddingFrame, text="", width=40)
paddingLabel.pack()

skuLabel = tk.Label(inputWindow, text="SKU:")
skuLabel.grid(row=3, column=1)

skuEntry = tk.Entry(inputWindow, text="")
skuEntry.grid(row=3, column=2)

nameLabel = tk.Label(inputWindow, text="Item Name:")
nameLabel.grid(row=4, column=1)

nameEntry = tk.Entry(inputWindow, text="")
nameEntry.grid(row=4, column=2)

departmentLabel = tk.Label(inputWindow, text="Department:")
departmentLabel.grid(row=5, column=1)

departmentEntry = tk.Entry(inputWindow, text="")
departmentEntry.grid(row=5, column=2)

quantityLabel = tk.Label(inputWindow, text="Quantity:")
quantityLabel.grid(row=6, column=1)

quantityEntry = tk.Entry(inputWindow, text="")
quantityEntry.grid(row=6, column=2)

priceLabel = tk.Label(inputWindow, text="Price:")
priceLabel.grid(row=7, column=1)

priceEntry = tk.Entry(inputWindow, text="")
priceEntry.grid(row=7, column=2)

paddingFrameTwo = tk.Frame(inputWindow)
paddingFrameTwo.grid(row=8, column=0, columnspan=4)

paddingLabelTwo = tk.Label(master=paddingFrameTwo, text="")
paddingLabelTwo.pack()

newFileButton = tk.Button(inputWindow, text="New File", command=newFile)
newFileButton.grid(row=9, column=1)

copyFileButton = tk.Button(inputWindow, text="Copy File", command=copyFile)
copyFileButton.grid(row=9, column=2)

openFileButton = tk.Button(inputWindow, text="Open File", command=openFile)
openFileButton.grid(row=10, column=1)

addToFileButton = tk.Button(inputWindow, text="Add To File", command=addToFile)
addToFileButton.grid(row=10, column=2)

deleteFromInventoryButton = tk.Button(inputWindow, text="Delete From Inventory", command=deleteFromFile)
deleteFromInventoryButton.grid(row=11, column=1)

closeButton = tk.Button(inputWindow, text="Close Program", command=closeProgram)
closeButton.grid(row=11, column=2)

outputWindow.mainloop()
