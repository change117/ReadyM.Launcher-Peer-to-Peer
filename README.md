# ReadyM.Launcher-Peer-to-Peer

A peer-to-peer launcher for ReadyM/Wukong that allows multiplayer gameplay without connecting to central servers. Direct peer-to-peer connections for enhanced privacy and control.

## 🚀 Quick Start with GitHub Codespaces

This repository is configured for GitHub Codespaces! You can start coding immediately:

1. Click the **Code** button on GitHub
2. Select the **Codespaces** tab
3. Click **Create codespace on main** (or your branch)
4. Wait for the environment to load (dependencies will auto-install)
5. Start developing!

The development environment includes:
- Node.js 20
- All necessary extensions (ESLint, Prettier, GitHub Copilot)
- Pre-configured ports forwarding (3000, 8080)
- Automatic dependency installation

## 📋 Features

- ✅ Direct peer-to-peer connections
- ✅ No central server dependency
- ✅ Enhanced privacy and control
- ✅ File upload and sharing support
- ✅ GitHub Codespaces ready
- 🔄 P2P game synchronization (coming soon)
- 🔄 Advanced peer discovery (coming soon)

## 🛠️ Local Development

If you prefer to work locally:

### Prerequisites
- Node.js 18 or higher
- npm or yarn

### Installation

```bash
# Clone the repository
git clone https://github.com/change117/ReadyM.Launcher-Peer-to-Peer.git
cd ReadyM.Launcher-Peer-to-Peer

# Install dependencies
npm install

# Start development server
npm run dev

# Or start production server
npm start
```

The launcher will be available at `http://localhost:3000`

## 📁 Project Structure

```
ReadyM.Launcher-Peer-to-Peer/
├── .devcontainer/          # GitHub Codespaces configuration
│   └── devcontainer.json   # Dev container settings
├── src/                    # Source code
│   └── index.js           # Main server file
├── public/                 # Static files
│   └── index.html         # Launcher UI
├── uploads/               # Uploaded files storage
├── package.json           # Project dependencies
└── README.md             # This file
```

## 🔧 Development

### Available Scripts

- `npm start` - Start the production server
- `npm run dev` - Start development server with auto-reload
- `npm test` - Run tests (to be implemented)

### Adding Files

You can upload files through:
1. The web UI at `http://localhost:3000`
2. Direct file copy to the `uploads/` directory
3. Git commits (for code/config files)

## 🤝 Contributing

1. Create a new branch for your feature
2. Make your changes
3. Test your changes
4. Submit a pull request

## 📝 License

MIT

## 🎮 About Wukong

This launcher is designed for the Wukong game, enabling peer-to-peer multiplayer connections without relying on central servers.

## 🔮 Roadmap

- [x] Basic project structure
- [x] GitHub Codespaces integration
- [x] File upload UI
- [ ] Implement actual file upload backend
- [ ] P2P connection protocol
- [ ] Peer discovery mechanism
- [ ] Game state synchronization
- [ ] NAT traversal (STUN/TURN)
- [ ] Encryption and security
