import socket
import threading

from cryptography.fernet import Fernet
from crypto import generate_key


HOST = "0.0.0.0"
PORT = 5000

clients = {}
KEY = generate_key()


def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.sendall(message)
            except:
                pass


def send_system_message(message):
    data = f"[SYSTEM] {message}".encode("utf-8")

    # encrypted = Fernet(KEY).encrypt(data)               #riga che ho messo opzionale per vedere da terminale server chi si è connesso

    for client in clients:
        try:
            client.sendall(data)
        except:
            pass


def handle_client(client):
    try:
        name = client.recv(1024).decode("utf-8")

        clients[client] = name

        print(f"{name} si è connesso.")

        send_system_message(f"{name} si è connesso.")

        while True:
            message = client.recv(4096)

            if not message:
                break

            print(f"Messaggio ricevuto da {name}: {message}")

            broadcast(message, client)

    except Exception as error:
        print("Errore:", error)

    finally:
        name = clients.get(client, "Utente")

        if client in clients:
            del clients[client]

        client.close()

        send_system_message(f"{name} si è disconnesso.")

        print(f"{name} si è disconnesso.")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen()

print("========================================")
print("           MINICHAT SERVER")
print("========================================")

print("\nNuova sessione creata.")
print("\nChiave della sessione:")
print(KEY.decode("utf-8"))

print("\nCondividi questa chiave con i partecipanti.")
print("\nIn attesa di connessioni...\n")


while True:
    client, address = server.accept()

    print(f"Nuova connessione da {address}")

    thread = threading.Thread(
        target=handle_client,
        args=(client,),
        daemon=True
    )

    thread.start()