class Tree:
    
    def __init__(self, str=None):
        self._label = str
        self._children = []
        self._value = None
        self._parent = None
        
    def setParent(self, np):
        self._parent = np
        
    def parent(self):
        return self._parent
        
    def isLeaf(self):
        return self._value != None
    
    def set_value(self, str):
        self._value = str
        
    def add(self, node):
        self._children.append(node)
        node.setParent(self)
        
    def children(self):
        return self._children
        
    def label(self):
        return self._label
    
    def value(self):
        return self._value
        
    def to_tree_string(self, deep=0):
        r = ""
        if self.isLeaf():
            return self.label()+"="+self.value()
        
        r += self.label()+"->\n"
        deep +=1
        
        for c in self.children():
            i = 0
            while i < deep:
                r += "  "
                i += 1
                
            r += c.to_tree_string(deep)+"\n"
        
        return r
        
    def content_string(self):
        r = ""
        if self.isLeaf():
            return self.value()
        
        
        for c in self.children():
            if r != "":
                r += " "
            r += c.content_string()
        
        return r    
     
     

           
    @classmethod
    def getword(cls, str, i):
        r = ""
        while i < len(str):
            c = str[i]
            i += 1
            if c != " " and c != "\n" and c != "(" and c != ")":
                r += c
            else:
                break
            
            
        return [r,i]
        
    @classmethod       
    def from_tree_string(cls, output_):
        r = None
        p = r
        w = ""
        current_node = r
        new_tree = None
        current_label = None
        
        i = 0
        while i < len(output_):
            
            c = output_[i]
            if c == '\n' or c == ' ':
                i += 1
                continue
                
            if c == '(':
                
                w,i  = cls.getword(output_, i+1)
                new_tree = Tree(w)
                if current_node == None:
                    r = current_node = new_tree
                else:
                     current_node.add(new_tree)
                     current_node = new_tree
                w = ""
                continue
            
            if c == ')':
                if w != "":
                    current_node.set_value(w)
                    w = ""
                current_node = current_node.parent()
                #if (current_node != None):
                #   print("current_node3:"+repr(current_node.label()))

                i+=1
            else:
                w += c
                i+=1

        
        return r    
             
if __name__ == '__main__':
    
    s = """
(ROOT
  (SBAR
      (WHADJP (WRB how) (JJ many))
          (S
                (NP (RB not) (NN ar) (NNS invoices))
                      (VP (VBP have) (RB not)
                              (VP (VBN been)
                                        (VP
                                                    (ADVP (RB partially))
                                                                (VBN paid)))))))
                                                                
                                                                
"""
    print(s)
    tree = Tree.from_tree_string(s)
    print(tree.content_string())
    print(tree.to_tree_string())