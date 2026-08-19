import socket
import threading

from crypto import encrypt_message, decrypt_message


SERVER_IP = input("Inserisci l'indirizzo IP del server: ")
PORT = 5000

NAME = input("Inserisci il tuo nome: ")

KEY_TEXT = input("Inserisci la chiave della chat: ")
KEY = KEY_TEXT.encode("utf-8")


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERVER_IP, PORT))


client.sendall(NAME.encode("utf-8"))


def receive_messages():
    while True:
        try:
            message = client.recv(4096)

            if not message:
                break

            try:
                decrypted = decrypt_message(message, KEY)

                print(f"\n{decrypted}")
                print("> ", end="", flush=True)

            except:
                print("\n[Messaggio non valido o chiave errata]")
                print("> ", end="", flush=True)

        except:
            print("\nConnessione chiusa.")
            break


thread = threading.Thread(
    target=receive_messages,
    daemon=True
)

thread.start()


print("\n" + "=" * 40)
print("             MINICHAT")
print("=" * 40)

print("\nConnesso al server.")
print("Scrivi un messaggio.")
print("Digita /exit per uscire.\n")


while True:

    message = input("> ")

    if message.lower() == "/exit":
        break

    full_message = f"[{NAME}] {message}"

    encrypted = encrypt_message(full_message, KEY)

    client.sendall(encrypted)


client.close()