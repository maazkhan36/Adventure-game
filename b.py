name=input("enter your name"  )
print("welcome",name, "to this game")
enter=input("press enter to continue")

answer=input("you are on dirt road, it has come to an en and you can go left or right,on which way you will go?" ).lower()
if answer =="left":
    answer=input("you come to river , you can walk around or swim across? will you walk or swim" ).lower()
    
    if answer=="swim":
      print("you swum and eaten by alligator")
    elif answer=="walk":    
       print("you walked many miles , ranout of water and lost game")
    else:
       print("not a valid option . you lose")
        
elif answer=="right":
    answer=input("you come to bridge , it looks wobbly , do you want to cross it or head back(cross/back)").lower()
    if answer=="back":
      print("you go back and lose")
    
    elif answer=="cross":    
       answer=input("you crossed bridge and meet with stranger , do you want to talk(yes/no)?")
       
       if answer=="yes":
           print("you talk to the stranger and he set right path to you . You win")
       elif answer=="no":
           print("you ignore the stranger and didnt know about right path . you lose")
       else:
                 print("not a valid option . you lose")
  
    else:
       print("not a valid option . you lose")
       
       
         
else:
    print("not a valid option . you lose")
print("thank you trying this adventure", name)