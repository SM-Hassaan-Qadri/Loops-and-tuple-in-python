# For loop

bank = ["HBL", "Alfalah", "MCB", "Meezan bank"]
for x in bank:
  print(x)
# opens a list,tuple etc

#Else with For 
for x in range(0):
 print(x)
else: print("Finished" )
#x is being printed for number of times the vaue in range

#List comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [z for z in fruits if "a" in z]
print(newlist)
#used for creating another list with few syntax based on value of existng one

#Extra 
#Tuples
food=("pizza", "meat" , "biryani" )
print(food)
#Tuples are created using round bracket in python
