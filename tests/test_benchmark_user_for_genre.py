import sys
sys.path.insert(0, '/home/p/Code/Henry/PI_ML_OPS/app/routes')
import time
from user_for_genre import most_played_user_by_genre, most_played_user_by_genre_slow

def benchmark(function, genre):
    start_time = time.time()
    result = function(genre)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

def main():
    genre = 'Action'  # replace with the genre you want to test

    result1, execution_time1 = benchmark(most_played_user_by_genre, genre)
    print(f"most_played_user_by_genre result: {result1}, execution time: {execution_time1}")

    result2, execution_time2 = benchmark(most_played_user_by_genre_slow, genre)
    print(f"most_played_user_by_genre_slow result: {result2}, execution time: {execution_time2}")

if __name__ == "__main__":
    main()


# execution time: 0.32280707359313965
# execution time: 0.30234694480895996