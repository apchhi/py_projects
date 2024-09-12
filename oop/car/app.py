from car import Car

CHANGE_SPEED = 5

def main():
    model = input('Enter car model: ')
    make = input('Enter car make: ')

    my_car = Car(model, make)

    for _ in range(CHANGE_SPEED):
        my_car.accelerate()
        print(f'{my_car.get_speed()} km/h')

    for _ in range(CHANGE_SPEED):
        my_car.breake()
        print(f'{my_car.get_speed()} km/h')

if __name__ == '__main__':
    main()
