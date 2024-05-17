# class ListNode:
#     def __init__(self, k =-1, vl =-1, next =None):
#         self.k=k
#         self.vl=vl
#         self.next=next

# class MyHashMap:

#     def __init__(self):
#         self.list = [ ListNode() for i in range(1000)]
        
#     def hash(self,k):
#         return k%len(self.list)

#     def put(self, k: int, vl: int) -> None:
#         # if value != self.new_dict[key]:
#         #     return self.new_dict[key].add(value)
#         c=self.list[self.hash(k)]
#         while c.next:
#             if c.next.k == k:
#                 c.next.vl = vl
#                 return
#             c=c.next
#         c.next = ListNode(k,vl)  

#     def get(self, k: int) -> int:
#         c=self.list[self.hash(k)]
#         while c:
#             if c.k ==k:
#                 return c.vl
#             c = c.next
#         return -1

        

#     def remove(self, k: int) -> None:
#         c=self.list[self.hash(k)]
#         while c and c.next:
#             if c.next.k == k:
#                 c.next = c.next.next
#                 return 


# # Your MyHashMap object will be instantiated and called as such:
# # obj = MyHashMap()
# # obj.put(key,value)
# # param_2 = obj.get(key)
# # obj.remove(key)

#######
# class ListNode:
#     def __init__(self, key=-1, val=-1, next=None):
#         self.key = key
#         self.val = val
#         self.next = next

# class MyHashMap:
#     def __init__(self):
#         self.map = [ListNode() for i in range(1000)]
        
#     def hashcode(self, key):
#         return key % len(self.map)

#     def put(self, key: int, value: int) -> None:
#         cur = self.map[self.hashcode(key)]
#         while cur.next:
#             if cur.next.key == key:
#                 cur.next.val = value
#                 return
#             cur = cur.next
#         cur.next = ListNode(key, value)
         
#     def get(self, key: int) -> int:
#         cur = self.map[self.hashcode(key)].next
#         while cur and cur.key != key:
#             cur = cur.next
#         if cur:
#             return cur.val
#         return -1

#     def remove(self, key: int) -> None:
#         cur = self.map[self.hashcode(key)]
#         while cur.next and cur.next.key != key:
#             cur = cur.next
#         if cur and cur.next:
#             cur.next = cur.next.next




class MyHashMap:

    def __init__(self):
        self.size = 10**6+1
        self.hash_map = [-1 for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        self.hash_map[key] = value

    def get(self, key: int) -> int:
        return self.hash_map[key]
        
    def remove(self, key: int) -> None:
        self.hash_map[key] = -1