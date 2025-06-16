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

## Using the MCP Server Exchange Tool

Once you have configured the MCP server, follow these steps to use it:

1. In VS Code, switch to Agent Mode
   - Open Command Palette (`Cmd + Shift + P` on macOS, `Ctrl + Shift + P` on Windows/Linux)
   - Type and select "Agent: Toggle Agent Mode"

2. Select the MCP Server Tool
   - Click on the "tools" button in the agent interface
   - Select "MCP Server: mcp-server-exchange-1234" from the list

3. Using the Currency Converter
   - Type your conversion request, for example: "convert 10 usd to euro"
   - The server will process the request with input:
     ```json
     {
       "amount": 10
     }
     ```
   - The result will be displayed showing the converted amount in euros

Example:
Input: "convert 10 usd to euro"
Output: 11.50 EUR (based on the exchange rate of 1 USD = 1.15 EUR)

## Note

Make sure to replace `/path/to/your/mcp_server_exchange.py` with the actual path to your MCP server implementation.
