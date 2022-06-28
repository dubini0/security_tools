# Ghidra Auto Decompiler 

This is a bash/python script for automatically decompiling binary with Ghidra.

Ghidra can be downloaded from https://ghidra-sre.org/

This uses `analyzeHeadless` from Ghidra, and saves all recongizable code from Ghidra.



## Usage

>  Note: You will need to modify GHIDRA_PATH variable in the script before running it.

### Example
```
./ghidra_auto_decompile.sh ~/path/to/binary_file
```



## Todos

- Modify bash script for multiple files
- Exclude basic functions (ex. frame_dummy, register_tm_clones, etc..)
- Make Python script prettier...
