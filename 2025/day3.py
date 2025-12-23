def part1():                    # works on example
    file_name='input3.txt'
    sum=0
    banks = None
    try:
        file=open(file_name, 'r')
        banks=file.read().split('\n')
    except Exception as e:
        print(e)
    for b in banks:
        best=0
        first=0
        for i in range(len(b)-1):
            if int(b[i]) > int(b[first]):
                first = i
            if b[first] == 9:
                break
        start = first +1
        second = 1
        for i in range(start, len(b)):
            if int(b[i]) > int(b[second]):
                second = i
            if b[second] == 9:
                break
        best = int(b[first] + b[second])
        sum=sum+best
        print(best)
    print(sum)
    
if __name__=='__main__':
    part1()
