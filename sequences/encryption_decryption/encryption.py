## encryption of files
import json
def main():
    codes = {'a': '!', 'b': '@', 'c': '#', 'd': '$', 'e': '%', 'f': '^', 'g': '&', 'h': '*', 'i': '(', 'j': ')', 'k': '_', 'l': '+', 'm': '-', 'n': '=', 'o': '{', 'p': '}', 'q': '[', 'r': ']', 's': ':', 't': ';', 'u': '"', 'v': "'", 'w': '<', 'x': '>', 'y': '`', 'z': '~', '0': '2', '1': '3', '2': '4', '3': '5', '4': '6', '5': '7', '6': '8', '7': '9', '8': '0', '9': '1',}
    with open('base_text.txt', 'r') as f:
        text = f.read()
    with open('encrypt_file.json', 'w') as f:
        for char in text:
            char = str(char)
            if char.isalpha():
                char = char.lower()
            if char in codes:
                json.dump(codes[char], f)
            else:
                json.dump(char, f)
    print('Successfully.')
if __name__ in '__main__':
    main()
