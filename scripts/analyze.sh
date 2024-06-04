#!/bin/bash

LOG_FILE="$(dirname "$(realpath "$0")")/../logs/session.log"

# Check if the log file exists
if [ ! -f "$LOG_FILE" ]; then
    echo "Log file not found: $LOG_FILE"
    exit 1
fi

awk '{
    total += $NF;
    count++;
} END {
    if (count > 0) {
        print "Average Rating: " (total / count);
    } else {
        print "No ratings found in the log file.";
    }
}' ../logs/session.log
