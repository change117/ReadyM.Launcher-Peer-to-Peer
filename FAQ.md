# Frequently Asked Questions (FAQ)

## General Questions

### Q: What is ReadyM.Launcher?
**A:** ReadyM.Launcher is a peer-to-peer game launcher that enables local network (LAN) multiplayer connectivity for games like Black Myth: Wukong without requiring connection to official game servers.

### Q: Is this legal to use?
**A:** This launcher is designed for legitimate use cases such as LAN parties, offline gaming, and educational purposes. Users must own legal copies of games and comply with all applicable terms of service.

### Q: Does this work with pirated games?
**A:** No. This launcher is for legitimate, legally-owned games only. We do not support or condone piracy.

### Q: Is this affiliated with Game Science (Wukong developer)?
**A:** No, this is an independent, community-developed tool not affiliated with or endorsed by Game Science.

---

## Setup and Configuration

### Q: What are the system requirements?
**A:**
- Python 3.7 or higher
- Black Myth: Wukong (legally obtained)
- Local network connection (LAN or WiFi)
- All players must be on the same network

### Q: How do I find my game installation path?
**A:** Common paths:
- **Windows (Epic):** `C:\Program Files\Epic Games\BlackMythWukong\Binaries\Win64\b1-Win64-Shipping.exe`
- **Windows (Steam):** `C:\Program Files (x86)\Steam\steamapps\common\BlackMythWukong\Binaries\Win64\b1-Win64-Shipping.exe`
- **Linux (Steam):** `~/.steam/steam/steamapps/common/BlackMythWukong/Binaries/Linux/b1-Linux-Shipping`

Or use search:
```bash
# Windows (PowerShell)
Get-ChildItem -Path "C:\Program Files" -Recurse -Filter "*wukong*.exe" -ErrorAction SilentlyContinue

# Linux
find ~ -name "*wukong*" -type f 2>/dev/null
```

### Q: Do I need to install any dependencies?
**A:** No external dependencies are required. The launcher uses only Python standard libraries (socket, json, os, etc.).

### Q: Can I use this on macOS?
**A:** Yes, if Python 3.7+ is installed and the game supports macOS. The launcher is cross-platform.

---

## Network and Connectivity

### Q: Do all players need to be on the same WiFi network?
**A:** Yes, all players must be on the same local network (LAN). This includes wired and wireless connections to the same router.

### Q: Can I use this over the internet?
**A:** By default, no. The launcher is configured for LAN-only (`lan_only: true`) for security. Advanced users could potentially configure port forwarding, but this is not recommended and not supported.

### Q: What ports does the launcher use?
**A:** 
- **Discovery Port:** UDP 25565 (configurable)
- **Game Port:** TCP/UDP 27015 (configurable)

### Q: Do I need to forward ports on my router?
**A:** No port forwarding is needed for LAN play. All players are on the local network.

### Q: Can other people on my network see my game session?
**A:** Yes, anyone on the same local network can discover your session. Only allow trusted individuals on your network during play.

---

## Usage

### Q: Do all players need to run the launcher?
**A:** Yes, all players should use the launcher to discover peers and coordinate game launches.

### Q: What's the difference between `--server` and `--discover`?
**A:**
- `--server`: Starts a discovery server that listens for other players (one player runs this)
- `--discover`: Searches for servers on the network (other players run this)

### Q: Can multiple players run `--server` at the same time?
**A:** Yes, but typically only one player needs to host. Multiple servers will create separate sessions.

### Q: How many players can connect?
**A:** The default configuration supports 4 players (`max_players: 4`), but this can be adjusted in `config.json` based on game limitations.

### Q: Do I need to keep the launcher running while playing?
**A:** Yes, it's recommended to keep the launcher running for the best experience, especially if hosting the server.

---

## Troubleshooting

### Q: "Permission denied" or "Operation not permitted" error
**A:** On Linux, network broadcasts may require elevated permissions:
```bash
sudo python3 launcher.py --server
# or
sudo python3 launcher.py --discover
```

### Q: Players can't discover each other
**A:** Common solutions:
1. Ensure all players are on the same network
2. Check firewall settings - UDP port 25565 must be open
3. Verify all players use the same `discovery_port` in config
4. Temporarily disable antivirus/firewall to test
5. Check that server is running before clients try to discover

### Q: "Game executable not found" error
**A:** Solutions:
1. Manually set `game_path` in `config.json`
2. Verify the game is installed
3. Check file permissions
4. Ensure the path is correct and uses proper slashes:
   - Windows: `C:\\Path\\To\\Game.exe` (double backslashes)
   - Linux/Mac: `/path/to/game`

