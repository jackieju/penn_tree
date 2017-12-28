# penn_tree
Simple tree builder for penn string like (ROOT(SBAR(...)


An alternative of nltk.tree
You can use it to parse output string of stanford sentence structure parser.

API:
1. parse from a penn string like:

```
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
tree = Tree.from_tree_string(s)
```

A tree object will be built.

2. Output string as a tree
```
print(tree.to_tree_string())
```
output:
```
how many not ar invoices have not been partially paid
```

3. Output stentence content
```
print(tree.content_string())
```
output:
```
ROOT->
  SBAR->
    WHADJP->
      WRB=how
      JJ=many
    S->
      NP->
        RB=not
        NN=ar
        NNS=invoices

      VP->
        VBP=have
        RB=not
        VP->
          VBN=been
          VP->
            ADVP->
              RB=partially

            VBN=paid
```

Sample:
===
```    
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
```

output:
```
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
                                                                
                                                                

how many not ar invoices have not been partially paid
ROOT->
  SBAR->
    WHADJP->
      WRB=how
      JJ=many

    S->
      NP->
        RB=not
        NN=ar
        NNS=invoices

      VP->
        VBP=have
        RB=not
        VP->
          VBN=been
          VP->
            ADVP->
              RB=partially

            VBN=paid
```
