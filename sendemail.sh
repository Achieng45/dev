#!/bin/bash

TO=""
SUBJECT="Test Email"
BODY="Graduate trainee first email"

{
	  echo "Subject:$SUBJECT"
	    echo ""
	      echo "$BODY"
     
} | /usr/sbin/ssmtp "$TO"
