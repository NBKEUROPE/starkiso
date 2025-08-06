import requests
import os

# BlockCypher Token
BLOCKCYPHER_API_TOKEN = "365254933adb43b0bf68594a5452442a"

# From environment or hardcoded for testing
SENDER_ADDRESS = os.getenv("BTC_SENDER_ADDRESS", "your-btc-testnet-address")
PRIVATE_KEY_WIF = os.getenv("BTC_PRIVATE_KEY", "your-testnet-private-key")

def send_btc(to_address, amount, testnet=True):
    try:
        network = 'btc/test3' if testnet else 'btc/main'
        base_url = f"https://api.blockcypher.com/v1/{network}"

        # Step 1: Fetch UTXOs
        utxo_url = f"{base_url}/addrs/{SENDER_ADDRESS}?unspentOnly=true&token={BLOCKCYPHER_API_TOKEN}"
        utxos = requests.get(utxo_url).json().get("txrefs", [])
        if not utxos:
            raise Exception("No UTXOs available for this address")

        # Step 2: Create TX skeleton
        inputs = [{"addresses": [SENDER_ADDRESS]}]
        outputs = [{"addresses": [to_address], "value": int(float(amount) * 1e8)}]
        tx_url = f"{base_url}/txs/new?token={BLOCKCYPHER_API_TOKEN}"
        tx_skeleton = requests.post(tx_url, json={"inputs": inputs, "outputs": outputs}).json()

        # Step 3: You MUST sign this skeleton — skipped here for safety
        raise NotImplementedError("Signing requires secure local handling with bitcoinlib or Electrum")

        # Step 4: Broadcast signed TX (placeholder)
        # send_url = f"{base_url}/txs/send?token={BLOCKCYPHER_API_TOKEN}"
        # result = requests.post(send_url, json=signed_tx).json()
        # return result.get("tx", {}).get("hash")

    except Exception as e:
        print(f"[BTC ERROR] {e}")
        return None
