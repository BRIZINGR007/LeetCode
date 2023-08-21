class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.next = next
        self.data = data
        self.prev = prev
    
class d_Linked_List:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,data):
        node = Node(data,self.head,None)
        self.head=node
    def insert_at_end(self,data):
        if self.head is None:
            node = Node(data,self.head,None)
            self.head =node
            return
        itr =self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None,itr)
    
    def remove_at_index(self,index):
        if index==1:
            self.head = self.head.next
            self.head.prev = None
            return
        count=0
        itr = self.head
        while itr:
            if count == index-2:
                if itr.next.next:
                    itr.next = itr.next.next
                    itr.next.next.prev = itr
                else:
                    itr.next=None
        
    def insert_at_index(self,index,data):
        if index == 1:
            node = Node(data,self.head,None)#data,next,prev
            self.head = node
            return
        itr = self.head
        count = 0
        while itr:
            if count==index-2:
                node = Node(data,itr.next,itr)
                if itr.next:
                    node.next.prev = node
                itr.next = node
                break
            count+=1
            itr = itr.next
    def reverse_double_ll(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.prev = current.next
            current.next=prev
            prev = current
            current = next
        self.head = prev


    def print(self):
        if self.head is None:
            print("Empty double Linked List")
        itr = self.head
        dllstr="None-->"
        while itr:
            dllstr+=str(itr.data)+'-->'
            itr=itr.next
        dllstr+="None"
        return dllstr
    def insert_value(self,data_list):
        for data in data_list:
            self.insert_at_end(data)

if __name__=='__main__':
    obj = d_Linked_List()
    obj.insert_value([1,2,3,4,5])
    print("Double Linked List:",obj.print())
    obj.insert_at_index(5,23)
    print("After Insertion , Double Linked List:",obj.print())
    obj.reverse_double_ll()
    print("After the reversing of the LinkedList:",obj.print())