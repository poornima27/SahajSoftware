import os
import csv
from flight_ticket_upgrader import validations
from flight_ticket_upgrader import error_strings
from flight_ticket_upgrader import offers

base_path = os.path.dirname(os.path.abspath(__file__))
print(base_path)

with open(base_path + "/input_files/input.csv", "r") as fl:
    header = fl.readline()
    print("Header line - {}".format(header))
    lines = fl.readlines()
    for index, line in enumerate(lines):
        line = line.split(",")
        print("line {} - {}".format(index, line))
        req_validation = {"pnr": line[2], "travel_date": [line[4], line[6]], "email": line[7], "mobile": line[8],
                          "cabin_type": line[9]}
        validation_result = validations.Validations().validate_objects(req_validation)
        found_error = []
        for key, value in validation_result.items():
            if not value:
                found_error.append(error_strings.error_strings.get(key))

        if found_error:
            line[9] = line[9].strip()
            line.extend(found_error)
            with open(base_path + "/output_files/error_data.csv", "a") as wef:
                csvwriter = csv.writer(wef, lineterminator='\n')
                csvwriter.writerow(line)
        else:
            offer = offers.get_offer_for_class(line[3].strip())
            line[9] = line[9].strip()
            line.append(offer)
            with open(base_path + "/output_files/parsed_data.csv", "a") as wpf:
                csvwriter = csv.writer(wpf, lineterminator='\n')
                csvwriter.writerow(line)
