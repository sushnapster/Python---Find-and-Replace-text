import random
import string

##Generate 10 character random data
N=10
sush_string= ''.join(random.choices(string.ascii_uppercase +string.digits, k = N))

print (sush_string)
