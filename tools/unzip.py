#!/usr/bin/python
import zipfile, sys, os, errno

def mkdir_p(path):
  try:
    os.makedirs(path)
  except OSError as exc: # Python >2.5
    if exc.errno == errno.EEXIST and os.path.isdir(path):
      pass
    else: raise


zfile = zipfile.ZipFile(sys.argv[1],'r')
# if len(sys.argv) >=3:
#   encoding = sys.argv[2]
# else:
encoding = "GBK"

for filename in zfile.namelist():
  data = zfile.read(filename)
  w_filename = filename.decode(encoding)
  if w_filename.endswith('/'):
    continue
  print w_filename
  dir_name = os.path.dirname(w_filename)
  if not os.path.isdir(dir_name):
    mkdir_p(dir_name)

  file = open(w_filename, 'w+b')
  file.write(data)
  file.close()
zfile.close()
