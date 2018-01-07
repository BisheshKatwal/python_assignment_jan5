my_list=list(range(0,100))
prime_no=[]
fp = open("prime_numbers.txt","w")

for each in my_list:
    for i in range(2, each - 1):
        if (each % i == 0):
            break
    else:
        prime_no.append(each)


fp.write(str(prime_no))
fp.close()