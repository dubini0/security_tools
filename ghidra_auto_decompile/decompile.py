from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor
import sys, os

linker_inserted_fns = [ '_start', 'deregister_tm_clones', 'register_tm_clones',
  '__do_global_dtors_aux', 'frame_dummy', '__libc_csu_init', '__libc_csu_fini',
  '_fini', '_init', '__gmon_start__']
filter_list = ['<EXTERNAL>::', '_ITM_']

# get the current program
program = currentProgram
decompinterface = DecompInterface()
name = currentProgram.getName()
decompinterface.openProgram(program);
print('[*] Binary Name : '+str(name))

# get all functions recognized
functions = program.getFunctionManager().getFunctions(True)

for function in list(functions):
    # exclude linker inserted functions
    if any((x in str(function)) for x in filter_list):
        continue
    if str(function) in linker_inserted_fns:
        continue
        
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
