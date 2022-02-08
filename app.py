# # # # # # # print('Hello World!')
# # # # # # # age: int = 34
# # # # # # # price = 19.55
# # # # # # # first_name = "'Bak'"
# # # # # # # is_online = False
# # # # # # # print(age)
# # # # # # # print(first_name)
# # # # # # # print(is_online)
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # # name = input("What is your name? ")
# # # # # # # print("hello "+ name + '  FF')
# # # # # # # birth_year = input("Enter your birth year: ")
# # # # # # # age: int = 2021 - int(birth_year)
# # # # # # # print(age)
# # # # # # First: float = input("First: ")
# # # # # # Second: float = input("Second: ")
# # # # # # Result: float = float(First) + float(Second)
# # # # # # print("Sum: " + str(Result))
# # # # #
# # # # # course = 'Unloser'
# # # # # print(course.replace('e','12'))
# # # # # print(3 ==2)
# # # # price = 25
# # # # print(price > 10 and price ==30)
# # # temp = 33
# # # if temp > 30:
# # #     print("GO swim")
# # # elif temp <30:
# # #     print('1')
# # i = 1
# # while i <= 10:
# #     print(i * '*')
# #     i += 1
#
# names = ["John", "KLOAN", "KOK", "LOL", "asd"]
# print(names[3])
# names.remove("asd")
# names.reverse()
# names.copy()
# print(names)

# numbers = [1,2,2,3,4,5]
# for item in numbers:
#     print(item)
#
# i = 0
# while i < len(numbers):
#     print(numbers[i] +  )
#     i += 1

i = 0
j = 0
lstnum = [77,98,1001,2,15,15,14,12,14,2002]
while i < len(lstnum):
    if j < lstnum[i]:
        j = lstnum[i]
    i+=1
print(j)
