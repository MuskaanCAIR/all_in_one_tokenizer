import os
from tibetan_bo.tib_g2p_model import tib_g2p
from chinese_zh.logograph_g2p_model.pipeline import zh_g2p
from util import reading,writing
import preprocess
import shutil

class tokenization:

    #----------------chinese------------------------
    def zh(input_file_path, output_file_path):
        print("working on tokenization !!!")
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
    
    #------------------------tibetan------------------
    def bo(input_file_path, output_file_path):
        print("working on tokenization !!!")
        #read uncleaned data
        uncleaned_data = reading.text_file_read(file_path=input_file_path)
        #cleaning the data
        cleaned_data_path = preprocess.bo_preprocess(uncleaned_data)
        cleaned_data = reading.text_file_read(file_path=cleaned_data_path)

        #tokenization
        token = tib_g2p.generate_tokens(cleaned_data)

        #saving in .word file
        writing.word_file_generate(tokens=token,
                                    input_file=input_file_path,
                                    output_file=output_file_path)


class g2p:

    #----------------chinese------------------------
    def zh(input_file_path, output_file_path):

        print("working on g2p !!!")
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
    
    
    #--------------tibetan------------------------    
    def bo(input_file_path, output_file_path):

        print("working on g2p !!!")
        input_file_name = os.path.basename(input_file_path)
        input_file_name = input_file_name.replace('.txt','.wrd')
        input_file_name = f'{output_file_path}/{input_file_name}'
        shutil.copy(input_file_name,'bin/tibet_tokens.txt')
        token_file_path = '/home/cair/Desktop/all_in_one_tokenizer/all_in_one_tokenizer/bin/tibet_tokens.txt'

        #g2p generation
        tib_word_dict = tib_g2p.generate_thl(token_file_path=token_file_path)
        # for key,value in tib_word_dict.items():
        #     print(key,'---->',value)

        g2p_list = []
        syl_path = input_file_name.replace('.wrd','.syl')
        
        with open(syl_path,'w+') as f:
            for key,value in tib_word_dict.items():
                phones = value[1].replace('"','')
                phones = phones.split(' ')
                g2p_list.append((key,phones))

                #saving in .syl file
                line = f'{key}\t\t\t\t{value[0].replace(" ","")}\n'
                f.write(line)

        #saving in .phn file
        writing.phone_file_generate(phone_list = g2p_list, 
                                    input_file = input_file_path, 
                                    output_file = output_file_path)