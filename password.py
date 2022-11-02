import random
import string
sym = string.ascii_letters + '0123456789' + '@#$%&-*+'
# while True:
ln = int(input("Enter length:"))
pw = ''.join(random.sample(sym, ln))
print(pw)
