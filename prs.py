print("Hello world")
import random
print("***************************************************************************")
print("*                * paper * rock * scissor *                    *")
print("***************************************************************************")
print("let star the game!!.......")
point=0
ai=0
hs=0
cs=0
ma=0
while('true'):
    if(ma>5):
        print("#################")
        print("total match:",ma)
        print("human score:",hs)
        print("AI score:",cs)
        if(hs>cs):
            print("congrats you won")
        elif(cs>hs):
            print("AI won.... better luck next time")
        else:
                print("match draw")
        print("#################")
        break
    c=input("choose the opption: paper->p rock->r scissor->s stop->stop")
    if(c=="p"): 
        print("paper")
        point=10+random.randint(1,3)
        match point:
            case 11:
                ma=ma+1
                hs=hs+1
                print("human: paper","AI:rock")
                print("match:",ma,"human score:",hs,"AI score:",cs)
                print("human wins","AI lost the match")
            case 12:
                ma=ma+1
                cs=cs+1
                print("human: paper","AI:scissor")
                print("match:",ma,"human score:",hs,"AI score:",cs)
                print("human lost","AI won the match")
            case 13:
                ma=ma+1
                hs=hs+1
                cs=cs+1
                print("human: paper","AI:paper")
                print("match:",ma,"human score:",hs,"AI score:",cs)
                print("match draw")
    elif(c=="r"):
        print("rock")
        point=20+random.randint(1,3)
        match point:
            case 21:
                ma=ma+1
                hs=hs+1
                print("human: rock","AI:scossor")
                print("match:",ma,"human score:",hs,"AI score:",cs)
                print("human wins","AI lost the match")
            case 22:
                ma=ma+1
                cs=cs+1
                print("human: rock","AI:paper")
                print("match:",ma,"human score:",hs,"AI score:",cs)
                print("human lost","AI won the match")
            case 23:
                ma=ma+1
                hs=hs+1
                cs=cs+1
                print("human: rock","AI:rock")
                print("match:",ma,"human score:",hs,"AI score:",cs)
                print("match draw")
    elif(c=="s"):
        print("scissor")
        point=30+random.randint(1,3)
        match point:
            case 31:
                ma=ma+1
                hs=hs+1
                print("human: scissor","AI:paper")
                print("match:",ma,"human score:",hs,"AI score:",cs)
                print("human wins","AI lost the match")
            case 32:
                ma=ma+1
                cs=cs+1
                print("human: scissor","AI:rock")
                print("match:",ma,"human score:",hs,"AI score:",cs)
                print("human lost","AI won the match")
            case 33:
                ma=ma+1
                hs=hs+1
                cs=cs+1
                print("human: scissor","AI:scissor")
                print("match:",ma,"human score:",hs,"AI score:",cs)
                print("match draw")
    elif(c=="stop"):
        break
print("program end")
    