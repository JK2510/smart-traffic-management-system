# Arduino Traffic Light Prototype — Wiring Guide

## Components

- Arduino Uno or compatible board
- 6 LEDs: 2 red, 2 yellow, and 2 green
- 6 current-limiting resistors (typically 220–330 ohms)
- Breadboard and jumper wires
- USB cable

## Pin Connections

| Traffic approach | LED colour | Arduino pin |
|---|---|---|
| North–South | Red | D3 |
| North–South | Yellow | D4 |
| North–South | Green | D5 |
| East–West | Red | D6 |
| East–West | Yellow | D7 |
| East–West | Green | D8 |

## Wiring Steps

1. Connect each Arduino output pin to the anode (long leg) of its LED through a current-limiting resistor.
2. Connect each LED cathode (short leg) to Arduino GND.
3. Check that every LED has its own resistor.
4. Connect the Arduino to your computer using USB.
5. Open the `.ino` sketch in the Arduino IDE, select the correct board and port, and upload it.
6. Observe the LEDs and verify that the two approaches alternate through red, yellow, and green phases.

## Safety

- This is a low-voltage educational prototype only.
- Never connect the Arduino directly to mains voltage or real traffic signals.
- Disconnect USB power before changing wiring.
- Verify the pin assignments before powering the circuit.

## Testing Status

The wiring and sketch must be physically tested before the prototype can be described as working.
