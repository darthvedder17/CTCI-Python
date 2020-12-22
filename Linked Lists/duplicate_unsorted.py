from rich import print


class Node:
  def __init__(self,data,next):
    self.data = data
    self.next = next 



class RemoveDuplicates:
  def printList(self,head):
    temp = head 
    while temp : 
      print(temp.data,  end = ' -> ')
      temp = temp.next


  def removeDuplicate(self,head):
    temp = head
    values= {temp.data : True}
    arr = []
    # Original List


    while temp.next :
      if temp.next.data in values : 
        temp.next = temp.next.next

      else : 
        values[temp.next.data] = True
        temp = temp.next
    return self.printList(head)



if __name__ == '__main__':
  obj = RemoveDuplicates()
  
  head = Node(1,Node(3,Node(3,Node(1,Node(5,None)))))
  print('The Original Linked list is : ')
  print(obj.printList(head))
  print('Linked List without duplicates is  : ')

  obj.removeDuplicate(head)