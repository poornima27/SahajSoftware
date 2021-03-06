import os
import csv
from flight_ticket_upgrader import object_validator
from flight_ticket_upgrader import error_strings
from flight_ticket_upgrader import offers
from flight_ticket_upgrader.constants import *


class PassengerDetailManager:
    """
    This class parses the input file, validates it and write the data back to the error and output files
    """
    def __init__(self):
        self.base_path = os.path.dirname(os.path.abspath(__file__))

    def parse_passenger_details(self):
        """
        Method to parse the passenger details
        :return:
        """
        validator = object_validator.ObjectValidator()
        with open(self.base_path + input_file, "r") as input_file_handler:
            header = input_file_handler.readline()
            print("Header line - {}".format(header))
            lines = input_file_handler.readlines()
            for index, line in enumerate(lines):
                line = line.split(",")
                print("line {} - {}".format(index, line))
                req_validation = {pnr: line[pnr_index],
                                  travel_date: [line[travel_date_index], line[booking_date_index]],
                                  email: line[email_index], mobile: line[mobile_index],
                                  cabin_type: line[cabin_type_index]}
                validation_result = validator.validate_objects(req_validation)
                found_error = list()
                for key, value in validation_result.items():
                    if not value:
                        found_error.append(error_strings.get_error_strings().get(key))

                if found_error:
                    self.write_error_data(line, found_error)
                else:
                    self.write_parsed_data(line)

    def write_error_data(self, data, error):
        """
        Method to write the data to error file
        :param data:
        :param error:
        :return:
        """
        data[cabin_type_index] = data[cabin_type_index].strip()
        found_error = " | ".join(error)
        data.append(found_error)
        with open(self.base_path + error_file, "a") as error_file_handler:
            csvwriter = csv.writer(error_file_handler, lineterminator='\n')
            csvwriter.writerow(data)

    def write_parsed_data(self, data):
        """
        Method to write valid data into the output file
        :param data:
        :return:
        """
        offer = offers.get_offer_for_class(data[fare_type_index].strip())
        data[cabin_type_index] = data[cabin_type_index].strip()
        data.append(offer)
        with open(self.base_path + output_file, "a") as output_file_handler:
            csvwriter = csv.writer(output_file_handler, lineterminator='\n')
            csvwriter.writerow(data)


PassengerDetailManager().parse_passenger_details()
