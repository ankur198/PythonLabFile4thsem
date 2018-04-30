def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

start = int(input("Enter start: "))
end = int(input("Enter end: "))

for x in range(start,end + 1):
    if isPrime(x):
        print(x)

'''
-------------------Output-------------------------
Enter start: 100
Enter end: 200
101
103
107
109
113
127
131
137
139
149
151
157
163
167
173
179
181
191
193
197
199
---------------------EOF--------------------------
'''
