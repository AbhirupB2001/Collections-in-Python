thisislist=["Apple","Orange","Cherry"]
thisistuple=("Apple","Orange","Cherry")
thisisset={"Apple","Orange","Cherry"}
print(thisislist)
print(thisistuple)
print(thisisset)
for p in thisislist:
    print(p)
thisisset.add("Mango")
print(thisisset)
thisislist.append("Mango")
print(thisislist)
thisislist.remove("Mango")
print(thisislist)
thisisset.remove("Mango")
print(thisisset)
if "Apple" in thisislist:
    print("Yes")
thisislist[1]="Blackcurrent"
print(thisislist)
thisislist.insert(3,"Grapes")
print(thisislist)
thisisset.pop()
print(thisisset)
thisisset.clear()
print(thisisset)
del thisislist[2]
print(thisislist)
x=thisislist.count("Apple")
print(x)
y=15,thisislist.copy()
print(y)
thisislist.extend(thisisset)
print(thisislist)
thisislist.sort()
print(thisislist)


    

