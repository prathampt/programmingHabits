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
    
    # Check if the entries already exist in .bashrc
    if ! grep -q "bash $(pwd)/scripts/main.sh &" ~/.bashrc; then
        echo >> ~/.bashrc
        echo "bash $(pwd)/scripts/main.sh &" >> ~/.bashrc
    fi
    
    if ! grep -q "bash $(pwd)/scripts/reminders.sh &" ~/.bashrc; then
        echo >> ~/.bashrc
        echo "bash $(pwd)/scripts/reminders.sh &" >> ~/.bashrc
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
