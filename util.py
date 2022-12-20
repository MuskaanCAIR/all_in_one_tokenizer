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


    def phone_file_generate_sh(phone_list_hindi,
                               phone_list_gur,
                               hindi_file, 
                               gur_file):

        for i in range(4):
            os.chdir('..')
        print(os.getcwd())

        #hindi  (tok,transliteration[0],ph_list_gur)
        with open(hindi_file,'a') as f_hindi:
            # for phone in phone_list_hindi:
            if phone_list_hindi[1] == None:
                f_hindi.write("")
            else:
                phone_str = '\t'.join(phone_list_hindi[2])
                line = f'{phone_list_hindi[0]}\t\t\t{phone_list_hindi[1]}\t\t\t{phone_str}\n'
                f_hindi.write(line)

        #gurumukhi  (tok,transliteration[0],ph_list_gur)
        with open(gur_file,'a') as f_gur:
            # for phone in phone_list_gur:
                if phone_list_gur[1] == None:
                    f_gur.write("")
                else:
                    phone_str = '\t'.join(phone_list_gur[2])
                    line = f'{phone_list_gur[0]}\t\t\t{phone_list_gur[1]}\t\t\t{phone_str}\n'
                    f_gur.write(line)
