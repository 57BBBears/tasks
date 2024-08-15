def get_bus_stop_count(
    buses: list[tuple[str, ...]], max_steps: int = 480
) -> int | None:
    """
    Given n drivers, each with their own circular route of stops, determine
    how many steps are required until all gossip known to each bus driver is
    known by all. Drivers only gossip if they arrive together at the same stop.
    :param buses:
    :param max_steps:
    :return:
    """
    # initial list of drivers with their own gossip
    bus_drivers = [{i} for i in range(len(buses))]

    for step in range(max_steps):
        cur_bus_stops = [bus[step % len(bus)] for bus in buses]
        stops_with_gossips = _get_stops_with_gossips(cur_bus_stops, bus_drivers)
        print(stops_with_gossips)
        for driver_i, stop in enumerate(cur_bus_stops):
            bus_drivers[driver_i] = stops_with_gossips[stop]

        print(step, ". ", bus_drivers)
        if all_gossips_known(bus_drivers):
            return step

    return None


def _get_stops_with_gossips(
    bus_stops: list[str], bus_drivers: list[set]
) -> dict[str, set]:
    stops_with_gossips = {}

    for stop_i in range(len(bus_stops)):
        if (bus_stop_name := bus_stops[stop_i]) not in stops_with_gossips:
            stops_with_gossips[bus_stop_name] = set()
        # union previous and current gossips
        stops_with_gossips[bus_stop_name] |= bus_drivers[stop_i]

    return stops_with_gossips


def all_gossips_known(drivers: list[set[int]]) -> bool:
    for driver_gossips in drivers:
        if len(driver_gossips) != len(drivers):
            return False
    return True


if __name__ == "__main__":
    assert get_bus_stop_count([("a", "b", "c"), ("c",)]) == 2
    assert get_bus_stop_count([("a", "b", "c"), ("c", "d"), ("d", "e")]) is None
    assert get_bus_stop_count([("a", "b", "c"), ("c", "e")]) == 2
    assert get_bus_stop_count([("c", "e"), ("d", "e")]) == 1
    assert get_bus_stop_count([("a", "b", "c"), ("c", "e"), ("d", "e")], 10) == 3
