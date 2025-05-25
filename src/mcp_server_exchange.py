from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="MCP Server Exchange", 
              version="0.1.0", 
              description="MCP Server for Money Exchange")

@mcp.tool(name="money exchange",
          description="Convert an amount from usd currency to bdt")
def exchange(
    amount: float
) -> float:
    """
    Convert an amount from usd to bdt.
    
    Parameters:
        amount (float): The amount of money to convert.
    
    Returns:
        float: The converted amount in the target currency.
    """
    
    exchange_rate = 85
    converted_amount = amount * exchange_rate
    return converted_amount

if __name__ == "__main__":
    print("MCP Server Exchange is running...")
    print("Use the tool 'money exchange' to convert USD to BDT.")
    mcp.run(transport="stdio")
