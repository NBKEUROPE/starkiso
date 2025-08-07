from iso_server.iso_parser import parse_iso_message
from payout.trigger import trigger_crypto_payout

def handle_iso_message(conn, addr):
    try:
        data = conn.recv(2048)
        print(f"[ISO8583] Received from {addr}: {data}")
        parsed = parse_iso_message(data)
        print(f"[Parsed ISO] {parsed}")

        if parsed['mti'] == '0200':
            print("[ISO8583] Approved transaction")
            trigger_crypto_payout(parsed['fields'])
            conn.sendall(b'0210 APPROVED')
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        conn.close()
