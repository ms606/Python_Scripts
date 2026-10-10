"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagon_id):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    return list(wagon_id)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """
    a, b, *rest =  each_wagons_id
    new_wagons_id = *rest, a, b
    locomotive, *trdy = new_wagons_id
    new_list = [locomotive, *missing_wagons, *trdy]
    return new_list


def add_missing_stops(route, **stops):
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        stops (dict): An arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.
    """
    stops_details = []
    list(stops.values())
    route["stops"] = list(stops.values())
    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """
    return {**route, **more_route_information}



def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[list[tuple]]): The list of rows of wagons.

    Returns:
        list[list[tuple]]: the list of rows of wagons.
    """
    a, b, c = zip(*wagons_rows)
    *wagons_rows, = [*a], [*b], [*c]
    print(list(wagons_rows))
    return (list(wagons_rows))
