# Test name: Python Skills Test for Beginners

# Test instructions:
# This test consists of 5 questions. 
# For each question, you will be given a task to perform using Python code. 
# You should write a function that completes the task as described, and then return the result. 
# You should not use any external libraries or modules to complete the tasks. 
# You should not define any global variables. 
# You may define additional helper functions if necessary.

# Test questions:

# Question 1:
# Write a function that takes an integer as an argument and returns the absolute value of the integer.
# Example: 
# input: -5
# output: 5
def absolute_value():
    while True:
        try:
            n=int(input("Enter an integer and I will return the absolute value.\n"))

        except:
            print("\nPlease enter a valid integer.\n")

        else:
            absValue=abs(n)
            print(absValue, "\n")
            break


# Question 2:
# Write a function that takes a string as an argument and returns the string with the first and last characters removed.
# Example:
# input: "hello"
# output: "ell"
def remove_first_last():
    string=input("Enter any word and I shall remove the first and last letter.\n")
    newString=string[1:(len(string)-1)]
    print(newString, "\n")

# Question 3:
# Write a function that takes a list of integers as an argument and returns the sum of all odd numbers in the list.
# Example:
# input: [1, 2, 3, 4]
# output: 4
def sum_odds():
    while True:
        intList = input("Enter integers separated by a space, and I will return any odd numbers.\n")
        numList = intList.split()

        oddNum = []

        # Convert to int and find odd numbers
        for num in numList:
            try:
                num = int(num)
                if num % 2 == 1:
                    oddNum.append(num)
            except ValueError:
                print("Invalid input. Please enter integers only.")
                break
        else:
            if len(oddNum) == 0:
                print("No odd numbers found.\n")
            else:
                print("Odd numbers:", oddNum)
                sumOdd = sum(oddNum)
                print("Sum:", sumOdd, "\n")
            break
#ChatGPT helped
    

            
# Question 4:
# Write a function that takes a list of strings as an argument and returns a new list with all strings that have length 4 or less.
# Example:
# input: ["cat", "dog", "bird", "elephant"]
# output: ["cat", "dog"]
def filter_short_strings():
    list=input("Enter strings separated by a space, and I will return strings with 4 characters or less.\n")
    list=list.split()

    strList=[]

    for i in list:
        if len(i)<=4:
            strList.append(i)

    if len(strList)==0:
        print("No strings with 4 characters or less.")

    print("Strings with 4 characters or less: ", strList, "\n")
            

# Question 5:
# Write a function that takes a dictionary as an argument and returns a new dictionary with all key-value pairs where the key is a string.
# Example:
# input: { "a": 1, "b": 2, "c": 3, 5: "d" }
# output: { "a": 1, "b": 2, "c": 3 }
def filter_string_keys(dictionary):
    new_dict = {}
    for key, value in dictionary.items():
        if isinstance(key, str):
            new_dict[key] = value
    return new_dict

dict={ "a": 1, "b": 2, "c": 3, 5: "d" }
    



#Made by ChatGPT

absolute_value()

remove_first_last()

sum_odds()

filter_short_strings()

resultDict=filter_string_keys(dict)
print(resultDict)




















    
