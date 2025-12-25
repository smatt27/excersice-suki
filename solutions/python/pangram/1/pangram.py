def is_pangram(sentence):
    abc = "abcdefghijklmnopqrstuvwxyz" 
    text = sentence.lower()
    new_text = ""
    for letter in text:
        if letter in abc:
            new_text += letter 
    return len(set(new_text)) == 26 
