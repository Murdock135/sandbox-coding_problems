# Program to remove vowels from a string


randomstr = input("Give me your string ")

# to test if the input was recieved correctly
#print("Your given string is {}" .format((randomstr)))
for i in randomstr:
    print(i, end='')

# specify the letters we don't want
vowels = ['a', 'e', 'i', 'o', 'u']
print(vowels)


for index in randomstr:  # index goes through all the values in randomstr
    if index not in vowels:
        print(index)
