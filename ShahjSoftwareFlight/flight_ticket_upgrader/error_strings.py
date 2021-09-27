from flight_ticket_upgrader.constants.literal_constants import *


def get_error_strings():
    """
    Returns the error strings
    :return:
    """
    return {
        email: "Email Invalid",
        mobile: "Mobile Invalid",
        travel_date: "Travel date not greater than booking date",
        pnr: "PNR Invalid",
        cabin_type: "Cabin Type Invalid"
    }
