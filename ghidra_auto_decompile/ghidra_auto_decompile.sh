#!/bin/bash

# Script to automatically decompile and output source code of a binary with ghidra
# Please check your $GHIDRA_PATH

GHIDRA_PATH=~/ghidra_10.1.4_PUBLIC
DECOMPILE_SCRIPT_PATH=.

if [ "$#" -ne  1 ]
then 
    echo "usage : $0 <binary path>"
    exit
fi

echo -e "[*] Path to decompile script: ${DECOMPILE_SCRIPT_PATH}"

echo "running command:"
echo time $GHIDRA_PATH/support/analyzeHeadless . tmp_ghidra_project -import $1  -postscript $DECOMPILE_SCRIPT_PATH/decompile.py
time $GHIDRA_PATH/support/analyzeHeadless . tmp_ghidra_project -import $1  -scriptPath $DECOMPILE_SCRIPT_PATH -postscript decompile.py

# Remove gpr and rep files after (CAREFUL!)
rm -rf *.gpr *.rep

