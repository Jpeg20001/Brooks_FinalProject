#Name: Michael Gonzales, Emmet Webb, Sean Dippold, David Brown
##mail: gonzame@mail.uc.edu, webbc7@mail.uc.edu,dippolst@mail.uc.edu, brown6dw@mail.uc.edu
#Assignment Title: Brooks_FinalProject
#Course: IS 4010
#Semester/Year: Fall 2023
# Brief Description: This our final project where we demonstrate the use of python to 
# create classes that invoke methods that read JSON file and decrypts messages 
# using the Cryptography and processes images
#Citations: Chat GPT chat.openai.com
from JsonDataReaderPackage.JsonDataReaderClass import *
from TextFileExtractorPackage.TextFileExtractorClass import *
from MessageDecryptorPackage.MessageDecryptorClass import *
from ImageLoaderPackage.ImageLoaderClass import *

if __name__ == "__main__":
    
    #[1] Json Data Reader
    #Finds the JSON file 
    json_reader = JsonDataReader('EncryptedGroupHints Fall 2023 Section 001 (2).json')
    #Processes the JSON data stores the information in a variable called brooks_data
    brooks_data = json_reader.get_brooks_data()
    #Converts brooks_data into integers using list comprehension 
    intBrooksNumbers = [int(num) for num in brooks_data]
    
    
    #[2]Text file extractor 
    # Replace 'your_text_file.txt' with the actual path to your text file
    txt_file_path = 'english-2.txt'
    # Specify the indexes you want to extract
    indexes_to_extract = intBrooksNumbers
    # Create an instance of TextFileExtractor
    text_extractor = TextFileExtractor(txt_file_path)
    # Extract information based on specified indexes
    result = text_extractor.extract_info_by_indexes(indexes_to_extract)
    # Display the result
    print(result)
    
    
    #[3] AES Decryption 
    # Replace 'your_key_here' with the actual key
    key = b'2tWgZTHycJHttRAQkazCO-Qr66EBdm1mW1-QgCcSzVs='
    decryptor = MessageDecryptor(key)
    json_reader = JsonDataReader('TeamsAndEncryptedMessagesForDistribution.json')
    movie_data = json_reader.get_brooks_data()
    strMovieMessage = ''.join([str(item) for item in movie_data])
    # Replace 'your_encrypted_message_here' with the actual encrypted message
    encrypted_message = strMovieMessage
    # Decrypt the message
    decrypted_message = decryptor.decrypt(encrypted_message)
    # Display the result
    print(decrypted_message)
    
    #Need Image Processing 
    #Image Processing

    # Create an instance of the ImageLoader class with the file path

    loader = ImageLoader('BrooksGroupPhoto.jpg')

    # Call the load_image method to load and display the image

    loaded_image = loader.load_image()