#conatins methods to preprocess input multilingual script for desired language
import re

def zh_preprocess(multi_corpus):

    process_file_path = "bin/cleaned_script_chinese.txt"
    with open(process_file_path,"w+") as f2:
        for letters in multi_corpus:
            r = re.compile(r'[\u4e00-\u9fff]')
            r1 = re.compile(r'\u0020')
            if r.search(letters) or r1.search(letters):
                # print (letters) 
                f2.write(letters)
    return process_file_path

def bo_preprocess(multi_corpus):

    process_file_path = "bin/cleaned_script_tibetan.txt"
    with open(process_file_path,"w+") as f2:
        for letters in multi_corpus:
            r = re.compile(r'[\u0f00-\u0fff]')
            r1 = re.compile(r'\u0020')
            if r.search(letters) or r1.search(letters):
                # print (letters) 
                f2.write(letters)
    return process_file_path

def sh_ur_preprocess(multi_corpus):

    process_file_path = "bin/cleaned_script_shahmukhi_or_urdu.txt"
    # count = 0
    with open(process_file_path,"w+") as f2:
        for letters in multi_corpus:
            r = re.compile(r'[\u0600-\u06ff]')
            r1 = re.compile(r'\u0020')
            # if r1.search(letters):
            #     count += 1
            if r.search(letters) or r1.search(letters):
                f2.write(letters)
    # print(count)
    return process_file_path  

def bangla_preprocess(multi_corpus):

    process_file_path = "bin/cleaned_script_bangla.txt"
    # count = 0
    with open(process_file_path,"w+") as f2:
        for letters in multi_corpus:
            r = re.compile(r'[\u0980-\u09ff]')
            r1 = re.compile(r'\u0020')
            # if r1.search(letters):
            #     count += 1
            if r.search(letters) or r1.search(letters):
                f2.write(letters)
    # print(count)
    return process_file_path  


def sinhala_preprocess(multi_corpus):

    process_file_path = "bin/cleaned_script_sinhala.txt"
    # count = 0
    with open(process_file_path,"w+") as f2:
        for letters in multi_corpus:
            r = re.compile(r'[\u0d80-\u0dff]')
            r1 = re.compile(r'\u0020')
            # if r1.search(letters):
            #     count += 1
            if r.search(letters) or r1.search(letters):
                f2.write(letters)
    # print(count)
    return process_file_path  