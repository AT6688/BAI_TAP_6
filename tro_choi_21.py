import random 

sum = 0

while(sum<=21):
    #lua chon nguoi choi dau tien
    if (sum == 0):
        r = random.randint(0,1)
        if (r == 0):
            current_player = "human"
        else:
            current_player = "computer"
            
    if(current_player == "computer"):
        value = random.randint(1,3)
        print("may tinh chon: ",value)
        current_player = "human"
    else:
        value = int(input("nguoi choi nhao vao so: "))
        while(value < 1 and value > 3): #yeu cau nhap lai neu ko dung 1-3
            print("so ban vua nhap khong nam trong 1,2,3")
            value = int(input("nhap lai so muon chon: "))
        current_player = "computer"
    
    sum += value
    print("tong hien tai la: ",sum)
print("tro choi ket thuc")
                      
if(current_player == "computer"):
    winner = "computer"
else:
    winner = "human"
                        
print("nguoi thang cuoc la: ",winner)
