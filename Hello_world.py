#/bin/python
import os,sys

def work():
  print 'Hello World!'

if __name__ == '__main__' :
  if sys.argv.length != 2 :
    print 'EXIT: please input the date'
  date = sys.argv[1]
  work()
