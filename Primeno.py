low = int(input("Enter the lowest range: "))
high = int(input("Enter the highest range: "))

for num in range(low,high+1):
    if num>1:
        for i in range(2,num):
            if(i%num==0):
                break
        else:
            print(num)