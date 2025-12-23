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

def part2():                                    # only works on example data
    file_name='input2.txt'
    invalid_sum=0
    ranges=None
    try:
        file=open(file_name, 'r')
        ranges=file.read().split(',')
    except Exception as e:
        print(e)
    for r in ranges:
        for n in range(int(r.split('-')[0]), int(r.split('-')[1])+1):
            if check(n):
                invalid_sum += n
    print(invalid_sum) 

def check(r):
    t = teiler(r)
    r = str(r)
    for te in t:
        first = r[:te]          # erste stück
        fine = True
        for i in range(te, len(r), te):
            if first != r[i:(i+te)]:
                fine = False
                break
        if fine:
            print(r)
            return True
    return False                

def teiler(r):
    l = len(str(r))
    t = [1]
    for i in range(2, l):
        if l%i == 0:
            t.append(i)
        if i > l/2:
            break
    return t

  
if __name__=='__main__':
    part1()
    part2()