"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """
    letters = ['A', 'B', 'C', 'D']
    current_number = 0
    while current_number < number:
        yield letters[current_number % 4]
        current_number += 1
 
    


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """
    current_number = 0
    row = 1
    letters = generate_seat_letters(number)

    while current_number < number:
        if row == 13:
            row = 14

        letter = next(letters)
        yield f"{row}{letter}"
    
        current_number += 1
        if current_number % 4 == 0:
            row += 1
    


def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """
    passenger_seats = {}
    seats = generate_seats(len(passengers))
    for passenger, seat in zip(passengers, seats):
        passenger_seats[passenger] = seat
    return passenger_seats    
    

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """
    for seat_number in seat_numbers:
        yield f"{seat_number}{flight_id}{'0' * (12 - len(seat_number + flight_id))}"
    
