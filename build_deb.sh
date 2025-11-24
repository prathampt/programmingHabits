#!/bin/bash

APP_NAME="programminghabits"
VERSION="1.0.0"
MAINTAINER="Pratham Tandale<prathamt12345@gmail.com>"

set -e # Exit on error

# Dependencies for build
sudo apt-get install -y dpkg gzip

echo "Starting PyInstaller Build for $APP_NAME v$VERSION..."
echo "Cleaning up old builds..."
rm -rf build/ dist/ deb_dist/ *.spec

echo "Compiling Binary..."
uv run pyinstaller --noconsole --onefile \
    --name "$APP_NAME" \
    --add-data "programminghabits/assets/programminghabits.png:assets" \
    --add-data "programminghabits/assets/alert.wav:assets" \
    --hidden-import "dbus.mainloop.glib" \
    --hidden-import "PyQt6.QtMultimedia" \
    --exclude-module "PyQt6.QtQml" \
    --exclude-module "PyQt6.QtQuick" \
    --exclude-module "PyQt6.QtSql" \
    --exclude-module "PyQt6.QtWebEngine" \
    --exclude-module "PyQt6.QtWebEngineCore" \
    --exclude-module "PyQt6.QtWebEngineWidgets" \
    --collect-all "programminghabits" \
    programminghabits/main.py

mkdir -p deb_dist/DEBIAN
mkdir -p deb_dist/usr/bin
mkdir -p deb_dist/usr/share/applications
mkdir -p deb_dist/usr/share/pixmaps
mkdir -p deb_dist/usr/share/doc/$APP_NAME
mkdir -p deb_dist/usr/share/man/man1

cp dist/$APP_NAME deb_dist/usr/bin/
chmod 755 deb_dist/usr/bin/$APP_NAME

cp programminghabits/assets/programminghabits.png deb_dist/usr/share/pixmaps/
chmod 644 deb_dist/usr/share/pixmaps/programminghabits.png

# License
cp LICENSE deb_dist/usr/share/doc/$APP_NAME/copyright
chmod 644 deb_dist/usr/share/doc/$APP_NAME/copyright

cp programminghabits.1 deb_dist/usr/share/man/man1/
chmod 644 deb_dist/usr/share/man/man1/programminghabits.1
gzip -f deb_dist/usr/share/man/man1/programminghabits.1

# Desktop Shortcut
cat > deb_dist/usr/share/applications/$APP_NAME.desktop <<EOF
[Desktop Entry]
Name=programmingHabits
Comment=Productivity timer with health breaks for Linux
Exec=/usr/bin/$APP_NAME
Icon=$APP_NAME
Type=Application
Terminal=false
Categories=Utility;TimeUtility;
Keywords=Pomodoro;Timer;Health;Break;
StartupNotify=true
EOF

cat > deb_dist/DEBIAN/control <<EOF
Package: $APP_NAME
Version: $VERSION
Section: utils
Priority: optional
Architecture: amd64
Maintainer: $MAINTAINER
Depends: libc6, libglib2.0-0, libdbus-1-3, pulseaudio-utils
Description: Programming Habits (Standalone)
 A smart productivity tool that enforces breaks with a full-screen overlay.
 .
 This version is self-contained and includes all necessary dependencies.
EOF

echo "Packaging into .deb..."
dpkg-deb --build deb_dist "${APP_NAME}_${VERSION}_amd64.deb"

rm -rf build/ dist/ deb_dist/ *.spec

echo "Installer created: ${APP_NAME}_${VERSION}_amd64.deb"
