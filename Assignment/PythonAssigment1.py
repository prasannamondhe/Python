#Problem statement:
#Create a program that takes a user input list, saves it to the list than displays it into and than displays the list.
#You can use sets/Dictionaries/lists to accomplish the task. 


#Accept user input into list
def createUserInputList():
    userListSize = int(input("Enter size of list: "))
    userList = []
    for i in range(userListSize):   
        userInput = input("Enter your input: ")
        userList.append(userInput)
    print("User input list is:\n", userList)
    


#Accept user input into dictionary
def createUserInputDictionary():
    userListSize = int(input("\nEnter size of dictionary: "))
    userDict = {}
    for i in range(userListSize):
        key = input("Enter key: ")
        value = input("Enter value: ")
        userDict[key] = value
    print("User input directory is:\n", userDict)


#Accept user input into sets
def createUserInputSet():
    userListSize = int(input("Enter size of list for set: "))
    userList = []
    for i in range(userListSize):
        userInput = input("Enter your input: ")
        userList.append(userInput)

    userSet = set(userList)
    print("user set is \n", userSet)


#Accept type of data structure user want to create
enteredInput = input("Enter data structure name [List/Dict/Sets]: ")
if(enteredInput=="List"):
    createUserInputList()
if(enteredInput=="Dict"):
    createUserInputDictionary()
if(enteredInput=="Sets"):
    createUserInputSet()

