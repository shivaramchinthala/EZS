class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Sll:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while temp:
                if(temp.next==None):
                    print(temp.data)
                else:
                    print(temp.data,"--->",end=" ")
                temp=temp.next
    def creation(self):
        n=int(input("enter the node u want to create:"))
        data=input("enter the data to insert:")
        new_node1=Node(data)
        self.head=new_node1
        count=1
        while(n!=count):
            data=input("enter the data to insert:")
            new_node2=Node(data)
            new_node1.next=new_node2
            new_node1=new_node2
            count=count+1
    def insertatbegin(self):
        data=input("enter the data to insert at begin:")
        new_node=Node(data)
        if(self.head==None):
            self.head=new_node
        else:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
    def insertatlocation(self):
        loc=int(input("enter the location:"))
        data=input("enter the data:")
        if(loc==1):
            self.insertatbegin(data)
        else:
            new_node=Node(data)
            temp=self.head
            count=1
            while(temp!=None and loc!=count):
                ptr=temp
                temp=temp.next
                count=count+1
            if(temp==None):
                print("location is not found")
            else:
                ptr.next=new_node
                new_node.next=temp
    def deleteatbegin(self):
        temp=self.head
        print("the deleted element is:",temp.data)
        self.head=temp.next
    def deleteatlocation(self):
        loc=int(input("enter the location:"))
        temp=self.head
        count=1
        while(temp!=None and loc!=count):
            ptr=temp
            temp=temp.next
            count=count+1
        print("the deleted node is:",temp.data)
        temp=temp.next
        ptr.next=temp
    def deleteatend(self):
        temp=self.head
        if(temp==None):
            print("the list is empty")
        else:
            if(temp.next==None):
                print("deleted element is :",temp.data)
                self.head=None
            else:
                while(temp.next!=None):
                    ptr=temp
                    temp=temp.next
                print("deleted element is :",temp.data)
                ptr.next=None      
sl=Sll()
while(1):
    print("enter the option")
    m=int(input("1.create 2.insertatbegin 3.insertatlocation 4.deleteatbegin 5.deleteatlocation 6.deleteatend 7.display 8.exit:"))
    if(m==1):
        sl.creation()
    elif(m==2):
        sl.insertatbegin()
    elif(m==3):
        sl.insertatlocation()
    elif(m==4):
        sl.deleteatbegin()
    elif(m==5):
        sl.deleteatlocation()
    elif(m==6):
        sl.deleteatend()
    elif(m==7):
        sl.display()
    elif(m==8):
        exit(0)
    else:
        print("enter the correct operation")
    
    

