# Coleta de argumento para o IP

import argparse

def getIP():
    parser = argparse.ArgumentParser(prog='IP Info', description='Quick collection of IP address information')

    parser.add_argument('IP', help='IP address')

    args = parser.parse_args()

    IP = args.IP

    if IP:
        return IP
