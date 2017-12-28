java_course={"john","jack","jill","joe"}
python_course={"jake","john","eric","jill"}
l=[]
s=[]
print(len(java_course))
for i in java_course:
    print(i)
for i in java_course:
    if i not in python_course:
        l.append(i)
        print(i)
for i in python_course:
    if i not in java_course:
        s.append(i)
        print(i)
print(java_course & python_course)
print(len(java_course & python_course))
print(java_course | python_course)
print(len(java_course | python_course))
print(l+s)
