import re
import time
from flight_ticket_upgrader.constants import *


class ObjectValidator:
    """
    This class validates the passenger details like email, mobile number, PNR, travel date, cabin
    """
    def validate_objects(self, validation_dict):

        result_dict = {
            email: None,
            mobile: None,
            pnr: None,
            cabin_type: None,
            travel_date: None
        }

        for obj_type, obj in validation_dict.items():
            if obj_type not in [email, mobile, pnr, cabin_type, travel_date]:
                raise Exception("Please provide a valid choice for validation object. Given {}".format(obj_type))

            if obj_type == email:
                result_dict[email] = self.validate(email_regex, obj.strip())
            if obj_type == mobile:
                result_dict[mobile] = self.validate(mobile_regex, obj.strip())
            if obj_type == pnr:
                result_dict[pnr] = self.validate(pnr_regex, obj.strip())
            if obj_type == cabin_type:
                result_dict[cabin_type] = obj.strip().lower() in cabin_type_choices
            if obj_type == travel_date:
                result_dict[travel_date] = self.validate_ticket_date(obj[0].strip(), obj[1].strip())

        print(result_dict)
        return result_dict

    @staticmethod
    def validate(regex, obj):

        if re.search(regex, obj):
            print("Valid object - {}".format(obj))
            return True
        print("Invalid object - {}".format(obj))
        return False

    @staticmethod
    def validate_ticket_date(ticket_date, booking_date):
        """
        Validates if ticket date is greater than the booking date
        :param ticket_date:
        :param booking_date:
        :return:
        """
        ticket_date_obj = time.strptime(ticket_date, "%Y-%m-%d")
        booking_date_obj = time.strptime(booking_date, "%Y-%m-%d")

        # Returns True if ticket date is greater than the booking date
        return ticket_date_obj > booking_date_obj
