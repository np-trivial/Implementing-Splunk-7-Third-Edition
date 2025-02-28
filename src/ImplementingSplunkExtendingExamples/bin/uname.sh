#!/bin/sh

date "+%Y-%m-%d %H:%M:%S"
echo hardware=\"$(uname -m)\"
echo node=\"$(uname -n)\"
echo proc=\"$(uname -p)\"
echo os_release=\"$(uname -r)\"
echo os_name=\"$(uname -s)\"
echo os_version=\"$(uname -v)\"
