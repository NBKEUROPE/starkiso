from payout.erc20 import send_erc20
from payout.trc20 import send_trc20
from payout.btc import send_btc

def trigger_crypto_payout(fields):
    pan = fields.get(2)
    amount = fields.get(4)
    print(f"[CRYPTO PAYOUT] PAN: {pan}, AMOUNT: {amount}")

    if pan.startswith('4'):
        print("[PAYOUT] Using ERC20")
        tx = send_erc20(to_address='0x...', amount=amount, testnet=True)
    elif pan.startswith('5'):
        print("[PAYOUT] Using TRC20")
        tx = send_trc20(to_address='T...', amount=amount, testnet=True)
    elif pan.startswith('6'):
        print("[PAYOUT] Using BTC")
        tx = send_btc(to_address='mz...', amount=amount, testnet=True)
    else:
        print("[PAYOUT] Unknown PAN")
        return

    print(f"[PAYOUT TXID] {tx}")
