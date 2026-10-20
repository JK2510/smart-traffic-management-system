# Smart Traffic Management System

An IoT-oriented smart traffic management project that explores vehicle detection, traffic-demand estimation, and adaptive traffic signal control.

## Overview

Traffic congestion can increase travel time and fuel consumption in urban areas. This project explores how computer vision and embedded systems can help monitor traffic and support traffic signal decisions.

The project is organized into software modules for vehicle detection, traffic logic, an optional Arduino-based traffic light prototype, and a planned traffic simulation component.

## Objectives

- Detect vehicles in traffic video using a pretrained YOLO model.
- Estimate traffic demand from vehicle detections.
- Explore traffic signal timing based on traffic demand.
- Provide an optional low-voltage Arduino LED prototype.
- Document testing, wiring, and future improvements.

## Technologies

- Python
- OpenCV
- YOLO
- Arduino
- Embedded systems and IoT concepts
- SUMO traffic simulation (planned extension)

## Planned Project Structure

```text
smart-traffic-management-system/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── vision_controller.py
│   └── traffic_logic.py
├── arduino/
│   └── traffic_light_controller/
│       └── traffic_light_controller.ino
├── docs/
├── simulation/
└── data/
```

## Current Scope

The software is intended to support traffic-video analysis and demonstrate traffic signal logic. The Arduino component is intended for a low-voltage tabletop prototype.

Hardware integration, real-time performance, and simulation results must be tested and verified before being reported as completed.

## Safety

This project is for educational and prototype use only. Do not connect it to real road traffic signals or use it to control public-road infrastructure.

## Future Improvements

- Evaluate vehicle detection on different traffic videos.
- Improve traffic-demand estimation and signal timing.
- Test the Arduino prototype with low-voltage LEDs.
- Integrate and validate a SUMO simulation.
- Document performance measurements and limitations.

## Author

Jasmeen Kaur

GitHub: [@JK2510](https://github.com/JK2510)
