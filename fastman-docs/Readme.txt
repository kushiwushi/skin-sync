***** fastman92 IMG Console 1.5 by fastman92

This open-source tool, easy to use IMG Console allows to create/modify GTA IMG archives with simplicity.
And two modes are available: interactive mode and script mode.
In interactive mode you can type commands from keyboard and execute in command prompt.
Script mode will be useful for modders who want to create automatic modification of IMG archives and depends on script file.
An application works with more one version of IMG archives:

• version 1 (GTA III, GTA VC, GTA III Mobile)
• version 2 (GTA SA)

IMG archive of max 8 terabytes is supported.
- - - - - - -  - - - - - - - - - -

***** Usage (after you installed mod)
• To run application in interactive mode just run fastman92ImgConsole.exe without any parameters.
• Type -help to get list of available commands.
• It's also possible to run script by specifying additional parameter as in example:
  fastman92ImgConsole.exe -script "myScript.txt"
  
***** Script syntax:
Each command is preceeded by '-' (dash)
Empty lines will be skipped.
// is used to comment line.

**** Example of script:
-open "test.img"
// -import "test.txt"
-import "my.txt"

-rename "my.txt" "look.txt"
-close
  
***** IMG limits:
128 MB - max filesize
8 TB - max .img archive size

IMG class used in tool can reach these limits with no errors.
  
**** Note:
C++ programmers may take (GTASA_CRC32.h, GTASA_CRC32.cpp, IMG.h and IMG.cpp) and use these files in newly compiled programs.

**** Changelog
** 1.5
- fixed error with offsets occuring when there existed files of 0 length in IMG archive
- fixed crashing when command name was unexpectedly too long (buffer overflow)
- fixed comments, they work now, use // two slashes at the beginning of line
- added new command: -importFromDirectory "path\\to\\directory"
- added new command: -getAmountOfUnusedSpace
It imports all files from specified directory.

** 1.4
- fixed export command, second argument is directory path now.

** 1.3
- delete & rename commands crashed a console when specified file in IMG archive did not exist. Fixed.

** 1.2
- export command crashed a console when specified file in IMG archive did not exist. Fixed.

** 1.1:
- added -rebuild and -rebuildifmoreuselessspacethan commands
- added line numbers in script mode
- comments were introduced and require two slashes //
- empty lines in script file are being skipped now
- fixed RebuildArchive function in IMG class
- fixed GetSizeOfUnusedSpace function in IMG class

**** Thanks to:
Function-X for creating EXE icon.
seggaeman for noticing error in help, unneccessary dashes before strings.

Copyright (c) 2012, fastman92
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

***** Informations:
Date of release: 07-10-2012
Author: fastman92
Version: 1.5
For: GTA San Andreas
E-mail: fastman92@gmail.com
Visit fastman92-site.tk