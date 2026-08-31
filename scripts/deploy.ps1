$ErrorActionPreference = 'Stop'
$cli = Get-Command genlayer -ErrorAction SilentlyContinue
if (-not $cli) { $cli = Get-Command genlayer.cmd -ErrorAction SilentlyContinue }
if (-not $cli) { throw 'GenLayer CLI not found. Install it with: npm install -g genlayer' }
& $cli.Source network set studionet
& $cli.Source account show
& $cli.Source deploy --contract contracts/endline.py
