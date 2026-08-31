$ErrorActionPreference = 'Stop'
$cli = 'C:\Users\ojiku\AppData\Roaming\npm\genlayer.cmd'
& $cli network set studionet
& $cli account show
& $cli deploy --contract contracts/endline.py
