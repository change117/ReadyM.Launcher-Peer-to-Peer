# Usage Examples for ReadyM.Launcher

## Example 1: Basic LAN Setup (Two Players)

### Setup

**Player 1 (Host):**
```bash
# Terminal 1 - Player 1 becomes the host
cd ReadyM.Launcher-Peer-to-Peer
python3 launcher.py --player-name "Alice"
python3 launcher.py --server
```

**Player 2 (Client):**
```bash
# Terminal 2 - Player 2 joins
cd ReadyM.Launcher-Peer-to-Peer
python3 launcher.py --player-name "Bob"
python3 launcher.py --discover
# Should see: "Found peer: Alice at 192.168.1.100"
python3 launcher.py --launch
```

### Expected Output

Player 1 (Host):
```
Discovery server started on port 25565
Player: Alice
Waiting for peers...
Discovery request from 192.168.1.101
```

Player 2 (Client):
```
Searching for peers...
Found peer: Alice at 192.168.1.100
Found 1 peer(s)
Launching game: /path/to/game/executable
Game launched with PID: 12345
```

---

## Example 2: Four Player LAN Party

### Scenario
Four friends at a LAN party want to play Wukong together.

### Network Setup
```
Router: 192.168.1.1
Alice (Host):   192.168.1.100
Bob:            192.168.1.101
Carol:          192.168.1.102
Dave:           192.168.1.103
```

### Steps

1. **Alice starts the server:**
```bash
python3 launcher.py --player-name "Alice"
python3 launcher.py --server
```

2. **Bob, Carol, and Dave all discover the server:**
```bash
# Bob's terminal
python3 launcher.py --player-name "Bob"
python3 launcher.py --discover

# Carol's terminal
python3 launcher.py --player-name "Carol"
python3 launcher.py --discover

# Dave's terminal
python3 launcher.py --player-name "Dave"
python3 launcher.py --discover
```

3. **Everyone launches the game:**
```bash
python3 launcher.py --launch
```

### Result
All four players can now see each other in-game and connect via P2P.

---

## Example 3: Windows Quick Start

### Using the GUI Script

1. **Double-click `start.bat`**

2. **First-time setup:**
   ```
   No configuration found. Creating default config...
   Please edit config.json to set your game path and player name
   ```

3. **Edit config.json:**
   ```json
   {
     "game_path": "C:\\Program Files\\Epic Games\\BlackMythWukong\\Binaries\\Win64\\b1-Win64-Shipping.exe",
     "player_name": "YourName"
   }
   ```

4. **Run `start.bat` again and choose an option:**
   ```
   Select an option:
   1) Host a game session (start server)
   2) Join a game session (discover peers)
   3) Launch game
   4) Show status
   5) Change player name
   6) Interactive mode
   7) Exit
   
   Enter choice [1-7]: 
   ```

---

## Example 4: Linux Steam Setup

### Configuration for Steam on Linux

1. **Create config:**
```bash
python3 launcher.py --setup
```

2. **Find your Steam installation:**
```bash
find ~/.steam -name "b1-*-Shipping" 2>/dev/null
# Example output: /home/user/.steam/steam/steamapps/common/BlackMythWukong/Binaries/Linux/b1-Linux-Shipping
```

3. **Update config.json:**
```json
{
  "game": "Wukong",
  "game_path": "/home/user/.steam/steam/steamapps/common/BlackMythWukong/Binaries/Linux/b1-Linux-Shipping",
  "player_name": "YourName"
}
```

4. **Start playing:**
```bash
# Host
sudo python3 launcher.py --server

# Join (in another terminal)
python3 launcher.py --discover
python3 launcher.py --launch
```

**Note:** `sudo` may be required for network broadcasts on Linux.

---

## Example 5: Interactive Mode Walkthrough

### Starting Interactive Mode

```bash
python3 launcher.py
```

### Session Example

