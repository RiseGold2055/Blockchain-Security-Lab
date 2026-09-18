"""Validate Bitcoin and Ethereum wallet addresses."""
import re


def check_ethereum(address):
    """Return True if the given string is a valid Ethereum wallet address.

    Args:
        address (str): The wallet address to validate.

    Returns:
        bool: True if the address matches the Ethereum format, otherwise False.
    """
    if not isinstance(address, str):
        return False

    pattern = r"0x[a-fA-F0-9]{40}"
    return bool(re.fullmatch(pattern, address))


def check_bitcoin(address):
    """Return True if the given string is a valid Bitcoin wallet address.

    Args:
        address (str): The wallet address to validate.

    Returns:
        bool: True if the address matches the Bitcoin format, otherwise False.
    """
    if not isinstance(address, str):
        return False

    pattern = r"(?:bc1|[13])[a-km-zA-HJ-NP-Z1-9]{25,62}"
    return bool(re.fullmatch(pattern, address))


def main():
    """Prompt for a wallet address and print whether it is valid."""
    wallet = input("Enter wallet address: ").strip()

    if check_ethereum(wallet):
        print("Valid Ethereum-style wallet address.")
    elif check_bitcoin(wallet):
        print("Valid Bitcoin-style wallet address.")
    else:
        print("Not a recognized standard Ethereum or Bitcoin address.")


if __name__ == "__main__":
    main()
