"""Simple traffic-demand estimation and adaptive signal timing logic."""

from dataclasses import dataclass


@dataclass
class TrafficDemand:
    vehicle_count: int
    waiting_time: float = 0.0


@dataclass
class SignalPlan:
    green_seconds: int
    reason: str


def calculate_green_time(
    demand: TrafficDemand,
    min_green: int = 10,
    max_green: int = 45,
) -> SignalPlan:
    """Calculate a demonstration green time from estimated vehicle demand."""
    if min_green <= 0 or max_green < min_green:
        raise ValueError("Invalid green-time limits.")

    count = max(0, demand.vehicle_count)
    green = min(max_green, min_green + count * 2)

    return SignalPlan(
        green_seconds=green,
        reason=f"Estimated demand: {count} vehicles",
    )


def choose_approach(
    north_south_count: int,
    east_west_count: int,
) -> str:
    """Choose the approach with more detected vehicles."""
    if north_south_count == east_west_count:
        return "NORTH_SOUTH"
    return (
        "NORTH_SOUTH"
        if north_south_count > east_west_count
        else "EAST_WEST"
    )


if __name__ == "__main__":
    ns_count = 12
    ew_count = 5

    approach = choose_approach(ns_count, ew_count)
    demand = TrafficDemand(vehicle_count=max(ns_count, ew_count))
    plan = calculate_green_time(demand)

    print(f"Selected approach: {approach}")
    print(f"Green time: {plan.green_seconds} seconds")
    print(plan.reason)
