
n=int(input("enter the num of items"))
l={}
dup={}
dup1={}
print("enter the items in dict")
for i in range(n):
	key=input("enter the extension:")
	value=input("enter the file:")
	l[key]=value
print("dict is:",l)

def find_duplicates(l,dup,dup1):
	for key,value in l.items():
		if value not in dup.values():
			dup[key]=value
		else:
			dup1[key]=value

#print(list(dup))
	print(dup1)
	print(list(dup1.keys()))

find_duplicates(l,dup,dup1)


