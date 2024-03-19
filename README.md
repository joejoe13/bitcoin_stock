# Bitcoin and US Stock Price Correlation Program

This is a simple Python program designed to fetch real-time prices of Bitcoin and US stocks and compare their price movements.

## How to Use

1. Clone or download this repository to your local environment.
2. Ensure that you have the `requests` library installed in your Python environment (if not, you can install it using `pip install requests`).
3. Open the `bitcoin_stock.py` file and fill in your Alpha Vantage API key.
4. Run the `bitcoin_stock.py` file:
    ```bash
    python bitcoin_stock.py
    ```
5. The program will output the real-time prices of Bitcoin and a US stock (defaulted to AAPL) and compare their price movements.

## Notes

- You need to register for an Alpha Vantage account to obtain an API key and fill it into the code.
- If you want to fetch prices of different stocks, you can modify the `stock_symbol` variable to your desired stock code.

## Contributions

Contributions, suggestions, or improvements are welcome. If you encounter any bugs, feel free to submit an issue.

## License

This project is licensed under the MIT License. Please see the [LICENSE](LICENSE) file for more details.
