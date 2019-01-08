import RPi.GPIO as G
import time 

G.setmode(G.BOARD)
G.setup(22,G.OUT)
p = G.PWM(22,50)
p.start(2.5)

try: 
    while True: 
        print("hello")
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        p.ChangeDutyCycle(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(12.5)
        time.sleep(1)

except KeyboardInterrupt:
    p.stop()
    G.cleanup()
