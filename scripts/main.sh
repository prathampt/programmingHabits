#!/bin/bash

source ../config/settings.conf

while true; do

    sleep $WORK_TIME
    notify-send "Time to take a break!" # For normal notification
    # For interactive notification...
    response=$(zenity --question --text="Time to take a break!" --ok-label="Take Break" --cancel-label="Snooze") 

    if [ $? -eq 0 ]; then
        sleep $BREAK_TIME
        notify-send "Break over, back to work!"
        zenity --info --text="Break over, back to work!"
        rating=$(zenity --scale --text="Rate this session:" --min-value=1 --max-value=5 --value=3)
        echo "$(date): $rating" >> ../logs/session.log
    else
        sleep $SNOOZE_TIME 
    fi
done
