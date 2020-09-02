#!/bin/bash

if [ $# -eq 0 ]; then
  read -p "input mysql password > " pd
else
  password=$1 
fi

export MYSQL_ROOT_PASSWD=$pd

echo $pd
