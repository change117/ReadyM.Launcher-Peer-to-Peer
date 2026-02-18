#!/usr/bin/env python3
"""
Tests for ReadyM.Launcher P2P functionality
"""

import unittest
import json
import os
import sys
import tempfile
import shutil
from pathlib import Path

# Add parent directory to path to import launcher
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from launcher import P2PLauncher


class TestP2PLauncher(unittest.TestCase):
    """Test cases for P2P Launcher."""
    
    def setUp(self):
        """Set up test environment."""
        # Create temporary directory for test configs
        self.test_dir = tempfile.mkdtemp()
        self.config_path = os.path.join(self.test_dir, "test_config.json")
    
    def tearDown(self):
        """Clean up test environment."""
        # Remove temporary directory
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_create_default_config(self):
        """Test creating default configuration."""
        launcher = P2PLauncher(config_path=self.config_path)
        config = launcher.create_default_config()
        
        # Verify required fields exist
        self.assertIn("game", config)
        self.assertIn("discovery_port", config)
        self.assertIn("game_port", config)
        self.assertIn("player_name", config)
        self.assertIn("lan_only", config)
        self.assertIn("max_players", config)
        
        # Verify default values
        self.assertEqual(config["game"], "Wukong")
        self.assertEqual(config["discovery_port"], 25565)
        self.assertEqual(config["game_port"], 27015)
        self.assertTrue(config["lan_only"])
    
    def test_save_and_load_config(self):
        """Test saving and loading configuration."""
        launcher = P2PLauncher(config_path=self.config_path)
        
        # Modify config
        launcher.config["player_name"] = "TestPlayer"
        launcher.config["max_players"] = 8
        
        # Save config
        launcher.save_config()
        
        # Verify file exists
        self.assertTrue(os.path.exists(self.config_path))
        
        # Load config in new instance
        launcher2 = P2PLauncher(config_path=self.config_path)
        
        # Verify loaded values
        self.assertEqual(launcher2.config["player_name"], "TestPlayer")
        self.assertEqual(launcher2.config["max_players"], 8)
    
    def test_config_structure(self):
        """Test configuration file structure."""
        launcher = P2PLauncher(config_path=self.config_path)
        launcher.save_config()
        
        # Read and parse JSON
        with open(self.config_path, 'r') as f:
            config_data = json.load(f)
        
        # Verify it's valid JSON and has expected structure
        self.assertIsInstance(config_data, dict)
        self.assertIn("game", config_data)
        self.assertIn("discovery_port", config_data)
    
    def test_find_game_executable_not_found(self):
        """Test game executable detection when game is not installed."""
        launcher = P2PLauncher(config_path=self.config_path)
        
        # Should return None when game is not found
        result = launcher.find_game_executable()
        self.assertIsNone(result)
    
    def test_find_game_executable_with_configured_path(self):
        """Test game executable detection with configured path."""
        # Create a fake executable
        fake_exe = os.path.join(self.test_dir, "wukong.exe")
        Path(fake_exe).touch()
        
        launcher = P2PLauncher(config_path=self.config_path)
        launcher.config["game_path"] = fake_exe
        
        # Should return configured path
        result = launcher.find_game_executable()
        self.assertEqual(result, fake_exe)
    
    def test_launcher_initialization(self):
        """Test launcher initialization."""
        launcher = P2PLauncher(config_path=self.config_path)
        
        # Verify launcher attributes
        self.assertIsNotNone(launcher.config)
        self.assertIsInstance(launcher.peers, list)
        self.assertEqual(len(launcher.peers), 0)
        self.assertIsNone(launcher.server_socket)
    
    def test_peer_list_management(self):
        """Test peer list management."""
        launcher = P2PLauncher(config_path=self.config_path)
        
        # Add peer
        peer1 = {"address": "192.168.1.100", "name": "Player1"}
        launcher.peers.append(peer1)
        
        # Verify peer added
        self.assertEqual(len(launcher.peers), 1)
        self.assertIn(peer1, launcher.peers)
        
        # Add another peer
        peer2 = {"address": "192.168.1.101", "name": "Player2"}
        launcher.peers.append(peer2)
        
        # Verify both peers
        self.assertEqual(len(launcher.peers), 2)
        self.assertIn(peer2, launcher.peers)
    
    def test_config_ports(self):
        """Test configuration port values."""
        launcher = P2PLauncher(config_path=self.config_path)
        
        # Verify default ports
        self.assertEqual(launcher.config["discovery_port"], 25565)
        self.assertEqual(launcher.config["game_port"], 27015)
        
        # Test custom ports
        launcher.config["discovery_port"] = 30000
        launcher.config["game_port"] = 30001
        launcher.save_config()
        
        # Reload and verify
        launcher2 = P2PLauncher(config_path=self.config_path)
        self.assertEqual(launcher2.config["discovery_port"], 30000)
        self.assertEqual(launcher2.config["game_port"], 30001)
    
    def test_lan_only_setting(self):
        """Test LAN only security setting."""
        launcher = P2PLauncher(config_path=self.config_path)
        
        # Verify default is LAN only
        self.assertTrue(launcher.config["lan_only"])
        
        # Test changing setting
        launcher.config["lan_only"] = False
        launcher.save_config()
        
        launcher2 = P2PLauncher(config_path=self.config_path)
        self.assertFalse(launcher2.config["lan_only"])
    
    def test_max_players_setting(self):
        """Test max players configuration."""
        launcher = P2PLauncher(config_path=self.config_path)
        
        # Verify default
        self.assertEqual(launcher.config["max_players"], 4)
        
        # Test various values
        for max_players in [2, 4, 8, 16]:
            launcher.config["max_players"] = max_players
            launcher.save_config()
            
            launcher2 = P2PLauncher(config_path=self.config_path)
            self.assertEqual(launcher2.config["max_players"], max_players)


class TestConfigValidation(unittest.TestCase):
    """Test configuration validation."""
    
    def test_valid_config_file(self):
        """Test loading a valid config file."""
        test_dir = tempfile.mkdtemp()
        config_path = os.path.join(test_dir, "valid_config.json")
        
        valid_config = {
            "game": "Wukong",
            "game_path": "/path/to/game",
            "discovery_port": 25565,
            "game_port": 27015,
            "player_name": "TestPlayer",
            "lan_only": True,
            "max_players": 4
        }
        
        with open(config_path, 'w') as f:
            json.dump(valid_config, f)
        
        launcher = P2PLauncher(config_path=config_path)
        
        # Verify all fields loaded correctly
        self.assertEqual(launcher.config["game"], "Wukong")
        self.assertEqual(launcher.config["player_name"], "TestPlayer")
        self.assertEqual(launcher.config["discovery_port"], 25565)
        
        # Cleanup
        shutil.rmtree(test_dir)
    
    def test_missing_config_file(self):
        """Test handling of missing config file."""
        test_dir = tempfile.mkdtemp()
        config_path = os.path.join(test_dir, "nonexistent_config.json")
        
        # Should create default config
        launcher = P2PLauncher(config_path=config_path)
        
        # Verify default config was created
        self.assertIsNotNone(launcher.config)
        self.assertEqual(launcher.config["game"], "Wukong")
        
        # Cleanup
        shutil.rmtree(test_dir)


def run_tests():
    """Run all tests."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTests(loader.loadTestsFromTestCase(TestP2PLauncher))
    suite.addTests(loader.loadTestsFromTestCase(TestConfigValidation))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return exit code
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code)
