import argparse
import os.path
# import docx2txt
import os, sys
# from docx import Document
from sh_ur.pad.pat_v4.pat.S2G import *
from sh_ur.pad.pat_v4.pat.D2R import *
from sh_ur.pad.pat_v4.pat.G2D import *
from sh_ur.pad.pat_v4.pat.G2S import *
from sh_ur.pad.pat_v4.pat.sindhi2hindi import *
from sh_ur.pad.pat_v4.pat.hindi2sindhi import *

def stringToDocx(text,fileName):
    document = Document()
    para=text.split('\n')
    for i in para:
        document.add_paragraph(i)
    document.save(fileName)

def removeExtraNewLine(inputText):
    lines = inputText.split('\n')
    if lines:
        i = 0
        inputText = ''
        while i < (len(lines)):
            if lines[i] == '':
                lines.pop(i)
            inputText += lines[i] + '\n'
            i += 1
        return inputText
    return inputText

def readDocxWordFile(inputFileName):
    return docx2txt.process(inputFileName)


def readTxtFile(inputFileName):
    with open(inputFileName, 'r', encoding='utf-8') as f:
        return f.read()


def checkFileType(inputFile):
    org_text = ''
    if os.path.exists(inputFile):
        if inputFile.endswith('.docx'):
            org_text = readDocxWordFile(inputFile)
        elif inputFile.endswith('.txt'):
            org_text = readTxtFile(inputFile)
        elif inputFile.endswith('.html'):
            org_text = readTxtFile(inputFile)
        else:
            print('file format not valid.')
            exit()
    else:
        print("file name does not exist.")
        exit()
    return org_text


def checkOuputFile(outputFile):
    if os.path.exists(outputFile):
        print('output file name already exits. enter a valid output file name.')
        exit()
        # with open (outputFile,"w+") as f:
        #     return f

def shahmukhiToHindi(inputText):
    # python3 main.py -i ../data/shah/input/sample1 -o ../data/shah/output/out -if 'txt' -of 'txt' -s shah -d hindi

    obj = S2G()
    outputGur = obj.startReg(inputText) 
    # print(f'back to main.py\n{outputGur}')
    obj_g2d = Gur2Dev()
    return (outputGur,obj_g2d.convertGurmukhiToDevanagariText(outputGur))


def hindiToGurmukhi(inputText):
    obj_g2d = Gur2Dev()
    outputGurmukhi = obj_g2d.convertDevanagariToGurmukhiText(inputText)
    return outputGurmukhi


def gurmukhiToHindi(inputText):
    obj_g2d = Gur2Dev()
    return obj_g2d.convertGurmukhiToDevanagariText(inputText)


def hindiToShahmukhi(inputText):
    obj_g2d = Gur2Dev()
    outputGurmukhi = obj_g2d.convertDevanagariToGurmukhiText(inputText)
    return startReg(outputGurmukhi)


def shahmukhiToRoman(inputText):
    obj_d2r = HindiToRoman()
    output = shahmukhiToHindi(inputText)
    return obj_d2r.getRomanForm(output)

def hindiToRoman(inputText):
    obj_d2r = HindiToRoman()
    return obj_d2r.getRomanForm(inputText)

def sindhiToHindi(inputText):
    obj = Sindhi2Hindi()
    outputGur = obj.startReg(inputText)
    return outputGur

def hindiToSindhi(inputText):
    obj = Sindhi2HindiReverse()
    outputGur = obj.startReg(inputText)
    return outputGur

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='Arguments')
#     parser.add_argument('-i', '--input', help='absolute path of input file')
#     parser.add_argument('-o', '--output', help='absolute path of output file')
#     parser.add_argument('-if', '--inputFormat', help='file format of input file')
#     parser.add_argument('-of', '--outputFormat', help='file format of output file')

#     requiredNamed = parser.add_argument_group('required named arguments')
#     requiredNamed.add_argument('-s', '--source', help='source language code e.g. dari|shah|pashto|sindhi|balochi|kashmiri|gur|hindi|roman', required=True)
#     requiredNamed.add_argument('-d', '--destination', help='destination language code e.g. dari|shah|pashto|sindhi|balochi|kashmiri|gur|hindi|roman', required=True)

#     args = parser.parse_args()

#     langCodes={'shah':1,'dari':2,'pashto':3,'sindhi':4,'kashmiri':5,'balochi':6,'hindi':7,'roman':8,'gur':9}
#     fileFormats=['txt','docx','html']
#     choiceInputLang = args.source

#     if choiceInputLang not in langCodes:
#         print('incorrect input language code.')
#         exit()

#     choiceOutputLang=args.destination
#     if choiceOutputLang not in langCodes:
#         print('incorrect output language code.')
#         exit()

#     if args.input:
#         inputFile = args.input
#         if args.inputFormat:
#             if args.inputFormat in fileFormats:
#                 inputText = checkFileType(inputFile+'.'+args.inputFormat)
#                 if args.inputFormat=='docx':
#                     inputText=removeExtraNewLine(inputText)
#             else:
#                 print('input file format not supported')
#                 exit()
#         else:
#             print('input file format not provided')
#             exit()
#     else:
#         inputText=input('enter text:-')

#     outputflag=False
#     if args.output:
#         if args.outputFormat:
#             if args.outputFormat in fileFormats:
#                 outputFileName=args.output+'.'+args.outputFormat
#                 outputFileName = checkOuputFile(outputFileName)
#             else:
#                 print('output file format not supported')
#                 exit()
#         else:
#             print('output file format not provided')
#             exit()
#     else:
#         outputflag=True

#     print('started....')
#     if langCodes[choiceInputLang] == 1 and langCodes[choiceOutputLang] == 7:
#         # print('in the shah-->hindi condition')
#         output = shahmukhiToHindi(inputText)
#     elif langCodes[choiceInputLang] == 1 and langCodes[choiceOutputLang] == 8:
#         output = shahmukhiToRoman(inputText)
#     elif langCodes[choiceInputLang] == 7 and langCodes[choiceOutputLang] == 9:
#         output = hindiToGurmukhi(inputText)
#     elif langCodes[choiceInputLang] == 7 and langCodes[choiceOutputLang] == 1:
#         output = hindiToShahmukhi(inputText)
#     elif langCodes[choiceInputLang] == 9 and langCodes[choiceOutputLang] == 7:
#         output = gurmukhiToHindi(inputText)
#         # print(output)
#     elif langCodes[choiceInputLang] == 7 and langCodes[choiceOutputLang] == 8:
#         output =hindiToRoman(inputText)
#     elif langCodes[choiceInputLang] == 4 and langCodes[choiceOutputLang] == 7:
#         output = sindhiToHindi(inputText)
#     elif langCodes[choiceInputLang] == 7 and langCodes[choiceOutputLang] == 4:
#         output = hindiToSindhi(inputText)
#     else:
#         print('invalid input/output language code combination')

#     if outputflag:
#         print(output)
#     elif args.outputFormat=='docx':
#         stringToDocx(output,fileName=outputFileName)
#     else:
#         outputFileName = '../data/shah/output/out'
#         with open(outputFileName, 'w+', encoding='utf-8') as f:
#             f.write(output)

#     print('Completed....')