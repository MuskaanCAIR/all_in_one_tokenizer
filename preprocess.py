#conatins methods to preprocess input multilingual script for desired language
import re

def zh_preprocess(multi_corpus):

    process_file_path = "bin/cleaned_script_chinese.txt"
    with open(process_file_path,"w+") as f2:
        for letters in multi_corpus:
            r = re.compile(r'[\u4e00-\u9fff]')
            if r.search(letters):
                # print (letters) 
                f2.write(letters)
    return process_file_path

def bo_preprocess(multi_corpus):

    process_file_path = "bin/cleaned_script_tibetan.txt"
    with open(process_file_path,"w+") as f2:
        for letters in multi_corpus:
            r = re.compile(r'[\u0f00-\u0fff]')
            if r.search(letters):
                # print (letters) 
                f2.write(letters)
    return process_file_path

def sh_preprocess(multi_corpus):

    process_file_path = "bin/cleaned_script_shahmukhi.txt"
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

def ur_preprocess(multi_corpus):

    process_file_path = "bin/cleaned_script_urdu.txt"
    with open(process_file_path,"w+") as f2:
        for letters in multi_corpus:
            r = re.compile(r'[\u0600-\u06ff]')
            r1 = re.compile(r'\u0020')
            if r.search(letters) or r1.search(letters):
                f2.write(letters)
    # print(count)
    return process_file_path    