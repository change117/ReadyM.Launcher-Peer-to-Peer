# ReadyM.Launcher-Peer-to-Peer

A peer-to-peer game launcher for local network multiplayer, specifically configured for Black Myth: Wukong.

## Quick Start

```bash
# Install Python 3.7+ if needed, then:
python3 launcher.py --setup          # Create configuration
python3 launcher.py --player-name "YourName"  # Set your name
python3 launcher.py --server         # Start as host (one player)
# OR
python3 launcher.py --discover       # Find host (other players)
python3 launcher.py --launch         # Launch the game
```

## Features

- 🎮 **Local Network Gaming** - Play with friends on your LAN
- 🔍 **Auto-Discovery** - Automatically find peers on your network
- ⚙️ **Easy Configuration** - Simple JSON-based setup
- 🚀 **Game Integration** - Launch Wukong directly from the launcher
- 🔒 **LAN Security** - Restricted to local network by default

## What This Does

This launcher enables multiplayer connections between players on the same local network (LAN) without requiring connection to official game servers. Perfect for:
- LAN parties
- Local co-op gaming
- Offline multiplayer sessions
- Network gaming workshops

## Documentation

- **[Complete Setup Guide](SETUP_GUIDE.md)** - Detailed installation and configuration
- **[Configuration Reference](#configuration)** - Settings and options
- **[Troubleshooting](#troubleshooting)** - Common issues and solutions

## Requirements

- Python 3.7 or higher
- Black Myth: Wukong (legally obtained)
- Local network connection (LAN/WiFi)
- All players on the same network

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/change117/ReadyM.Launcher-Peer-to-Peer.git
   cd ReadyM.Launcher-Peer-to-Peer
   ```

2. **Create configuration:**
   ```bash
   python3 launcher.py --setup
   ```

3. **Edit config.json** to set your game path and player name

4. **Start playing!**

## Configuration

Edit `config.json` to customize settings:

```json
{
  "game": "Wukong",
  "game_path": "/path/to/game/executable",
  "discovery_port": 25565,
  "game_port": 27015,
  "player_name": "YourName",
  "lan_only": true,
  "max_players": 4
}
```

## Usage Examples

### Host a Game Session

```bash
python3 launcher.py --server
```

Keep this running - other players will discover your session.

### Join a Game Session

```bash
# Find available sessions
python3 launcher.py --discover

# Launch game to connect
python3 launcher.py --launch
```

### Interactive Mode

```bash
python3 launcher.py
```

Type commands interactively: `discover`, `server`, `launch`, `status`, `help`, `quit`

## Troubleshooting

### Can't Find Game

Set the `game_path` in `config.json` to your game's executable:
- Windows: `C:\Program Files\Epic Games\BlackMythWukong\Binaries\Win64\b1-Win64-Shipping.exe`
- Linux: `~/.steam/steam/steamapps/common/BlackMythWukong/Binaries/Linux/b1-Linux-Shipping`

### Peers Not Found

1. Ensure all players are on the same network
2. Check firewall allows UDP port 25565
3. Try disabling firewall temporarily to test

### Connection Issues

- Open ports in firewall (UDP 25565, TCP/UDP 27015)
- Verify all players have compatible game versions
- Check antivirus isn't blocking connections

See [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed troubleshooting.

## How It Works

1. **Discovery Phase**: Launcher broadcasts UDP packets on LAN to find peers
2. **Connection Phase**: Peers exchange connection information
3. **Game Launch**: Game is launched with appropriate parameters for P2P mode
4. **Play**: Players connect directly to each other (peer-to-peer)

## Security

- **LAN Only**: Default configuration restricts to local network
- **No External Access**: No internet connection required
- **Firewall Friendly**: Uses standard gaming ports
- **Privacy**: No data sent outside your local network

## Legal & Ethical Use

This launcher is for **legitimate, legal use only**:
- ✅ Playing with legally owned game copies
- ✅ Local LAN parties with friends
- ✅ Educational networking projects
- ✅ Offline multiplayer sessions
- ❌ Not for piracy or ToS violations
- ❌ Not for bypassing DRM

**Users are responsible for compliance with all applicable laws and terms of service.**

## Contributing

Contributions welcome! Areas for improvement:
- Additional game support
- Enhanced peer discovery
- Better error handling
- UI improvements
- Documentation

## License

Educational and personal use. See code for details.

## Disclaimer

Not affiliated with or endorsed by Game Science (Black Myth: Wukong developer). Provided as-is for educational purposes. Users responsible for legal compliance.

---

**Ready to play?** See the [Complete Setup Guide](SETUP_GUIDE.md) for step-by-step instructions!
