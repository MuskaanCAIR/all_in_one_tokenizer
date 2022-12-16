#file contains all read and write methods 
import pandas as pd
import os
class reading:

    def text_file_read(file_path):

        with open(file_path,'r') as f:
            script = f.read()

        return script

class writing:

    def word_file_generate_zh(tokens,input_file, output_file):

        file_name = f'{output_file}/{os.path.basename(input_file)}'
        file_name = file_name.replace('.txt','.wrd')
        print(file_name)
        with open(file_name,'w+') as f:
            for tok in tokens:
                f.write(tok[0])
                f.write('\n')
        
        print("word file generation complete !!!")

    
    def word_file_generate(tokens,input_file, output_file):

        file_name = f'{output_file}/{os.path.basename(input_file)}'
        file_name = file_name.replace('.txt','.wrd')
        print(file_name)
        with open(file_name,'w+') as f:
            for tok in tokens:
                f.write(tok)
                f.write('\n')
        
    def phone_file_generate(phone_list, input_file, output_file):

        file_name = f'{output_file}/{os.path.basename(input_file)}'
        file_name = file_name.replace('.txt','.phn')
        print(file_name)
        with open(file_name,'w+') as f:
            for phone in phone_list:
                if phone[1] == None:
                    continue
                else:
                    phone_str = ' '.join(phone[1])
                    line = f'{phone[0]}\t\t\t\t{phone_str}\n'
                    f.write(line)

        print("phones and syllable file generation complete !!!")

