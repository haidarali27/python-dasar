# belajar dictionary di python

user = {
    "name" : "haidar ali",
    "age" : 30,
    "is_admin" : True
}

name = user["name"]
user["username"] = "haidar_ali"
user["name"] = "haidar ali akbar"

temp = user.get("name")

print("")
print(temp)