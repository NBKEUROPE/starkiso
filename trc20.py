from tronpy import Tron
from tronpy.keys import PrivateKey
import os

# Trongrid API Key
TRONGRID_API_KEY = "90556144-eb12-4d28-be5f-24368bb813ff"

# Environment Variables (use .env or production vault)
PRIVATE_KEY = os.getenv("TRC20_PRIVATE_KEY", "your-private-key")
SENDER_ADDRESS = os.getenv("TRC20_SENDER_ADDRESS", "TX...")

# USDT contract address (same for Mainnet and Shasta)
USDT_MAINNET = "TXLAQ63Xg1NAzckPwKHvzw7CSEmLMEqcdj"
USDT_TESTNET = "TXLAQ63Xg1NAzckPwKHvzw7CSEmLMEqcdj"  # Same as Mainnet

def send_trc20(to_address, amount, testnet=True):
    try:
        # Connect to TRON network
        client = Tron(network='shasta' if testnet else 'mainnet', api_key=TRONGRID_API_KEY)

        # Load private key and sender address
        priv_key = PrivateKey(bytes.fromhex(PRIVATE_KEY[2:] if PRIVATE_KEY.startswith("0x") else PRIVATE_KEY))
        from_addr = priv_key.public_key.to_base58check_address()

        # Load USDT contract
        contract = client.get_contract(USDT_TESTNET if testnet else USDT_MAINNET)

        # Convert USDT to 6 decimal base
        base_amount = int(float(amount) * 1_000_000)

        # Build, sign and broadcast transaction
        txn = (
            contract.functions.transfer(to_address, base_amount)
            .with_owner(from_addr)
            .fee_limit(2_000_000)
            .build()
            .sign(priv_key)
        )
        result = txn.broadcast().wait()
        return result["txid"]

    except Exception as e:
        print(f"[TRC20 ERROR] {e}")
        return None
