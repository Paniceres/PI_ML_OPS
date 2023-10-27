import sys
import time
sys.path.insert(0, '/home/p/Code/Henry/PI_ML_OPS/app/routes')
from userdata import userdata

def benchmark(function, User_id):
    start_time = time.time()
    result = function(User_id)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

def main():
    User_id = 'Sp3ctre'  # replace with the User_id you want to test

    result, execution_time = benchmark(userdata, User_id)
    print(f"userdata result: {result}, execution time: {execution_time}")


if __name__ == "__main__":
    main() 


# execution time: 0.2179110050201416
# execution time: 0.16936087608337402