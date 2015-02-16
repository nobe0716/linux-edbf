__author__ = 'nobe0716'
PYTHON_DIRECTORY_PATH='C:\\10_Linux\\linux-2.6.32.9\\linux-2.6.32.9\\drivers\\'

import os
import re

def checker(file):
    #print (file)
    f = open(file, "r")

    target_name = os.path.basename(file).replace('.c', '')
    pos_init = 0
    pos_setup_irq = 0
    pos_register = 0

    try:
        lines = f.readlines()
    except:
        print ( 'exception occurs readline @ ' + file )
    for line_idx in range(0, len(lines)):
        line = lines[line_idx]
        if re.match('void __init .*_init.*', line):
            pos_init = line_idx
           # print('init ' + file + str(line_idx))
        elif re.match('.*setup_irq.*', line):
            pos_setup_irq = line_idx
            #print(file + str(line_idx))
        elif re.match('.*register\(.*', line):
            pos_register = line_idx
            #print(file + str(line_idx))

    if pos_init > 0 and pos_setup_irq > 0 and pos_register > 0:
        if pos_init < pos_setup_irq and pos_setup_irq < pos_register:
            print (file + "\t====(%d, %d, %d" % pos_init % pos_setup_irq % pos_register)
        else:
            print ( 'no bugs at ' + target_name )

for r, d, f in os.walk(PYTHON_DIRECTORY_PATH):
    for file in f:
        if not file.endswith('.c'):
            continue
        checker( os.path.join(r, file) )
        #print( file )
