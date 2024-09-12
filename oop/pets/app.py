import pets

def main():
    name = input("Enter the animal's name: ")
    animal_type = input("Enter the animal's type: ")
    age = input("Enter the animal's age: ")

    pet = pets.Pet(name, animal_type, age)

    print(f"Animal's name - {pet.get_age()}, type - {pet.get_animal_type()}, age - {pet.get_age()} years old.")


if __name__ == '__main__':
    main()
