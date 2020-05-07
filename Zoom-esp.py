#python 2.7.6
# -*- encoding: utf-8 -*-
import re, time
filename = "client.dll"


def find_fuc():
  with open(filename, mode='rb') as r:
      strings = re.findall('Maximum visible distance\x00\x00\x00\x00\d{4}', r.read())
      def_cam = ''.join(strings)[28:32]
      return def_cam



def changer_cam():
  with open (filename, mode ='rb') as s:
    file_read = s.read() 
  with open(filename, mode='rb+') as outfile:
    res = re.compile('Maximum visible distance\x00\x00\x00\x00\d{4}')
    cam = res.sub('Maximum visible distance\x00\x00\x00\x00'+ (str(num_cam)), file_read)
    outfile.write(cam)


def edit():
  global num_cam
  print "Zoom actual", find_fuc()
  a=u"Escriba un número de 4 dígitos en el rango 1200 a 1800"
  print a
  print "Zoom recomendado 1666"
  while True:
    try:
      num_cam = int(raw_input())
      if len(str(num_cam)) == 4 and num_cam <= 1900 and num_cam >=1200:
        changer_cam()
        print "Completo""\n", "Tu nuevo zoom es:", find_fuc()
        time.sleep(3)
        exit()
      else:
        b=u"Solo números de 4 dígitos"
        print b
    except ValueError:
      c=u"Sin palabras, solo números" 
      print c

edit()
