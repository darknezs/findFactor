from find_class import findFactor
from time import time
import threading
from config import a,b,c,n

pub_key =  8389*6863


start = time()

find = findFactor(pub_key)
find.find_normal_factor(1,pub_key+1)
# print("------------------------------------")
# find.gen_prime(500000)
# find.find_big_factor()
# find.every_thread_get_in_here()

end = time()
total = end - start
print("\nTime: ",str(total)," sec")






# a = [(1,10),(2,5),(5,2),(10,1)]
# if (2,10/2) in a or (10/5,2) in a:
#     print('yes')


# arr = []
# stop_arr = []
# start_arr = []
# max = 1000000
# tmp = 0
#
# divide = int(max/20)
# for i in range(1,20+1):
#     tmp = tmp + divide
#     arr.append(tmp)
# # print(arr)
#
# for i in range(len(arr)):
#     stop_arr.append(arr[i])
#
# for i in range(len(arr)-1):
#     start_arr.append(arr[i]+1)
# start_arr.insert(0, 1)
#
# for i in range(0,20):
#     print(start_arr[i], stop_arr[i])
#
#
# def A(st,en):
#     for i in range(st, en):
#         for j in range(st, en):
#             print(i*j)

# def B():
    # print("sleep 1 sec")
    # time.sleep(1)
    # print('done sleeping')

# def C(st, en):
#     for i in range(st, en):
#         print(i)
#
# start = time.perf_counter()
# #
# # A(1,1000)
# process = []
# for i in range(len(start_arr)):
#     t1 = threading.Thread(target=C, args=(start_arr[i], stop_arr[i]))
#     t1.start()
#     # t1.join()
#     process.append(t1)
#
# for pcs in process:
#     pcs.join()
#
#
#
# end = time.perf_counter()
# total = end - start
# print(float(total))
