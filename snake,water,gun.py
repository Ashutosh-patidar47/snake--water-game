import random
ch=input("Enter 'S' to Start the Game : ")
if(ch=='S' or ch=='s'):
        while True:
            print("-----Snake, Water, Gun Game------")
            print("Snake = 1,Water = 2,Gun = 3\n")
            py=int(input("player turn : "))
            print("Computer Turns wait...")
            com=random.randint(1,3)
            print("Computer select :",com,"\n")
            if(py==com):
                print("\n-Match draw-")
            elif(py==1 and com==2):
                print("-You win-")
            elif(py==2 and com==3):
                print("-You win-")
            elif(py==3 and com==1):
                print("-You win-")
            elif(py<1 or py>3):
                print("Invaild input try again....Computer Win-")
            else:
                print("-Computer Win-")
            c=input("you want to add more item(y/n): ")
            if (c=="n"or c=="N"):
                break
else:
    print("Thankyou for executing the prgram:")
   