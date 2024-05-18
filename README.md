<p align="center">
  <img src="https://img.icons8.com/?size=512&id=52515&format=png" width="150" />
  
</p>
<p align="center">
    <h1 align="center">programmingHabits</h1>
</p>
<p align="center">
  <img src="https://img.shields.io/github/license/prathampt/programmingHabits?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/prathampt/programmingHabits?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/prathampt/programmingHabits?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/prathampt/programmingHabits?style=flat&color=0080ff" alt="repo-language-count">
</p>
<p align="center">
		<em>Developed with: </em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Bash-4EAA25.svg?style=flat&logo=gnu-bash&logoColor=white" alt="Bash">
</p>
<hr>

## Description
**programmingHabits** is a shell script designed to enhance your productivity by integrating the Pomodoro technique into your daily routine. It provides regular break reminders, allows you to rate your work sessions, and includes additional reminders for drinking water, eating, walking, and reading.

## Inspiration
As a programmer, I often found myself getting so engrossed in coding that I would forget to take breaks, stay hydrated, or even move around. This led to fatigue and decreased productivity over time. Realizing the importance of maintaining good habits and overall health, I decided to create a project that would help programmers like me stay healthy and productive. Thus, **programmingHabits** was born, a tool to remind us to take care of ourselves while we code.


## Features
- **Pomodoro Timer**: Customizable work and break periods.
- **Notifications**: Alerts for breaks and work resumption.
- **Snooze Functionality**: Option to snooze break reminders.
- **Session Rating**: Rate your productivity after each session.
- **Session Analysis**: Analyze your productivity over time.
- **Healthy Reminders**: Regular reminders to drink water, eat, take walks, read books, exercise and many more.

Suggestions are welcome...

## Usage
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/prathampt/programmingHabits
    cd programmingHabits
    ```

2. **Configuration**:
    - Edit the configuration file `config/settings.conf` to customize your session and break times.
    - Default values:
      ```ini
      WORK_TIME=1500  # 25 minutes
      BREAK_TIME=300  # 5 minutes
      ```

3. **Running the Scripts**:
    - Start the main Pomodoro timer script:
      ```bash
      bash scripts/main.sh
      ```
    - Start the additional reminders script:
      ```bash
      bash scripts/reminders.sh
      ```

4. **Add to Startup**:
    - Ensure the scripts run when your system starts by adding the following lines to your `.bashrc` or appropriate startup file:
      ```bash
      echo "bash /path/to/programmingHabits/scripts/main.sh &" >> ~/.bashrc
      echo "bash /path/to/programmingHabits/scripts/reminders.sh &" >> ~/.bashrc
      ```

5. **Session Analysis**:
    - Analyze your session ratings:
      ```bash
      bash scripts/analyze.sh
      ```

## Files and Directories
- `scripts/main.sh`: Main script for the Pomodoro timer.
- `scripts/reminders.sh`: Script for hydration, eating, walking, and reading reminders.
- `scripts/analyze.sh`: Script to analyze session ratings.
- `config/settings.conf`: Configuration file for session and break times.
- `logs/session.log`: Log file for session ratings.

## Technologies Used
- **Bash**: The scripting language used for the entire project.
- **zenity**: A tool for displaying GTK+ dialog boxes from the command line, used for user interaction.
- **notify-send**: A command to send desktop notifications, used for break and reminder alerts.
- **awk**: A programming language used for text processing and session analysis.

## Contribution
Feel free to fork this repository and submit pull requests. Your contributions are welcome!

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/prathampt/programmingHabits
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

## License
This project is licensed under the *GNU GENERAL PUBLIC LICENSE Version 3* - see the [LICENSE](LICENSE) file for details.

### Fork and Star..
Don't forget to fork the repository and give a star if you liked it...
