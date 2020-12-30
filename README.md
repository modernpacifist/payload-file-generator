# payload-generator
A small command line interface script for generation of payload sequences/files with payload sequences with NOP slides of arbitrary length and your custom payload strings/shellcode.
This script is mainly aimed at buffer overflow/stack smashing vulnerabilities and therefore provides easy-to-use format for generating specific payloads.

Usage:
```
$ ./payload-generator.py --length <NOP_SLIDE_LENGTH> --payload <PLAIN_TEXT>[--shellcode <SHELLCODE>] --filename <FILENAME>
```
