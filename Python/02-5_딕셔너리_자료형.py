# dic = {"name": "pey", "phone": "010-1234-5678", "birth": "1118"}
# print(dic)

# a = {1: "hi"}
# print(a)

# a = {"a": [1, 2, 3]}
# print(a)

# a = {1: "a"}
# a[2] = "b"
# print(a)

# a["name"] = "pey"
# print(a)

# a[3] = [1, 2, 3]
# print(a)

# del a[1]
# print(a)

# del a["name"]
# print(a)

# grade = {"pey": 10, "julliet": 99}
# print(grade["pey"])
# print(grade["julliet"])

# a = {1: "a", 2: "b"}
# print(a[1])
# print(a[2])

# a = {"a": 1, "b": 2}
# print(a["a"])
# print(a["b"])

# dic = {"name": "pey", "phone": "010-1234-5678", "birth": "1111"}
# print(dic["name"])
# print(dic["phone"])
# print(dic["birth"])

# a = {1: "a", 1: "b"}
# print(a)

# a = {[1, 2]: "hi"}
# print(a)

a = {"name": "pey", "phone": "010-1234-5678", "birth": "1111"}
# print(a.keys())
# print(a.values())

# for k in a.keys():
#     print(k)

# print(list(a.keys()))

# print(a.items())

# a.clear()
# print(a)

# print(a.get("name"))
# print(a.get("phone"))
# print(a.get("birth"))

# print(a.get("nokey"))
# print(a.get("sure"))
# print(a.get("name"))
# print(a["name"])

# print(a.get("nokey", "정보 없음"))
# print(a.get("name", "정보 없음"))

# print("name" in a)
# print("email" in a)

email = a.pop("email", "정보 없음")
print(email)
print(a)