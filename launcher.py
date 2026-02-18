#!/usr/bin/env python3
"""
ReadyM.Launcher - Peer-to-Peer Game Launcher
Enables local network multiplayer connectivity for supported games.
"""

import os
import sys
import json
import socket
import threading
import argparse
from pathlib import Path
from typing import Dict, List, Optional

class P2PLauncher:
    """Main launcher class for peer-to-peer game connectivity."""
    
    def __init__(self, config_path: Optional[str] = None):
        """Initialize the launcher with configuration."""
        self.config_path = config_path or "config.json"
        self.config = self.load_config()
        self.peers: List[Dict] = []
        self.server_socket: Optional[socket.socket] = None
        
    def load_config(self) -> Dict:
        """Load configuration from file or create default."""
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                return json.load(f)
        else:
            return self.create_default_config()
    
    def create_default_config(self) -> Dict:
        """Create default configuration."""
        config = {
            "game": "Wukong",
            "game_path": "",
            "discovery_port": 25565,
            "game_port": 27015,
            "player_name": "Player1",
            "lan_only": True,
            "max_players": 4
        }
        return config
    
    def save_config(self):
        """Save current configuration to file."""
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=2)
        print(f"Configuration saved to {self.config_path}")
    
    def find_game_executable(self) -> Optional[str]:
        """Attempt to find the game executable."""
        game_name = self.config.get("game", "Wukong")
        
        # Common game installation paths
        common_paths = [
            "C:\\Program Files\\Epic Games\\BlackMythWukong",
            "C:\\Program Files (x86)\\Steam\\steamapps\\common\\BlackMythWukong",
            "D:\\Games\\BlackMythWukong",
            os.path.expanduser("~/.steam/steam/steamapps/common/BlackMythWukong"),
            "/opt/games/BlackMythWukong"
        ]
        
        # Check configured path first
        if self.config.get("game_path"):
            if os.path.exists(self.config["game_path"]):
                return self.config["game_path"]
        
        # Search common paths
        for base_path in common_paths:
            if os.path.exists(base_path):
                # Look for executable
                for root, dirs, files in os.walk(base_path):
                    for file in files:
                        if file.endswith(('.exe', '.sh')) and 'wukong' in file.lower():
                            return os.path.join(root, file)
        
        return None
    
    def start_discovery_server(self):
        """Start UDP discovery server for finding peers on LAN."""
        discovery_port = self.config.get("discovery_port", 25565)
        
        try:
            # Create UDP socket for discovery
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind(('', discovery_port))
            
            print(f"Discovery server started on port {discovery_port}")
            print(f"Player: {self.config.get('player_name', 'Unknown')}")
            print("Waiting for peers...")
            
            while True:
                data, addr = self.server_socket.recvfrom(1024)
                message = data.decode('utf-8')
                
                if message.startswith("DISCOVER:"):
                    # Respond to discovery request
                    response = f"PEER:{self.config.get('player_name', 'Unknown')}"
                    self.server_socket.sendto(response.encode('utf-8'), addr)
                    print(f"Discovery request from {addr[0]}")
                    
                elif message.startswith("PEER:"):
                    # Peer announcement
                    peer_name = message.split(":", 1)[1]
                    peer_info = {"address": addr[0], "name": peer_name}
                    if peer_info not in self.peers:
                        self.peers.append(peer_info)
                        print(f"Discovered peer: {peer_name} at {addr[0]}")
                        
        except Exception as e:
            print(f"Discovery server error: {e}")
        finally:
            if self.server_socket:
                self.server_socket.close()
    
    def discover_peers(self) -> List[Dict]:
        """Send discovery broadcast to find peers."""
        discovery_port = self.config.get("discovery_port", 25565)
        
        try:
            # Create UDP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.settimeout(5.0)
            
            # Send discovery broadcast
            message = f"DISCOVER:{self.config.get('player_name', 'Unknown')}"
            sock.sendto(message.encode('utf-8'), ('255.255.255.255', discovery_port))
            
            print("Searching for peers...")
            found_peers = []
            
            # Listen for responses
            start_time = threading.Event()
            timeout = 3.0
            
            try:
                while True:
                    data, addr = sock.recvfrom(1024)
                    response = data.decode('utf-8')
                    
                    if response.startswith("PEER:"):
                        peer_name = response.split(":", 1)[1]
                        peer_info = {"address": addr[0], "name": peer_name}
                        if peer_info not in found_peers:
                            found_peers.append(peer_info)
                            print(f"Found peer: {peer_name} at {addr[0]}")
            except socket.timeout:
                pass
            
            sock.close()
            return found_peers
            
        except Exception as e:
            print(f"Discovery error: {e}")
            return []
    
    def launch_game(self, args: List[str] = None):
        """Launch the game with specified arguments."""
        game_path = self.find_game_executable()
        
        if not game_path:
            print("Error: Could not find game executable.")
            print("Please set the game_path in config.json")
            return False
        
        print(f"Launching game: {game_path}")
        
        # Build launch command
        launch_args = args or []
        
        try:
            import subprocess
            process = subprocess.Popen([game_path] + launch_args)
            print(f"Game launched with PID: {process.pid}")
            return True
        except Exception as e:
            print(f"Error launching game: {e}")
            return False
    
    def show_status(self):
        """Display current launcher status."""
        print("\n=== ReadyM.Launcher Status ===")
        print(f"Game: {self.config.get('game', 'Unknown')}")
        print(f"Player: {self.config.get('player_name', 'Unknown')}")
        print(f"Discovery Port: {self.config.get('discovery_port', 'Unknown')}")
        print(f"Game Port: {self.config.get('game_port', 'Unknown')}")
        print(f"Max Players: {self.config.get('max_players', 'Unknown')}")
        print(f"LAN Only: {self.config.get('lan_only', True)}")
        
        game_path = self.find_game_executable()
        if game_path:
            print(f"Game Path: {game_path}")
        else:
            print("Game Path: Not found")
        
        print(f"\nKnown Peers: {len(self.peers)}")
        for peer in self.peers:
            print(f"  - {peer['name']} at {peer['address']}")
        print("=============================\n")


