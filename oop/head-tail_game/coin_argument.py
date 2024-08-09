## Эта программа передает объект Coin
## в качестве аргумента в функцию

import coin

def main():
    ## Создать объект
    my_coin = coin.Coin()
    
    ## Эта инструкция покажет "Орёл"
    print(coin.get_sideup())

    ## Передать объект в функцию
    flip(my_coin)

    ## Эта инструкция покажет "Орёл" 
    ## или "Решка"
    print(coin.get_sideup())

## Ф-ция подбрасывает монетку
def flip(coin_obj):
    coin_obj.toss()

if __name__ == '__main__':
    main()
