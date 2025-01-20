#!/usr/bin/env python3
# Author: Dechen Phub
# Author ID: 148596190
# Date Created: 2025/01/20
 
import sys


if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])


while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")