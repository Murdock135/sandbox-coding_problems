# Given an array of integers, return indices of the two numbers such that they add up to a specific target
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


list_of_nums = []
count=0

while count<5:
    string_nums = input('Enter a digit: ')
    nums = int(string_nums)

    if string_nums.isdigit()==True:
        list_of_nums.append(nums)
        count = count+1
    else:
        break

target = int(input(' What\' the target? '))

print('your list is ', list_of_nums)
listLength = len(list_of_nums)
# print(listLength)
# print(list_of_nums[0])

#APPROACH 1: Brute Force
# for m in range(0, listLength-1):
#     for n in range(m+1, listLength-1):
#         if list_of_nums[m]==list_of_nums[n]:
#             continue
#         elif list_of_nums[m]+list_of_nums[n]==target:
#             print(m,n)


#APPROACH 2: Hash table
hashTable = {}

for index in range(0,len(list_of_nums)):
    complement = target - list_of_nums[index]
    if complement not in hashTable:
        hashTable[list_of_nums[index]] = index
    else:
        print(hashTable[complement], index)