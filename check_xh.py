#coding=utf8
import thread
import sys

class scan:
    def __init__(self,ip,port,lock):
        import socket
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.settimeout(5)
        self.ip=ip
        self.port=port
        self.lock=lock
        self.packet='''GET / HTTP/1.1\r
Host: rd.go.10086.cn\r
X-Online-Host: m.so.com\r
Connection: keep-alive\r
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r
Upgrade-Insecure-Requests: 1\r
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36\r
Accept-Language: zh-CN,zh;q=0.8\r
\r
'''

    def run(self):
        try:
            self.s.connect((self.ip, port))
            self.s.send(self.packet)
            buf = self.s.recv(1024)
            while len(buf):
                print buf
                buf = self.s.recv(1024)
            self.s.close()
        except:
            self.s.close()
        self.lock.release()

if __name__ == '__main__':
    locks = []
    fip='111.13'
    port=80
    try:
        for x in range(0,256):
            for y in range(0,256):
                lock = thread.allocate_lock()
                lock.acquire();
                locks.append(lock);
                #port= x*y
                ip=fip+'.'+str(x)+'.'+str(y)
                #ip=fip+str(x)
                thread.start_new_thread(scan(ip,port,lock).run, ())
                print ip
            for lock in locks:
                while lock.locked():
                    pass
    except KeyboardInterrupt:
        sys.exit(0)
