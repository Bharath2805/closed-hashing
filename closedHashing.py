"create a class node"

class Node:
    def __init__(self,key,value):
     self.key = key
     self.value=value
     self.next=None

"create empty linkedlist"
class LinkedList:
     def __init__(self):
         self.head=None
         self.n=0

# length of linked list
     def __len__(self):
         return self.n



#insert at tail

     def append(self,key,value):
         new_node = Node(key,value)
         if self.head == None:
             self.head=new_node
             self.n+=1
             return

         cur = self.head
         while cur.next != None:
             cur=cur.next
             cur.next = new_node
             self.n+=1
     def delete_head(self):
        if self.head == None:
            return "empty LL"

        self.head = self.head.next
        self.n = self.n -1


     

# delete by value
     def remove(self,key):
         if self.head == None:
             return "empty"
         if self.head.key == key:
             self.delete_head()
             self.n = self.n-1
         cur = self.head
         while cur.next != None:
             if cur.next.key == key:
                 break
             cur = cur.next
             if cur.next == None:
                 return "not found"
             else:
                 cur.next = cur.next.next
                 self.n = self.n-1

#traverse
     def traverse(self):
      cur = self.head
      while cur != None:
        print(cur.key, "-->", cur.value," ",end= " ")
        cur = cur.next
# search
     def search(self,key):
         cur = self.head
         pos = 0
         while cur != None:
             if cur.key == key :
                 return pos
             cur=cur.next
             pos+=1
         return -1


      
   
# get_node_by_index

     def get_node_at_index(self,index):
      cur = self.head
      counter = 0
      while cur != None:
        if counter == index:
          return cur
        cur = cur.next
        counter += 1

class Dictionary:
  def __init__(self,capacity):
    self.capacity = capacity
    self.size = 0
# create array of linkedList
    self.buckets = self.makeArray(self.capacity)
  
  def makeArray(self,capacity):
    L =[]
    for i in range(capacity):
      L.append(LinkedList())
#create hash
  def hashFunction(self,key):
    return abs(hash(key)) % self.capacity

#put function

  def put(self,key,value):
    bucketIndex = hashFunction(key)
    nodeIndex = getNodeIndex(bucketIndex,key)
    if nodeIndex == -1 :
      self.bucket[bucketIndex].append(key,value)
    else:
      node = self.buckets[bucketIndex].get_node_at_index(nodeIndex)
      node.value = value

  def getNodeIndex(bucketIndex,key):
    nodeIndex = self.buckets[bucketIndex].search(key) 
    return nodeIndex
