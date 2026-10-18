import socket

HOST = "127.0.0.1"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((HOST, PORT))

    print("Berhasil terhubung ke server!")
    print("Ketik 'exit' untuk keluar.\n")
    
    while True:
        message = input("Masukkan pesan: ")

        client.sendall(message.encode("utf-8"))

        response = client.recv(1024).decode("utf-8")

        print("Balasan server:", response)

        if message.lower() == "exit":
            break

except ConnectionRefusedError:
    print("Server belum berjalan. Jalankan server.py terlebih dahulu.")

except OSError as error:
    print("Terjadi kesalahan:", error)

finally:
    client.close()
    print("Koneksi client ditutup.")