def check_wallet(address):
if address.startswith("0x") and len(address) == 42:
print("This looks like an Ethereum-style address.")
else:
print("This does not look like a standard Ethereum-Style address")

wallet = input("Enter a wallet address: ")
check_wallet(wallet)
def wallet_checker.py

import re
4def check_ethereum(address):
6"""Validate Ethereum wallet address."""
7pattern = r"^0x[a-fA-F0-9]{40}$"
8
return bool(re.match(pattern, address))
def check_bitcoin(address):
11
"""Basic Bitcoin address validation."""
12pattern = r"^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,62}$"
13
return bool(re.match(pattern, address))
def main():
wallet = input("Enter wallet address: ").strip()7
if check_ethereum(wallet):
print("Valid Ethereum wallet address.")0
elif check_bitcoin(wallet):
print("Valid Bitcoin wallet address.")
else:
print("Invalid or unsupported wallet address.")
