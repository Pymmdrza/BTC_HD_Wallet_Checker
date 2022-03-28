@Echo off
title INSTALL Mmdrza.Com
Pushd "%~dp0"
:loop
pip install hdwallet colorama lxml requests
start btcHDall.cmd
goto loop