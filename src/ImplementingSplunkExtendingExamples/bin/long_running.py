import time
import random
import sys

for i in range(1, 1000):
    print "%s Hello." % time.strftime('%Y-%m-%dT%H:%M:%S')
    #make sure python actually sends the output
    sys.stdout.flush()
    time.sleep(random.randint(1, 5))
