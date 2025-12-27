def is_valid(isbn):
    bn_clean = list(isbn.replace("-", ""))
    if len(bn_clean) != 10:
        return False
    if bn_clean[-1] == "X":
        bn_clean[-1] = "10"  
    for num in bn_clean:
        if not num.isdigit():
            return False 
    t = 0 
    count = 9 
    for num in bn_clean:
        t += int(num) * (10 - count)
        count -= 1 
    return t % 11 == 0 

    