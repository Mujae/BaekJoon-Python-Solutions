import sys

def rot13(text):
    result = []
    for char in text:
        if 'A' <= char <= 'Z':  
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        elif 'a' <= char <= 'z': 
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        else:  
            result.append(char)
    return "".join(result)

input_text = sys.stdin.readline().rstrip()
print(rot13(input_text))
