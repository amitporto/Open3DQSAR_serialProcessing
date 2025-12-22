from subprocess import Popen, PIPE, STDOUT
import os
import glob
import sys


def ffd_match_line (match_text,infilename):
    x=[]
    #match_text='r2(pred)'
    with open(infilename, 'r') as f:
         lines = f.readlines()
         for i, line in enumerate(lines):
             if match_text in line:
                x.append(lines[i:i+8])
    return x

path=sys.argv[1]
#path='C:\open3dtools\open3dqsar\example\MM\ismail_androgen'
safe_path = path.encode('unicode_escape').decode()
ls=safe_path.split('\\\\')
newpath="\\".join(str(n) for n in ls)
os.path.join(newpath)
print(newpath)
l = glob.glob(newpath+'\\*.txt')

for e in l:
    print(e)
    file_name = e.split("\\")[-1]
    fname = file_name.split(".")[0]
    outfile = os.path.join(newpath, fname + "_log.txt")
    print('processing '+fname)
    cmd = "open3DQSAR.exe -i " + e + " -o " + outfile
    proc = Popen(cmd, shell=True, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    stdout, _ = proc.communicate()
    print(stdout.decode("utf-8", errors="ignore"))

import glob
files=glob.glob(newpath+'\\'+'*_log.txt')


fl=[]
print(newpath)
with open(newpath+'\\'+'Summary_FFDSEL_results.txt', 'w') as f:
     for file in files:
          f.write(file.split('.')[0]+'_results \n')
          y=ffd_match_line('Average q2',file)
          x=ffd_match_line('r2(pred)',file)
          for item1 in y[1]:
             f.write(item1)
          for item2 in x[1]:
             f.write(item2)
          f.write('\n')       
             #f.write(item2)
    #fl.append(x[1])

with open(newpath+'\\'+'Summary_UVEPLS_results.txt', 'w') as f:
     for file in files:
          f.write(file.split('.')[0]+'_results \n')
          y=ffd_match_line('Average q2',file)
          x=ffd_match_line('r2(pred)',file)
          for item1 in y[2]:
             f.write(item1)
          for item2 in x[2]:
             f.write(item2)
          f.write('\n')       
             #f.write(item2)
    #fl.append(x[1])