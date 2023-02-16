# ALL-in-One Tokenizer and G2P Converter

This project constitues tokenization/word segmentation and g2p conversion tools for Indic, abjad and logographic writing scripts. Different tokenization tools were tested and after thorough research, the best tool among all for each of the following languages was chosen. Following is a table representing language name and their respective tokenization and g2p tool used in the project:

| Language | Tokenizer    | G2P_tool                |
|----------|:------------:|:-----------------------:|
|Chinese   | Jieba        | G2pM                    |
|Tibetan   | Botok (Pybo) | THL                     |
|Shahmukhi | Spacy        | Sangam (transliteration)|
|Urdu      | Spacy        | Sangam (transliteration)|
|Bangla    | white space  | unicode                 |
|Sinhala   | white space  | unicode                 |

# How to use the tool

After downloading the zip file, type the this command in the terminal

        python main.py -l [LANG_CODE] -i [INPUT_FILE_PATH] -o [OUTPUT_FOLDER_PATH]
        
where the following should be replaced with any one of the options:

[LANG_CODE]: "sh"| "ur"| "zh"| "bo"| "bn"| "sin"

[INPUT_FILE_PATH]: the path to your input unstructured text file

[OUTPUT_FOLDER_PATH]: path to where you want your output files to be

# Output

The tool returns two files:
1. .wrd : containing tokenized words seperated by new line
2. .phn : containing phonetic expansion of the above tokenized words seperated by tabs 

