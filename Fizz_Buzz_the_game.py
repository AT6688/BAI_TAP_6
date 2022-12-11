nhap = input("nhap vao 2 so: ")

nhap_splited = nhap.split(" ")

start = int(nhap_splited[0])

end = int(nhap_splited[1])

if (start > end):
    print("so ket thuc can lon hon so bat dau!!!")
else:
    for i in range(start, end+1):
        if (i%3==0 and i%5==0):
            print("Fizz Buzz")
        elif (i%5==0):
            print("Buzz")
        elif(i%3==0):
            print("Fizz")
        else:
            print(i)