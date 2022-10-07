_E = "3PQtD6B1crUVvNHt6fVY5HvdajRrJ6EeGq"
_D = "1Ca72914TemMMuDpAscEMeZV3494sztc81"
_C = "localhost"
_B = "%m/%d/%Y, %H:%M:%S"
_A = "\n"
import pickle, os, random, time
from pymemcache.client import base
from datetime import datetime

DATA_PATH = "data/"
print("loading memcached...")
client = base.Client((_C, 11211))
print("uploading data...")
print(datetime.now().strftime(_B))
count = len(os.listdir(DATA_PATH))
ret_list = client.get_multi([_D, _E])
if ret_list:
    print("test check pass")
else:
    for (c, p) in enumerate(os.listdir(DATA_PATH)):
        print("\rreading data: " + str(c + 1) + "/" + str(count), end=" ")
        with open(DATA_PATH + p, "rb") as file:
            data = pickle.load(file)
            client.set_multi(dict.fromkeys(data, 1), expire=0)
        data = []
    print("data loaded!")
    print(datetime.now().strftime(_B))
    ret_list = client.get_multi([_E, _D])
    if ret_list:
        print("testing passed!")
    else:
        print("testing failed!")
DATA_PATH = "data/data.txt"
test_1_i = random.randint(0, 34000000)
test_2_i = random.randint(0, 34000000)
test_1_s = ""
test_2_s = ""
print("connect memcached...")
client = base.Client((_C, 11211))
print("Loading and injecting data")
print(datetime.now().strftime(_B))
startTime = time.time()
i_add = 0
f = open(DATA_PATH, "r")
while True:
    alist = []
    lines = f.readlines(32768)
    if not lines:
        break
    for i in lines:
        alist.append(i.rstrip(_A))
        i_add += 1
        if i_add == test_1_i:
            test_1_s = i.rstrip(_A)
        if i_add == test_2_i:
            test_2_s = i.rstrip(_A)
    client.set_multi(dict.fromkeys(alist, 1), expire=0)
    print("\raddresses: " + str(i_add), end=" ")
f.close()
endTime = time.time()
executionTime = endTime - startTime
print(
    "DATA LOADED: Addresses loadeded in " + str(round(executionTime, 2)) + " seconds!"
)
print("test 1: " + test_1_s + " test 2: " + test_2_s)
print(datetime.now().strftime(_B))
f = open("test.txt", "w")
f.write(test_1_s + _A)
f.write(test_2_s + _A)
f.close()
exec(open("scanner.py").read())
