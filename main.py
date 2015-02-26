__author__ = 'nobe0716'
#PYTHON_DIRECTORY_PATH='C:\\10_Linux\\linux-2.6.32.9\\linux-2.6.32.9\\drivers\\clocksource'
#PYTHON_DIRECTORY_PATH='C:\\10_Linux\\linux-2.6.32.9\\linux-2.6.32.9\\drivers\\'


PYTHON_DIRECTORY_PATH='C:\\10_Linux\\linux-3.19\\linux-3.19'
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
        # print ('read lines ' + file)
    except:
        #print ( 'exception occurs readline @ ' + file )
        return None
    for line_idx in range(0, len(lines)):
        line = lines[line_idx]


        if re.match('^.*setup_irq.*;$', line):
            pos_setup_irq = line_idx + 1
        elif re.match('^.*_register\(.*;$', line):
            pos_register = line_idx + 1

    if pos_setup_irq > 0 and pos_register > 0:
        if pos_setup_irq < pos_register:

            print ("[%-20s\t====[ %d, %d ]" % (os.path.basename(file), pos_setup_irq, pos_register) )

    f.close();

for r, d, f in os.walk(PYTHON_DIRECTORY_PATH):
    for file in f:
        if not file.endswith('.c'):
            continue
        checker( os.path.join(r, file) )
        #print( file )
