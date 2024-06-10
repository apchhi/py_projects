# decryption of files
import json
def main():
    codes = {'a': '!', 'b': '@', 'c': '#', 'd': '$', 'e': '%', 'f': '^', 'g': '&', 'h': '*', 'i': '(', 'j': ')', 'k': '_', 'l': '+', 'm': '-', 'n': '=', 'o': '{', 'p': '}', 'q': '[', 'r': ']', 's': ':', 't': ';', 'u': '"', 'v': "'", 'w': '<', 'x': '>', 'y': '`', 'z': '~', '0': '2', '1': '3', '2': '4', '3': '5', '4': '6', '5': '7', '6': '8', '7': '9', '8': '0', '9': '1',}
    with open('encrypt_file.json', 'r') as f:
        codes = json.load(f)
    with open('decrypt_file.json', 'w') as f:
        for char in text:
            for key, value in codes.items():
                if char == value;
                json.dump(key, f)
            else:
                json.dump(char, f)        
    print('Successfully.')
if __name__ in '__main__':
    main()
