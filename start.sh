#!/bin/bash
# Quick start script for ReadyM.Launcher

echo "ReadyM.Launcher - Quick Start"
echo "=============================="
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.7 or higher"
    exit 1
fi

# Check if config exists
if [ ! -f "config.json" ]; then
    echo "No configuration found. Creating default config..."
    python3 launcher.py --setup
    echo ""
    echo "Please edit config.json to set your game path and player name"
    echo "Then run this script again"
    exit 0
fi

# Display menu
echo "Select an option:"
echo "1) Host a game session (start server)"
echo "2) Join a game session (discover peers)"
echo "3) Launch game"
echo "4) Show status"
echo "5) Change player name"
echo "6) Interactive mode"
echo "7) Exit"
echo ""
read -p "Enter choice [1-7]: " choice

case $choice in
    1)
        echo "Starting discovery server..."
        echo "Press Ctrl+C to stop"
        python3 launcher.py --server
        ;;
    2)
        echo "Searching for peers..."
        python3 launcher.py --discover
        ;;
    3)
        echo "Launching game..."
        python3 launcher.py --launch
        ;;
    4)
        python3 launcher.py --status
        ;;
    5)
        read -p "Enter your player name: " name
        python3 launcher.py --player-name "$name"
        ;;
    6)
        python3 launcher.py
        ;;
    7)
        echo "Goodbye!"
        exit 0
        ;;
    *)
        echo "Invalid choice"
        exit 1
        ;;
esac
