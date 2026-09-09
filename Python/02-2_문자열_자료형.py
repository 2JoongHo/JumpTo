# a = "Life is too short"
# print(len(a))

# a = "Life is too short, You need Python"
# print(a[3])
# print(a[12])
# print(a[-1])

# print(a[-0])

# print(a[-2])

# b = a[0] + a[1] + a[2] + a[3]
# print(b)
# print(a[0:4])
# print(a[0:3])
# print(a[0:5])
# print(a[19:])
# print(a[:17])
# print(a[:])
# print(a)

# a = "20260830Rainy"
# year = a[:4]
# month = a[4:6]
# day = a[6:8]
# # day = a[4:8]
# # date = a[:8]
# weather = a[8:]
# print(year)
# print(month)
# print(day)
# print(weather)

# print("I eat %d apples." % 3)
# print("I eat %s apples." % "five")

# number = 3
# print("I eat %d apples" % number)

# number = 10
# day = "three"
# print("I ate %d apples. so I was sick for %s days." % (number, day))

# print("%10s" % "hi")
# print("%-10sjane" % "hi")

# print("%0.4f" % 3.42134234)

# print("%10.4f" % 3.42134234)

# print("I eat {0} apples".format(3))
# print("I eat {0} apples".format("five"))

# number = 3
# print("I eat {0} apples".format(number))

# number = 10
# day = "three"
# print("I ate {0} apples. so I was sick for {1} days.".format(number, day))

# print("I ate {number} apples. so I was sick for {day} days".format(number = 10, day = 3))

# print("I ate {0} apples. so I was sick for {day} days".format(10, day=3))

# print("{0:^10}".format("hi"))

# y = 3.42134234
# print("{0:0.4f}".format(y))
# print("{0:10.4f}".format(y))

# print("{{ and }}".format())

# name = "홍길동"
# age = 30
# print(f"나의 이름은 {name}입니다. 나이는 {age}입니다.")

# age = 30
# print("나는 내년이면 {age + 1}살이 된다.")

# d = {"name": "홍길동", "age": 30}
# print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

# print(f'{"hi":<10}')
# print(f'{"hi":>10}')
# print(f'{"hi":^10}')

# print(f'{"hi":=^10}')
# print(f'{"hi":!<10}')

# y = 3.42134234
# print(f'{y:0.4f}')
# print(f"{y:10.4f}")

# print(f"{{ and }}")

# print(f"난 {1500000:,}원이 필요해")

# a = "hobby"
# print(a.count("b"))

# a = "Python is the best choice"
# print(a.find("b"))
# print(a.find("a"))

# print(a.index("t"))

# print(",".join("abcd"))

# print(",".join(["a", "b", "c", "d"]))

# a = "HI"
# print(a.lower())

# a = " hi "
# print(a.lstrip())
# print(a.rstrip())
# print(a.strip())

# a = "Life is too short"
# print(a.replace("Life", "Your leg"))

# print(a.split())

# b = "a:b:c:d"
# print(b.split(":"))

# s = "Python"
# print(s.isalpha())

# s = "Python3"
# print(s.isalpha())

# s = "Hello World"
# print(s.isalpha())

# s = "12345"
# print(s.isdigit())

# s = "1234a"
# print(s.isdigit())

# s = "12 34"
# print(s.isdigit())

s = "Life is too short"
print(s.startswith("Life"))
print(s.startswith("L"))
print(s.endswith("too"))
print(s.endswith("t"))