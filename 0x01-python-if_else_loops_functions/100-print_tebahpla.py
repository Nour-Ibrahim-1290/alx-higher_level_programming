#!/usr/bin/python3

output = [chr(i + 32) if i % 2 == 0 else chr(i) for i in range(90, 64, -1)]
print("{}".format(''.join(output)), end='')
