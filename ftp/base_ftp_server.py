import logging

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler, ThrottledDTPHandler
from pyftpdlib.servers import FTPServer

from config_ftp import *


def init_ftp_server():
    authorizer = DummyAuthorizer()
    """
            读权限:
             - "e" = 改变文件目录
             - "l" = 列出文件 (LIST, NLST, STAT, MLSD, MLST, SIZE, MDTM commands)
             - "r" = 从服务器接收文件 (RETR command)

            写权限:
             - "a" = 文件上传 (APPE command)
             - "d" = 删除文件 (DELE, RMD commands)
             - "f" = 文件重命名 (RNFR, RNTO commands)
             - "m" = 创建文件 (MKD command)
             - "w" = 写权限 (STOR, STOU commands)
             - "M" = 文件传输模式 (SITE CHMOD command)  
    """
    if enable_anonymous:
        authorizer.add_anonymous(anonymous_path)

    for user in user_list:
        name, passwd, permit, homedir = user
        try:
            authorizer.add_user(name, passwd, homedir, perm=permit)
        except:
            print('配置文件错误请检查是否正确匹配了相应的用户名、密码、权限、路径')
            print(user)

    dtp_hander = ThrottledDTPHandler
    dtp_hander.read_limit = max_download
    dtp_hander.write_limit = max_upload
    handler = FTPHandler
    handler.authorizer = authorizer

    if enable_logging:
        logging.basicConfig(filename='pyftp.log', level=logging.INFO)

    handler.banner = welcom_banner
    handler.masquerade_address = masquerade_address
    handler.passive_ports = range(passive_ports[0], passive_ports[1])

    address = (ip, port)
    server = FTPServer(address, handler)

    server.max_cons = max_cons
    server.max_cons_per_ip = max_pre_ip
    server.serve_forever()


def ignor_octothrpe(text):
    for x, item in enumerate(text):
        if item == '#':
            return text[:x]
    return text


def init_user_config():
    f = open("baseftp.ini", encoding='utf-8')
    while 1:
        line = f.readline()
        if len(ignor_octothrpe(line)) > 3:
            user_list.append(line.split())
        if not line:
            break


if __name__ == '__main__':
    user_list = []
    init_user_config()
    init_ftp_server()

