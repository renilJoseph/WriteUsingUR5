import math
import urx
import logging
import time
import alphabets
import sys


if __name__ == "__main__":
    logging.basicConfig(level=logging.WARN)

    # print sys.argv[1], "***"

    rob = urx.Robot("192.168.43.107")
    rob.set_tcp((0,0,0,0,0,0))
    rob.set_payload(0.5, (0,0,0))
    try:
        l = 0.05
        v = 1
        a = 0.3

        
        for ch in sys.argv[1]:
            if ch==' ':
                ch= '_'
            getattr(alphabets, 'draw%c' % ch)(rob,a,v)
              

       
    finally:
        rob.close()

