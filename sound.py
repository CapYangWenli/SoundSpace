from syn import genSound
import time

for i in range(1, 20):
    genSound(1, i*100, 20000)
    time.sleep(1)



