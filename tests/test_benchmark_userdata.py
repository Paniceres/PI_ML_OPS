import sys
import time
sys.path.insert(0, '/home/p/Code/Henry/PI_ML_OPS/app/routes')
from userdata import userdata, userdata_slow

def benchmark(function, User_id):
    start_time = time.time()
    result = function(User_id)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

def main():
    User_id = 'js41637'  # replace with the User_id you want to test

    result1, execution_time1 = benchmark(userdata, User_id)
    print(f"userdata result: {result1}, execution time: {execution_time1}")

    result2, execution_time2 = benchmark(userdata_slow, User_id)
    print(f"userdata_slow result: {result2}, execution time: {execution_time2}")

if __name__ == "__main__":
    main() 


# userdata result: (29.98, 0.0, 2), execution time: 0.2179110050201416
# userdata_slow result: (29.98, 100.0, 2), execution time: 0.15660953521728516