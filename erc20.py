from web3 import Web3
import json
import os

# Alchemy Endpoints
MAINNET_URL = "https://eth-mainnet.g.alchemy.com/v2/aoFOuxpUykKwNpGlzJVHA"
TESTNET_URL = "https://eth-sepolia.g.alchemy.com/v2/aoFOuxpUykKwNpGlzJVHA"

# Token Addresses (update testnet one if needed)
USDT_MAINNET = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
USDT_TESTNET = "0x0000000000000000000000000000000000000000"  # Replace with real one if available

ERC20_ABI = json.loads('[{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"type":"function"}]')

# Replace with your private key & address (set via env in production)
SENDER_PRIVATE_KEY = os.getenv("ERC20_PRIVATE_KEY", "0xYourPrivateKey")
SENDER_ADDRESS = os.getenv("ERC20_SENDER_ADDRESS", "0xYourSenderAddress")

def send_erc20(to_address, amount, testnet=True):
    try:
        w3 = Web3(Web3.HTTPProvider(TESTNET_URL if testnet else MAINNET_URL))
        if not w3.is_connected():
            raise Exception("Web3 connection failed")

        token_address = Web3.to_checksum_address(USDT_TESTNET if testnet else USDT_MAINNET)
        contract = w3.eth.contract(address=token_address, abi=ERC20_ABI)

        # USDT = 6 decimals
        base_amount = int(float(amount) * 10**6)

        nonce = w3.eth.get_transaction_count(SENDER_ADDRESS)
        txn = contract.functions.transfer(to_address, base_amount).build_transaction({
            "from": SENDER_ADDRESS,
            "nonce": nonce,
            "gas": 100000,
            "gasPrice": w3.eth.gas_price
        })

        signed = w3.eth.account.sign_transaction(txn, private_key=SENDER_PRIVATE_KEY)
        tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
        return tx_hash.hex()

    except Exception as e:
        print(f"[ERC20 ERROR] {e}")
        return None
