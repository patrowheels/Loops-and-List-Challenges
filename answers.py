# challenge 1 answer
print("challenge number 1: ")
my_list = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]
odd = []
even = []

for i in my_list:
  if i%2 == 0:
    even.append(i)
  else:
    odd.append(i)

print(odd)
print(even)

# challenge 2 answer
print()
print("challenge number 2: ")
sum = 0
for i in my_list:
  sum += i
print(sum)

# challenge 3 answer
print()
print("challenge number 3: ")


# challenge 4 answer 1
list = [1,2,3,4,5]
happy = []
for i in list:
  happy.append(i)
  print(happy)
  
# challenge 4 answer 2
print()
string = "23456"
string1 = "1"
for i in string:
 print(string1)
 string1 += " "
 string1 += i


# challenge 5 answer
print()
print("challenge number 5: ")
print("here is my list:")
print(my_list)

number = input("select a number from my_list: ")

sum = 0
for i in my_list:
    sum += i
    if i == int(number):
      print(sum)

# challenge 6 answer
print()
print("challenge number 6: ")
# s: store sum of all numbers
s = 0
n = int(input("Enter number "))
# run loop n times
# stop: n+1 (because range never include stop number in result)
for i in range(1, n + 1, 1):
    # add current number to sum variable
    s += i
print("Sum is: ", s)

# challenge 7 answer
my_list1 = [1, 2, 3,20,39,50, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4,88, 90, 70, 54, 63]
new_list = []
print()
print("challenge number 6: ")


for i in my_list1:
  if i < 10:
    continue 
  if i > 60:
    break
  if i % 5 == 0:
    new_list.append(i)
  
print(new_list)


# challenge 8 answer 
print()
print("challenge number 8: ")

string = "123456" [::-1]
new_str = ""

for i in string:
  new_str += i
  new_str += " "
  print(new_str)

for i in string:
  string = string.replace(i,"")
  print(" ".join(string))


  #  challenge 9 answer 
print()
print("challenge number 9: ")
list1 = [10, 20, 30, 40, 50]
# actual solution
list1 = list1 [::-1]
for i in list1:
  print(i)

# easy solution
[50, 40, 30, 20, 10]
list1.reverse()
print(list1)


# challenge 10 answer
print()
print("challenge number 10: ")

number = 12345
# gets the number converted into a string
new_number = str(number)
# reverses the string
new_number = new_number [::-1]
# converts the string back into an integer
new_number = int(new_number)
print(new_number)

# or use a while loop to reverse an integer
'''num = input("give me a number to reverse? ")
num = int(num)
reversed_num = 0

while num != 0:
  # this line gets the last number of number given
    digit = num % 10 
    # 
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))'''


# challenge 11 answer

print()
print("challenge number 11: ")
for i in range(15):
  if i <= 4:
    print(i)
  else:
    print("done")
    break