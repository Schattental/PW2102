import time
from pw2102 import FunctionGenerator
import numpy as np

start = 10000
step = 10000
num = 9

freqs = start + np.arange(0, num) * step

try:
    fg = FunctionGenerator(port='COM2')
    fg.set_waveform('sine')
    # Small delay between commands, this delay can probably be reduced
    # or removed entirely (most stable behaviour was seen with a short delay).
    time.sleep(0.1)
    fg.set_output_level(10)
    time.sleep(0.1)
    fg.set_offset(0)
    time.sleep(0.1)
    fg.set_duty_cycle(50)
    time.sleep(0.1)
    
    for f in freqs:
        fg.set_frequency(f)
        # 5 second delay for the function generator frequency to settle.
        # This delay can be reduced, but switching between frequency ranges can cause unexpected behaviour
        # which is why a delay is recommended before recording data or taking other actions.
        time.sleep(5)
        
except:
    print('error')
finally:
    fg.close()
