import asyncio

from mcp.server.mcpserver import MCPServer


server = MCPServer("Basic MCP Server")


@server.tool()
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


async def main():
    await server.run_stdio_async()


if __name__ == "__main__":
    asyncio.run(main())