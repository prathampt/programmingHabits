#!/bin/bash

while true; do

    sleep 3600  # Every hour
    notify-send "Time to drink water!"
    sleep 7200  # Every two hours
    notify-send "Time to eat something!"
    sleep 10800 # Every three hours
    notify-send "Time to take a walk!"
    sleep 86400 # Every day
    notify-send "Did you read a book today?"
    
done
