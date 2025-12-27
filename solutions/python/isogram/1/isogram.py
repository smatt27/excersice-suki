def is_isogram(string):
    text = string.lower()
    if text == "":
        return True 
    for letter in text:
        if text.count(letter) > 1 and letter not in ("- _ . : ;  "):
            return False 
    return True 
        