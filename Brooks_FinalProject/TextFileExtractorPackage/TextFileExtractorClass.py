
#TextFileClass.py

import json



class TextFileExtractor:

    def __init__(self, txt_file_path):

        """

        Constructor for TextFileExtractor

        @Param: txt_file_path (str): The path to the text file.

        """

        self.txt_file_path = txt_file_path

        self.extracted_info = []



    def extract_info_by_indexes(self, indexes):

        """

        Extract information from the text file based on specified indexes.



        @Param: indexes(list): List of indexes to extract information from.



        @return: str: Extracted information as a sentence.

        """

        try:

            with open(self.txt_file_path, 'r', encoding='utf-8') as txt_file:

                lines = txt_file.readlines()



                for index in indexes:

                    try:

                        # Append the line at the specified index to the list

                        self.extracted_info.append(lines[index].strip())

                    except IndexError:

                        # Handle the case where the index is out of range

                        print(f"Error: Index {index} is out of range.")



                # Print the result as a sentence

                if self.extracted_info:

                    sentence = " ".join(self.extracted_info)

                    return f"{sentence}"

                else:

                    print("No information extracted.")

        except FileNotFoundError:

            print(f"Error: File not found - {self.txt_file_path}")