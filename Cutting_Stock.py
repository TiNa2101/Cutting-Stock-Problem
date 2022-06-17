import timeit
import numpy

with open('test1.txt', 'r') as test_1:
    L_1 = int(test_1.readline())
    details_length_1 = [int(i) for i in test_1.readline().split()]
    details_price_1 = [int(i) for i in test_1.readline().split()]

with open('test2.txt', 'r') as test_2:
    L_2 = int(test_2.readline())
    details_length_2 = [int(i) for i in test_2.readline().split()]
    details_price_2 = [int(i) for i in test_2.readline().split()]

with open('test3.txt', 'r') as test_3:
    L_3 = int(test_3.readline())
    details_length_3 = [int(i) for i in test_3.readline().split()]
    details_price_3 = [int(i) for i in test_3.readline().split()]

with open('test4.txt', 'r') as test_4:
    L_4 = int(test_4.readline())
    details_length_4 = [int(i) for i in test_4.readline().split()]
    details_price_4 = [int(i) for i in test_4.readline().split()]

with open('test5.txt', 'r') as test_5:
    L_5 = int(test_5.readline())
    details_length_5 = [int(i) for i in test_5.readline().split()]
    details_price_5 = [int(i) for i in test_5.readline().split()]

with open('test6.txt', 'r') as test_6:
    L_6 = int(test_6.readline())
    details_length_6 = [int(i) for i in test_6.readline().split()]
    details_price_6 = [int(i) for i in test_6.readline().split()]

with open('test7.txt', 'r') as test_7:
    L_7 = int(test_7.readline())
    details_length_7 = [int(i) for i in test_7.readline().split()]
    details_price_7 = [int(i) for i in test_7.readline().split()]

def Heuristic(L, details_length, details_price):
    n = len(details_length)
    profit = 0
    details_counter = [0] * n
    details_length_unit = [0] * n
    temp_length = L

    for i in range(n):
        details_length_unit[i] = details_price[i] / details_length[i]
    sorted_indexes = [i[0] for i in sorted(enumerate(details_length_unit), key=lambda x:x[1])]
    sorted_indexes.reverse()

    for i in sorted_indexes:
        while temp_length > 0:
            if temp_length - details_length[i] >= 0:
                details_counter[i] += 1
                profit += details_price[i]
                temp_length -= details_length[i]
            else:
                break
    return profit, details_counter

def DP(L, details_length, details_price):
    n = len(details_length)
    profit = [0] * (L + 1)
    detail_number = [0] * (L + 1)
    details_counter = [0] * n

    for l in range(L + 1):
        for i in range(n):
            if (details_length[i] <= l) and (profit[l] < profit[l-details_length[i]]+details_price[i]):
                profit[l] = profit[l - details_length[i]] + details_price[i]
                detail_number[l] = i + 1

    l = L
    while detail_number[l] > 0:
        i = detail_number[l] - 1
        details_counter[i] += 1
        l -= details_length[i]

    return profit, details_counter, detail_number


#==============================================================
print("TEST 1:", '\n')
print("INPUT DATA:")
print("Length of initial material -", L_1)
print("Details lengths - ", details_length_1)
print("Details prices -  ", details_price_1, '\n')

temp_profit, temp_details_counter, temp_detail_number = DP(L_1, details_length_1, details_price_1)

#for i in range(L_1 + 1):
#    print(i, temp_profit[i], temp_detail_number[i])

print("Dynamic programming:")
print("The profit of optimal cutting: ", temp_profit[L_1])
for i in range(len(details_length_1)):
    print("Number of details of", i + 1, "type:", temp_details_counter[i])
print()

temp_profit, temp_details_counter = Heuristic(L_1, details_length_1, details_price_1)
print("Heuristic algorithm:")
print("The profit of optimal cutting: ", temp_profit)
for i in range(len(details_length_1)):
    print("Number of details of", i + 1, "type:", temp_details_counter[i])
print()
#==============================================================
print("TEST 2:", '\n')
print("INPUT DATA:")
print("Length of initial material -", L_2)
print("Details lengths - ", details_length_2)
print("Details prices -  ", details_price_2, '\n')

temp_profit, temp_details_counter, temp_detail_number = DP(L_2, details_length_2, details_price_2)

#for i in range(L_2 + 1):
#    print(i, temp_profit[i], temp_detail_number[i])

print("Dynamic programming:")
print("The profit of optimal cutting: ", temp_profit[L_2])
for i in range(len(details_length_2)):
    print("Number of details of", i + 1, "type:", temp_details_counter[i])
print()

