from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor
import sys, os

# get the current program
program = currentProgram
decompinterface = DecompInterface()
name = currentProgram.getName()
decompinterface.openProgram(program);
print('[*] Binary Name : '+str(name))

# get all functions recognized
functions = program.getFunctionManager().getFunctions(True)

for function in list(functions):
    print("[*] Function Found : "+str(function))
    # decompile each function
    tokengrp = decompinterface.decompileFunction(function, 0, ConsoleTaskMonitor())
    #print(tokengrp.getDecompiledFunction().getC())
    
    # make directory in advance
    try:
        if not os.path.exists(name):
            os.makedirs(name)
    except OSError:
        print('[!] Error creating directory : '+name)
       
    with open('./'+name+'/'+str(function)+'.c', 'w') as f:
    	f.write(str(tokengrp.getDecompiledFunction().getC()))
