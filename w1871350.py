# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20212082
 
# Date: 08th December 2021

pass_credit = 0
defer_credit = 0
fail_credit = 0

progress_list = []
trailer_list = []
retriever_list = []
exclude_list = []

new_progress = []
new_module_trailer = []
new_retriver = []
new_exclude = []

progress_total = 0
progress_mod_trailer_total = 0
retriver_total = 0
exclude_total = 0

inputInt = 0

def useList(userChoise):  #This function is used to print lest of data, write that data to the file and read data from the file
    listData = ""
    for i in range(progress_total):
        for x in range(3):
            item_progress = str(progress_list[i][0]) + "," + str(progress_list[i][1]) + "," + str(progress_list[i][2])
            listData += "Progress                          -" + item_progress + "\n"
            break
    for i in range(progress_mod_trailer_total):
        for x in range(3):
            item_progress_trailer = str(trailer_list[i][0]) + "," + str(trailer_list[i][1]) + "," + str(trailer_list[i][2])
            listData += "Progress (Module trailer)         -" + item_progress_trailer + "\n"
            break
    for i in range(retriver_total ):
        for x in range(3):
            item_retriver = str(retriever_list[i][0]) + "," + str(retriever_list[i][1]) + "," + str(retriever_list[i][2])
            listData += "Do not Progress - module retriver -" + item_retriver + "\n"
            break
    for i in range(exclude_total):
        for x in range(3):
            item_exclude = str(exclude_list[i][0]) + "," + str(exclude_list[i][1]) + "," + str(exclude_list[i][2])
            listData += "Exclude                           -" + item_exclude + "\n"
            break

    if (userChoise == 1):
        print(listData)
    if (userChoise == 2):
        with open('textFile.txt', 'a') as file:
            file.write(listData)
            print("Data saved to textFile.txt")
    if (userChoise == 3):
        with open('textFile.txt', 'r') as file:
            display = file.read()
            print(display)

def printHorizontalHistrogram():               # Function horizontal histrogram
    print("\n| ================================HORIZONTAL HISTROGRAM=================================== |\n")
    print("Progress      %d :  " %(progress_total), end="")
    print("*" * progress_total)
    print("Trailer       %d :  " %(progress_mod_trailer_total), end="")
    print("*" * progress_mod_trailer_total)
    print("Retriver      %d :  " %(retriver_total), end="")
    print("*" * retriver_total)
    print("Exclude       %d :  " %(exclude_total), end="")
    print("*" * exclude_total)

    total = progress_total+progress_mod_trailer_total+retriver_total+exclude_total
    print("\n%d outcomes in total. \n"%(total))
    print("---------------------------------------------------------------------------------------------\n")


def printVerticalHistrogram():              # Function vertical histrogram
    print("| ==================================VERTICAL HISTROGRAM===================================== |\n")
    print("Progress    Trailer    Retriver    Excluded")
    max = 0
    if (progress_total > max):
        max = progress_total
    else:
        max =  max
    if (progress_mod_trailer_total > max):
        max = progress_mod_trailer_total
    else:
        max =  max
    if (retriver_total > max):
        max = retriver_total
    else:
        max =  max
    if (exclude_total > max):
        max = exclude_total
    else:
        max =  max

    for x in range(max):
        if (x< progress_total):
            print("*", end="            ")
        else:
            print("             ", end="")
        if (x< progress_mod_trailer_total):
            print("*", end="            ")
        else:
            print("             ", end="")
        if (x< retriver_total):
            print("*", end="           ")
        else:
            print("             ", end="")
        if (x< exclude_total):
            print("*")
        print("\n")

    total = progress_total+progress_mod_trailer_total+retriver_total+exclude_total
    print("\n%d outcomes in total. \n"%(total))
    print("---------------------------------------------------------------------------------------------\n")
            
def printMainMenu():         # function- mainMenu
    print("\n| ============================= MEAIN MENU ============================= |\n")
    print("| -------------------- Horizontal Histrogram - Enter Number - 1 ------------------------- |")
    print("| -------------------- Vertical Histrogram   - Enter Number - 2 ------------------------- |")
    print("| -------------------- Print List            - Enter Number - 3 ------------------------- |")
    print("| -------------------- Write Text File       - Enter Number - 4 ------------------------- |")
    print("| -------------------- Read Text File        - Enter Number - 5 ------------------------- |")
    print("| -------------------- Exit Program          - Enter Number - 6 ------------------------- |\n")

    while True:             # Above written functions call inside the MainMenu function.
        inputInt  = int(input("\nEnter the menu number : "))
        if (inputInt == 1):
            printHorizontalHistrogram()
        elif (inputInt == 2):
            printVerticalHistrogram()
        elif (inputInt == 3):
            useList(1)
        elif (inputInt == 4):
            useList(2)
        elif (inputInt == 5):
            useList(3)
        elif (inputInt == 6):
            break
        else:
            print("Invalid input")
            continue
           
            
while True:                 # Exception handling
    try:
        pass_credit = int(input("Please enter your credits at pass  : "))
        if(pass_credit not in range (0,121,20)):
            print("out of range\n")
            continue
        defer_credit = int(input("Please enter your credits at defer : "))
        if(defer_credit not in range (0,121,20)):
            print("out of range\n")
            continue
        fail_credit = int(input("Please enter your credits at pass  : "))
        if(fail_credit not in range (0,121,20)):
            print("out of range\n")
            continue
        total = pass_credit+ defer_credit+ fail_credit
        if total != 120:
            print("Total incorrect\n")
            continue
    except ValueError:
        print("Integer Required")
        continue

    if(pass_credit == 120):
        print("Progress")
        new_progress = [pass_credit, defer_credit, fail_credit]
        progress_list.append(new_progress)
        progress_total +=1

    elif(pass_credit == 100):
        print("Progress (Module trailer)")
        new_module_trailer = [pass_credit, defer_credit, fail_credit]
        trailer_list.append(new_module_trailer)
        progress_mod_trailer_total +=1

    elif(fail_credit == 80 or fail_credit == 100 or fail_credit ==120):
        print("Exclude")
        new_exclude = [pass_credit, defer_credit, fail_credit]
        exclude_list.append(new_exclude)
        exclude_total +=1

    elif(pass_credit in range(0,81,20)and defer_credit in range (0,121,20) and fail_credit in range (0,61,20)):
        print("Do not Progress -  module retriever")
        new_retriver = [pass_credit, defer_credit, fail_credit]
        retriever_list.append(new_retriver)
        retriver_total +=1

    print("\nWould you like to enter another set of data? ")
    result_input = input("Enter 'y' for yes or 'q' to quit and view results : ")
    if(result_input == "y"):
        continue
    if(result_input == "q"):
        break
    
         
printMainMenu()   #call mainMenu function










        
    
