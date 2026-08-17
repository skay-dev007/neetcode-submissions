class ListNode:
    def __init__(self,key,val):
        self.val = val
        self.key = key 
        self.next = None
        self.prev = None  


class LRUCache:
    # hash map and dll 
    # hash map will store key and node address 
    # node will store key and value 
    # if the key does not exist do nothing 
    # if it already exists, and we do put then first delete the key then put 
    # if it is already at capcity then remove from the end 
    # while getting get and move it to the start
    # while getting if it does not exist then return -1 

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.capacity = capacity 

        self.head = ListNode(-1,-1)
        self.tail = ListNode(-2,-1)
        self.head.next = self.tail 
        self.tail.prev = self.head 

     
    

    def get(self, key: int) -> int:
        
        # can get it only if it exists 
        res = -1 
        if key in self.hashmap:
            #NOOO! the node also from the hashmap 
            node = self.hashmap[key] 

            node.prev.next = node.next 
            node.next.prev = node.prev 

            # add the node to the start 

            curr = self.head.next 
            self.head.next = node 
            node.next= curr 
            curr.prev = node 
            node.prev = self.head 

            res = node.val

        return res 
        
    def put(self, key: int, value: int) -> None:

        # edge case: if it already exists then remove it also from the hashmap 
        if key in self.hashmap:
            node = self.hashmap.pop(key)

            node.prev.next = node.next 
            node.next.prev = node.prev 

        if len(self.hashmap) == self.capacity:
            #remove the last node 
            lastnode = self.tail.prev 
            lastkey = lastnode.key
            self.tail.prev = lastnode.prev 
            lastnode.prev.next = self.tail 

            self.hashmap.pop(lastkey)

        newnode = ListNode(key,value)
        self.hashmap[key] = newnode 

        #add at the start 
        currhead = self.head.next 
        self.head.next = newnode 
        newnode.prev = self.head 
        currhead.prev = newnode 
        newnode.next = currhead
    
        # if capactiy greater than capcity delete from the end

        
