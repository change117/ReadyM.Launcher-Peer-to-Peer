# ReadyM.Launcher - Peer-to-Peer Setup Guide

## Overview

ReadyM.Launcher is a peer-to-peer game launcher that enables local network multiplayer connectivity for games like Black Myth: Wukong. This launcher allows you to play with friends on your local network (LAN) without requiring connection to official game servers.

## Features

- **Local Network Discovery**: Automatically find other players on your LAN
- **Peer-to-Peer Connectivity**: Direct connection between players
- **Game Launch Management**: Easily launch games with custom parameters
- **Configurable Settings**: Customize ports, player names, and game paths
- **Cross-Platform Support**: Works on Windows, Linux, and macOS

## Requirements

- Python 3.7 or higher
- Black Myth: Wukong installed on your system
- Local network connection (LAN or WiFi)
- All players must be on the same network

## Installation

### Step 1: Clone or Download

Clone this repository or download the files to your computer:

```bash
git clone https://github.com/change117/ReadyM.Launcher-Peer-to-Peer.git
cd ReadyM.Launcher-Peer-to-Peer
```

### Step 2: Install Python (if not already installed)

Download and install Python 3.7+ from [python.org](https://www.python.org/downloads/)

### Step 3: Verify Installation

```bash
python3 --version
# or on Windows:
python --version
```

## Configuration

### Initial Setup

1. Create the default configuration file:

```bash
python3 launcher.py --setup
```

This creates a `config.json` file with default settings.

2. Edit `config.json` to set your game path:

```json
{
  "game": "Wukong",
  "game_path": "C:\\Program Files\\Epic Games\\BlackMythWukong\\Binaries\\Win64\\b1-Win64-Shipping.exe",
  "discovery_port": 25565,
  "game_port": 27015,
  "player_name": "YourName",
  "lan_only": true,
  "max_players": 4
}
```

### Configuration Options

| Option | Description | Default |
|--------|-------------|---------|
| `game` | Game identifier | "Wukong" |
| `game_path` | Full path to game executable | "" (auto-detect) |
| `discovery_port` | UDP port for peer discovery | 25565 |
| `game_port` | Port for game connections | 27015 |
| `player_name` | Your display name | "Player1" |
| `lan_only` | Restrict to LAN only | true |
| `max_players` | Maximum players in session | 4 |

## Usage

### Quick Start

The launcher supports both command-line and interactive modes.

#### Command-Line Mode

```bash
# Create configuration
python3 launcher.py --setup

# Set your player name
python3 launcher.py --player-name "YourName"

# Show current status
python3 launcher.py --status

# Discover peers on network
python3 launcher.py --discover

# Start discovery server (one player should run this)
python3 launcher.py --server

# Launch the game
python3 launcher.py --launch
```

#### Interactive Mode

Run without arguments for interactive mode:

```bash
python3 launcher.py
```

Available commands in interactive mode:
- `help` - Show available commands
- `discover` - Find peers on local network
- `server` - Start discovery server
- `launch` - Launch the game
- `status` - Show current status
- `config` - Save current configuration
- `quit` - Exit launcher

### Setting Up Multiplayer

#### Host (Server) Player:

1. Start the discovery server:
```bash
python3 launcher.py --server
```

2. Keep this running while others connect

#### Client Players:

1. Discover the host:
```bash
python3 launcher.py --discover
```

2. You should see the host's name and IP address

3. Launch the game:
```bash
python3 launcher.py --launch
```

## Wukong-Specific Setup

### Finding the Game Executable

The launcher will automatically search common installation paths:

**Windows (Epic Games Store):**
```
C:\Program Files\Epic Games\BlackMythWukong\Binaries\Win64\b1-Win64-Shipping.exe
```

**Windows (Steam):**
```
C:\Program Files (x86)\Steam\steamapps\common\BlackMythWukong\Binaries\Win64\b1-Win64-Shipping.exe
```

**Linux (Steam):**
```
~/.steam/steam/steamapps/common/BlackMythWukong/Binaries/Linux/b1-Linux-Shipping
```

If auto-detection fails, manually set the path in `config.json`.

### Game Launch Parameters

You can customize how the game launches by editing the launcher script or passing arguments through the configuration.

## Troubleshooting

### Peers Not Discovered

**Problem:** Discovery doesn't find other players

**Solutions:**
1. Ensure all players are on the same network
2. Check firewall settings - UDP port 25565 must be open
3. Try disabling antivirus/firewall temporarily to test
4. Make sure all players are running the same launcher version

### Game Won't Launch

**Problem:** Launcher can't find or launch the game

**Solutions:**
1. Verify game is installed
2. Set `game_path` manually in `config.json`
3. Check file permissions
4. Run launcher as administrator (Windows) or with sudo (Linux)

### Connection Issues

**Problem:** Can discover peers but can't connect in-game

**Solutions:**
1. Ensure game port (27015) is open in firewall
2. Check game supports LAN multiplayer
3. Verify all players have compatible game versions
4. Try restarting both launcher and game

### Port Already in Use

**Problem:** "Address already in use" error

**Solutions:**
1. Change `discovery_port` in config.json to different port
2. Close other applications using the same port
3. Wait a few minutes for port to be released

## Security Considerations

### LAN Only Mode

By default, the launcher operates in LAN-only mode for security:
- Restricts connections to local network only
- No external internet connectivity required
- Reduces risk of unauthorized access

### Firewall Configuration

Configure your firewall to allow:
- UDP port 25565 (or your configured discovery_port) - for peer discovery
- TCP/UDP port 27015 (or your configured game_port) - for game traffic

### Best Practices

1. **Keep lan_only enabled** unless you specifically need external connections
2. **Use strong player names** - avoid sharing personal information
3. **Only play with trusted friends** on your local network
4. **Keep your game updated** to the latest version
5. **Regular security updates** - update Python and dependencies

## Advanced Usage

### Custom Ports

If default ports conflict with other applications:

```json
{
  "discovery_port": 35565,
  "game_port": 37015
}
```

All players must use the same ports.

### Multiple Game Profiles

Create multiple configuration files for different setups:

```bash
# Profile for home network
python3 launcher.py --config home-config.json

# Profile for LAN party
python3 launcher.py --config lan-party-config.json
```

### Scripting and Automation

The launcher can be integrated into scripts:

```bash
#!/bin/bash
# Auto-discover and launch
python3 launcher.py --discover
sleep 2
python3 launcher.py --launch
```

## Limitations

- **LAN Only**: This launcher is designed for local network play only
- **Game Support**: Requires game to support LAN multiplayer mode
- **No Matchmaking**: Manual peer discovery required
- **Same Network**: All players must be on same local network
- **Compatible Versions**: All players need same game version

## Legal Notice

This launcher is provided for educational purposes and legitimate use cases such as:
- Local LAN parties
- Offline gaming sessions
- Game preservation when official servers shut down
- Educational networking projects

**Important:**
- Only use with legally obtained copies of games
- Respect game developers' terms of service
- This tool does not bypass DRM or enable piracy
- Not affiliated with or endorsed by Game Science (Wukong developer)

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for:
- Bug fixes
- Feature improvements
- Documentation updates
- Additional game support

## License

This project is provided as-is for educational purposes.

## Support

For issues, questions, or suggestions:
1. Check the Troubleshooting section above
2. Search existing GitHub issues
3. Open a new issue with detailed information

## Changelog

### Version 1.0.0 (Current)
- Initial release
- Basic P2P discovery functionality
- LAN peer discovery
- Game launch integration
- Wukong game support
- Cross-platform compatibility

---

**Disclaimer:** This software is provided for educational and legitimate networking purposes only. Users are responsible for complying with all applicable laws and terms of service.
