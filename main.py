import random     #In_built Module to produce random numbers
import artwork

def gamewin(comp,you):                     #is a function that i created
    if comp == you:
        return None


    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True

    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False

    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True


    
print(artwork.art)

print("Computer's Turn: Rock[r],Paper[p],Scissor[s]")#choosing something from this 3
randno =random.randint(1,3)

if randno==1:
    comp='r'

elif randno==2:
    comp='p'

elif randno==3:
    comp='s'



you = input('Rock[r],Paper[p],Scissor[s] what do you choose?\n=')


a=gamewin(comp,you)

print(f"Computer Choose {comp}")    #tells what computer choose
print(f"You Choose {you}")    #tells what u choose
print('Hence')    

if a == None:        #predits and evaluates and checks what result was and according ot result gives feedback using given string
    print("This Game is a Tie!!! Nerd")   

elif a == True:
    print("Yeee Boi You won this Game!!! ggs")

elif a == False:
    print("You lost nerd!! Try again later")

else:
    print("invalid info check for error")
