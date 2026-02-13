# 1
numbers = [3, 12, 7, 25, 9, 10, 18, 4, 30, 6]

for i in numbers:
    if i >= 10:
        print(i)


# 2
name = input("Enter your name: ")
print("First letter:", name[0])
print("Last letter:", name[-1])


# 3
list1 = [1, 2, 3, 4, 5]
reversed_list = list1[::-1]
print(reversed_list)


# 4
surname = input("Enter your surname: ")
first_five = surname[:5]
print(first_five[::-1])


# 5
list2 = [1, 2, 3, 4, 5, 6]
n = int(input("Enter a number between 1 and 5: "))
print(list2[n-1::n])
