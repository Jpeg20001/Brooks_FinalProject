#JsonDataReaderClass.py
import json

class JsonDataReader:
    def __init__(self, json_file_path):
        """
        Constructor for JsonDataReader.
        @param: json_file_path: the file to be processed 
        """
        self.json_file_path = json_file_path
        self.data = None

    def read_data(self):
        """
        Read data from the JSON file and store it in the 'data' attribute.
        """
        with open(self.json_file_path, 'r') as json_file:
            # Load JSON data and assign it to the 'data' attribute
            # Assuming the structure of the JSON file has a key 'Brooks'
            self.data = json.load(json_file)['Brooks']

    def get_data(self):
        """
        Get the stored data.

        @Returns: The data read from the JSON file.
        """
        return self.data

    def get_brooks_data(self):
        """
        Get 'Brooks' data directly using the class instance.
        @Returns: The 'Brooks' data from the JSON file.
        """
        # Check if data is already loaded
        if self.data is None:
            # If not, load data
            self.read_data()

        return self.data