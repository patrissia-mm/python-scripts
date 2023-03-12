def func(inp=2,out=3):
    return inp*out
print(func(out=2))

lst=[[x for x in range(3)]for y in range(3)]
for r in range(3):
    for c in range(3):
        if lst[r][c]%2!=0:
            print("#")


a=1
b=0
a=a^b
b=a^b
a=a^b
print(a,b)


    