def main():
    """Main entry point for the launcher."""
    parser = argparse.ArgumentParser(
        description="ReadyM.Launcher - P2P Game Launcher for Wukong"
    )
    parser.add_argument(
        '--config', 
        type=str, 
        default='config.json',
        help='Path to configuration file'
    )
    parser.add_argument(
        '--discover',
        action='store_true',
        help='Discover peers on local network'
    )
    parser.add_argument(
        '--server',
        action='store_true',
        help='Start discovery server'
    )
    parser.add_argument(
        '--launch',
        action='store_true',
        help='Launch the game'
    )
    parser.add_argument(
        '--status',
        action='store_true',
        help='Show launcher status'
    )
    parser.add_argument(
        '--setup',
        action='store_true',
        help='Create default configuration file'
    )
    parser.add_argument(
        '--player-name',
        type=str,
        help='Set player name'
    )
    
    args = parser.parse_args()
    
    # Create launcher instance
    launcher = P2PLauncher(config_path=args.config)
    
    # Update player name if provided
    if args.player_name:
        launcher.config['player_name'] = args.player_name
        launcher.save_config()
    
    # Handle commands
    if args.setup:
        launcher.save_config()
        print("Default configuration created.")
        print("Please edit config.json to set your game path.")
        
    elif args.server:
        launcher.start_discovery_server()
        
    elif args.discover:
        peers = launcher.discover_peers()
        print(f"\nFound {len(peers)} peer(s)")
        
    elif args.launch:
        launcher.launch_game()
        
    elif args.status:
        launcher.show_status()
        
    else:
        # Interactive mode
        print("ReadyM.Launcher - P2P Game Launcher")
        print("Type 'help' for available commands\n")
        
        launcher.show_status()
        
        while True:
            try:
                cmd = input("> ").strip().lower()
                
                if cmd == 'help':
                    print("\nAvailable commands:")
                    print("  discover  - Find peers on local network")
                    print("  server    - Start discovery server")
                    print("  launch    - Launch the game")
                    print("  status    - Show current status")
                    print("  config    - Save current configuration")
                    print("  quit      - Exit launcher")
                    print()
                    
                elif cmd == 'discover':
                    launcher.discover_peers()
                    
                elif cmd == 'server':
                    print("Starting server... (Press Ctrl+C to stop)")
                    launcher.start_discovery_server()
                    
                elif cmd == 'launch':
                    launcher.launch_game()
                    
                elif cmd == 'status':
                    launcher.show_status()
                    
                elif cmd == 'config':
                    launcher.save_config()
                    
                elif cmd in ('quit', 'exit', 'q'):
                    print("Goodbye!")
                    break
                    
                else:
                    print(f"Unknown command: {cmd}")
                    print("Type 'help' for available commands")
                    
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except EOFError:
                break


if __name__ == "__main__":
    main()
