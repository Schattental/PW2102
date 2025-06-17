# PW2102
Global Specialties 2MHz Function Generator PW2102 control code using pyserial via RS-232C. Model (105-2102)

The manual that can be found online for this device lists an incorrect baud rate of 300, and has other mistakes. This library can be used to control the function generator without having to consult the manual.

It is recommended to use a small delay between sending commands and especially after setting a frequency. When the function generator switched between frequency ranges, unexpected behaviour may occur temporarily. See the example code for details.
