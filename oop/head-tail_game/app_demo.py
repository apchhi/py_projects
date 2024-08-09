## Программа импортирует модуль и создат 3 экземпляра класса Coin

import coin_demo as coin

## главная функция
def main():
    ## создание 3 объектов на основе класса Coin
    coin1 = coin.Coin()
    coin2 = coin.Coin()
    coin3 = coin.Coin()
    
    ## показать обращенную вверх сторону 3 монет
    print('Эти стороны монет обращены верх:') 
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    
    ## подбросить монеты
    print('Подбрасываем монету...')
    coin1.toss()
    coin2.toss()
    coin3.toss()

    ## показать обращенные вверх стороны монет
    print('Теперь эти стороны монет обращены верх:') 
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())

## вызвать главную функию
if __name__ == '__main__':
    main()
