
def stc_push(i):
    print("enter the element to insert:")
    e=input()
    i=i+1
    stc.append(e)
    print(stc)
def stc_pop(i):
    if not stc:
        print("stack is empty")
    else:
        print("the deleted element is:",stc[i])
        i=i-1
        stc.pop()
        if not stc:
            print("stack is empty")
        else:
            print(stc)
    
stc=[]
i=-1
while(1):
    print("select your operation 1.push 2.pop 3.exit")
    choice=int(input())
    if(choice==1):
        stc_push(i)
    elif(choice==2):
        stc_pop(i)
    elif(choice==3):
        exit(0)
    else:
        print("enter the correct choice")