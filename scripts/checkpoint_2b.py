# Import DAC chip library
from DAH import MCP4922

# Define DAC as SPI chip 1 (CE1/GPIO7)
DAC1 = MCP4922( chip=1 )

# Output 1.3V on channel 0 of DAC1
DAC1.analogWriteVolt( 0, 1.3 )
