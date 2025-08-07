# config/wallet_pool.py
ERC20_WALLETS = ["0xWallet1", "0xWallet2", "0xWallet3", "0xWallet4", "0xWallet5"]
TRC20_WALLETS = ["TWallet1", "TWallet2", "TWallet3", "TWallet4", "TWallet5"]
BTC_WALLET = "mzWallet1"

def get_next_wallet(chain):
    if chain == 'erc20':
        return ERC20_WALLETS[0]  # Simulated round-robin
    elif chain == 'trc20':
        return TRC20_WALLETS[0]
    elif chain == 'btc':
        return BTC_WALLET
    return None
