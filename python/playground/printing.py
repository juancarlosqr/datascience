#!/usr/bin/env python

import os, sys

def main():
  patt = "*" * 40
  print "%s os variables %s" % (patt, patt)
  for elem in dir(os):
    print elem
  print "%s sys variables %s" % (patt, patt)
  for elem in dir(sys):
    print elem

if __name__ == '__main__':
  main()