```
ReadyM.Launcher - P2P Game Launcher
Type 'help' for available commands

=== ReadyM.Launcher Status ===
Game: Wukong
Player: Player1
Discovery Port: 25565
Game Port: 27015
Max Players: 4
LAN Only: True
Game Path: /path/to/game

Known Peers: 0
=============================

> help

Available commands:
  discover  - Find peers on local network
  server    - Start discovery server
  launch    - Launch the game
  status    - Show current status
  config    - Save current configuration
  quit      - Exit launcher

> discover
Searching for peers...
Found peer: Alice at 192.168.1.100
Found peer: Bob at 192.168.1.101

Found 2 peer(s)

> status

=== ReadyM.Launcher Status ===
Game: Wukong
Player: Player1
Discovery Port: 25565
Game Port: 27015
Max Players: 4
LAN Only: True
Game Path: /path/to/game

Known Peers: 2
  - Alice at 192.168.1.100
  - Bob at 192.168.1.101
=============================

> launch
Launching game: /path/to/game
Game launched with PID: 23456

> quit
Goodbye!
```

---

## Example 6: Custom Port Configuration

### Scenario
Default ports are blocked or in use. Need to use custom ports.

### Setup

1. **Edit config.json:**
```json
{
  "game": "Wukong",
  "discovery_port": 35565,
  "game_port": 37015,
  "player_name": "Player1"
}
```

2. **All players must use the same ports:**
   - Copy the config.json to all players
   - Or ensure everyone manually sets the same ports

3. **Open firewall ports:**
   - UDP 35565 (discovery)
   - TCP/UDP 37015 (game)

4. **Start as normal:**
```bash
python3 launcher.py --server
# or
python3 launcher.py --discover
```

---

## Example 7: Multiple Sessions

### Scenario
Multiple groups playing in the same location, need separate sessions.

### Solution: Different Ports for Each Group

**Group A:**
```json
{
  "discovery_port": 25565,
  "game_port": 27015
}
```

**Group B:**
```json
{
  "discovery_port": 26565,
  "game_port": 28015
}
```

Each group operates independently on different ports.

---

## Example 8: Troubleshooting Connection Issues

### Problem: Can't discover peers

**Step 1: Check network connectivity**
```bash
# Ping another player
ping 192.168.1.100
```

**Step 2: Check firewall**
```bash
# Linux - check if port is open
sudo netstat -tuln | grep 25565

# Windows - check firewall rules
netsh advfirewall firewall show rule name=all | findstr 25565
```

**Step 3: Test with firewall disabled (temporarily)**
```bash
# Linux
sudo ufw disable
python3 launcher.py --discover
sudo ufw enable

# Windows - disable in Windows Defender Firewall GUI
```

**Step 4: Verify all players on same network**
```bash
# Check your IP
ip addr show  # Linux
ipconfig      # Windows
```

### Problem: Game won't launch

**Solution: Verify game path**
```bash
python3 launcher.py --status
# Check "Game Path" line

# If not found, manually set in config.json
```

---

## Tips and Best Practices

1. **Always start the server (host) first** before clients try to discover
2. **Use descriptive player names** to identify who is who
3. **Keep launcher running** while playing for continued P2P connectivity
4. **Same game version** - ensure all players have compatible game versions
5. **Local network only** - keep `lan_only: true` for security
6. **Test connectivity** - use `--discover` before launching to verify peers
7. **One server per session** - only one player needs to run `--server`
8. **Firewall configuration** - configure once, works for all sessions

---

## Advanced: Scripting Automation

### Auto-Discovery and Launch Script

```bash
#!/bin/bash
# auto-join.sh

echo "Auto-discovering peers..."
python3 launcher.py --discover

echo "Waiting 2 seconds..."
sleep 2

echo "Launching game..."
python3 launcher.py --launch
```

### Server Startup Script with Monitoring

```bash
#!/bin/bash
# server-monitor.sh

while true; do
    echo "Starting discovery server..."
    python3 launcher.py --server
    
    echo "Server stopped. Restarting in 5 seconds..."
    sleep 5
done
```

Make executable:
```bash
chmod +x auto-join.sh server-monitor.sh
```
