from concurrent.futures import ThreadPoolExecutor
from multiprocessing import process
import subprocess
import os 

executor = ThreadPoolExecutor(max_workers=4)


def _grep(fileName, needle): 
    result = subprocess.run(['grep', needle, fileName], capture_output=True, text=True, check=True)
    return result.stdout


def list_directory(path):
    result = subprocess.run(['ls', path], capture_output=True, text=True, check=True)
    return result.stdout.splitlines()

futures = []

def grep(path, needle):
    files = list_directory(path)
    for file in files:
        os.chdir(path)
        future = executor.submit(_grep, file, needle)
        futures.append(future)



grep("/home/s-linux/repos/dojo/strings", "a")

for index, future in enumerate(futures):
    print(index, future.result())
# list_directory('')


