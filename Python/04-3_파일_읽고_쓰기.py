# f = open("새파일.txt", "w")
# f.close()

# f = open("새파일.txt", "w")
# for i in range(1, 11):
#     data = f"{i}row.\n"
#     f.write(data)
# f.close()

# f = open("새파일.txt", "w")
# for i in range(1, 11):
#     data = f"{i}번째 줄입니다.\n"
#     f.write(data)
# f.close()

# f = open("새파일.txt", "r")
# line = f.readline()
# print(line)
# f.close()

# f = open("새파일.txt", "r")
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

# f = open("새파일.txt", "r")
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()

# f = open("새파일.txt", "r")
# lines = f.readlines()
# for line in lines:
#     line = line.strip()
#     print(line)
# f.close()

# f = open("새파일.txt", "r")
# data = f.read()
# print(data)
# f.close()

# f = open("새파일.txt", "r")
# for line in f:
#     print(line)
# f.close()

# f = open("새파일.txt", "a")
# for i in range(11, 21):
#     data = f"{i}번째 줄입니다.\n"
#     f.write(data)
# f.close()

# f = open("foo.txt", "w")
# f.write("Life is too short, you need python")
# f.close()

# with open("foo.txt", "w") as f:
#     f.write("Life is too short, tou need python")

with open("test.txt", "w") as f:
    content = "Hello, Python!"
    f.write(content)
print(content)