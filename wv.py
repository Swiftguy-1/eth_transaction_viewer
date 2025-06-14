import requests

def get_transactions(address, api_key):
    url = f"https://api.etherscan.io/api"
    params = {
        "module": "account",
        "action": "txlist",
        "address": address,
        "startblock": 0,
        "endblock": 99999999,
        "page": 1,
        "offset": 5,
        "sort": "desc",
        "apikey": api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data["status"] == "1":
        return data["result"]
    elif data["message"] == "No transactions found":
        print("❌ No transactions found for this address.")
        return []
    else:
        print("⚠️ Error:", data["message"])
        return []

def display_transactions(transactions):
    if not transactions:
        print("No transactions to display.")
        return

    print("\n🔍 Latest Transactions:")
    for tx in transactions:
        print("-------------------------------------------------")
        print("Hash:", tx["hash"])
        print("From:", tx["from"])
        print("To  :", tx["to"])
        print("Value (ETH):", int(tx["value"]) / 10**18)
        print("Gas Used:", tx["gasUsed"])
        print("TimeStamp:", tx["timeStamp"])
    print("-------------------------------------------------")

def main():
    print("🔗 Ethereum Transaction Viewer")
    address = input("📥 Enter Ethereum wallet address: ").strip()
    
    api_key = "EI9SBEFUWYF1V2AJVNZP735RXD654DG9V1" 

    transactions = get_transactions(address, api_key)
    display_transactions(transactions)

if __name__ == "__main__":
    main()