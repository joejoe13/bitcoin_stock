import requests

def get_bitcoin_price():
    # 使用Coinbase API获取比特币价格
    url = "https://api.coinbase.com/v2/prices/spot?currency=USD"
    response = requests.get(url)
    data = response.json()
    bitcoin_price = float(data['data']['amount'])
    return bitcoin_price

def get_stock_price(symbol):
    # 使用Alpha Vantage API获取股票价格，你需要注册一个免费账户获取API密钥
    api_key = "YOUR_API_KEY"
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    stock_price = float(data['Global Quote']['05. price'])
    return stock_price

def main():
    bitcoin_price = get_bitcoin_price()
    stock_symbol = "AAPL"  # 可以替换成你感兴趣的股票代码
    stock_price = get_stock_price(stock_symbol)

    print(f"比特币价格：${bitcoin_price}")
    print(f"{stock_symbol}股票价格：${stock_price}")

    # 比较比特币价格和股票价格，输出涨跌情况
    if bitcoin_price > stock_price:
        print("比特币价格高于股票价格")
    elif bitcoin_price < stock_price:
        print("比特币价格低于股票价格")
    else:
        print("比特币价格与股票价格相同")

if __name__ == "__main__":
    main()
