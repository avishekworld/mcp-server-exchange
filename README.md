# MCP Server Exchange

This repository contains an MCP (Model Context Protocol) server implementation.

## Adding MCP Server to VS Code

There are two ways to add an MCP server to VS Code:

### Method 1: Using Command Palette

1. Open VS Code Command Palette:
   - Windows/Linux: Press `Ctrl + Shift + P`
   - macOS: Press `Cmd + Shift + P`

2. Type and select "MCP: Add Server"

3. Select "Command stdio" from the options

4. In the command field, enter the path to your MCP server:
   ```
   /path/to/your/mcp_server_exchange.py
   ```

### Method 2: Manual Configuration in Settings

1. Open VS Code Settings:
   - Windows/Linux: Press `Ctrl + ,`
   - macOS: Press `Cmd + ,`

2. In the search bar, type "mcp" to filter settings

3. Look for "MCP > Servers: Servers"

4. Click on "Edit in settings.json"

5. Add your MCP server configuration in the JSON:
   ```json
   "mcp": {
    
        "servers": {
            "mcp-server-exchange-1234": {
                "type": "stdio",
                "command": "python",
                "args": [
                    "/path/to/your/mcp_server_exchange.py"
                ]
            }
        }
    }
   ```

6. Save the settings.json file

## Note

Make sure to replace `/path/to/your/mcp_server_exchange.py` with the actual path to your MCP server implementation.
