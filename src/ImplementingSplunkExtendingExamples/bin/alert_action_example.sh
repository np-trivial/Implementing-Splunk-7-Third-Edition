#!/bin/sh

DIRPATH=`dirname "$8"`
DIRNAME=`basename "$DIRPATH"`

DESTFILE="$DIRNAME.csv.gz"
cp "$8" /mnt/archive/alert_action_example_output/$DESTFILE

URL="http://mymonitoringsystem.mygreatcompany/open_ticket.cgi"
URL="$URL?name=$4&count=$1&filename=$DESTFILE"
echo Calling $URL
curl -v $URL
