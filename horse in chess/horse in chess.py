d={
    'A':1,
    'B':2,
    'C':3,
    'D':4,
    'E':5,
    'F':6,
    'G':7,
    'H':8,
}

f = open('input.txt')
n = f.readline()
if len(n) != 5:
    ans = 'Error'
else:
    o = n
    o = [o[x:x+1] for x in range(0, len(o), 1)]
    if o[2] != '-':
        ans = "Error - "
    else:
        n = n.split('-')
        a = n[0]
        a = [a[x:x+1] for x in range(0, len(a), 1)]
        b = n[1]
        b = [b[x:x+1] for x in range(0, len(b), 1)]
        a1 = a[0]
        a2 = a[1]
        b1 = b[0]
        b2 = b[1]
        if a1 == 'A' or a1 == 'B' or a1 == 'C' or a1 == 'D' or a1 == 'E' or a1 == 'F' or a1 == 'G' or a1 == 'H':
            if b1 == 'A' or b1 == 'B' or b1 == 'C' or b1 == 'D' or b1 == 'E' or b1 == 'F' or b1 == 'G' or b1 == 'H':
                if a2 == '1' or a2 == '2' or a2 == '3' or a2 == '4' or a2 == '5' or a2 == '6' or a2 == '7' or a2 == '8':
                    if b2 == '1' or b2 == '2' or b2 == '3' or b2 == '4' or b2 == '5' or b2 == '6' or b2 == '7' or b2 == '8':
                        b2 = int(b2)
                        a2 = int(a2)
                        a1 = int(d.get(a1))
                        b1 = int(d.get(b1))
                        c = abs(a1 - b1)
                        d = abs(a2 - b2)
                        if c == 1 and d == 2 or c == 2 and d == 1:
                            ans = 'YES'
                        else:
                            ans = 'NO'
                    else:
                        ans = 'ERROR b2'
                else:
                    ans = 'ERROR a2'
            else:
                ans = 'ERROR b1'
        else:
            ans = 'ERROR a1'

with open('output.txt','w') as f:
    f.write(ans)