## vowels and consonants

def main():
    list_vowels = ['a','e','i','o','u']
    list_consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

    string = input('Enter your text: ').lower()
    vowels, consonants = counter(string, list_vowels, list_consonants)
    print(f'Vowels count: {vowels}')
    print(f'Consonants count: {consonants}')


def counter(string, list_vowels, list_consonants):
    counter_vowels = 0
    counter_consonants = 0
    for ch in string:
        if ch in list_vowels:
            counter_vowels += 1
        if ch in list_consonants:
            counter_consonants += 1
    return counter_vowels, counter_consonants

def consonants(string, list_consonants):
    pass




main()
