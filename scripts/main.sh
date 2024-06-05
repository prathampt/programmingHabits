#!/bin/bash

SCRIPT_DIR="$(dirname "$(realpath "$0")")"
CONFIG_FILE="$SCRIPT_DIR/../config/settings.conf"

load_config() {
    source "$CONFIG_FILE"
}

save_config() {
    echo "WORK_TIME=$WORK_TIME" > "$CONFIG_FILE"
    echo "BREAK_TIME=$BREAK_TIME" >> "$CONFIG_FILE"
    echo "SNOOZE_TIME=$SNOOZE_TIME" >> "$CONFIG_FILE"
}

change_config() {
    config_input=$(zenity --forms --title="Change Configuration" \
        --text="Enter the new config options." \
        --add-entry="Work Time (seconds)" \
        --add-entry="Break Time (seconds)" \
        --add-entry="Snooze Time (seconds)" \
        --separator="," \
        --forms-date-format="%s" \
         2> /dev/null)
    
    if [ $? -eq 0 ]; then
        IFS=',' read -r WORK_TIME BREAK_TIME SNOOZE_TIME <<< "$config_input"
        save_config
        load_config
    fi
}

# Check for command-line arguments
if [[ "$1" == "--config" ]]; then
    change_config
    exit 0
fi

load_config

while true; do
    # Sleep for the configured work time
    sleep $WORK_TIME

    # Notify the user to take a break
    notify-send "Time to take a break!"

    # Interactive notification
    response=$(zenity --question --text="Time to take a break!" --ok-label="Take Break" --cancel-label="Snooze" 2> /dev/null)

    if [ $? -eq 0 ]; then
        # User chooses to take a break
        sleep $BREAK_TIME
        notify-send "Break over, back to work!"
        zenity --info --text="Break over, back to work!" 2> /dev/null

        # Get user rating for the session
        rating=$(zenity --scale --text="Rate this session:" --min-value=1 --max-value=5 --value=3 2> /dev/null)
        echo "$(date): $rating" >> "$SCRIPT_DIR/../logs/session.log"
    else
        # User chooses to snooze
        sleep $SNOOZE_TIME
    fi

    # Reload the config
    load_config
done