temp_profit, temp_details_counter = Heuristic(L_2, details_length_2, details_price_2)
print("Heuristic algorithm:")
print("The profit of optimal cutting: ", temp_profit)
for i in range(len(details_length_2)):
    print("Number of details of", i + 1, "type:", temp_details_counter[i])
print()
#==============================================================
print("TEST 3:", '\n')
print("INPUT DATA:")
print("Length of initial material -", L_3)
print("Details lengths - ", details_length_3)
print("Details prices -  ", details_price_3, '\n')

temp_profit, temp_details_counter, temp_detail_number = DP(L_3, details_length_3, details_price_3)

#for i in range(L_3 + 1):
#    print(i, temp_profit[i], temp_detail_number[i])

print("Dynamic programming:")
print("The profit of optimal cutting: ", temp_profit[L_3])
for i in range(len(details_length_3)):
    print("Number of details of", i + 1, "type:", temp_details_counter[i])
print()

temp_profit, temp_details_counter = Heuristic(L_3, details_length_3, details_price_3)
print("Heuristic algorithm:")
print("The profit of optimal cutting: ", temp_profit)
for i in range(len(details_length_3)):
    print("Number of details of", i + 1, "type:", temp_details_counter[i])
print()
#==============================================================
print("TEST 4:", '\n')
print("INPUT DATA:")
print("Length of initial material -", L_4)
print("Details lengths - ", details_length_4)
print("Details prices -  ", details_price_4, '\n')

temp_profit, temp_details_counter, temp_detail_number = DP(L_4, details_length_4, details_price_4)

#for i in range(L_4 + 1):
#    print(i, temp_profit[i], temp_detail_number[i])

print("Dynamic programming:")
print("The profit of optimal cutting: ", temp_profit[L_4])
for i in range(len(details_length_4)):
    print("Number of details of", i + 1, "type:", temp_details_counter[i])
print()

temp_profit, temp_details_counter = Heuristic(L_4, details_length_4, details_price_4)
print("Heuristic algorithm:")
print("The profit of optimal cutting: ", temp_profit)
for i in range(len(details_length_4)):
    print("Number of details of", i + 1, "type:", temp_details_counter[i])
print()
#==============================================================
print("TEST 5:", '\n')
print("INPUT DATA:")
print("Length of initial material -", L_5)
print("Details lengths - ", details_length_5)
print("Details prices -  ", details_price_5, '\n')

temp_profit, temp_details_counter, temp_detail_number = DP(L_5, details_length_5, details_price_5)

#for i in range(L_5 + 1):
#    print(i, temp_profit[i], temp_detail_number[i])

print("Dynamic programming:")
print("The profit of optimal cutting: ", temp_profit[L_5])
for i in range(len(details_length_5)):
    if temp_details_counter[i] != 0:
        print("Number of details of", i + 1, "type:", temp_details_counter[i])
print()

temp_profit, temp_details_counter = Heuristic(L_5, details_length_5, details_price_5)
print("Heuristic algorithm:")
print("The profit of optimal cutting: ", temp_profit)
for i in range(len(details_length_5)):
    if temp_details_counter[i] != 0:
        print("Number of details of", i + 1, "type:", temp_details_counter[i])
print()
#==============================================================
'''
print("TEST 6:", '\n')
print("INPUT DATA:")
print("Length of initial material -", L_6)
print("Details lengths - ", details_length_6)
print("Details prices -  ", details_price_6, '\n')

temp_profit, temp_details_counter, temp_detail_number = DP(L_6, details_length_6, details_price_6)

#for i in range(L_6 + 1):
#    print(i, temp_profit[i], temp_detail_number[i])

print("Dynamic programming:")
print("The profit of optimal cutting: ", temp_profit[L_6])
for i in range(len(details_length_6)):
    if temp_details_counter[i] != 0:
        print("Number of details of", i + 1, "type:", temp_details_counter[i])
print()

temp_profit, temp_details_counter = Heuristic(L_6, details_length_6, details_price_6)
print("Heuristic algorithm:")
print("The profit of optimal cutting: ", temp_profit)
for i in range(len(details_length_6)):
    if temp_details_counter[i] != 0:
        print("Number of details of", i + 1, "type:", temp_details_counter[i])
print()
#==============================================================
'''
print("TEST 7:", '\n')
print("INPUT DATA:")
print("Length of initial material -", L_7)
print("Details lengths - ", details_length_7)
print("Details prices -  ", details_price_7, '\n')

temp_profit, temp_details_counter, temp_detail_number = DP(L_7, details_length_7, details_price_7)

#for i in range(L_7 + 1):
#    print(i, temp_profit[i], temp_detail_number[i])

print("Dynamic programming:")
print("The profit of optimal cutting: ", temp_profit[L_7])
for i in range(len(details_length_7)):
    if temp_details_counter[i] != 0:
        print("Number of details of", i + 1, "type:", temp_details_counter[i])
