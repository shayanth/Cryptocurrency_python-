from backend.blockchain.blockchain  import Blockchain
import time
from backend.config import SECONDS

blockchain = Blockchain()

times = []

for i in range(1000):
    start_time = time.time_ns()
    blockchain.Add_block(i)
    end_time = time.time_ns()

    time_to_time = (end_time - start_time)/ SECONDS
    times.append(time_to_time)

    average_time = sum(times) / len(times)

    print(f'New Block Difficulty : {blockchain.chain[-1].difficulty}')
    print(f'New Block hash : {blockchain.chain[-1].hash}')
    print(f'Time to mine new Block : {time_to_time}s')
    print(f'Average time to mine new Block : {average_time}s\n')
    print("##################################################\n")

