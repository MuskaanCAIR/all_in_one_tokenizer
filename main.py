import sys
import argparse
import os

from tools import tokenization,g2p


if __name__ == '__main__':

    #------------------parser argument------------------
    help_txt = 'language code:    "sh"-->shahmukhi| "ur"-->urdu| "zh"-->chinese| "bo"-->tibetan| "bn"-->bengali| "sin"-->sinhala'
    parser = argparse.ArgumentParser(usage='main.py -l [LANG_CODE] -i [INPUT_FILE_PATH] -o [OUTPUT_FOLDER_PATH]')
    parser.add_argument('-l','--lang',metavar='\b',help=help_txt,required=True)
    parser.add_argument('-i','--input',metavar='\b',help='\tabsolute file path of input file',required=True)
    parser.add_argument('-o','--output',metavar='\b',help='\toutput folder path')
    # parser.add_argument('-sh', '--shah', metavar='\b', help='shahmukhi')
    # parser.add_argument('-ur', '--urdu', metavar='\b', help='urdu')
    # parser.add_argument('-zh', '--zh', metavar='\b', help='chinese')
    # parser.add_argument('-bo', '--tib', metavar='\b', help='tibetan')
    # parser.add_argument('-bn', '--ben', metavar='\b', help='bengali')
    # parser.add_argument('-sin','--sin', metavar='\b', help='sinhala')
    args = parser.parse_args()

    lang_codes = ['sh', 'ur', 'zh', 'bo', 'bn', 'sin']
    file_formats = ['docx','txt','pdf','html']

    arguments = sys.argv
    input_path = arguments[4]
    try:
        output_path = arguments[6]
    except IndexError:
        output_path = './'
    input_lang_code = arguments[2]

        
    if input_lang_code == 'zh':
        tokenization.zh(input_file_path=input_path,
                        output_file_path=output_path)
        g2p.zh(input_file_path=input_path,
               output_file_path=output_path)
        
    elif input_lang_code == 'bo':
        tokenization.bo(input_file_path=input_path,
                        output_file_path=output_path)
        g2p.bo(input_file_path=input_path,
                output_file_path=output_path)

    elif input_lang_code == 'sh':
        tokenization.shah(input_file_path=input_path,
                        output_file_path=output_path)
        g2p.shah(input_file_path=input_path,
                output_file_path=output_path)

    elif input_lang_code == 'ur':
        tokenization.shah(input_file_path=input_path,
                        output_file_path=output_path)
        g2p.shah(input_file_path=input_path,
                output_file_path=output_path)
        
        input_file_name = os.path.basename(input_path)
        input_file_name = os.path.splitext(input_file_name)[0]
        gur_file_name = f'{output_path}/{input_file_name}_gur.phn'

        os.remove(gur_file_name)
        
      
    elif input_lang_code == 'bn':
        tokenization.bangla(input_file_path=input_path,
                            output_file_path=output_path)
        g2p.bangla(input_file_path=input_path,
                    output_file_path=output_path)

    elif input_lang_code == 'sin':
        tokenization.sinhala(input_file_path=input_path,
                            output_file_path=output_path)
        g2p.sinhala(input_file_path=input_path,
                    output_file_path=output_path)

    else:
        print("Incorrect Language Code!!\n")
        exit(0)
