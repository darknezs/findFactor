from time import time
import threading
import math

class findFactor:
    """ whatever """
    def __init__(self,pub_key):
        self.pub_key = pub_key

    def find_normal_factor(self,point_start, point_end):
        arr = []
        for fac in range(point_start, point_end):
            if self.pub_key%fac == 0:
                print(fac, int(self.pub_key/fac))
                arr.append((fac, int(self.pub_key/fac)))

        # print(arr)

    def find_big_factor(self):
        '''for RSA purpose
        when pub_key = prime x prime
        '''
        min_of_digit, max_of_digit = self.find_min_max_of_digit_divide_2(self.pub_key)
        arr = []
        for fac in range(min_of_digit, max_of_digit):
            if self.pub_key%fac == 0:
                print(fac, int(self.pub_key/fac))
                if (fac,int(self.pub_key/fac)) in arr or (int(self.pub_key/fac),fac) in arr:
                # if fac == round(math.sqrt(self.pub_key)):
                    break
                arr.append((fac, int(self.pub_key/fac)))
        print(arr)

    def find_min_max_of_digit_divide_2(self,n):
        length = int(len(str(n)) / 2)
        temp = ""
        temp2 = ""
        for i in range(length-1): #find min
            temp += '0'
        for j in range(length-1): #find max
            temp2 += '9'
        # return  int("1" + temp)
        min = int("1" + temp)
        max = int("9" + temp2)
        return min,max

    def gen_prime(self ,limit):
        '''generating prime number'''
        # f = open("primeNumber_2.txt", "w")


        for i in range(1,limit):
            cnt = 0
            for j in range(1,limit):
                print(i,j)
                if i%j == 0:
                    cnt = cnt + 1
            if cnt == 2:
                print(i)
                # f.write(str(i)+"\n")
        # f.close()
    def every_thread_get_in_here(self):
        # a,b = self.find_min_max_of_digit_divide_2(4444*4444)
        arr = []
        stop_arr = []
        start_arr = []
        value_in_loop = self.pub_key
        tmp = 0
        number_of_thread = 10

        divide = int(math.ceil(value_in_loop/number_of_thread))

        for i in range(1,number_of_thread+1):
            tmp = tmp + divide
            arr.append(tmp)

        for i in range(len(arr)):
            stop_arr.append(arr[i])

        for i in range(len(arr)-1):
            start_arr.append(arr[i]+1)
        start_arr.insert(0, 1)

        #### monitoring
        # for i in range(0,number_of_thread):
        #     print(start_arr[i], stop_arr[i])
        ####

        thread_s = []
        for i in range(len(start_arr)):
            t1 = threading.Thread(target=self.find_normal_factor, args=(start_arr[i],stop_arr[i]+1))
            t1.start()
            thread_s.append(t1)

        for pcs in thread_s:
            pcs.join()
