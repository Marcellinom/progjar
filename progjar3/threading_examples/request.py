import socket

def send_request(i = None):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 45000))
    request = "TIME\r\n"
    client_socket.send(request.encode('utf-8'))
    response = client_socket.recv(32).decode('utf-8')
    print(("worker %d: " % i)+response)
    client_socket.close()