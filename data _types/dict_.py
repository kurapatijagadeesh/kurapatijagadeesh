#dict
data={"name":"sai","age":28,"college":"cbit","dob":"1992-07-15"}
data2={"tuple":["sai","shiva",123,4],"age":28,"college":"cbit","dob":"1992-07-15"}
print(data)
print(data2)
print(type(data))
print(dir(data))
print(data.get("dob"))
print(data["dob"])
print(data.keys())
print(data.values())
print(data.items())
data.update(data2)
print(data.setdefault("sai",25000))
print("15--",data)


data=[1,2,3,4]
print(type(data)