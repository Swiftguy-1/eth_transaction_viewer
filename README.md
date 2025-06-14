# 🧠 Ethereum Transaction Viewer (Python)

This is a simple Python script that lets you **view the recent Ethereum transactions** of any wallet address using the **Etherscan API**.

I built it as a mini project to sharpen my Python skills and explore how blockchain wallets and APIs work. You just paste a wallet address, and boom — you see the last few transactions.

---

## 💡 What It Does

- ✅ Asks for an Ethereum wallet address
- ✅ Fetches recent transactions from [etherscan.io](https://etherscan.io)
- ✅ Displays info like:
  - Sender & Receiver
  - Value (in ETH)
  - Gas used
  - Timestamp
  - Tx hash

Perfect for devs and crypto bros who wanna peek into Ethereum wallets

## 🤖 Why I Made This

I’m currently learning Python and exploring Web3. This project helped me understand:

How APIs work

How blockchain explorers provide data

How to write useful scripts for crypto

---

## ⚙️ How to Run

> 💻 You need Python 3 and the `requests` library.

1. Clone this repo or copy the code
2. Install `requests` if you don’t have it:
   ```bash
   pip install requests