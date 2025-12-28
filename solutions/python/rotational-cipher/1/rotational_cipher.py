def rotate(text, key):
    abc = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    abc_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher = "" 
    for char in text: 
        if char in abc or char in abc_2:
            if char in abc_2:
                cipher += abc_2[abc_2.index(char) + key]
            else:
                cipher += abc[abc.index(char) + key]
        else:
            cipher += char 
    return cipher
