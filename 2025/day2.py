def part1():
    file_name='input2.txt'
    invalid_sum=0
    ranges=None
    try:
        file=open(file_name, 'r')
        ranges=file.read().split(',')
    except Exception as e:
        print(e)
    for r in ranges:
        start,ende=r.split('-')
        start = int(start)
        ende=int(ende)
        print(start, ende)
        for i in range(ende-start+1):
            num=start+i
            string=str(num)
            l = len(string)
            l2=int(l/2)
            if l%2 != 0:
                pass
            elif int(string[:l2]) == int(string[l2:]):
                invalid_sum+=num
    print(invalid_sum) 

def part2():
    file_name='example.txt'
    invalid_sum=0
    ranges=None
    try:
        file=open(file_name, 'r')
        ranges=file.read().split(',')
    except Exception as e:
        print(e)
    for r in ranges:
        start,ende=r.split('-')
        start = int(start)
        ende=int(ende)
        print(start, ende)
        for i in range(ende-start+1):
            num=start+i
            invalid_sum+=inner(num)                              
    print(invalid_sum)   

def inner(num):
    string=str(num)
    l = len(string)

    for t in getTeiler(l):
        isL = True
        for j in range(int(l/t)):
            k1=j*t
            k2=(j+1)*t
            k3=(j+2)*t
            if int(string[k1:k2]) != int(string[k2:k3]):
                isL = False
        if isL==True:
            return num
    return 0

def getTeiler(n):
    ts=[1]
    for i in range(1, n):
        if n%i == 0:
            ts.append(i)
    return ts
    
if __name__=='__main__':
    part2()