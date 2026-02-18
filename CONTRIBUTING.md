# Contributing to ReadyM Launcher P2P

Thank you for your interest in contributing! This guide will help you get started.

## Getting Started with Codespaces

### Using GitHub Codespaces (Recommended)

1. Navigate to the repository on GitHub
2. Click the green **Code** button
3. Select the **Codespaces** tab
4. Click **Create codespace on [branch]**
5. Wait for the environment to set up (30-60 seconds)
6. Start coding immediately!

### Local Development

If you prefer working locally:

```bash
git clone https://github.com/change117/ReadyM.Launcher-Peer-to-Peer.git
cd ReadyM.Launcher-Peer-to-Peer
npm install
npm run dev
```

## Development Workflow

1. **Create a branch** for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** in the appropriate files:
   - `src/` - Server-side code
   - `public/` - Client-side UI
   - `uploads/` - User-uploaded files

3. **Test your changes**:
   ```bash
   npm start
   # Visit http://localhost:3000
   ```

4. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

5. **Push and create a PR**:
   ```bash
   git push origin feature/your-feature-name
   ```

## Code Style

- Use 2 spaces for indentation
- Follow existing code patterns
- Add comments for complex logic
- Keep functions small and focused

## Testing

Currently, testing infrastructure is minimal. When adding tests:
- Place test files in a `test/` directory
- Name test files `*.test.js`
- Use a consistent testing framework

## File Uploads

The file upload feature is designed to:
- Accept game files, mods, and configurations
- Store files in the `uploads/` directory
- Enable P2P sharing between clients

## Questions?

Feel free to open an issue for any questions or concerns!
