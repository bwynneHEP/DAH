from DAH import MCP23S17

# Define the device using SPI chip 0
# and hardware address (A0, A1, A2 all grounded)
mcp0 = MCP23S17( chip=0, address=0x20 )
