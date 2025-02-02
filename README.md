
# 🚀 Cryptocurrency Price Alert System

This Python project fetches real-time cryptocurrency prices using the **CoinGecko API** and triggers alerts if prices cross predefined thresholds.

## 📌 Features
- Fetches real-time market data for cryptocurrencies.
- Checks if a coin’s price exceeds or falls below a specified range.
- Prints alerts for triggered price conditions.

## 📂 Project Structure
```
📁 Project Folder
│── crypto_data.py   # Fetches and processes cryptocurrency data from CoinGecko API
│── main.py          # Defines price alert logic and executes the program
│── README.md        # Documentation (this file)
```

## 🛠️ Requirements
- Python 3.7+
- `requests` library (for API calls)

## 🔧 Installation
1. Clone the repository or download the files:
   ```bash
   git clone https://github.com/sks01dev/crypto-alert.git
   cd crypto-alert
   ```
2. Install dependencies:
   ```bash
   pip install requests
   ```

## 🚀 Usage
1. Run `main.py` to check cryptocurrency prices:
   ```bash
   python main.py
   ```
2. Modify the `alert()` function in `main.py` to change the monitored coins and their price thresholds.

## 📝 Example Output
```
Bitcoin (BTC): $69,500
Ethereum (ETH): $3,100
XRP (XRP): $2.5 !!TRIGGERED!!
```
If a coin price moves beyond the set range, an **alert is triggered** (`!!TRIGGERED!!`).

## 🔄 Future Improvements
- Add email/SMS notifications for price alerts.
- Implement a GUI for easier configuration.
- Support for more cryptocurrencies and time-based tracking.
