x = 'WELCOME'

n, m = map(int,input().split())

midpoint = (-(-n // 2))
line_length = m
x = ".|."
msg1= ".|."
msg2 = "WELCOME"


for i in range(1, n + 1):
    
    if(i < midpoint):
        print(f"{msg1.center(line_length, '-')}")
        msg1 = x + msg1 + x
    elif(i == midpoint):
        print(f"{msg2.center(line_length, '-')}")
    else:    
        msg1 = msg1[3:]
        msg1 = msg1[:-3]
        print(f"{msg1.center(line_length, '-')}")
