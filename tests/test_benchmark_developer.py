import timeit
import pandas as pd
import sys
sys.path.insert(0, '/home/p/Code/Henry/PI_ML_OPS/app/routes')

from developer import developer, developerv2

# Define the setup code
setup_code = """
import pandas as pd
from developer import developer, developerv2

df = pd.read_parquet('/home/p/Code/Henry/PI_ML_OPS/data/steam_games.parquet', engine='pyarrow')
"""

# Define the code for the first function
developer_code = "developer('Dovetail Games')"

# Define the code for the second function
developerv2_code = "developerv2('Dovetail Games')"

# Execute the timeit statement
developer_time = timeit.timeit(setup=setup_code, stmt=developer_code, number=100)
developerv2_time = timeit.timeit(setup=setup_code, stmt=developerv2_code, number=100)

print(f"Execution time of developer: {developer_time}")
print(f"Execution time of developerv2: {developerv2_time}")

# Execution time of developer: 0.3150518580005155
# Execution time of developerv2: 0.3112390649985173