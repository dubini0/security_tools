# Ghidra Auto Decompiler 

This is a bash/python script for automatically decompiling binary with Ghidra.

Ghidra can be downloaded from https://ghidra-sre.org/

This uses `analyzeHeadless` from Ghidra, and saves decompiled code and information from Ghidra.



## Usage

>  Note: You will need to modify GHIDRA_PATH variable in the script before running it.

### Example
```
./ghidra_auto_decompile.sh ~/path/to/binary_file
```



## Todos

- ~~Modify bash script for multiple files~~ [CANCELED]
- ~~Exclude basic functions (ex. frame_dummy, register_tm_clones, etc..)~~ [DONE]
- ~~Make Python script prettier...~~ [DONE]
- ~~Turn output into a JSON file~~ [DONE]
- Fix problems with txt -> json
