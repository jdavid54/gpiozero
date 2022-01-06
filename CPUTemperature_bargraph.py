from gpiozero import LEDBarGraph, CPUTemperature
from signal import pause

# Use minimums and maximums that are closer to "normal" usage so the
# bar graph is a bit more "lively"
cpu = CPUTemperature(min_temp=30, max_temp=70, threshold=50)
print(cpu.is_active, cpu.value)
print('Initial temperature: {}C'.format(cpu.temperature))

# https://gpiozero.readthedocs.io/en/stable/api_boards.html?highlight=LEDBarGraph#gpiozero.LEDBarGraph
graph = LEDBarGraph(5, 6, 13, 19, 25, pwm=True)
print(graph)
print('LED on',graph.lit_count)
graph.source = cpu
print(graph.source)
#graph.value = 2/5
print(cpu.value,graph.value)
print('LED on',graph.lit_count)

pause()