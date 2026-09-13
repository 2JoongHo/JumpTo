# money = False
# if money:
#     print("택시를 타고 가라")
# else:
#     print("걸어 가라")

# money = True
# if money:
#     print("택시를")
#     print("타고")
#     print("가라")

# x = 3
# y = 2
# print(x > y)
# print(x < y)
# print(x != y)

# money = 3000
# if money >= 3000:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")

# money = 2000
# card = True
# if money >= 3000 or card:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")

# print(1 in [1, 2, 3])
# print(1 not in [1, 2, 3])

# print("a" in ("a", "b", "c"))
# print("P" not in "python")

# pocket = ["paper", "cellphone", "money"]
# # if 'money' in pocket:
# #     print('택시를 타고 가라')
# # else:
# #     print('걸어가라')
# if 'money' in pocket:
#     pass
# else:
#     print("카드를 꺼내라")

# pocket = ["paper", "cellphone"]
# card = True
# # if 'money' in pocket:
# #     print("택시를 타고 가라")
# # else:
# #     if card:
# #         print("택시를 타고가라")
# #     else:
# #         print("걸어가라")
# if "money" in pocket:
#     print("택시 타고가")
# elif card:
#     print("카드로 택시 타고가")
# else:
#     print("걸어가")

# grade = "B"
# if grade == "A":
#     print("탁월한 성적입니다")
# elif grade == "B":
#     print("우수한 성적입니다")
# elif grade == "C":
#     print("보통입니다")
# else:
#     print("노력이 필요합니다")

# grade = "B"
# match grade:
#     case "A":
#         print("탁월한 성적입니다")
#     case "B":
#         print("우수한 성적입니다")
#     case "C":
#         print("보통입니다")
#     case _:
#         print("노력이 필요합니다")

# grade = "B"
# match grade:
#     case "A":
#         print("A")
#     case "B":
#         print("B")
#     case "C":
#         print("C")
#     case _:
#         print("노력하세요")

# grade = "B"
# match grade:
#     case "A" | "B" | "C":
#         print("합격입니다")
#     case _:
#         print("불합격입니다")

# x = 5
# print(1 < x < 10)
# print((1 < x) and (x < 10))
# print(10 <= x <= 20)
# print((10 <= x) and (x <= 20))

# score = 85
# if score >= 60:
#     result = "합격"
# else:
#     result = "불합격"
# print(result)

# score = 85
# result = "합격" if score >= 60 else "불합격"
# print(result)

age = 19
status = "성인" if age >= 18 else "미성년"
print(status)

temperature = 25
weather = "따뜻함" if temperature > 20 else "추움"
print(weather)

money = 5000
transportation = "버스" if money >= 1000 else "도보"
print(transportation)