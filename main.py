from crypto_data import getCoins, Coin
import time

def alert(symbol: str, bottom: float, top: float, coins_list: list[Coin]):
    for coin in coins_list:
        if coin.symbol.lower() == symbol.lower():  # Case-insensitive comparison
            if coin.current_price > top or coin.current_price < bottom:
                print(coin, "!!TRIGGERED!!")
            else:
                print(coin)

if __name__ == '__main__':
    coins: list[Coin] = getCoins()
    
    alert('btc', bottom=70_000, top=100_000, coins_list=coins)
    alert('eth', bottom=2000, top=3300, coins_list=coins)
    alert('xrp', bottom=2, top=3, coins_list=coins)
    
    #while True:
        # time.sleep(30) // for automatic refresh