# linked list that does have a circle 

def is_circle(lst):
    flag = False
    for node in lst:
        node.flag = True 
        if node.next.flag == True:
            return True 
        else:
            return False

