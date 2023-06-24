class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class Sll:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            print("printing forward")
            while temp.next!=self.head:
                print(temp.data,"--->",end=" ")
                temp=temp.next
            if(temp.next==self.head):
                print(temp.data)
            print("reverse order")
            while temp.next!=self.head:
                temp=temp.next
            while temp!=self.head:
                print(temp.data,"--->",end=" ")
                temp=temp.prev
            print(temp.data)
            
            
    
    def creation(self):
        if(self.head!=None):
            print("list is already created")
        else:
            n=int(input("enter the node u want to create:"))
            data=input("enter the data to insert at begin:")
            new_node1=Node(data)
            self.head=new_node1
            new_node1.next=new_node1
            count=1
            while(n!=count):
                data=input("enter the data to insert at begin:")
                new_node2=Node(data)
                new_node1.next=new_node2
                new_node2.prev=new_node1
                new_node1=new_node2
                self.tail=new_node1
                count=count+1
            new_node1.next=self.head
    def insertatbegin(self):
        data=input("enter the data to insert at begin:")
        new_node=Node(data)
        temp=self.head
        temp1=self.head
        if(self.head==None):
            self.head=new_node
            new_node.next=node_next
        else:
            new_node=Node(data)
            new_node.next=temp
            temp1.prev=new_node
            while temp.next!=temp1:
                temp=temp.next
            new_node.prev=temp
            temp.next=new_node
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
                new_node.prev=ptr
                new_node.next=temp
                temp.prev=new_node
    def insertatend(self):
        data=input("enter the data to insert at begin:")
        new_node=Node(data)
        if(self.head==None):
            self.head=new_node
            new_node.next=node_next
        else:
            temp=self.head
            while(temp.next!=self.head):
                    ptr=temp
                    temp=temp.next
            temp.next=new_node
            new_node.prev=temp
            new_node.next=self.head
    def deleteatbegin(self):
        if(self.head==None):
            print("list is empty")
        else:
            temp=self.head
            ptr=temp.next
            print("the deleted element is:",temp.data)
            while temp.next!=self.head:
                temp=temp.next
            temp.next=ptr
            ptr.prev=temp
            self.head=ptr
    def deleteatlocation(self):
        loc=int(input("enter the location:"))
        if(loc==1):
            deleteatbegin()
        else:
            temp=self.head
            count=1
            while(temp!=None and loc!=count):
                ptr=temp
                temp=temp.next
                count=count+1
            if(temp.next==None):
                deleteatend()
            elif(temp==None):
                print("location not found")
            else:
                print("the deleted node is:",temp.data)
                temp=temp.next
                temp.prev=ptr
                ptr.next=temp
    def deleteatend(self):
        if(self.head==None):
            print("the list is empty")
        else:
            temp=self.head
            while(temp.next!=self.head):
                temp5=temp
                temp=temp.next
            print("deleted element is :",temp.data)
            temp5.next=self.head
            temp.prev=temp5
        
    def detect_loop(self):
        if(self.head==None):
            print("list is empty")
        elif(self.head==self.tail.next):
            print("loop exists")
        else:
            print("no loop exists")
        
sl=Sll()
while(1):
    print("enter the option")
    m=int(input("1.create 2.insertatbegin 3.insertatlocation 4.insertatend 5.deleteatbegin 6.deleteatlocation 7.deleteatend 8.display 9.exit:"))
    if(m==1):
        sl.creation()
    elif(m==2):
        sl.insertatbegin()
    elif(m==3):
        sl.insertatlocation()
    elif(m==4):
        sl.insertatend()
    elif(m==5):
        sl.deleteatbegin()
    elif(m==6):
        sl.deleteatlocation()
    elif(m==7):
        sl.deleteatend()
    elif(m==8):
        sl.detect_loop()
        sl.display()
    elif(m==9):
        exit(0)
    else:
        print("enter the correct operation")
    
    


