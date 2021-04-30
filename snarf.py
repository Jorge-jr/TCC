import threading, os, time, datetime, random, socket
from scapy.all import *


def hopper(iface):

  channel = 11
  stop_hopper = False

  while not stop_hopper:
    time.sleep(0.5)
    os.system(f"iwconfig {iface} channel {channel}")  # configura o canal a ser monitorado
    print(f"current channel: {channel}         ", end='\r')
    channel = int(random.randint(1,14)) # próximo canal escolhido aleatóriamente


def frame_reporter(pkt):
  if pkt.type == 0 and pkt.subtype == 4:  # filtrando probe requests
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # CRIA UM SOCKET (ipv4, tcp)
    server.connect(('192.198.0.127', 1234))
    server.send(bytes(pkt.addr2 + '|' + datetime.datetime.now()), "utf-8")
    print(f"{pkt.addr2} enviado")
    server.shutdown(socket.SHUT_RDWR)
    server.close()


if __name__ == "__main__":
  thread = threading.Thread(target=hopper, args=("mon0",), name="hopper")
  thread.daemon = True
  thread.start()
  sniff(iface="mon0", prn=frame_reporter)
