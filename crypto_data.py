import requests
from dataclasses import dataclass
from typing import Final, List

BaseUrl: Final[str] = 'https://api.coingecko.com/api/v3/coins/markets'

@dataclass
class Coin:
    name: str
    symbol: str
    current_price: float
    high_24h: float
    low_24h: float
    priceChange_24h: float
    priceChange_percent_24h: float

    def __str__(self):
        return f'{self.name}({self.symbol}): ${self.current_price:,}'

def getCoins() -> list[Coin]:
    payload: dict = {'vs_currency': 'usd', 'order': 'market_cap_desc'} # payload for api query
    response = requests.get('https://api.coingecko.com/api/v3/coins/markets', params=payload)
    json_data = response.json()

    coin_list: list[Coin] = []
    for item in json_data:
        current_coin = Coin(
            name=item.get('name'),
            symbol=item.get('symbol'),
            current_price=item.get('current_price'),
            high_24h=item.get('high_24h'),
            low_24h=item.get('low_24h'),
            priceChange_24h=item.get('price_change_24h'),
            priceChange_percent_24h=item.get('price_change_percentage_24h')
        )
        coin_list.append(current_coin)

    return coin_list


if __name__ == '__main__':
    coins = getCoins()

    for coin in coins:
        print(coin)