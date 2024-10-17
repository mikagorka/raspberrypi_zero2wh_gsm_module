#!/bin/bash

# Default values for variables
number=""
message=""
time=""

# Function to display usage/help message
usage() {
    echo "Usage: $0 --number <number> --message <message> --time <time>"
    exit 1
}

# Function to convert date format
convert_time_format() {
    local input_time="$1"
    # Remove the dot after the day and rearrange
    formatted_time=$(echo "$input_time" | sed -E 's/^([0-9]{1,2})\. ([A-Za-z]{3}) ([0-9]{4}) at ([0-9]+:[0-9]+)$/\4 \1 \2 \3/')
    echo "$formatted_time"
}

# Parse command-line options using a while loop
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --number)   # Option for number
            number="$2"
            shift 2
            ;;
        --message)  # Option for message
            message="$2"
            shift 2
            ;;
        --time)     # Option for time
            time="$2"
            shift 2
            ;;
        --user)     # Option for user
            user="$2"
            shift 2
            ;;
        *)          # If unknown option or wrong usage, show usage
            echo "Unknown parameter: $1"
            usage
            ;;
    esac
done

# Check if all required arguments are provided
if [[ -z "$number" || -z "$message" || -z "$time" ]]; then
    echo "Error: Missing required arguments."
    usage
fi

number_plus="+49$number"

# Check time format without using regex
if [[ "$time" == *" at "* ]] && [[ "$time" == *"."* ]]; then
    time=$(convert_time_format "$time")
else
    echo "Error: Time format must be 'DD. Mon YYYY at HH:MM'."
    exit 1
fi

# Der Befehl, der an 'at' übergeben wird
command="python3 github/raspberrypi_zero2wh_gsm_module/scripts/module_scripts/send_sms.py \"$number_plus\" \"$message\""

# Den Befehl über 'at' ausführen
echo "$command" | at "$time"
