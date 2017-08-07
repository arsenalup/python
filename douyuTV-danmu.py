import multiprocessing
import socket
import time
import re
import signal

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname('openbarrage.douyutv.com')
port = 8601
client.connect((host, port))

#弹幕查询
danmu_re = re.compile(b'txt@=(.+?)/cid@')
username_re = re.compile(b'nn@=(.+?)/txt@')


def send_req_msg(msgstr):
    """api请求"""
    msg = msgstr.encode('utf-8')
    data_length = len(msg) + 8
    code = 689
    #构造协议头
    msgHead = int.to_bytes(data_length, 4, 'little') + int.to_bytes(data_length, 4, 'little') + int.to_bytes(code, 4, 'little')
    client.send(msgHead)
    sent = 0
    while sent < len(msg):
        tn = client.send(msg[sent:])
        sent = sent + tn


def DM_start(roomid):
    """登陆请求"""
    msg = 'type@=loginreq/roomid@={}/\0'.format(roomid)
    send_req_msg(msg)
    #弹幕消息请求
    msg_more = 'type@=joingroup/rid@={}/gid@=-9999/\0'.format(roomid)
    send_req_msg(msg_more)

    while True:
        #返回的数据
        data = client.recv(1024)
        #正则匹配数据
        danmu_username = username_re.findall(data)
        danmu_content = danmu_re.findall(data)
        if not data:
            break
        else:
            for i in range(0, len(danmu_content)):
                try:
                    #输出弹幕内容
                    print('[{}]:{}'.format(danmu_username[0].decode('utf8'),
                          danmu_content[0].decode('utf8')))
                except:
                    continue


def keeplive():
    while True:
        msg = 'type@=keeplive/tick@=' + str(int(time.time())) + '/\0'
        send_req_msg(msg)
        print('保持连接')
        time.sleep(15)


def logout():
    msg = 'type@=logout/'
    send_req_msg(msg)
    print('已经断开连接')


def singal_handler(singal, frame):
    p1.terminate()
    p2.terminate()
    logout()
    print('bye')

if __name__ == '__main__':
    room_id = input('请输入房间id')
    if not room_id:
        room_id = 2020877

    signal.signal(signal.SIGINT, singal_handler)

    p1 = multiprocessing.Process(target=DM_start, args=(room_id, ))
    p2 = multiprocessing.Process(target=keeplive)
    p1.start()
    p2.start()
