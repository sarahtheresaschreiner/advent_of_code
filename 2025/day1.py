def part1():
    zeros=0
    try:
        file_name='input1.txt'
        file = open(file_name, 'r')
        aktuell=50
        line = file.readline()
        while(line!=''):
            dir = line[0]
            amount=int(line[1:])
            if dir=="R":
                aktuell+=amount
            else:
                aktuell-=amount
            while aktuell<0:
                aktuell+=100
            while aktuell>99:
                aktuell-=100
            if aktuell==0:
                zeros+=1
            line=file.readline()
        file.close()
    except Exception as e:
        print(e)
    print(zeros)

    
# 1043
# 6492
def part2():
    file_name='input1.txt'
    zeros=0
    aktuell=50
    try:
        file=open(file_name, 'r')
        line=file.readline()
        while (line!=''):
            
            dir = line[0]
            clicks=int(line[1:])
            print(clicks)
            if dir=='R':
                aktuell+=clicks
            else:
                aktuell-=clicks
            print(clicks, aktuell)
            if aktuell>99:
                zeros += int(aktuell/100)
                aktuell = aktuell % 100
            elif aktuell<0:
                if aktuell+ clicks == 0:
                    zeros-=1
                zeros+=(int((-1)*aktuell/100)+1)
                aktuell = aktuell % 100
            elif aktuell ==0:
                zeros+=1
            line=file.readline()
        file.close()
    except Exception as e:
        print('fehler', e)
    print(zeros) 

    
if __name__ == "__main__":
    part1()
    part2()    