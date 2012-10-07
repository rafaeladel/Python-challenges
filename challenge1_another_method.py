import string

if __name__ == "__main__":
    target = raw_input("Enter target to solve :")
    old_str = string.ascii_lowercase
    new_str = string.ascii_lowercase[2:] + string.ascii_lowercase[:2]
    
    trans = string.maketrans(old_str, new_str)
    print target.translate(trans)
