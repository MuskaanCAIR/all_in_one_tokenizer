import sys
import argparse
import os

if __name__ == '__main__':

    #------------------parser argument------------------
    help_txt = 'language code:    "sh"-->shahmukhi| "ur"-->urdu| \
                "zh"-->chinese| "bo"-->tibetan| \
                "bn"-->bemgali| "sin"-->sinhala'
    parser = argparse.ArgumentParser(usage='main.py -l [lANG_CODE] -i [INPUT_FILE_PATH] -o [OUTPUT_FOLDER_PATH]')
    parser.add_argument('-l','--lang',metavar='\b',help=help_txt,required=True)
    parser.add_argument('-i','--input',metavar='\b',help='\tabsolute file path of input file',required=True)
    parser.add_argument('-o','--output',metavar='\b',help='\toutput folder path',required=True)
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
    input_lang_code = arguments[2]
    if input_lang_code not in lang_codes:
        print("Incorrect Language Code!!\n")
        exit(0)