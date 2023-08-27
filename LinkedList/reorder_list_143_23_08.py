class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        itr = self.head
        while itr.next:
            itr=itr.next
        itr.next = Node(data,None)
    
    def print(self):
        if self.head is None:
            print("Linked List is empty.")
            return
        itr=self.head
        llstr =""
        while itr:
            llstr+=str(itr.data)+'-->'
            itr=itr.next
        llstr+="None"
        print(llstr)
    def get_ll(self):
        return self.head

    def insert_value(self,data_list):
        for data in data_list:
            self.insert_at_end(data)
    def reorder_list(self):
        slow = self.head
        fast = self.head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next
        second = prev
        head = self.head
        while head and second:
            tmp1,tmp2 = head.next,second.next
            head.next = second
            second.next = tmp1
            head = tmp1
            second = tmp2
        

        


        
    
if __name__=='__main__':
    obj = LinkedList()
    list1 = [1,2,3,4]
    obj.insert_value(list1)
    obj.print()
    obj.reorder_list()
    obj.print()
    print("Helllo")