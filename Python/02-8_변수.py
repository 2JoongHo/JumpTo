# a = 1
# b = "python"
# c = [1, 2, 3]

# name = "홍길동"
# age = 25
# user_name = "gildong"
# userName = "gildong"
# _private = "비공개"
# count1 = 10

# student_name = "김철수"
# total_score = 95
# user_age = 20

# a = [1, 2, 3]
# print(id(a))

# a = [1, 2, 3]
# b = a
# print(b)
# print(id(a))
# print(id(b))

# a[1] = 4
# print(a)
# print(b)

# a = [1, 2, 3]
# b = a[:]
# a[1] = 4
# print(a)
# print(b)

# from copy import copy
# a = [1, 2, 3]
# b = copy(a)
# print(b is a)

# a, b = ("python", "life")

a = 3
b = 5
a, b = b, a
print(a)
print(b)