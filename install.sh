#!/bin/bash

SCRIPT_NAME="yaclum"
TARGET_DIR="/usr/local/bin"
SCRIPT_PATH="$(pwd)/main.py"

if [ ! -w "$TARGET_DIR" ]; then
    echo "Error: You don't have permission to write to $TARGET_DIR. Try running this script with sudo."
    exit 1
fi

if [ ! -f "$SCRIPT_PATH" ]; then
    echo "Error: main.py not found in the current directory. Make sure you run this script from the project root."
    exit 1
fi

chmod +x "$SCRIPT_PATH"

echo "Creating symbolic link..."
ln -sf "$SCRIPT_PATH" "$TARGET_DIR/$SCRIPT_NAME"

if [ -L "$TARGET_DIR/$SCRIPT_NAME" ]; then
    echo "Symbolic link created successfully! You can now run the utility using '$SCRIPT_NAME'."
else
    echo "Failed to create symbolic link. Please check your permissions."
    exit 1
fi
