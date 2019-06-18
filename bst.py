class Binary_Tree:
    def __init__(self, val):
        self.value = val
        self.mag = 1
        self.right = None
        self.left = None
        
    # insert for binary search tree
    
    def insert(self, val):
        curr = self.value                
        if val < curr:
            if not self.left:
                self.left = Binary_Tree(val)
                print(self.left.value)
            else:
                self.left.insert(val)
        else:
            if not self.right:
                self.right = Binary_Tree(val)
                print(self.right.value)
            else:
                self.right.insert(val)

    #find value
    def find_val(self, val):   
        curr = self.value   
        if curr == val:
            print('found it',val, True)
            
        else:
            if val < curr and self.left:
                 self.left.find_val(val)
                
            elif val >= curr and self.right:
                 self.right.find_val(val)
                
            else:
                print('cannotfind val', False, val)
                
    # find largest node val that is smaller than key inserted
    def largest_smaller_key(key):
        if not self.right and not self.left:
            return self.value
        


tree = Binary_Tree(20)



tree.insert(2)
tree.insert(1)
tree.insert(4)
tree.insert(5)
tree.insert(100)
tree.find_val(20)
tree.find_val(2)
tree.find_val(5)
tree.find_val(100)
tree.find_val(12)