### Q: "Address already in use" error
**A:** Solutions:
1. Change `discovery_port` to a different port (e.g., 25566)
2. Close other applications using port 25565
3. Wait a few minutes for the port to be released
4. Restart your computer

### Q: Game launches but can't connect to other players
**A:** Solutions:
1. Ensure game port (27015) is open in firewall
2. Verify all players have compatible game versions
3. Check that the game supports LAN multiplayer
4. Try restarting both launcher and game
5. Verify all players are on the same network segment

### Q: Peers discovered but show wrong IP addresses
**A:** This may happen if players have multiple network interfaces (WiFi + Ethernet). Ensure all players are using the same network interface.

---

## Configuration

### Q: Can I use different configurations for different scenarios?
**A:** Yes! Use the `--config` parameter:
```bash
python3 launcher.py --config home.json
python3 launcher.py --config lan-party.json
```

### Q: What does `lan_only: true` do?
**A:** It restricts connections to the local network only, preventing external connections for security.

### Q: Can I change my player name after setup?
**A:** Yes:
```bash
python3 launcher.py --player-name "NewName"
```
Or edit `player_name` in `config.json`.

### Q: What happens if I delete config.json?
**A:** The launcher will create a new default configuration file on next run.

---

## Security

### Q: Is my network traffic encrypted?
**A:** The launcher itself doesn't encrypt traffic. For security, we recommend:
- Using LAN-only mode
- Only playing with trusted friends
- Using a secure local network

### Q: Can hackers access my computer through this?
**A:** The launcher only opens necessary ports for local network gaming. Keep `lan_only: true` and only use on trusted networks.

### Q: Should I allow the launcher through my firewall?
**A:** Yes, but only allow local network access, not internet access.

---

## Advanced

### Q: Can I modify the launcher code?
**A:** Yes! The launcher is open-source Python. Feel free to customize it for your needs.

### Q: Can I add support for other games?
**A:** Yes! The launcher can be adapted for other games with LAN multiplayer:
1. Change the `game` field in config
2. Update game paths
3. Adjust ports if needed
4. Modify game launch logic in `launcher.py`

### Q: Can I run multiple game sessions simultaneously?
**A:** Yes, use different port configurations for each session (different `discovery_port` and `game_port`).

### Q: How can I debug connection issues?
**A:** Check logs and network activity:
```bash
# Check if discovery port is listening
sudo netstat -tuln | grep 25565

# Watch network traffic (Linux)
sudo tcpdump -i any port 25565

# Check Python process
ps aux | grep launcher.py
```

### Q: Can I create a GUI version?
**A:** Yes! The launcher could be extended with a GUI using tkinter, PyQt, or similar. Contributions welcome!

---

## Performance

### Q: Does the launcher affect game performance?
**A:** No, the launcher has minimal resource usage and doesn't affect game performance.

### Q: How much bandwidth does P2P use?
**A:** Bandwidth usage depends on the game, not the launcher. The launcher only handles discovery and session setup.

---

## Contributing

### Q: How can I contribute to the project?
**A:** Contributions are welcome! Areas for improvement:
- Bug fixes
- Additional game support
- Enhanced peer discovery
- Better error handling
- GUI development
- Documentation improvements

See the repository for contribution guidelines.

### Q: I found a bug. How do I report it?
**A:** Please open an issue on GitHub with:
- Description of the bug
- Steps to reproduce
- Your operating system and Python version
- Relevant config.json settings
- Error messages or logs

---

## Other Games

### Q: Does this work with games other than Wukong?
**A:** The launcher is designed for Wukong but can potentially be adapted for other games with LAN multiplayer. You would need to:
1. Update game paths
2. Adjust launch parameters
3. Configure appropriate ports
4. Test game-specific requirements

### Q: Will you add support for [other game]?
**A:** We welcome contributions! If you'd like support for another game, feel free to:
- Submit a pull request with the changes
- Open an issue with game details
- Fork the project and create your own version

---

## License and Legal

### Q: What license is this under?
**A:** See the repository for license details. This is provided for educational purposes.

### Q: Can I use this commercially?
**A:** This tool is intended for personal, educational, and non-commercial use.

### Q: Will using this get me banned from the game?
**A:** This launcher facilitates LAN connections and doesn't modify game files or bypass authentication. However, always review and comply with game terms of service. We cannot guarantee how game developers or publishers may respond.

---

## Still Have Questions?

If your question isn't answered here:
1. Check the [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed setup instructions
2. See [EXAMPLES.md](EXAMPLES.md) for usage examples
3. Search existing GitHub issues
4. Open a new issue on GitHub with your question

---

**Last Updated:** 2026-02-18
