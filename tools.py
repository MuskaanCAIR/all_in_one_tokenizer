from tibetan.tib_g2p_model import tib_g2p
from chinese.logograph_g2p_model.pipeline import zh_g2p
from util import reading
import preprocess

class tokenization:

    def zh(input_file_path, output_file_path):

        #read uncleaned input file by user
        uncleaned_data = reading.text_file_read(file_path=input_file_path)
        #cleaning the data
        cleaned_data_path = preprocess.zh_preprocess(uncleaned_data)
        cleaned_data = reading.text_file_read(file_path=cleaned_data_path)

        #tokenization
        tokens = zh_g2p.generate_tokens(cleaned_data)
        return tokens
    
    def bo():
        return