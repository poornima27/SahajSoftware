import re
import time

class Validations:

    def validate_objects(self, validation_dict):

        return_dict = {
            "email": None,
            "mobile": None,
            "pnr": None,
            "cabin_type": None,
            "travel_date": None
        }
        for obj_type, obj in validation_dict.items():
            if obj_type not in ["email", "mobile", "pnr", "cabin_type", "travel_date"]:
                raise Exception("Please provide a vaild choice for validation object. Given {}".format(obj_type))

            email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            mobile_regex = r'^(0|91)?[0-9]{10}$'
            pnr_regex = r'^[A-Za-z0-9]{6}$'
            cabin_type_choices = ["economy", "premium economy", "business", "first"]

            if obj_type == "email":
                return_dict["email"] = self.validate(email_regex, obj.strip())
            if obj_type == "mobile":
                return_dict["mobile"] = self.validate(mobile_regex, obj.strip())
            if obj_type == "pnr":
                return_dict["pnr"] = self.validate(pnr_regex, obj.strip())
            if obj_type == "cabin_type":
                return_dict["cabin_type"] = obj.strip().lower() in cabin_type_choices
            if obj_type == "travel_date":
                return_dict["travel_date"] = self.validate_ticket_date(obj[0].strip(), obj[1].strip())

        print(return_dict)
        return return_dict

    @staticmethod
    def validate(regex, obj):

        if re.search(regex, obj):
            print("Valid object - {}".format(obj))
            return True
        print("Invalid object - {}".format(obj))
        return False

    @staticmethod
    def validate_ticket_date(ticket_date, booking_date):

        d1 = time.strptime(ticket_date, "%Y-%m-%d")
        d2 = time.strptime(booking_date, "%Y-%m-%d")

        return d1 > d2
