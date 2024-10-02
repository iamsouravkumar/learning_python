dic = {
    "Sourav": "Human Being", 
    "Laptop": "Electronic Machine"
    }
print(dic["Sourav"])

dic= {
    786: "Sourav",
    55: "Gourav",
    66: "Lucky",
    74: "Lakshita"
}

print(dic[786])

info = {
    "Name": "Sourav",
    "Age": 19,
    "Eligible": True
}

print(info)
print(info["Name"]) # throws error if key is not present
print(info.get("Name2")) # to print the value even if key is not present, but returns None when key is not present
print(info.keys()) # to print all the keys
print(info.values()) # to print all the values

for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items()) # to print all the key-value pairs

for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")