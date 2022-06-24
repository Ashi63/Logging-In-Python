import sys 

try:
    1/0
except Exception as e:
    print (sys.exc_info())