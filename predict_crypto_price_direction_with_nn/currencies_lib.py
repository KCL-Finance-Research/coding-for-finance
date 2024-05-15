from types import MappingProxyType as ImmutableDict

_DEFAULT_CURRENCIES = ImmutableDict({
    "BTC": "Bitcoin",
    "ETH": "Ethereum",
    "BNB": "Binance Coin",
    "SOL": "Solana",
    "XRP": "Ripple",
    "ADA": "Cardano",
    "AVAX": "Avalanche",
    "DOGE": "Dogecoin",
    "TRX": "TRON",
    "LINK": "Chainlink",
    "DOT": "Polkadot",
    "MATIC": "Polygon",
    "ICP": "Internet Computer",
    "SHIB": "Shiba Inu",
    "BCH": "Bitcoin Cash",
    "LTC": "Litecoin",
    "ATOM": "Cosmos",
    "ETC": "Ethereum Classic"
})

_DEFAULT_FILE_PATH = "output/currencies.csv"


def store_to_file(currencies: dict = _DEFAULT_CURRENCIES, path: str = _DEFAULT_FILE_PATH):
    import pandas as pd
    import os.path

    parent_directory = os.path.dirname(path)
    if parent_directory and not os.path.exists(parent_directory):
        os.makedirs(parent_directory)

    data_frame = pd.DataFrame({key: [value] for key, value in currencies.items()})
    data_frame.to_csv(path, index=False)
    return data_frame


def read_from_file(path: str = _DEFAULT_FILE_PATH):
    import pandas as pd

    return pd.read_csv(path)


def generate_currency_pairs(currencies: dict = _DEFAULT_CURRENCIES.keys()):
    length = len(currencies)
    for i in range(length):
        for j in range(i + 1, length):
            yield currencies[i], currencies[j]
