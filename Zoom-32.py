#!/usr/bin/env python2.7.6
import re, time
lib = "client.dll"
with open(lib, mode='rb') as s:
    d = s.readlines()


with open(lib, mode='rb') as r:
    strings = re.findall('\d{4}\x00\x00\x00\x00r_propsmaxdist', r.read())
    c = ''.join(strings)[0:4]
    print "Your size =", c


def complete():
  with open(lib, mode='wb') as outfile:
    for line in d:
      res = re.compile('\d{4}\x00\x00\x00\x00r_propsmaxdist')
      cam = res.sub((str(x)) +'\x00\x00\x00\x00r_propsmaxdist', line)
      outfile.write(cam)

print "Type 4-digits number"
while True:
  try:
    x = int(raw_input())
    if len(str(x)) == 4 and x <= 1900 and x >=1200:
      print "Complete""\n", "Your new size is:", x
      complete()
      time.sleep(6)
      exit()
    else:
      print "Only 4-digit numbers"
  except ValueError:
    print "No words, only numbers"
