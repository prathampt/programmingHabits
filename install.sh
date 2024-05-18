#!/bin/bash

# Function to install dependencies
install_dependencies() {

    echo "Installing dependencies..."
    sudo apt-get update
    sudo apt-get install -y zenity notify-osd

}

# Function to add scripts to .bashrc
add_to_bashrc() {

    echo "Adding programmingHabits to .bashrc..."

    SCRIPT_DIR="$(dirname "$(realpath "$0")")"
    MAIN_SCRIPT="$SCRIPT_DIR/scripts/main.sh"
    REMINDERS_SCRIPT="$SCRIPT_DIR/scripts/reminders.sh"
    
    # Check if the entries already exist in .bashrc
    if ! grep -q "bash $MAIN_SCRIPT &" ~/.bashrc; then
        echo "bash $MAIN_SCRIPT &" >> ~/.bashrc
    fi

    if ! grep -q "bash $REMINDERS_SCRIPT &" ~/.bashrc; then
        echo "bash $REMINDERS_SCRIPT &" >> ~/.bashrc
    fi

    source ~/.bashrc
}

# Function to set up the project
setup_project() {

    echo "Setting up programmingHabits project..."
    
    # Create the logs directory if it doesn't exist
    mkdir -p logs
    
    # Touch the session log file
    touch logs/session.log

    # Copy the example settings file to the config directory if it doesn't exist
    if [ ! -f config/settings.conf ]; then
        cp config/settings.conf.example config/settings.conf
    fi

    echo "Project setup complete."

}

main() {
  install_dependencies
  setup_project
#   add_to_bashrc

  echo "Installation complete!"
}

main
