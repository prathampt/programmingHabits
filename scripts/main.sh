#!/bin/bash

SCRIPT_DIR="$(dirname "$(realpath "$0")")"
CONFIG_FILE="$SCRIPT_DIR/../config/settings.conf"

load_config() {
    source $CONFIG_FILE
}

load_config

while true; do

    sleep $WORK_TIME
    notify-send "Time to take a break!" # For normal notification
    # For interactive notification...
    response=$(zenity --question --text="Time to take a break!" --ok-label="Take Break" --cancel-label="Snooze" 2> /dev/null)

    if [ $? -eq 0 ]; then
        sleep $BREAK_TIME
        notify-send "Break over, back to work!"
        zenity --info --text="Break over, back to work!" 2> /dev/null
        rating=$(zenity --scale --text="Rate this session:" --min-value=1 --max-value=5 --value=3 2> /dev/null)
        echo "$(date): $rating" >> $SCRIPT_DIR/../logs/session.log
    else
        sleep $SNOOZE_TIME
    fi

    # Reload configuration at every break to apply changes in the config file
    load_config
done