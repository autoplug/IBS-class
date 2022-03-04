#print odd number
# for num in range(100,150):
#     if num%2 != 0:
#         print(num)

req = 17
big = 2
small = 5
success = False
for x in range(1,big+1):
    for y in range(1,small+1):
        if x * small + y == req :
            print(x,y)
            success = True

if success == False : 
    print(-1,-1)