from collections import deque
import string

if __name__ == "__main__":
    old_list = list(string.ascii_lowercase)    
    new_list = deque(old_list)
    new_list.append(new_list.popleft())
    new_list.append(new_list.popleft())

    target = raw_input("Enter target to solve :")
    
    old_list = "".join(old_list)
    new_list = "".join(new_list)

    trans = string.maketrans(old_list, new_list)
    print target.translate(trans)

##    destination = ""
##    for i in target:
##        if i in old_list:
##            index = old_list.index(i)
##            destination += new_list[index]
##        else:
##            destination += i
##    print destination
        
    
    