print()

temp_profit, temp_details_counter = Heuristic(L_7, details_length_7, details_price_7)
print("Heuristic algorithm:")
print("The profit of optimal cutting: ", temp_profit)
for i in range(len(details_length_7)):
    if temp_details_counter[i] != 0:
        print("Number of details of", i + 1, "type:", temp_details_counter[i])
print()
#==============================================================

time1_DP = 0
time2_DP = 0
time3_DP = 0
time4_DP = 0
time5_DP = 0
time6_DP = 0
time7_DP = 0
time1_Heuristic = 0
time2_Heuristic = 0
time3_Heuristic = 0
time4_Heuristic = 0
time5_Heuristic = 0
time6_Heuristic = 0
time7_Heuristic = 0
for i in range(100):
    t_start = timeit.default_timer()
    DP(L_1, details_length_1, details_price_1)
    t_stop = timeit.default_timer()
    time1_DP += t_stop - t_start

    t_start = timeit.default_timer()
    DP(L_2, details_length_2, details_price_2)
    t_stop = timeit.default_timer()
    time2_DP += t_stop - t_start

    t_start = timeit.default_timer()
    DP(L_3, details_length_3, details_price_3)
    t_stop = timeit.default_timer()
    time3_DP += t_stop - t_start

    t_start = timeit.default_timer()
    DP(L_4, details_length_4, details_price_4)
    t_stop = timeit.default_timer()
    time4_DP += t_stop - t_start

    t_start = timeit.default_timer()
    DP(L_5, details_length_5, details_price_5)
    t_stop = timeit.default_timer()
    time5_DP += t_stop - t_start
#--------------------------------------------------------------
    t_start = timeit.default_timer()
    Heuristic(L_1, details_length_1, details_price_1)
    t_stop = timeit.default_timer()
    time1_Heuristic += t_stop - t_start

    t_start = timeit.default_timer()
    Heuristic(L_2, details_length_2, details_price_2)
    t_stop = timeit.default_timer()
    time2_Heuristic += t_stop - t_start

    t_start = timeit.default_timer()
    Heuristic(L_3, details_length_3, details_price_3)
    t_stop = timeit.default_timer()
    time3_Heuristic += t_stop - t_start

    t_start = timeit.default_timer()
    Heuristic(L_4, details_length_4, details_price_4)
    t_stop = timeit.default_timer()
    time4_Heuristic += t_stop - t_start

    t_start = timeit.default_timer()
    Heuristic(L_5, details_length_5, details_price_5)
    t_stop = timeit.default_timer()
    time5_Heuristic += t_stop - t_start

    t_start = timeit.default_timer()
    Heuristic(L_6, details_length_6, details_price_6)
    t_stop = timeit.default_timer()
    time6_Heuristic += t_stop - t_start

    t_start = timeit.default_timer()
    Heuristic(L_7, details_length_7, details_price_7)
    t_stop = timeit.default_timer()
    time7_Heuristic += t_stop - t_start

'''
t_start = timeit.default_timer()
DP(L_6, details_length_6, details_price_6)
t_stop = timeit.default_timer()
time6_DP += t_stop - t_start
'''
t_start = timeit.default_timer()
DP(L_7, details_length_7, details_price_7)
t_stop = timeit.default_timer()
time7_DP += t_stop - t_start


print("Average execution time:\n",
      "|DP test 1|: ", '%.6f' % (time1_DP / 100), "\n",
      "|DP test 2|: ", '%.6f' % (time2_DP / 100), "\n",
      "|DP test 3|: ", '%.6f' % (time3_DP / 100), "\n",
      "|DP test 4|: ", '%.6f' % (time4_DP / 100), "\n",
      "|DP test 5|: ", '%.6f' % (time5_DP / 100), "\n",
      "|DP test 6|: ", '%.6f' % (time6_DP), "\n",
      "|DP test 7|: ", '%.6f' % (time7_DP), "\n", "\n",
      "|Heuristic test 1|: ", '%.6f' % (time1_Heuristic / 100), "\n",
      "|Heuristic test 2|: ", '%.6f' % (time2_Heuristic / 100), "\n",
      "|Heuristic test 3|: ", '%.6f' % (time3_Heuristic / 100), "\n",
      "|Heuristic test 4|: ", '%.6f' % (time4_Heuristic / 100), "\n",
      "|Heuristic test 5|: ", '%.6f' % (time5_Heuristic / 100), "\n",
      "|Heuristic test 6|: ", '%.6f' % (time6_Heuristic / 100), "\n",
      "|Heuristic test 7|: ", '%.6f' % (time7_Heuristic / 100))
