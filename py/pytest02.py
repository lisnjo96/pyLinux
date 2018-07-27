achieve=True
sum=0

while achieve:
    al_col=['green','yellow','red']
    inserted=input("Please enter your color(green,yellow,red): ")
    color=inserted.lower()

    if color in al_col:
        if color==al_col[0]:
            sum+=5
            print("5 point scored!")
        elif color==al_col[1]:
            sum+=10
            print("10 point scored!")
        else:
            sum+=15
            print("15 point scored")
    else:
         print("invalid input!")

    print("current score: "+str(sum))

    if sum>100:
        achieve=False
    else:
        achieve=True

print("you achieved the score!")
