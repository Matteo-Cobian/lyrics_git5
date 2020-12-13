from csv import DictWriter

def append_dict_as_row(file_name, dict_of_name, field_name):
    """ The function allows to add user's researches into a csv file.
    The reaserches will be available in csv file hystory.csv

    :param file_name: it is our file history.csv that will show the researches 
    :type file_name: string
    :param dict_of_name: key and values of the dictionary created in main.py
    :type dict_of_name: dict
    :param field_name: columns name of the csv file
    :type field_name: list
    """
    # copy in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames=field_name)
        # Add dictionary as in the csv
        dict_writer.writerow(dict_of_name)
