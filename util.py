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
        with open(file_name,'w+') as f:
            for tok in tokens:
                f.write(tok[0])
                f.write('\n')
        
        print("word file generation complete !!!")
        return file_name


