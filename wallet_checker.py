"""Utilities for validating Bitcoin and Ethereum wallet addresses."""

import re


def check_ethereum(address):
    """Return whether the input matches the Ethereum wallet address format.

    Ethereum addresses are 40-character hexadecimal values prefixed with ``0x``.
    The comparison is case-insensitive for the hexadecimal characters.

    Args:
        address (str): Wallet address to validate.

    Returns:
        bool: ``True`` if the value is a valid Ethereum-style address, otherwise
        ``False``.
    """
    if not isinstance(address, str):
        return False

    pattern = r"0x[a-fA-F0-9]{40}"
    return bool(re.fullmatch(pattern, address))


def check_bitcoin(address):
    """Return whether the input matches the Bitcoin wallet address format.

    Supported Bitcoin formats include legacy addresses beginning with ``1`` or
    ``3`` and SegWit addresses beginning with ``bc1``.

    Args:
        address (str): Wallet address to validate.

    Returns:
        bool: ``True`` if the value is a valid Bitcoin-style address, otherwise
        ``False``.
    """
    if not isinstance(address, str):
        return False

    pattern = r"(?:bc1|[13])[a-km-zA-HJ-NP-Z1-9]{25,62}"
    return bool(re.fullmatch(pattern, address))


def main():
    """Prompt the user for a wallet address and print its validation result.

    Reads the value from standard input, strips surrounding whitespace, checks it
    against the supported Ethereum and Bitcoin address patterns, and prints a
    human-readable result.
    """
    wallet = input("Enter wallet address: ").strip()

    if check_ethereum(wallet):
        print("Valid Ethereum-style wallet address.")
    elif check_bitcoin(wallet):
        print("Valid Bitcoin-style wallet address.")
    else:
        print("Not a recognized standard Ethereum or Bitcoin address.")


if __name__ == "__main__":
    main()
