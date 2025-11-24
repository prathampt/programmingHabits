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
<img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Qt-41CD52?style=flat&logo=qt&logoColor=white" alt="Qt">
</p>
<p align="center">
<em>Developed for: </em>
</p>
<p align="center">
<img src="https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black" alt="Linux">
</p>
<hr>

## Description
**programmingHabits** is a native Linux productivity tool designed to integrate the Pomodoro technique into your desktop environment. Unlike simple timers, it enforces healthy habits by taking over your screen during breaks, ensuring you actually stop working to stretch, hydrate, and rest your eyes. It is built to look and feel like a native part of your Desktop Environment.

## Inspiration
As a programmer, I often found myself getting so engrossed in coding that I would forget to take breaks, stay hydrated, or even move around. This led to fatigue and a decline in productivity over time. Realising the importance of maintaining good habits and overall health, I decided to create a project that would help programmers like me stay healthy and productive. Thus, **programmingHabits** was born, a tool to remind us to take care of ourselves while we code.

## Features

- **Smart Pomodoro Timer:** Customizable work and break intervals stored permanently.
- **Enforced Breaks:** A full-screen, semi-transparent overlay blocks the screen, gently forcing you to step away.
- **Native Theme Integration:** Automatically detects your Linux Desktop theme and adapts the UI to match it perfectly.
- **Smart Media Control:** Automatically pauses Spotify, YouTube, or any media player when a break starts (via DBus).
- **Health & Wisdom:** Displays curated health tips and programming wisdom during breaks.
- **System Tray Control:** Manage the timer, access settings, or quit the app directly from your system tray.
- **Audio Alerts:** Gentle chimes to signal the start and end of breaks (supports native system audio).

## Installation

### Option 1 (Recommended): Install via APT (Ubuntu/Debian/Mint)

1.  **Make sure you have dependencies:**
    ```bash
    sudo apt install dbus
    ```

2.  **Add the Repository Key:**
    ```bash
    curl -fsSL https://prathampt.github.io/programmingHabits/KEY.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/programminghabits.gpg
    ```

3.  **Add the Repository:**
    ```bash
    echo "deb [signed-by=/etc/apt/trusted.gpg.d/programminghabits.gpg] https://prathampt.github.io/programmingHabits/ /" | sudo tee /etc/apt/sources.list.d/programminghabits.list
    ```

4.  **Install:**
    ```bash
    sudo apt update
    sudo apt install programminghabits
    ```

### Option 2: Build from Source
If you want to contribute or build it manually:

1.  **Make sure you have dependencies:**
    ```bash
    sudo apt install dbus
    ```

2. **Clone the Repository**:
    ```bash
    git clone https://github.com/prathampt/programmingHabits
    cd programmingHabits
    ```

3. **Install Dependencies** (Using `uv` is recommended):
    ```bash
    uv sync
    ```

4. **Run in Dev Mode**:
    ```bash
    uv run python -m programminghabits.main
    ```

5. **Compile to .deb**:
    Run the included build script to generate a standalone Debian package using PyInstaller:
    ```bash
    chmod +x build_deb.sh
    ./build_deb.sh
    ```

## Architecture & Configuration

### Directory Structure
The project is modularized for maintainability and scalability:

- `programminghabits/main.py`: Entry point. Handles System Tray, Theme detection, and application lifecycle.
- `programminghabits/ui_overlay.py`: Logic for the full-screen break window and media pausing.
- `programminghabits/ui_settings.py`: The GUI for configuring time and preferences.
- `programminghabits/config.py`: Handles saving/loading JSON settings to `~/.config/`.
- `programminghabits/utils.py`: Resource path management for compiled binaries.
- `programminghabits/assets/`: Stores icons and sound files.

### Configuration
The settings are stored in JSON format at:
`~/.config/programminghabits/config.json`

You can edit this file manually or use the **Settings GUI** via the System Tray icon to:
- Enable/Disable the timer.
- Change Work/Break duration.
- Add your own custom motivational quotes.

## Technologies Used
- **Python 3**: The core logic language.
- **PyQt6**: For a robust, cross-platform Graphical User Interface.
- **DBus**: For communicating with Linux media players (Spotify/YouTube).
- **Subprocess**: For detecting GNOME/GTK system themes and colors.
- **PyInstaller**: For compiling the Python code into a standalone binary.
- **Debian Packaging**: For native installation support.

## Contribution
Feel free to fork this repository and submit pull requests. Your contributions are welcome!

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b feature/amazing-feature
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented amazing feature.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin feature/amazing-feature
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

</details>

## License
This project is licensed under the *GNU GENERAL PUBLIC LICENSE Version 3* - see the [LICENSE](LICENSE) file for details.

### Fork and Star
Don't forget to fork the repository and give a star if you find it useful! Happy Coding & Stay Healthy.
