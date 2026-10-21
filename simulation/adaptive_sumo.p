"""Template for experimenting with adaptive traffic signals in SUMO.

Requires a configured SUMO network and traffic-light program.
This template has not been validated against a specific network.
"""

import os
import sys


def main():
    sumo_home = os.environ.get("SUMO_HOME")

    if not sumo_home:
        raise RuntimeError(
            "SUMO_HOME is not set. Install SUMO and configure its environment."
        )

    tools_dir = os.path.join(sumo_home, "tools")
    if not os.path.isdir(tools_dir):
        raise RuntimeError(
            f"SUMO tools directory was not found: {tools_dir}"
        )

    if tools_dir not in sys.path:
        sys.path.append(tools_dir)

    try:
        import traci
    except ImportError as exc:
        raise RuntimeError(
            "Could not import TraCI. Check your SUMO installation."
        ) from exc

    config_file = os.environ.get("SUMO_CONFIG", "simulation.sumocfg")
    if not os.path.isfile(config_file):
        raise FileNotFoundError(
            f"SUMO configuration file not found: {config_file}. "
            "Provide a valid .sumocfg file."
        )

    print("Starting SUMO with configuration:", config_file)
    traci.start(["sumo-gui", "-c", config_file])

    try:
        while traci.simulation.getMinExpectedNumber() > 0:
            traci.simulationStep()

            # TODO:
            # 1. Identify the traffic-light ID in your SUMO network.
            # 2. Read vehicle counts or lane occupancy for each approach.
            # 3. Map demand to valid signal phases for that network.
            # 4. Apply safe phase transitions and minimum/maximum green times.
            # 5. Record waiting-time and queue-length metrics.

    finally:
        traci.close()

    print("SUMO run finished.")


if __name__ == "__main__":
    main()
