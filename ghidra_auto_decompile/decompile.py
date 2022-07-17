from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor
import sys, os, json

ignore_func = [ '_start', 'deregister_tm_clones', 'register_tm_clones',
  '__do_global_dtors_aux', 'frame_dummy', '__libc_csu_init', '__libc_csu_fini',
  '_fini', '_init', '__gmon_start__']
filter_list = ['<EXTERNAL>::', '_ITM_']

def init():
    # get the current program
    program = currentProgram
    decompinterface = DecompInterface()
    name = program.getName()
    decompinterface.openProgram(program);
    print('[*] Binary Name : '+str(name))

    return [program, decompinterface, name]

def get_func_info(program, decompinterface, name, file_data):
    # get all functions recognized
    functions = program.getFunctionManager().getFunctions(True)
    file_data["funcInfo"] = list()

    for function in list(functions):
        # exclude linker inserted functions
        if any((x in str(function)) for x in filter_list):
            continue
        if str(function) in ignore_func:
            continue
            
        print("[*] Function Found : "+str(function))
        # decompile each function
        tokengrp = decompinterface.decompileFunction(function, 0, ConsoleTaskMonitor())
        entrypoint = function.getEntryPoint()
        # c_code : <type 'unicode'>
        c_code = tokengrp.getDecompiledFunction().getC()
        func_dict = {"funcName": str(function), "funcStartAddr": str(entrypoint), "decompiledFuncCode": str(c_code)}
        file_data["funcInfo"].append(func_dict)
        
    return file_data

def dict_to_txt(name, file_data):
    #print(json.dumps(file_data, ensure_ascii=False, indent='\t'))
    filename = './results/'+name+'.txt'
    with open(filename, 'w') as f:
        #json.dump(file_data, f, ensure_ascii=False)
        f.write(str(file_data))
    print("[*] Done writing in "+filename)

if __name__ == "__main__":
    info = init()
    program, decompinterface, name = info[0], info[1], info[2]
    file_data = {"isStripped": "True", "decompilerName": "Ghidra", "compilerName": "gcc", "optLevel": "-O", "binaryName": str(name)}
    
    file_data = get_func_info(program, decompinterface, name, file_data)
    #print(file_data)
    dict_to_txt(str(name), file_data)
