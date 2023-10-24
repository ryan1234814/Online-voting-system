c1= input("please enter the name of 1st candidate")
c2 =input ("please enter the name of 2nd candidate")
c1vote=0
c2vote=0
vid=[1,2,3,4,5,6]

n= len(vid)
print("number of voters in the elections=", n)
votedlist=[]
while True:
    if vid==[]:
        print("voting process has concluded /nThank You")
        if c1vote>c2vote:
            print (f"{c1}is declared as winner with{c1vote} votes ")
                   
        elif c2vote>c1vote:
            print (f"{c2}is declared as winner with {c2vote} votes ")
            
        elif c1vote==c2vote:
            print ("Both candidates have equal number of votes. The result is a tie.")
            break
    else:
            
        voterchoice=int(input("please enter your voter id number"))
        if voterchoice in votedlist:
            print("you have already voted")
        else:
            if voterchoice in vid:
                print(f"1.{c1}\n2{c2}"  )   
                option= int(input("enter your option"))
                if option ==1 :
                    c1vote+=1
                    print(f"you voted for {c1}")
                elif option==2:
                    c2vote+=1  
                    print(f"you voted for {c2}")
                vid.remove(voterchoice)
                votedlist.append(voterchoice)    
            else:
                print("sorry! you are not allowed to vote")
                
        
