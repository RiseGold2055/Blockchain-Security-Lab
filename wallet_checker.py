"""validate bitcoin and etherum wallet wallet addresses."""
import re

def check_ethereum(address):
    pattern = r"^0x[a-fA-F0-9]{40}$"
    return bool(re.match(pattern, address))

def check_bitcoin(address):
    pattern = r"^(bc1|[13])[a-km-zA-HJ-NP-Z1-9]{25,62}$"
    return bool(re.match(pattern, address))

def main():
    wallet = input("Enter wallet address: ").strip()

    if check_ethereum(wallet):
        print("Valid Ethereum-style wallet address.")
    elif check_bitcoin(wallet):
        print("Valid Bitcoin-style wallet address.")
    else:
        print("Not a recognized standard Ethereum or Bitcoin address.")

if __name__ == "__main__":
    main()
