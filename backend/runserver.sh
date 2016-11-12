#!/bin/bash

if [ -n "$1" ]
then
    port="$1"
else
    port=8080
fi
exec ./manage.py runserver 0.0.0.0:"$port"