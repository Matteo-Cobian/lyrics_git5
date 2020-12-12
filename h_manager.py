from csv import DictWriter


def append_dict_as_row(file_name, dict_of_name, field_name):
    # copy in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames=field_name)
        # Add dictionary as in the csv
        dict_writer.writerow(dict_of_name)

