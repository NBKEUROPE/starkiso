import socket
from threading import Thread
from iso_server.handler import handle_iso_message

def start_iso_server():
    def listen():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('0.0.0.0', 5001))
            s.listen()
            print('[ISO8583] Listening on port 5001...')
            while True:
                conn, addr = s.accept()
                Thread(target=handle_iso_message, args=(conn, addr)).start()
    Thread(target=listen, daemon=True).start()
