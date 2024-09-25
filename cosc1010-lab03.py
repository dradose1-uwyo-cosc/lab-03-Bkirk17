# Your Name Here
# UWYO COSC 1010
# Submission Date
# Lab 03 
# Lab Section: 
# Sources, people worked with, help given to: 
# your
# comments
# here



# This is your second lab section. It will primarily be based on the Introducing Lists lecture, reference it if you need
# Complete all sections of this assignment 


print("Part One------------------------------------------------------------------------")
#We are going to start with the basics. Declare a list  states that contains the elements: Wyoming, Colorado, Montana in that order 
#Note this is the ONLY point where you need to declare the states list



#print the entire list
States = ["Wyoming","Colorado","Montana"]


#now print the first element in the list
print(States[0])

#Print the last element using the syntax shown in class to access the final element (hint, think negatives)
print(states[-1])

#Using an F-string to access the first and second element print the string "COLORADO is south of WYOMING", matching the casing provided
print(f"{States[1]} is south of {States[0]}")



print("Part Two------------------------------------------------------------------------")
#Append the following states to your list: Washington, Oregon, California and print your list
States = ["Wyoming","Colorado","Montana"]
States.Append["Washington"]
States.Append["Oregon"]
States.Append["Califorinia"]
print(states)

#Again using the specific syntax mentioned in class overwrite the second to last element to be Maine, printing the list 
states[-2]= "Maine"
print(states)
#Insert the state Texas to be the third element in the list, again printing your list
states[-1]= "Texas"
print(states)

#Using the `del` statement remove the fourth item from the list, print your list 
del states[3]
print(states)
#Remove Texas using its value, print the list
del states[4]
print(states)
print("Part Three----------------------------------------------------------------------")
#Temporarily sort your list, print it both sorted and unsorted 
print("unsorted",states)
sorted_states=sorted(states)
print("sorted",sorted_states)

#Permanently sort your list in reverse order, printing it out
state_sort(reverse=true)
print("rsorted in reverse order", states)

#Using the reverse method reverse the list and print it
states.reverse()
print("Reversed list:", states)
