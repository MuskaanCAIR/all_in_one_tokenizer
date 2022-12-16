import os
# from tibetan.tib_g2p_model import tib_g2p
from chinese.logograph_g2p_model.pipeline import zh_g2p
from util import reading,writing
import preprocess

class tokenization:

    print(" working on tokenization !!!")
    def zh(input_file_path, output_file_path):

        #read uncleaned input file by user
        uncleaned_data = reading.text_file_read(file_path=input_file_path)
        #cleaning the data
        cleaned_data_path = preprocess.zh_preprocess(uncleaned_data)
        cleaned_data = reading.text_file_read(file_path=cleaned_data_path)

        #tokenization
        tokens = zh_g2p.generate_tokens(cleaned_data)

        #saving in .word file
        writing.word_file_generate_zh(tokens=tokens,
                                    input_file=input_file_path,
                                    output_file=output_file_path)
    
    def bo():
        return


class g2p:

    print(" working on g2p !!!")
    def zh(input_file_path, output_file_path):

        input_file_name = os.path.basename(input_file_path)
        input_file_name = input_file_name.replace('.txt','.wrd')
        token_file_path = f'{output_file_path}/{input_file_name}'
        #reading the generated token file
        tokens = reading.text_file_read(token_file_path)
        tokens = tokens.split('\n')
        g2p_list=[]

        #g2p generation
        for tok in tokens:
            generated_g2p = zh_g2p.generate_g2p(tok)
            g2p_list.append((tok,generated_g2p))

        #saving in .phn file
        writing.phone_file_generate(phone_list = g2p_list, 
                                    input_file = input_file_path, 
                                    output_file = output_file_path)
        
    def bo():
        return