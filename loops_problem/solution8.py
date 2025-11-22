# exponential backoff - impliment a exponential backoff starategy that doubles that thw wait time between retries , starting from 1 sec but stop after 5 sec 
import time 

wait_time=1
max_retries=5
attempts=0

while attempts<max_retries:
    print("attempt",attempts+1,"-wait time",wait_time,)
    time.sleep(wait_time)
    wait_time*=2
    attempts+=1

# isma mja aya bro ya or jana or sikho, smjho 

