#coding=utf-8
import socket


def send_message(udp_socket):
    msg = input("请输入发送的信息")
    add = input("请输入IP地址")
    port = input("请输入端口号")
    udp_socket.sendto(msg.encode("utf-8"), (add, port))


def receive_msg(udp_socket):
    rec_msg = udp_socket.recvform(1024)
    msg = rec_msg[0].decode("utf-8")
    ip = rec_msg[1]
    print("从ip是：%s接受到的信息为：%s"%(ip, msg))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('', 1234))
    while True:
        num = input("请输入编号")
        if num == '1':
            send_message(udp_socket)
        elif num == '2':
            receive_msg(udp_socket)
        else:
            print("输入有误，重新输入")


if __name__ == "__main__":
    main()

