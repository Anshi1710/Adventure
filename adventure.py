a = input("What you like to play? (yes/no)")
if a.lower().strip() == "yes":
     a=input("You reach a crossroads, wouald u like to left or right?").lower().strip()
     if a=='left':
         a=input("U encounter a monster, would u like to run or attack.")

         if a=="attack":
             print("lost")
        else:
            print("good choose, safe")
    elif a=="right":
        print("fall on a patch")
    else:
        print("invalid choice")
else:
    print("That's to bad")
            
