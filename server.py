import socket
import time

HOST = "127.0.0.1"
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server sedang berjalan...")
print(f"Server menunggu client di {HOST}:{PORT}")

try:
    while True:
        client_socket, client_address = server.accept()
        print(f"\nClient terhubung: {client_address}")

        try:
            while True:
                data = client_socket.recv(1024)

                if not data:
                    break

                message = data.decode("utf-8")
                print(f"Pesan dari client: {message}")

                if message.lower() == "exit":
                    response = "Koneksi ditutup."
                    client_socket.sendall(
                        response.encode("utf-8")
                    )
                    break

                response = f"Pesan diterima: {message}"
                client_socket.sendall(
                    response.encode("utf-8")
                )

                time.sleep(0.1)

        finally:
            client_socket.close()
            print("Koneksi client ditutup.")

except KeyboardInterrupt:
    print("\nServer dihentikan oleh pengguna.")

finally:
    server.close()
    print("Server selesai.")