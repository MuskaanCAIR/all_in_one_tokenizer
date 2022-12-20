import numpy as np
import os.path
import re
import string
import io
import os,sys

FILESIZE = 260000
CORPUS = 150000
CORPUS_FILESIZE = 6400
DICSIZE = 62000
BISIZE = 4000
BIGRAM_SIZE = 200000
INDEX_SIZE = 8000
URDU_BIGRAM_SIZE = 3000
URDUCORPUS = 140000
SIMILAR_SIZE = 10000

word_total = 0
word_found = 0
bi_word_found = 0
word_not_found = 0
remove_diactric = 0
olda = 0
corpus_word_count = 0
corpus_found = 0
multi_count = 0
dict_word_count = 0

corpus_flag = 0
conversion_level = 3

max_joint = 0
total_joint = 0
merged_word_count = 0
average_joint_count = 0.0

urdu_corpus_total = 0
similar_word_count = 0

total_merged_words=[]
RULE_BASE_ONLY = 0
appPath=os.getcwd()#os.path.dirname(sys.argv[0])
appPath = os.path.join(appPath,'g2s')

QTS=[]
MSG = "Started"
isActive =  False

pre_bigram_total=0
post_bigram_total=0
pre_bigram_index_count=0
post_bigram_index_count=0
urdu_bigram_total=0
extra_word_count=0




gurmukhi_dict=np.empty((DICSIZE,26),dtype='i')
urdu_dict=np.empty((DICSIZE,26),dtype='i')


class urdu_bigram_gur:
    urdu1=[]
    urdu2=[]
    gurmukhi=[]
urdu_bigram=[]

class normalised_corpus():
    original_word=[]
    normalised_word=[]
    freq=0

corpus_words=[]

class similar_dictionary():
    original=[]
    similar=[]
sd=[]

class urdu_corpus:
    original_word=[]
    freq=0

urdu_corpus_words=[]

class bigram_corpus:
    first_word=[]
    second_word=[]
    freq=0
pre_bigram=[]
post_bigram=[]
pre_bigram_index=[]
post_bigram_index=[]

class tunion:
    uc=[]
    ui=0
    def __init__(self):
        self.uc=[0]*2
        self.ui=0

class wlist:
    word=[]
    count=0
wordlist=[]

def test_Satluj(text, len):
        max = 100
        sc = 0
        uc = 0
        rc = 0
        if (text[0] == 255) and (text[1] == 254): return False
        if max > len:
            max = len
        for i in range(1, max, 2):
            if text[i] < 11 and text[i] != 0:
                uc += 1
            else:
                if text[i - 1] < 127 and text[i] == 0:
                    rc += 1
                else:
                    sc += 1
        return (sc > uc)

def strlen(source):
    if len(source)==0: return 0
    size = len(source)
    length = 0
    for t in range(0, size):
        if source[t] != 0:
            length += 1
        else:
            break
    return length

def strcmp(str1, str2):
    len1 = strlen(str1)
    len2 = strlen(str2)
    if len1 > len2:
        length = len1
    else:
        length = len2
    for t in range(0, length):
        if str1[t] < str2[t]: return -1
        if str1[t] > str2[t]: return 1
    return 0

def strcpy(str1, str2):
    len2 = strlen(str2)
    for t in range(0, len2 + 1):
        if t < len(str1):
            try:
                str1[t] = str2[t]
            except IndexError:
                str1[t] = 0
                break
        else:
            str1[len(str1) - 1] = 0
            break

def StrToByteArray(str):
    # System.Text.Encoding Myencoding = new System.Text.Encoding
    rbytes = []
    for i in str:
        data = format(ord(i), '#06x')
        rbytes.append(int(data[-2:], 16))
        rbytes.append(int(data[-4:-2], 16))

    # TODO: i have removed first two bytes 255 and 254 when reading from file
    # if rbytes[0] == 255 and rbytes[1] == 254:
    #     rbytes.pop(0)
    #     rbytes.pop(0)
    # TODO:not checked how this test satluj function works
    if test_Satluj(rbytes, len(rbytes)):
        satlujBytes = []
        j = 0
        for i in range(0, len(rbytes), 2):
            j += 1
            satlujBytes[j] = rbytes[i]
        return satlujBytes
    else:
        return rbytes

def byte2Str(dBytes, length):
    word=''

    for i in range(0, length, 2):
        lastByte = hex(dBytes[i])
        lastByte = lastByte.split('0x')
        if len(str(lastByte[-1])) == 1:
            lastByte[-1] = '0' + lastByte[-1]

        firstByte = hex(dBytes[i + 1])
        firstByte = firstByte.split('0x')
        if len(str(firstByte[-1])) == 1:
            firstByte[-1] = '0' + firstByte[-1]
        code = '0x' + firstByte[-1] + lastByte[-1]
        char = int(code, 16)
        if char!=0:
            word += chr(char)
    return word

def check_punctuation(ch, ch1):
    if ch1 == 9:
        if (ch >= int("0x64", 16)) and (ch <= int("0x65", 16)):
            return 1
        return 0
    if ch1 == 10:
        if (ch >= int("0x66", 16)) and (ch <= int("0x6f", 16)): return 1
    if (ch1 == 0) and (ch == int("0x2d", 16)):
        return 0
    if ch1 != 10: return 1
    return 0

def start(input):
            file_length_in = 0
            file_length_out = 0
            global remove_diactric
            global word_found
            global word_not_found
            urdu =[0]*FILESIZE
            gurmukhi =[0]*FILESIZE
            if  isDacritic:
                remove_diactric = 0
            else:
                remove_diactric = 1

            if len(input)== 0:
                return "Empty String...."
            inputbytes = StrToByteArray(input)
            if len(inputbytes)+ 1 > len(urdu):
                return "TOO MUCH DATA"
            for  i in range(0,len(inputbytes)):
                urdu[i] =inputbytes[i]

            file_length_in = len(inputbytes)
            file_length_out=normalise_text(urdu, file_length_in, gurmukhi)
            file_length_in = file_length_out

            file_length_out=convert_gurmukhi_to_urdu(gurmukhi, file_length_in, urdu)
            total_words = word_found + word_not_found;
            return byte2Str(urdu, file_length_out)

def gurmukhi_word_to_urdu_rulebased(gurmukhi_word, gurmukhi_word_size, urdu_word):
    gurmukhi_strip = [0] * 40
    similar = [0] * 40
    urdu_subword = [0] * 40
    sub_similar =[0] * 40

    urdu_word_size = 0
    urdu_subword_size = 0
    scnt = 0
    UnicodeTo8(gurmukhi_word, gurmukhi_word_size, gurmukhi_strip)
    normalise_gurmukhi_dot(gurmukhi_strip)
    normalise_gurmukhi_word(gurmukhi_strip)
    rule_based_gurmukhi_word_to_urdu(gurmukhi_strip, urdu_word)
    urdu_word_size = len(urdu_word)
    return urdu_word_size

def convert_gurmukhi_to_urdu(gurmukhi, size, urdu):
            urdu_size=0
            temp_roman_word =[0]*5000
            gurmukhi_word = [0]*100
            urdu_word = [0]*100
            gurmukhi_strip = [0]*25

            urdu_word_size = 0
            gurmukhi_word_size = 0
            temp_roman_word_size = 0
            cword = 0

            gurmukhi_ptr = 0
            while  gurmukhi_ptr <= size:
                ch = gurmukhi[gurmukhi_ptr]
                ch1 = gurmukhi[gurmukhi_ptr + 1]
                if  check_punctuation(ch, ch1) > 0:
                    cword+=1
                    if  RULE_BASE_ONLY == 1:
                        urdu_word_size = gurmukhi_word_to_urdu_rulebased(gurmukhi_word, gurmukhi_word_size, urdu_word)
                    else:
                        urdu_word_size = gurmukhi_word_to_urdu(gurmukhi_word, gurmukhi_word_size, urdu_word)
                    i = 0
                    while i < urdu_word_size:
                        if urdu_word[i] == 254:
                            urdu[urdu_size] = ord('-')
                            urdu_size += 1
                            urdu[(urdu_size)] = 0
                            urdu_size += 1
                            i += 1
                        else:
                            urdu[urdu_size] = urdu_word[i]
                            urdu_size += 1
                        i += 1
                    gurmukhi_word_size = 0
                    while  check_punctuation(ch, ch1) > 0:
                        temp_roman_word_size=convert_gurmukhi_punctuation_to_urdu(ch, ch1, temp_roman_word)
                        for  i in range(0,temp_roman_word_size):
                            urdu[urdu_size] = temp_roman_word[i]
                            urdu_size+=1
                        gurmukhi_ptr += 2
                        if  gurmukhi_ptr >= size: break
                        ch = gurmukhi[gurmukhi_ptr]
                        ch1 = gurmukhi[gurmukhi_ptr + 1]
                else:
                    gurmukhi_word[gurmukhi_word_size] = ch
                    gurmukhi_word_size+=1
                    gurmukhi_word[gurmukhi_word_size] = ch1
                    gurmukhi_word_size+=1
                    gurmukhi_ptr += 2
            return urdu_size

def convert_gurmukhi_punctuation_to_urdu(ch, ch1, roman):
            urdu_to_roman =[0]*256
            roman_ptr = 0

            for  i in range(0,256):
                urdu_to_roman[i] = i
            for  i in range(128,256):
                urdu_to_roman[i] = 0

            urdu_to_roman[ord(',')] =int("0x0c",16)
            urdu_to_roman[ord(';')] =int("0x1b",16)
            urdu_to_roman[ord('?')] =int("0x1f",16)
            urdu_to_roman[ord('%')] =int("0x6a",16)
            urdu_to_roman[ord('*')] =int("0x6d",16)

            urdu_to_roman[int("0xff",16)] = 0


            if  (ch == 255) and (ch1 == 254):
                roman[roman_ptr] = ch
                roman_ptr+=1
                roman[roman_ptr] = ch1
                roman_ptr+=1
            else:
                if  ch1 == 9:
                    if  ch ==int("0x64",16):
                        roman[roman_ptr] =int("0xd4",16)
                        roman_ptr+=1
                        roman[roman_ptr] = 6
                        roman_ptr+=1
                    elif  ch ==int("0x65",16):
                        roman[roman_ptr] =int("0xd4",16)
                        roman_ptr+=1
                        roman[roman_ptr] = 6
                        roman_ptr+=1
                        roman[roman_ptr] =int("0xd4",16)
                        roman_ptr+=1
                        roman[roman_ptr] = 6
                        roman_ptr+=1
                else:
                    if  ch1 == 10:
                        if  (ch >=int("0x66",16)) and (ch <=int("0x6f",16)):
                            roman[roman_ptr] = (ord('0') + ch - int("0x66",16))
                            roman_ptr+=1
                            roman[roman_ptr] = 0
                            roman_ptr+=1

                    else:
                        if  ch1 == 0:
                            roman[roman_ptr] = urdu_to_roman[ch]
                            roman_ptr+=1
                            if  (ch == ord(',')) or (ch == ord(';')) or (ch == ord('?')) or (ch == ord('%')) or (ch == ord('*')):
                                roman[roman_ptr] = 6
                                roman_ptr+=1
                            else:
                                roman[roman_ptr] = 0
                                roman_ptr+=1
                        else:
                            roman[roman_ptr] = ch
                            roman_ptr+=1
                            roman[roman_ptr] = ch1
                            roman_ptr+=1
            roman_size = roman_ptr
            return roman_size

def write_frequency():
       pass

def check_urdu_word_bigram(urdu, p_urdu, urdu_size, p_urdu_size, roman, roman_size):
            global urdu_bigram_total
            low = 0
            mid = 0
            last = 0
            found = 0
            high = urdu_bigram_total
            read_word=[0]*20
            Urdu_UTF8=[0]*20
            Urdu1_UTF8=[0]*20
            temp=[0]*50
            UnicodeTo8(p_urdu, p_urdu_size, Urdu_UTF8)
            while  low <= high:
                mid = int((low + high) / 2)
                strcpy(read_word, urdu_bigram[mid][0])
                while  not(strcmp(urdu_bigram[mid][0], Urdu_UTF8) != 0):
                    found = 1
                    UnicodeTo8(urdu, urdu_size, Urdu1_UTF8)
                    if  not(strcmp(urdu_bigram[mid][1], Urdu1_UTF8) != 0):
                        strcpy(temp, urdu_bigram[mid][2])
                        k=0
                        for  i in range(0,strlen(temp)):
                            if  temp[i] == 255:
                                if  i < strlen(temp) - 1:
                                    roman[k] = 32
                                    k+=1
                                    roman[k] = 0
                                    k+=1
                                else:
                                    continue
                            else:
                                if  temp[i] == 254:
                                    roman[k] = ord('-')
                                    k+=1
                                    roman[k] = 0
                                    k+=1
                                else:
                                    roman[k] = temp[i]
                                    k+=1
                                    roman[k] = 9
                                    k+=1
                        roman_size = k
                        return 1
                    if  strcmp(urdu_bigram[mid][1], Urdu1_UTF8) > 0:
                        mid-=1
                        if last > 0:
                            mid = -1
                        last = -1
                    else:
                        mid+=1
                        if  last < 0:
                            mid = -1
                        last = 1

                    if  (mid < 0) or (mid >= urdu_bigram_total): return 0

                if  found > 0: return 0
                if  strcmp(read_word, Urdu_UTF8) < 0:
                    low = mid + 1
                else:
                    high = mid - 1
            return 0

def check_urdu_word_dictionary(gurmukhi, urdu):
            mid=0
            urdu_ptr = 0
            roman_ptr = 0
            flag = 0
            low = 0
            kk = 0
            break_flag = 0
            file_length_in = 0
            ccount = 0
            temp=[0]*40
            read_word=[0]*40
            Urdu_UTF8=[0]*40
            high = dict_word_count - 1
            while  low <= high:
                mid = int((low + high) / 2)
                strcpy(read_word, gurmukhi_dict[mid])
                if  not(strcmp(read_word, gurmukhi) != 0):
                    strcpy(temp, urdu_dict[mid])
                    k=0
                    for  i in range(0,strlen(temp)):
                        if  temp[i] == 255:
                            if  i < strlen(temp) - 1:
                                urdu[k] = 32
                                k+=1
                                urdu[k] = 0
                                k+=1
                            else:
                                continue
                        else:
                            if  temp[i] == 254:
                                urdu[k] = ord('-')
                                k+=1
                                urdu[k] = 0
                                k+=1
                            else:
                                if  temp[i] == 253:
                                    urdu[k] =int("0xf2",16)
                                    k+=1
                                    urdu[k] =int("0xfd",16)
                                    k+=1
                                else:
                                    if  remove_diactric > 0:
                                        if  (i < strlen(temp) - 1) and ((temp[i] ==int("0x50",16)) or (temp[i] ==int("0x51",16)) or (temp[i] ==int("0x58",16)) or (temp[i] ==int("0x4f",16)) or (temp[i] ==int("0x4e",16))):
                                            continue
                                        else:
                                            urdu[k] = temp[i]
                                            k+=1
                                            urdu[k] = 6
                                            k+=1

                                    else:
                                        urdu[k] = temp[i]
                                        k+=1
                                        urdu[k] = 6
                                        k+=1
                    return k
                if  strcmp(read_word, gurmukhi) < 0:
                    low = mid + 1
                else:
                    high = mid - 1
            return 0
def check_similar_word_dictionary(gurmukhi, similar):
            low = 0
            read_word=[0]*40
            global similar_word_count
            high = similar_word_count - 1
            strcpy(similar, gurmukhi)
            while  low <= high:
                mid = int((low + high) / 2)
                strcpy(read_word, sd[mid].original)
                if  not(strcmp(read_word, gurmukhi) != 0):
                    strcpy(similar, sd[mid].similar)
                    return 1
                if  strcmp(read_word, gurmukhi) < 0:
                    low = mid + 1
                else:
                    high = mid - 1
            return 0
def add_frequency(urdu, urdu_size):
            read_word=[0]*80
            Urdu_UTF8=[0]*40
            temp=[0]*80

            return 1


            if  urdu_size <= 2: return 1
            UnicodeToUtf8(urdu, urdu_size, Urdu_UTF8)
            for  i in range(0,word_total):
                if  not(strcmp(wordlist[i].word, Urdu_UTF8) != 0):
                    wordlist[i].count+=1
                    return 1
            wordlist[word_total].count = 1
            strcpy(wordlist[word_total].word, Urdu_UTF8)
            word_total+=1
            return 0
def normalise_urdu(urdu, urdu_size):
            for  i in range(0,urdu_size,2):
                if  (urdu[i] ==int("0x49",16)) or (urdu[i] ==int("0x4a",16)):
                    urdu[i] =int("0xcc",16)

def normalise_urdu_word(urdu, urdu_size):
            j = urdu_size
            temp_urdu=[0]*100
            j=0
            for  i in range(0,urdu_size,2):
                if  (urdu[i] ==int("0x27",16)) and (urdu[i + 2] ==int("0x53",16)):
                    temp_urdu[j] =int("0x22",16)
                    j+=1
                    i += 2
                else:
                    if  (i == urdu_size - 2) and (urdu[i] ==int("0x26",16)):
                        temp_urdu[j] =int("0xcc",16)
                        j+=1
                        temp_urdu[j] = 6
                        j+=1
                        temp_urdu[j] =int("0x54",16)
                        j+=1

                    else:
                        if  (urdu[i] ==int("0xd3",16)):
                            temp_urdu[j] =int("0xd2",16)
                            j+=1
                            temp_urdu[j] = 6
                            j+=1
                            temp_urdu[j] =int("0x54",16)
                            j+=1

                        else:
                            if  (urdu[i] ==int("0x4a",16)) or (urdu[i] ==int("0x49",16)):
                                temp_urdu[j] =int("0xcc",16)
                                j+=1
                            else:
                                if  ((urdu[i] ==int("0x85",16)) or (urdu[i] ==int("0x86",16))) and (urdu[i + 1] ==int("0xfe",16)):
                                    temp_urdu[j] =int("0x24",16)
                                    j+=1
                                else:
                                    temp_urdu[j] = urdu[i]
                                    j+=1
                temp_urdu[j] = 6
                j+=1

            for  i in range(0,j):
                urdu[i] = temp_urdu[i]
            urdu_size = j
def check_urdu_hyphen_dictionary(gurmukhi_word, urdu_word):
            gurmukhi_strip =[0]*20
            urdu_strip =[0]*40
            ulen = 0
            urdu_len = 0
            j=0
            for  i in range(0,strlen(gurmukhi_word)):
                if  gurmukhi_word[i] == 254:
                    gurmukhi_strip[j] = 0
                    j+=1
                    ulen = check_urdu_word_dictionary(gurmukhi_strip, urdu_strip)
                    if  ulen > 0:
                        for  k in range(0,ulen):
                            urdu_word[urdu_len] = urdu_strip[k]
                            urdu_len+=1
                        urdu_word[urdu_len] =int("0x2d",16)
                        urdu_len+=1
                        urdu_word[urdu_len] = 0
                        urdu_len+=1
                    else: return 0
                    j = 0
                    for k in range(ulen):
                        gurmukhi_strip[k]=0
                else:
                    gurmukhi_strip[j] = gurmukhi_word[i]
                    j+=1
            if  j > 0:


                ulen = check_urdu_word_dictionary(gurmukhi_strip, urdu_strip)
                if  ulen > 0:
                    for  k in range(0,ulen):
                        urdu_word[urdu_len] = urdu_strip[k]
                        urdu_len+=1
                else: urdu_len = 0
            return urdu_len
def check_urdu_hyphen_word(gurmukhi_word, urdu_word):
            gurmukhi_strip = [0]*40
            urdu_strip =[0]*40
            ulen = 0
            urdu_len = 0
            j=0
            global word_found
            global word_not_found
            for  i in range(0,strlen(gurmukhi_word)):
                if  gurmukhi_word[i] == 254:
                    gurmukhi_strip[j] = 0
                    j+=1
                    ulen = check_urdu_word_dictionary(gurmukhi_strip, urdu_strip)
                    if  ulen > 0:
                        for  k in range(0,ulen):
                            urdu_word[urdu_len] = urdu_strip[k]
                            urdu_len+=1
                        urdu_word[urdu_len] =int("0x2d",16)
                        urdu_len+=1
                        urdu_word[urdu_len] = 0
                        urdu_len+=1
                        word_found+=1
                    else:
                        normalise_gurmukhi_word(gurmukhi_strip)
                        rule_based_gurmukhi_word_to_urdu(gurmukhi_strip, urdu_strip)
                        improve_urdu_word(urdu_strip)
                        for  k in range(0,strlen(urdu_strip)):
                            urdu_word[urdu_len] = urdu_strip[k]
                            urdu_len+=1
                        urdu_word[urdu_len] =int("0x2d",16)
                        urdu_len+=1
                        urdu_word[urdu_len] = 0
                        urdu_len+=1
                        if  strlen(urdu_strip) > 2:
                            word_not_found+=1
                        else:
                            word_found+=1
                        add_frequency(gurmukhi_strip, j)
                    j = 0
                else:
                    gurmukhi_strip[j] = gurmukhi_word[i]
                    j+=1
            if  j > 0:
                ulen = check_urdu_word_dictionary(gurmukhi_strip, urdu_strip)
                if  ulen > 0:
                    for  k in range(0,ulen):
                        urdu_word[urdu_len] = urdu_strip[k]
                        urdu_len+=1
                    word_found+=1
                else:
                    normalise_gurmukhi_word(gurmukhi_strip)
                    rule_based_gurmukhi_word_to_urdu(gurmukhi_strip, urdu_strip)
                    improve_urdu_word(urdu_strip)
                    for  k in range(0,strlen(urdu_strip)):
                        urdu_word[urdu_len] = urdu_strip[k]
                        urdu_len+=1
                    if  strlen(urdu_strip) > 2:
                        word_not_found+=1
                    else:
                        word_found+=1
                    add_frequency(gurmukhi_strip, j)

            return urdu_len
def normalise_gurmukhi_dot(gurmukhi_word):
            t_gurmukhi_word=[0]*40
            j = 0

            i = 0
            while  gurmukhi_word[i] > 0:
                if  (gurmukhi_word[i] ==int("0x38",16)) and (gurmukhi_word[i + 1] ==int("0x3c",16)):
                    t_gurmukhi_word[j] =int("0x36",16)
                    i+=1
                else:
                    if  (gurmukhi_word[i] ==int("0x32",16)) and (gurmukhi_word[i + 1] ==int("0x3c",16)):
                        t_gurmukhi_word[j] =int("0x33",16)
                        i+=1
                    else:
                        if  (gurmukhi_word[i] ==int("0x16",16)) and (gurmukhi_word[i + 1] ==int("0x3c",16)):
                            t_gurmukhi_word[j] =int("0x59",16)
                            i+=1
                        else:
                            if  (gurmukhi_word[i] ==int("0x17",16)) and (gurmukhi_word[i + 1] ==int("0x3c",16)):
                                t_gurmukhi_word[j] =int("0x5a",16)
                                i+=1
                            else:
                                if  (gurmukhi_word[i] ==int("0x1c",16)) and (gurmukhi_word[i + 1] ==int("0x3c",16)):
                                    t_gurmukhi_word[j] =int("0x5b",16)
                                    i+=1
                                else:
                                    if  (gurmukhi_word[i] ==int("0x2b",16)) and (gurmukhi_word[i + 1] ==int("0x3c",16)):
                                        t_gurmukhi_word[j] =int("0x5e",16)
                                        i+=1
                                    else:
                                        t_gurmukhi_word[j] = gurmukhi_word[i]
                i+=1
                j+=1
            strcpy(gurmukhi_word, t_gurmukhi_word)
def gurmukhi_word_to_urdu(gurmukhi_word, gurmukhi_word_size, urdu_word):
            gurmukhi_strip=[0]*40
            similar=[0]*40
            urdu_subword=[0]*40
            sub_similar=[0]*40
            urdu_word_size = 0
            urdu_subword_size = 0
            scnt = 0
            global word_found
            global word_not_found
            UnicodeTo8(gurmukhi_word, gurmukhi_word_size, gurmukhi_strip)

            normalise_gurmukhi_dot(gurmukhi_strip)
            urdu_word_size = check_urdu_word_dictionary(gurmukhi_strip, urdu_word)
            if urdu_word_size  > 0:
                word_found+=1
                return urdu_word_size


            urdu_word_size = check_urdu_hyphen_dictionary(gurmukhi_strip, urdu_word)
            if urdu_word_size > 0:
                word_found+=1
                return urdu_word_size

            if  not(check_similar_word_dictionary(gurmukhi_strip, similar) != 0):
                return check_urdu_hyphen_word(gurmukhi_strip, urdu_word)
            else:
                scnt = 0
                while True:
                    strcpy(gurmukhi_strip, similar)
                    scnt+=1
                    if  scnt > 3: break
                    if  not check_similar_word_dictionary(gurmukhi_strip, similar) > 0:
                        break
                urdu_word_size = check_urdu_word_dictionary(similar, urdu_word)
                if  urdu_word_size > 0:
                    word_found+=1
                    return urdu_word_size

                j=0
                for  i in range(0,strlen(similar)+1):
                    if  (similar[i] < 254) and (similar[i] > 0):
                        gurmukhi_strip[j] = similar[i]
                        j+=1
                    else:
                        gurmukhi_strip[j] = 0
                        j+=1
                        j = 0
                        if  check_similar_word_dictionary(gurmukhi_strip, sub_similar) > 0:
                            strcpy(gurmukhi_strip, sub_similar)
                        urdu_subword_size = check_urdu_word_dictionary(gurmukhi_strip, urdu_subword)
                        if  urdu_subword_size > 0:
                            word_found+=1
                        else:
                            normalise_gurmukhi_word(gurmukhi_strip)
                            rule_based_gurmukhi_word_to_urdu(gurmukhi_strip, urdu_subword)
                            improve_urdu_word(urdu_subword)
                            urdu_subword_size = strlen(urdu_subword)
                            if  urdu_subword_size > 2:
                                word_not_found+=1
                            else:
                                word_found+=1
                            add_frequency(gurmukhi_word, gurmukhi_word_size)
                        if  similar[i] == 255:
                            urdu_subword[urdu_subword_size] = 32
                            urdu_subword_size+=1
                            urdu_subword[urdu_subword_size] = 0
                            urdu_subword_size+=1
                        else:
                            if  similar[i] == 254:
                                urdu_subword[urdu_subword_size] = ord('-')
                                urdu_subword_size+=1
                                urdu_subword[urdu_subword_size] = 0
                                urdu_subword_size+=1
                        for  k in range(0,urdu_subword_size):
                            urdu_word[urdu_word_size] = urdu_subword[k]
                            urdu_word_size+=1
                        urdu_subword_size = 0
            return urdu_word_size
def gurmukhi_word_to_urdu_rulebased(gurmukhi_word, gurmukhi_word_size, urdu_word):
            gurmukhi_strip=[0]*40
            similar=[0]*40
            urdu_subword=[0]*40
            sub_similar=[0]*40
            urdu_word_size = 0
            urdu_subword_size = 0
            scnt = 0
            UnicodeTo8(gurmukhi_word, gurmukhi_word_size, gurmukhi_strip)
            normalise_gurmukhi_dot(gurmukhi_strip)
            normalise_gurmukhi_word(gurmukhi_strip)
            rule_based_gurmukhi_word_to_urdu(gurmukhi_strip, urdu_word)
            urdu_word_size = strlen(urdu_word)
            return urdu_word_size

def improve_urdu_word(urdu):
            urdu_size = strlen(urdu)
            for  i in range(2,urdu_size):
                if  (urdu[i - 2] ==int("0x26",16)) and (urdu[i] ==int("0x26",16)):
                    urdu[i] =int("0xcc",16)
def check_gurmukhi_full_matra(u):
            exp = (((u > 3) and (u <int("0x0b",16))) or ((u >int("0x0c",16)) and (u <int("0x15",16))))
            if  exp:
                return 1
            else:
                return 0
def rule_based_gurmukhi_word_to_urdu(gurmukhi, urdu):
            pos = 0
            global olda
            cp=-1
            fc = 0
            sc = 0
            urdu_size = 0
            gurmukhi_size = strlen(gurmukhi)
            olda = 0
            urdu_size = 0
            cp+=1
            while  cp < gurmukhi_size:
                a = gurmukhi[cp]
                if  cp > 0:
                    prev = gurmukhi[cp - 1]
                if  cp > 0:
                    pos = 1
                if  cp == 0: pos = 0
                if  cp == gurmukhi_size - 1: pos = 2

                if  (a ==int("0x2",16)) and (cp == gurmukhi_size - 2) and (gurmukhi[cp + 1] ==int("0x5",16)): pos = 2
                fc,sc=convert_gurmukhi_urdu_char(a, pos)
                if  fc > 0:
                    urdu[(urdu_size)] = fc
                    urdu_size+=1
                    urdu[(urdu_size)] = 6
                    urdu_size+=1
                if  sc > 0:
                    urdu[(urdu_size)] = sc
                    urdu_size+=1
                    urdu[(urdu_size)] = 6
                    urdu_size+=1
                cp+=1
            urdu[(urdu_size)] = 0
            urdu_size+=1
def UnicodeTo8(UnicodeString, UnicodePos, szOut):
            len = 0
            j = 0
            for  i in range(0,UnicodePos,2):
                if  (not(UnicodeString[i + 1] != 0)) and (UnicodeString[i] == ord('-')):
                    szOut[j] = 254
                    j+=1
                else:
                    szOut[j] = UnicodeString[i]
                    j+=1
            szOut[j] = 0
            j+=1
            return
def convert_gurmukhi_urdu_char(u, pos):
            table=[0]*256

            for  i in range(0,255):
                table[i] = 0

            table[int("0x2",16)] =int("0x46",16)
            table[int("0x5",16)] =int("0x27",16)
            table[int("0x6",16)] =int("0x22",16)
            table[int("0x7",16)] =int("0x27",16)
            table[int("0x8",16)] =int("0x27",16)
            table[int("0x9",16)] =int("0x27",16)
            table[int("0xa",16)] =int("0x27",16)
            table[int("0xf",16)] =int("0x27",16)
            table[int("0x10",16)] =int("0x27",16)
            table[int("0x13",16)] =int("0x27",16)
            table[int("0x14",16)] =int("0x27",16)
            table[int("0x38",16)] =int("0x33",16)
            table[int("0x39",16)] =int("0xc1",16)
            table[int("0x15",16)] =int("0xa9",16)
            table[int("0x16",16)] =int("0xa9",16)
            table[int("0x17",16)] =int("0xaf",16)
            table[int("0x18",16)] =int("0xaf",16)
            table[int("0x19",16)] =int("0x46",16)
            table[int("0x1a",16)] =int("0x86",16)
            table[int("0x1b",16)] =int("0x86",16)
            table[int("0x1c",16)] =int("0x2c",16)
            table[int("0x1d",16)] =int("0x2c",16)
            table[int("0x1e",16)] =int("0x46",16)
            table[int("0x1f",16)] =int("0x79",16)
            table[int("0x20",16)] =int("0x79",16)
            table[int("0x21",16)] =int("0x88",16)
            table[int("0x22",16)] =int("0x88",16)
            table[int("0x23",16)] =int("0x46",16)
            table[int("0x24",16)] =int("0x2a",16)
            table[int("0x25",16)] =int("0x2a",16)
            table[int("0x26",16)] =int("0x2f",16)
            table[int("0x27",16)] =int("0x2f",16)
            table[int("0x28",16)] =int("0x46",16)
            table[int("0x2a",16)] =int("0x7e",16)
            table[int("0x2b",16)] =int("0x7e",16)
            table[int("0x2c",16)] =int("0x28",16)
            table[int("0x2d",16)] =int("0x28",16)
            table[int("0x2e",16)] =int("0x45",16)
            table[int("0x2f",16)] =int("0xcc",16)
            table[int("0x30",16)] =int("0x31",16)
            table[int("0x32",16)] =int("0x44",16)
            table[int("0x35",16)] =int("0x48",16)
            table[int("0x5c",16)] =int("0x91",16)
            table[int("0x36",16)] =int("0x34",16)
            table[int("0x59",16)] =int("0x2e",16)
            table[int("0x5a",16)] =int("0x3a",16)
            table[int("0x5b",16)] =int("0x32",16)
            table[int("0x5e",16)] =int("0x41",16)
            table[int("0x33",16)] =int("0x44",16)
            table[int("0x3e",16)] =int("0x27",16)
            table[int("0x3f",16)] =int("0x50",16)
            table[int("0x40",16)] =int("0xcc",16)
            table[int("0x41",16)] =int("0x4f",16)
            table[int("0x42",16)] =int("0x48",16)
            table[int("0x4b",16)] =int("0x48",16)
            table[int("0x4c",16)] =int("0x48",16)
            table[int("0x47",16)] =int("0xcc",16)
            table[int("0x48",16)] =int("0xcc",16)
            table[int("0x70",16)] =int("0x46",16)
            table[int("0x71",16)] =int("0x51",16)
            table[int("0x75",16)] =int("0xbe",16)
            table[254] = 254

            if  pos > 0:
                table[int("0x5",16)] =int("0x26",16)
                table[int("0x6",16)] =int("0x22",16)
                table[int("0x7",16)] =int("0x26",16)
                table[int("0x8",16)] =int("0x26",16)
                table[int("0x9",16)] =int("0x24",16)
                table[int("0xa",16)] =int("0x24",16)
                table[int("0x13",16)] =int("0x24",16)
                table[int("0x14",16)] =int("0x24",16)
                table[int("0xf",16)] =int("0x26",16)
                table[int("0x10",16)] =int("0x26",16)


            if  pos == 2:
                table[int("0x2",16)] =int("0xba",16)
                table[int("0x70",16)] =int("0xba",16)
                table[int("0x47",16)] =int("0xd2",16)
                table[5] =int("0x21",16)

            fc = table[u]

            for  i in range(0,255):
                table[i] = 0

            table[int("0x7",16)] =int("0x50",16)
            table[int("0x8",16)] =int("0xcc",16)
            table[int("0x9",16)] =int("0x4f",16)
            table[int("0xa",16)] =int("0x48",16)
            table[int("0xf",16)] =int("0xd2",16)
            table[int("0x10",16)] =int("0xd2",16)
            table[int("0x13",16)] =int("0x48",16)
            table[int("0x14",16)] =int("0x24",16)
            table[int("0x16",16)] =int("0xbe",16)
            table[int("0x18",16)] =int("0xbe",16)
            table[int("0x1b",16)] =int("0xbe",16)
            table[int("0x1d",16)] =int("0xbe",16)
            table[int("0x1e",16)] =int("0x2c",16)
            table[int("0x20",16)] =int("0xbe",16)
            table[int("0x22",16)] =int("0xbe",16)
            table[int("0x25",16)] =int("0xbe",16)
            table[int("0x27",16)] =int("0xbe",16)
            table[int("0x2b",16)] =int("0xbe",16)
            table[int("0x2d",16)] =int("0xbe",16)

            if  pos > 0:
                table[int("0x7",16)] = 0
                table[int("0x9",16)] = 0
                table[int("0xa",16)] = 0
                table[int("0x13",16)] = 0
                table[int("0x14",16)] = 0
                table[int("0x10",16)] = 0

            sc = table[u]

            return fc, sc
def checkMATRA(u):
            return (u ==int("0x0622",16) or u ==int("0x0627",16) or u ==int("0x0650",16) or u ==int("0x064f",16) or u ==int("0x064e",16) or u == 1740)
def read_binary_corpus(corpus_words, corpus_word_count):


            i = 0

            FILE_NAME = appPath + "fcorpus.bin"
            if  not os.path.exists(FILE_NAME):
                printMSG(f"{FILE_NAME} File not exists! ")
                return


            r = open(FILE_NAME, 'rb')
            corpus_word_count = int.from_bytes(r.read(4),'little')
            for  i in range(0,corpus_word_count):
                corpus_words.append(normalised_corpus())
                corpus_words[i].original_word = r.read(16)
                corpus_words[i].normalised_word = r.read(16)
                corpus_words[i].freq = int.from_bytes(r.read(4),'little')
            r.close()
def read_similar_dict(similar_words):


            FILE_NAME = appPath + "similar.bin"
            global similar_word_count
            if  not os.path.exists(FILE_NAME):
                printMSG(f"{FILE_NAME} File not exists! ")
                return


            r = open(FILE_NAME, 'rb')
            similar_word_count = int.from_bytes(r.read(4),'little')
            for  i in range(0,similar_word_count):
                similar_words.append(similar_dictionary)
                similar_words[i].original =r.read(len(similar_words[i].original));
                similar_words[i].similar =r.read(len(similar_words[i].similar));
            r.close()
            return similar_word_count
def read_urdu_gurmukhi_dict():



            global dict_word_count
            corpus_word=[0]*200
            freq=[0]*8
            FILE_NAME = appPath + "dict_s2g.bin"
            if not os.path.exists(FILE_NAME):
                printMSG(f"{FILE_NAME} File not exists! ")
                return

            r = open(FILE_NAME, 'rb')
            dict_word_count = int.from_bytes(r.read(4),'little')
            for  i in range(0,dict_word_count):
                dBytes=[]
                rawBytes = r.read(len(gurmukhi_dict[i]))
                for byte in rawBytes:
                    dBytes.append(byte)
                gurmukhi_dict[i]=np.array(dBytes)

                dBytes.clear()
                rawBytes = r.read(len(urdu_dict[i]))
                for byte in rawBytes:
                    dBytes.append(byte)
                urdu_dict[i]=np.array(dBytes)
            r.close()

def read_urdu_corpus():
            FILE_NAME = appPath + "ucorpus.bin"
            global urdu_corpus_word_count
            if not os.path.exists(FILE_NAME):
                printMSG(f"{FILE_NAME} File not exists! ")
                return


            r = open(FILE_NAME, 'rb')
            urdu_corpus_word_count = int.from_bytes(r.read(4),'little')
            for  i in range(0,urdu_corpus_word_count):
                urdu_corpus_words[i].original_word=r.read(len(urdu_corpus_words[i]))
                urdu_corpus_words[i].freq = int.from_bytes(r.read(4),'little')
            r.Close()
def read_pre_bigram_corpus(pre_bigram, pre_bigram_total, pre_bigram_index, pre_bigram_index_count):
            pre_count = 0
            corpus_word=[0]*200
            freq=[0]*8
            word=[0]*20
            t_corpus=bigram_corpus()
            word[0] = 0
            FILE_NAME = appPath + "pre_bigram.bin"
            if  not os.path.exists(FILE_NAME):
                printMSG(f"{FILE_NAME} File not exists! ")
                return


            r = open(FILE_NAME, 'rb')
            pre_bigram_total = int.from_bytes(r.read(4),'little')
            for  i in range(0,pre_bigram_total):
                pre_bigram[i].first_word = r.read(len(pre_bigram[i].first_word))
                pre_bigram[i].second_word = r.read(len(pre_bigram[i].second_word))
                pre_bigram[i].freq = int.from_bytes(r.read(4),'little')
            r.close()

            FILE_NAME = appPath + "pre_normal_bigram.bin"
            if not os.path.exists(FILE_NAME):
                printMSG(f"{FILE_NAME} File not exists! ")
                return

            r2 = open(FILE_NAME, 'rb')
            pre_bigram_index_count = int.from_bytes(r2.read(4),'little')
            pre_bigram_index_count = 0
            for  i in range(0,pre_bigram_total):
                try:
                    pre_bigram_index[i].normalised_word = r2.read(len(pre_bigram_index[i].normalised_word))
                    pre_bigram_index[i].index = int.from_bytes(r2.read(4),'little')
                    pre_bigram_index_count+=1
                except IndexError as e:
                    printMSG("read_pre_bigram_corpus |::| " + e)
                    break

            r2.Close()
def read_post_bigram_corpus(post_bigram, post_bigram_total, post_bigram_index, post_bigram_index_count):
            post_count = 0
            corpus_word=[0]*200
            freq=[0]*8
            word=[0]*20
            t_corpus=bigram_corpus()
            word[0] = 0
            FILE_NAME = appPath + "post_bigram.bin"
            if not os.path.exists(FILE_NAME):
                printMSG(f"{FILE_NAME} File not exists! ")
                return

            r = open(FILE_NAME, 'rb')
            post_bigram_total = int.from_bytes(r.read(4), 'little')
            for  i in range(0,post_bigram_total):
                post_bigram[i].first_word = r.read(len(post_bigram[i].first_word))
                post_bigram[i].second_word = r.read(len(post_bigram[i].second_word))
                post_bigram[i].freq = int.from_bytes(r.read(4), 'little')
            r.close()

            FILE_NAME = appPath + "post_normal_bigram.bin"
            if not os.path.exists(FILE_NAME):
                printMSG(f"{FILE_NAME} File not exists! ")
                return

            r2 = open(FILE_NAME, 'rb')

            post_bigram_index_count = int.from_bytes(r2.read(4), 'little')
            post_bigram_index_count = 0
            for  i in range(0,post_bigram_total):
                try:
                    post_bigram_index[i].normalised_word = r2.read(len(post_bigram_index[i].normalised_word))
                    post_bigram_index[i].index = int.from_bytes(r2.read(4), 'little')
                    post_bigram_index_count+=1
                except:
                    break
            r2.close()
def read_urdu_bigram():
            FILE_NAME = appPath + "BigramUrdu.bin"
            global urdu_bigram_total
            if not os.path.exists(FILE_NAME):
                printMSG(f"{FILE_NAME} File not exists! ")
                return

            r = open(FILE_NAME, 'rb')
            urdu_bigram_total = int.from_bytes(r.read(4), 'little')
            for  i in range(0,urdu_bigram_total):
                urdu_bigram[i].urdu1=r.read(len(urdu_bigram[i]))
                urdu_bigram[i].urdu2=r.read(len(urdu_bigram[i]))
                urdu_bigram[i].gurmukhi=r.read(len(urdu_bigram[i]))
            r.close()

def get_corpus_pos(corpus_words, count, gurmukhi_word):
            for  i in range(count - 1,-1,-1):
                if  strcmp(corpus_words[i].normalised_word, gurmukhi_word) <= 0:
                    return i
            return 0
def search_corpus(corpus_words, total, gurmukhi_word):

            high = total - 1
            low = 0
            mid = 0
            read_word=[0]*16

            while  low <= high:
                mid = int((low + high) / 2)
                strcpy(read_word, corpus_words[mid].normalised_word)
                if  not(strcmp(read_word, gurmukhi_word) != 0):
                    return mid
                if  strcmp(read_word, gurmukhi_word) < 0:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1
def get_word_corpus(gurmukhi_int, gurmukhi_int_size, final_word):
            multi = 0
            gurmukhi_word=[0]*20
            first_gurmukhi_word=[0]*16
            rest_gurmukhi_word=[0]*16

            final_word[0] = 0
            pos = search_corpus(corpus_words, corpus_word_count, first_gurmukhi_word)
            if  pos < 0: return 0
            strcpy(final_word, corpus_words[pos].original_word)
            if  multi > 0:
                strcat(final_word, rest_gurmukhi_word)
            return 1
def check_gurmukhi_corpus(gurmukhi_int, gurmukhi_int_size, final_word):
            multi = 0
            gurmukhi_word=[0]*20
            first_gurmukhi_word=[0]*16
            rest_gurmukhi_word=[0]*16


            pos = search_corpus(corpus_words, corpus_word_count, first_gurmukhi_word)
            if  pos < 0: return 0
            low = high = pos
            strcpy(final_word, corpus_words[pos].original_word)
            if  multi > 0:
                strcat(final_word, rest_gurmukhi_word)
            return corpus_words[pos].freq
def normalise_gurmukhi_word(gurmukhi_word):
            gurmukhi_int_size = strlen(gurmukhi_word)
            t_gurmukhi_word=[0]*30
            zer_flag = remove_diactric
            i = j = 0
            while  i < gurmukhi_int_size:
                if  (gurmukhi_word[i] ==int("0x38",16)) and (gurmukhi_word[i + 1] ==int("0x3c",16)):
                    t_gurmukhi_word[j] =int("0x36",16)
                    i+=1
                else:
                    if  (gurmukhi_word[i] ==int("0x32",16)) and (gurmukhi_word[i + 1] ==int("0x3c",16)):
                        t_gurmukhi_word[j] =int("0x33",16)
                        i+=1
                    else:
                        if  (gurmukhi_word[i] ==int("0x16",16)) and (gurmukhi_word[i + 1] ==int("0x3c",16)):
                            t_gurmukhi_word[j] =int("0x59",16)
                            i+=1
                        else:
                            if  (gurmukhi_word[i] ==int("0x17",16)) and (gurmukhi_word[i + 1] ==int("0x3c",16)):
                                t_gurmukhi_word[j] =int("0x5a",16)
                                i+=1
                            else:
                                if  (gurmukhi_word[i] ==int("0x1c",16)) and (gurmukhi_word[i + 1] ==int("0x3c",16)):
                                    t_gurmukhi_word[j] =int("0x5b",16)
                                    i+=1
                                else:
                                    if  (gurmukhi_word[i] ==int("0x2b",16)) and (gurmukhi_word[i + 1] ==int("0x3c",16)):
                                        t_gurmukhi_word[j] =int("0x5e",16)
                                        i+=1
                                    else:

                                        if  gurmukhi_word[i] ==int("0x71",16):
                                            t_gurmukhi_word[j] = gurmukhi_word[i + 1]
                                            t_gurmukhi_word[j + 1] = gurmukhi_word[i]
                                            i+=1
                                            j+=1
                                        else:
                                            if  gurmukhi_word[i] ==int("0x4d",16):
                                                if  gurmukhi_word[i + 1] ==int("0x39",16):
                                                    t_gurmukhi_word[j] =int("0x75",16)
                                                    i+=1
                                                else:
                                                    j-=1
                                            else:
                                                if  (i > 0) and ((gurmukhi_word[i - 1] ==int("0x3e",16)) or (gurmukhi_word[i - 1] ==int("0x6",16))) and (gurmukhi_word[i] ==int("0x7",16)) and (gurmukhi_word[i + 1] ==int("0x6",16)):
                                                    t_gurmukhi_word[j] =int("0x2f",16)
                                                    t_gurmukhi_word[j + 1] =int("0x3e",16)
                                                    j+=1
                                                    i+=1
                                                else:
                                                    if  (i > 0) and (gurmukhi_word[i - 1] ==int("0x8",16)) and (gurmukhi_word[i] ==int("0x6",16)):
                                                        t_gurmukhi_word[j] =int("0x3e",16)
                                                    else:
                                                        if  (i > 0) and (gurmukhi_word[i] ==int("0x7",16)) and (gurmukhi_word[i + 1] ==int("0x6",16)):
                                                            t_gurmukhi_word[j] =int("0x2f",16)
                                                            t_gurmukhi_word[j + 1] =int("0x3e",16)
                                                            j+=1
                                                            i+=1
                                                        else:
                                                            if  (gurmukhi_word[i] ==int("0x38",16)) and (gurmukhi_word[i + 1] ==int("0x3c",16)):
                                                                t_gurmukhi_word[j] =int("0x36",16)
                                                                i+=1
                                                            else:
                                                                if  (gurmukhi_word[i] ==int("0x16",16)) and (gurmukhi_word[i + 1] ==int("0x3c",16)):
                                                                    t_gurmukhi_word[j] =int("0x59",16)
                                                                    i+=1
                                                                else:
                                                                    if  (gurmukhi_word[i] ==int("0x17",16)) and (gurmukhi_word[i + 1] ==int("0x3c",16)):
                                                                        t_gurmukhi_word[j] =int("0x5a",16)
                                                                        i+=1
                                                                    else:
                                                                        if  (gurmukhi_word[i] ==int("0x1c",16)) and (gurmukhi_word[i + 1] ==int("0x3c",16)):
                                                                            t_gurmukhi_word[j] =int("0x5b",16)
                                                                            i+=1
                                                                        else:
                                                                            if  (gurmukhi_word[i] ==int("0x2b",16)) and (gurmukhi_word[i + 1] ==int("0x3c",16)):
                                                                                t_gurmukhi_word[j] =int("0x5e",16)
                                                                                i+=1
                                                                            else:
                                                                                if  (gurmukhi_word[i] ==int("0x32",16)) and (gurmukhi_word[i + 1] ==int("0x3c",16)):
                                                                                    t_gurmukhi_word[j] =int("0x33",16)
                                                                                    i+=1
                                                                                else:
                                                                                    if  (i > 0) and (gurmukhi_word[i] ==int("0x3f",16)) and (gurmukhi_word[i + 1] ==int("0x6",16)):
                                                                                        t_gurmukhi_word[j] =int("0x2f",16)
                                                                                        t_gurmukhi_word[j + 1] =int("0x3e",16)
                                                                                        j+=1
                                                                                        i+=1
                                                                                    else:
                                                                                        if  (i > 0) and (gurmukhi_word[i] ==int("0x70",16)) and (gurmukhi_word[i + 1] ==int("0x28",16)):
                                                                                            t_gurmukhi_word[j] =int("0x28",16)
                                                                                            t_gurmukhi_word[j + 1] =int("0x71",16)
                                                                                            i+=1
                                                                                            j+=1

                                                                                        else:
                                                                                            if  (i > 0) and (gurmukhi_word[i] ==int("0x70",16)) and (gurmukhi_word[i + 1] ==int("0x2a",16)):
                                                                                                t_gurmukhi_word[j] =int("0x2e",16)
                                                                                                t_gurmukhi_word[j + 1] =int("0x2a",16)
                                                                                                i+=1
                                                                                                j+=1

                                                                                            else:
                                                                                                if  (i > 0) and (gurmukhi_word[i] ==int("0x3f",16)) and ((gurmukhi_word[i + 1] ==int("0x13",16)) or (gurmukhi_word[i + 1] ==int("0x9",16))):
                                                                                                    t_gurmukhi_word[j] =int("0x2f",16)
                                                                                                    t_gurmukhi_word[j + 1] =int("0x4b",16)
                                                                                                    i+=1
                                                                                                    j+=1

                                                                                                else:
                                                                                                    if  (i > 0) and (gurmukhi_word[i] ==int("0x7",16)) and ((gurmukhi_word[i + 1] ==int("0x13",16)) or (gurmukhi_word[i + 1] ==int("0x9",16))):
                                                                                                        t_gurmukhi_word[j] =int("0x7",16)
                                                                                                        t_gurmukhi_word[j + 1] =int("0x2f",16)
                                                                                                        t_gurmukhi_word[j + 2] =int("0x4b",16)
                                                                                                        i+=1
                                                                                                        j+=1
                                                                                                        j+=1

                                                                                                    else:
                                                                                                        if  (i > 0) and (gurmukhi_word[i] ==int("0x8",16)) and ((gurmukhi_word[i + 1] ==int("0x0f",16)) or (gurmukhi_word[i + 1] ==int("0x0f",16))):
                                                                                                            t_gurmukhi_word[j] =int("0x8",16)
                                                                                                            t_gurmukhi_word[j + 1] =int("0x47",16)
                                                                                                            i+=1
                                                                                                            j+=1

                                                                                                        else:
                                                                                                            if  (i > 0) and (gurmukhi_word[i] ==int("0x7",16)) and (gurmukhi_word[i + 1] ==int("0xa",16)):
                                                                                                                t_gurmukhi_word[j] =int("0x7",16)
                                                                                                                t_gurmukhi_word[j + 1] =int("0x2f",16)
                                                                                                                t_gurmukhi_word[j + 2] =int("0x42",16)
                                                                                                                i+=1
                                                                                                                j+=1
                                                                                                                j+=1

                                                                                                            else:
                                                                                                                if  (i > 0) and (gurmukhi_word[i] ==int("0x41",16)) and (gurmukhi_word[i + 1] ==int("0x6",16)):
                                                                                                                    t_gurmukhi_word[j] =int("0x41",16)
                                                                                                                    t_gurmukhi_word[j + 1] =int("0x35",16)
                                                                                                                    t_gurmukhi_word[j + 2] =int("0x3e",16)
                                                                                                                    i+=1
                                                                                                                    j+=1
                                                                                                                    j+=1

                                                                                                                else:
                                                                                                                    if  (i > 0) and (gurmukhi_word[i] ==int("0x3f",16)) and (gurmukhi_word[i + 1] ==int("0xa",16)):
                                                                                                                        t_gurmukhi_word[j] =int("0x3f",16)
                                                                                                                        t_gurmukhi_word[j + 1] =int("0x2f",16)
                                                                                                                        t_gurmukhi_word[j + 2] =int("0x42",16)
                                                                                                                        i+=1
                                                                                                                        j+=1
                                                                                                                        j+=1

                                                                                                                    else:
                                                                                                                        if  (i > 0) and (gurmukhi_word[i] ==int("0x6",16)) and not((gurmukhi_word[i - 1] ==int("0x21",16)) or (gurmukhi_word[i - 1] ==int("0x26",16)) or (gurmukhi_word[i - 1] ==int("0x27",16)) or (gurmukhi_word[i - 1] ==int("0x30",16)) or (gurmukhi_word[i - 1] ==int("0x3f",16)) or (gurmukhi_word[i - 1] ==int("0x5b",16)) or (gurmukhi_word[i - 1] ==int("0x4b",16)) or (gurmukhi_word[i - 1] ==int("0x4c",16)) or (gurmukhi_word[i - 1] ==int("0x42",16)) or (gurmukhi_word[i - 1] ==int("0x5c",16))):
                                                                                                                            t_gurmukhi_word[j] =int("0x3e",16)
                                                                                                                        else:
                                                                                                                            if  ((gurmukhi_word[i] ==int("0x10",16)) or (gurmukhi_word[i] ==int("0x0f",16))) and (i != gurmukhi_int_size - 1):
                                                                                                                                t_gurmukhi_word[j] =int("0x8",16)

                                                                                                                            else:
                                                                                                                                if  (i > 0) and ((gurmukhi_word[i] ==int("0x2",16)) or (gurmukhi_word[i] ==int("0x70",16))) and ((gurmukhi_word[i + 1] ==int("0x2c",16)) or (gurmukhi_word[i + 1] ==int("0x2d",16))):
                                                                                                                                    t_gurmukhi_word[j] =int("0x2e",16)
                                                                                                                                else:
                                                                                                                                    if  (gurmukhi_word[i] ==int("0x48",16)) and (i == gurmukhi_int_size - 1):
                                                                                                                                        t_gurmukhi_word[j] =int("0x47",16)

                                                                                                                                    else:
                                                                                                                                        if  (gurmukhi_word[i] ==int("0x70",16)) and ((gurmukhi_word[i + 1] ==int("0x2e",16))):
                                                                                                                                            t_gurmukhi_word[j] =int("0x2e",16)
                                                                                                                                            j+=1
                                                                                                                                            t_gurmukhi_word[j] =int("0x71",16)

                                                                                                                                            i+=1

                                                                                                                                        else:
                                                                                                                                            t_gurmukhi_word[j] = gurmukhi_word[i]
                i+=1
                j+=1
            t_gurmukhi_word[j] = 0
            strcpy(gurmukhi_word, t_gurmukhi_word)

            if  zer_flag > 0:
                gurmukhi_int_size = strlen(gurmukhi_word)
                i = j = 0
                while  i < gurmukhi_int_size:
                    if  (i < gurmukhi_int_size - 1) and ((gurmukhi_word[i] ==int("0x3f",16)) or (gurmukhi_word[i] ==int("0x41",16)) or (gurmukhi_word[i] ==int("0x71",16))):
                        i+=1
                    else:
                        if  (i == 0) and ((gurmukhi_word[i] ==int("0x7",16)) or (gurmukhi_word[i] ==int("0x9",16))):
                            t_gurmukhi_word[j] =int("0x5",16)
                            j+=1
                            i+=1
                        else:
                            t_gurmukhi_word[j] = gurmukhi_word[i]
                            i+=1
                            j+=1
                t_gurmukhi_word[j] = 0
                strcpy(gurmukhi_word, t_gurmukhi_word)
def check_gurmukhi_matra(u):
            return (((u > 3) and (u <int("0x0b",16))) or ((u >int("0x0c",16)) and (u <int("0x15",16))) or ((u >int("0x3d",16)) and (u <int("0x43",16))) or ((u >int("0x45",16)) and (u <int("0x4d",16))))
def check_gurmukhi_diactric(u):
            return ((u >int("0x3d",16)) and (u <int("0x4d",16)))
def UnicodeToUtf8(UnicodeString, UnicodePos, szOut):
            len = 0
            j = 0
            uc1 = tunion(2)
            normalise_urdu(UnicodeString, UnicodePos)
            for  i in range(0,UnicodePos,2):
                uc1.uc[0] = UnicodeString[i]
                uc1.uc[1] = UnicodeString[i + 1]

                if  uc1.ui <int("0x0080",16):
                    szOut[j] = UnicodeString[i]
                    j+=1

                elif  uc1.ui <int("0x0800",16):
                    szOut[j] = int("0xc0",16) | uc1.ui >> 6
                    j+=1
                    szOut[j] = int("0x80",16) | (uc1.ui & int("0x3f",16))
                    j+=1
                else:
                    szOut[j] = int("0xe0",16) | uc1.ui >> 12
                    j+=1
                    szOut[j] = int("0x80",16) | (uc1.ui >> 6 & int("0x3f",16))
                    j+=1
                    szOut[j] = int("0x80",16) | (uc1.ui & int("0x3f",16))
                    j+=1
            szOut[j] = 0
            return
def check_long_gurmukhi_matra(u):
            return (((u > 3) and (u <int("0x0b",16))) or ((u >int("0x0c",16)) and (u <int("0x15",16))) or (u ==int("0x3e",16)) or (u ==int("0x40",16)) or (u ==int("0x42",16)) or ((u >int("0x45",16)) and (u <int("0x4d",16))))
def search_word_pre_bigram(word, low, high, selected_word):
            read_word=[0]*20

            while  low <= high:
                mid = int((low + high) / 2)
                strcpy(read_word, pre_bigram[mid].second_word)
                if  not(strcmp(read_word, word) != 0):
                    strcpy(selected_word, pre_bigram[mid].first_word)
                    return pre_bigram[mid].freq
                if  strcmp(read_word, word) < 0:
                    low = mid + 1
                else:
                    high = mid - 1

            return 0
def search_word_post_bigram(word, low, high, selected_word):
            read_word=[0]*20

            while  low <= high:
                mid = int((low + high) / 2)
                strcpy(read_word, post_bigram[mid].first_word)
                if  not(strcmp(read_word, word) != 0):
                    strcpy(selected_word, post_bigram[mid].second_word)
                    return post_bigram[mid].freq
                if  strcmp(read_word, word) < 0:
                    low = mid + 1
                else:
                    high = mid - 1

            return 0
def search_word_pre_bigram_index(word, start, end):
            read_word=[0]*20
            global pre_bigram_index_count
            high = pre_bigram_index_count - 1
            low = 0
            while  low <= high:
                mid = int((low + high) / 2)
                strcpy(read_word, pre_bigram_index[mid].normalised_word)
                if  not(strcmp(read_word, word) != 0):
                    if  mid == 0:
                        start = 0
                    else:
                        start = pre_bigram_index[mid - 1].index + 1
                    end = pre_bigram_index[mid].index
                    return 1
                if  strcmp(read_word, word) < 0:
                    low = mid + 1
                else:
                    high = mid - 1

            return 0
def search_word_post_bigram_index(word, start, end):
            global post_bigram_index_count
            read_word=[0]*20
            mid=0
            high = post_bigram_index_count - 1
            low = 0
            while  low <= high:
                mid = int((low + high) / 2)
                strcpy(read_word, post_bigram_index[mid].normalised_word)
                if  not(strcmp(read_word, word) != 0):
                    if  mid == 0:
                        start = 0
                    else:
                        start = post_bigram_index[mid - 1].index + 1
                    end = post_bigram_index[mid].index
                    return 1
                if  strcmp(read_word, word) < 0:
                    low = mid + 1
                else:
                    high = mid - 1

            return 0
def get_freq(word):
            global corpus_word_count
            low = 0
            mid = 0
            high = corpus_word_count - 1
            gurmukhi_int = [0]*20
            normalise=[0]*20
            read_word=[0]*20

            for  k in range(0,strlen(word)):
                gurmukhi_int[k] = word[k]

            while  low <= high:
                mid = int((low + high) / 2)
                strcpy(read_word, corpus_words[mid].normalised_word)
                if  not(strcmp(read_word, normalise) != 0):
                    if  not(strcmp(corpus_words[mid].original_word, word) != 0):
                        return corpus_words[mid].freq
                    else:
                        return 0
                if  strcmp(read_word, normalise) < 0:
                    low = mid + 1
                else:
                    high = mid - 1
            return 0

def test_font_type(text, len):
            max = 100
            sc = 0
            uc = 0
            ac = 0
            if  (text[0] == 255) and (text[1] == 254): return 1
            if  max > len:
                max = len
            for  i in range(1,max,2):
                if  text[i] < 11: uc+=1
                else:
                    sc+=1
                    ac+=1
            for  i in range(0,max,2):
                if  text[i] < 122:
                    uc+=1
                    ac+=1
                else:
                    sc+=1
            if  (uc > sc) and (uc > ac): return 1
            if  (sc > ac) and (sc > uc): return 2
            if  (ac > sc) and (ac > uc): return 3
            return 0
def expand_satluj_text(satluj, satluj_len, normalise, normalise_len):
    partial_unicode = [0] * 10
    i = 0
    k = 0

    for i in range(0, satluj_len):
        if satluj[i] == 166:
            normalise[k] = 241
            k += 1
            normalise[k] = 191
            k += 1
        else:
            if (satluj[i] == 211) and (satluj[i + 1] == 218):
                normalise[k] = 199
                k += 1
                normalise[k] = 242
                k += 1
                normalise[k] = 188
                k += 1
                normalise[k] = 218
                k += 1
                i += 1
            else:
                normalise[k] = satluj[i]
                k += 1
    normalise_len = k

def normalise_text(gurmukhi, len1, normalised):
            i = 0
            font_type = 0
            len2=0

            font_type = test_font_type(gurmukhi, len1)
            if  font_type == 1:
                for  i in range(0,len1):
                    normalised[i] = gurmukhi[i]
                len2 = len1
                return len2
            else:
                if  font_type == 3:
                    len2=anmol_to_satluj(gurmukhi, len1, normalised)
                else:
                    len2=expand_satluj_text(gurmukhi, len1, normalised)
                len1 = len2
                for  i in range(0,len1):
                    gurmukhi[i] = normalised[i]
                len2=satluj_text_to_unicode(gurmukhi, len1, normalised)
                return len2
def satluj_text_to_unicode(satluj, satluj_len, unicode, unicode_len):
            partial_unicode=[0]*10
            i = 0

            for  i in range(1,satluj_len):
                if  satluj[i] == 122:
                    if  (satluj[i + 1] > 122) and (satluj[i - 1] > 122):
                        satluj[i] = 204


                if  (satluj[i] == 188) or (satluj[i] == 190) or (satluj[i] == 181):
                    satluj[i] = 181
                else:
                    if  (satluj[i] == 189) or (satluj[i] == 207):
                        satluj[i] = 189
                    else:
                        if  (satluj[i] == 167) or (satluj[i] == 179) or (satluj[i] == 191):
                            satluj[i] = 167
                        else:
                            if  (satluj[i] == 169) or (satluj[i] == 174) or (satluj[i] == 204):
                                satluj[i] = 204
                            else:
                                if  (satluj[i] == 176) or (satluj[i] == 185):
                                    satluj[i] = 176
                                else:
                                    if  (satluj[i] == 177) or (satluj[i] == 200):
                                        satluj[i] = 177
                if  (satluj[i] == 167) or (satluj[i] == 175) or (satluj[i] == 181) or (satluj[i] == 182) or (satluj[i] == 189) or (satluj[i] == 203):
                    if  (satluj[i + 1] == 176) or (satluj[i + 1] == 177) or (satluj[i + 1] == 183) or (satluj[i + 1] == 201) or (satluj[i + 1] == 204):
                        c = satluj[i]
                        satluj[i] = satluj[i + 1]
                        satluj[i + 1] = c


            for  i in range(0,satluj_len):
                if  (satluj[i] == 167) or (satluj[i] == 179) or (satluj[i] == 191):
                    if  (satluj[i + 1] == 200) or (satluj[i + 1] == 185) or (satluj[i + 1] == 176) or (satluj[i + 1] == 177) or (satluj[i + 1] == 204):
                        satluj[i] = satluj[i + 1]
                        satluj[i + 1] = 191

                else:
                    if  (satluj[i] == 188) or (satluj[i] == 190) or (satluj[i] == 181):
                        if  (satluj[i + 1] == 200) or (satluj[i + 1] == 185) or (satluj[i + 1] == 176) or (satluj[i + 1] == 177) or (satluj[i + 1] == 204):
                            satluj[i] = satluj[i + 1]
                            satluj[i + 1] = 188

                    else:
                        if  satluj[i] == 182:
                            if  (satluj[i + 1] == 183):
                                satluj[i] = satluj[i + 1]
                                satluj[i + 1] = 182

                        else:
                            if  satluj[i] == 192:
                                if  (satluj[i + 1] == 185) or (satluj[i + 1] == 176):
                                    satluj[i] = 155
                                    satluj[i + 1] = 206
                                if  (satluj[i + 1] == 200) or (satluj[i + 1] == 177):
                                    satluj[i] = 156
                                    satluj[i + 1] = 206
                            else:
                                if  satluj[i] == 193:
                                    if  satluj[i + 1] == 197:
                                        satluj[i] = 152
                                        satluj[i + 1] = 206
                                    if  satluj[i + 1] == 203:
                                        satluj[i] = 158
                                        satluj[i + 1] = 206
                                    if  (satluj[i + 1] == 189) or (satluj[i + 1] == 207):
                                        satluj[i] = 159
                                        satluj[i + 1] = 206
                                    if  satluj[i + 1] == 187:
                                        satluj[i] = 161
                                        satluj[i + 1] = 206
                                else:
                                    if  satluj[i] == 194:
                                        if  i > 0 and satluj[i - 1] == 199:
                                            satluj[i - 1] = 153
                                            satluj[i] = 206
                                        if  satluj[i + 1] == 198:
                                            satluj[i] = 154
                                            satluj[i + 1] = 206
                                        if  satluj[i + 1] == 182:
                                            satluj[i] = 157
                                            satluj[i + 1] = 206
                                        if  satluj[i + 1] == 196:
                                            satluj[i] = 154
                                            satluj[i + 1] = 186
                                    else:
                                        if  (satluj[i] == 199) and (satluj[i + 1] != 194):
                                            satluj[i] = satluj[i + 1]
                                            satluj[i + 1] = 199
                                            if  (satluj[i + 2] == 122) or (satluj[i + 2] == 169) or (satluj[i + 2] == 204):
                                                satluj[i + 1] = 204
                                                satluj[i + 2] = 199
                                                i+=1
                                            if  (satluj[i + 2] == 183) or (satluj[i + 2] == 201):
                                                satluj[i + 1] = satluj[i + 2]
                                                satluj[i + 2] = 199
                                                i+=1
                                            i+=1



            k = 0
            unicode[k] = 255
            k+=1
            unicode[k] = 254
            k+=1
            for  i in range(0,satluj_len):
                len = satluj_char_to_unicode(satluj[i], partial_unicode)

                for  j in range(0,len):
                    unicode[k] = partial_unicode[j]
                    k+=1

            unicode_len = k


def satluj_char_to_unicode(satluj, unicode):
    # {
    table = [0] * 256
    len = 0
    end_table = [0] * 256

    for i in range(0, 256):
        table[i] = 0
    for i in range(0, 123):
        table[i] = i
    for i in range(0, 123):
        end_table[i] = 0
    for i in range(123, 256):
        end_table[i] = 10
    for i in range(49, 57 + 1):
        end_table[i] = 10

    end_table[142] = 9
    end_table[162] = 9
    end_table[163] = 9
    end_table[168] = 9
    end_table[205] = 9
    end_table[210] = 0
    end_table[211] = 0

    table[10] = 13

    table[ord('0')] = int("0x66", 16)
    table[ord('1')] = int("0x67", 16)
    table[ord('2')] = int("0x68", 16)
    table[ord('3')] = int("0x69", 16)
    table[ord('4')] = int("0x6a", 16)
    table[ord('5')] = int("0x6b", 16)
    table[ord('6')] = int("0x6c", 16)
    table[ord('7')] = int("0x6d", 16)
    table[ord('8')] = int("0x6e", 16)
    table[ord('9')] = int("0x6f", 16)

    table[64] = '0'
    table[65] = '1'
    table[66] = '2'
    table[67] = '3'
    table[68] = '4'
    table[69] = '5'
    table[70] = '6'
    table[71] = '7'
    table[72] = '8'
    table[73] = '9'

    table[ord('J')] = ord('*')
    table[ord('L')] = ord('*')
    table[84] = 147
    table[85] = 148

    table[123] = int("0x1a", 16)
    table[124] = int("0x1f", 16)
    table[125] = int("0x24", 16)
    table[126] = int("0x39", 16)
    table[142] = int("0x64", 16)

    table[152] = int("0x6", 16)
    table[153] = int("0x7", 16)
    table[154] = int("0x8", 16)
    table[155] = int("0x9", 16)
    table[156] = int("0xa", 16)
    table[157] = int("0xf", 16)
    table[158] = int("0x10", 16)
    table[159] = int("0x14", 16)
    table[161] = int("0x6", 16)

    table[162] = int("0x64", 16)
    table[163] = int("0x65", 16)
    table[165] = int("0x28", 16)
    table[166] = int("0x32", 16)
    table[167] = int("0x70", 16)
    table[168] = int("0x65", 16)
    table[169] = int("0x30", 16)
    table[174] = int("0x30", 16)
    table[170] = int("0x9", 16)
    table[171] = int("0x32", 16)

    table[172] = int("0x32", 16)
    table[175] = int("0x4b", 16)
    table[176] = int("0x41", 16)
    table[177] = int("0x42", 16)
    table[179] = int("0x70", 16)
    table[180] = int("0x15", 16)
    table[181] = int("0x71", 16)
    table[182] = int("0x47", 16)
    table[183] = int("0x39", 16)
    table[185] = int("0x41", 16)
    table[186] = int("0x2", 16)
    table[187] = int("0x3e", 16)

    table[188] = int("0x71", 16)
    table[189] = int("0x4c", 16)
    table[190] = int("0x71", 16)
    table[191] = int("0x70", 16)
    table[192] = int("0x73", 16)
    table[193] = int("0x5", 16)
    table[194] = int("0x72", 16)
    table[195] = int("0x38", 16)
    table[196] = int("0x40", 16)
    table[197] = int("0x3e", 16)

    table[198] = int("0x40", 16)
    table[199] = int("0x3f", 16)
    table[200] = int("0x42", 16)
    table[201] = int("0x35", 16)
    table[203] = int("0x48", 16)
    table[204] = int("0x30", 16)
    table[205] = int("0x64", 16)
    table[207] = int("0x4c", 16)
    table[210] = 39
    table[211] = 39
    table[212] = int("0x39", 16)
    table[213] = int("0x15", 16)
    table[214] = int("0x16", 16)

    table[215] = int("0x17", 16)
    table[216] = int("0x18", 16)
    table[217] = int("0x19", 16)  # modified 29/7/9
    table[218] = int("0x1a", 16)
    table[219] = int("0x1b", 16)
    table[220] = int("0x1c", 16)
    table[221] = int("0x2f", 16)
    table[222] = int("0x1d", 16)
    table[223] = int("0x1e", 16)
    table[224] = int("0x1f", 16)
    table[225] = int("0x20", 16)
    table[226] = int("0x21", 16)
    table[227] = int("0x22", 16)

    table[228] = int("0x23", 16)
    table[229] = int("0x24", 16)
    table[230] = int("0x25", 16)
    table[231] = int("0x26", 16)
    table[232] = int("0x27", 16)
    table[233] = int("0x28", 16)
    table[234] = int("0x2a", 16)
    table[235] = int("0x2b", 16)
    table[236] = int("0x2c", 16)
    table[237] = int("0x2d", 16)

    table[238] = int("0x2e", 16)
    table[239] = int("0x2f", 16)
    table[240] = int("0x30", 16)
    table[241] = int("0x32", 16)
    table[242] = int("0x35", 16)
    table[243] = int("0x5c", 16)
    table[244] = int("0x36", 16)
    table[245] = int("0x59", 16)
    table[246] = int("0x5a", 16)
    table[247] = int("0x5b", 16)

    table[248] = int("0x5e", 16)
    table[249] = int("0x28", 16)
    table[250] = int("0x13", 16)
    table[251] = int("0x25", 16)
    table[252] = int("0x1a", 16)
    table[253] = int("0x74", 16)  # modified 29/7/9
    table[254] = int("0x39", 16)
    table[255] = int("0x33", 16)

    # table[122] =int("0x4d",16)
    table[123] = int("0x4d", 16)
    table[124] = int("0x4d", 16)
    table[125] = int("0x4d", 16)
    table[126] = int("0x4d", 16)
    table[165] = int("0x4d", 16)
    table[183] = int("0x4d", 16)
    table[201] = int("0x4d", 16)
    table[204] = int("0x4d", 16)

    if (satluj != 206) and (table[satluj]) > 0:
        # {
        unicode[len] = table[satluj]
        len += 1
        unicode[len] = end_table[satluj]
        len += 1
    # }
    for i in range(0, 256):
        table[i] = 0
    table[10] = 10
    table[161] = int("0x2", 16)
    table[166] = int("0x70", 16)
    table[170] = int("0x2", 16)
    table[171] = int("0x41", 16)
    table[172] = int("0x42", 16)
    table[180] = int("0x4d", 16)
    table[187] = int("0x2", 16)
    table[196] = int("0x2", 16)
    table[249] = int("0x42", 16)
    table[251] = int("0x41", 16)
    table[252] = int("0x41", 16)
    #	table[253] =int("0x1#modified",16) 29/7/9
    #	table[254] =int("0x39#modified",16) 29/7/9
    #	table[253] =int("0x1",16)  #modified 29/7/9
    table[254] = int("0x48", 16)  # modified 29/7/9

    # table[122] =int("0x30",16)
    table[123] = int("0x1a", 16)
    table[124] = int("0x1f", 16)
    table[125] = int("0x24", 16)
    table[126] = int("0x39", 16)
    table[183] = int("0x39", 16)
    table[201] = int("0x35", 16)
    table[204] = int("0x30", 16)

    if table[satluj] > 0:
        # {
        unicode[len] = table[satluj]
        len += 1
        unicode[len] = end_table[satluj]
        len += 1
    # }
    if satluj == 249:
        # {
        unicode[len] = int("0x70", 16)
        len += 1
        unicode[len] = 10
        len += 1
    # }
    elif satluj == 180:
        # {
        unicode[len] = int("0x30", 16)
        len += 1
        unicode[len] = 10
        len += 1
    # }

    return len
    # {
    table = [0] * 256
    len = 0
    end_table = [0] * 256

    for i in range(0, 256):
        table[i] = 0
    for i in range(0, 123):
        table[i] = i
    for i in range(0, 123):
        end_table[i] = 0
    for i in range(123, 256):
        end_table[i] = 10
    for i in range(49, 57 + 1):
        end_table[i] = 10

    end_table[142] = 9
    end_table[162] = 9
    end_table[163] = 9
    end_table[168] = 9
    end_table[205] = 9
    end_table[210] = 0
    end_table[211] = 0

    table[10] = 13

    table[ord('0')] = int("0x66", 16)
    table[ord('1')] = int("0x67", 16)
    table[ord('2')] = int("0x68", 16)
    table[ord('3')] = int("0x69", 16)
    table[ord('4')] = int("0x6a", 16)
    table[ord('5')] = int("0x6b", 16)
    table[ord('6')] = int("0x6c", 16)
    table[ord('7')] = int("0x6d", 16)
    table[ord('8')] = int("0x6e", 16)
    table[ord('9')] = int("0x6f", 16)

    table[64] = '0'
    table[65] = '1'
    table[66] = '2'
    table[67] = '3'
    table[68] = '4'
    table[69] = '5'
    table[70] = '6'
    table[71] = '7'
    table[72] = '8'
    table[73] = '9'

    table[ord('J')] = '*'
    table[ord('L')] = '*'
    table[84] = 147
    table[85] = 148

    table[123] = int("0x1a", 16)
    table[124] = int("0x1f", 16)
    table[125] = int("0x24", 16)
    table[126] = int("0x39", 16)
    table[142] = int("0x64", 16)

    table[152] = int("0x6", 16)
    table[153] = int("0x7", 16)
    table[154] = int("0x8", 16)
    table[155] = int("0x9", 16)
    table[156] = int("0xa", 16)
    table[157] = int("0xf", 16)
    table[158] = int("0x10", 16)
    table[159] = int("0x14", 16)
    table[161] = int("0x6", 16)

    table[162] = int("0x64", 16)
    table[163] = int("0x65", 16)
    table[165] = int("0x28", 16)
    table[166] = int("0x32", 16)
    table[167] = int("0x70", 16)
    table[168] = int("0x65", 16)
    table[169] = int("0x30", 16)
    table[174] = int("0x30", 16)
    table[170] = int("0x9", 16)
    table[171] = int("0x32", 16)

    table[172] = int("0x32", 16)
    table[175] = int("0x4b", 16)
    table[176] = int("0x41", 16)
    table[177] = int("0x42", 16)
    table[179] = int("0x70", 16)
    table[180] = int("0x15", 16)
    table[181] = int("0x71", 16)
    table[182] = int("0x47", 16)
    table[183] = int("0x39", 16)
    table[185] = int("0x41", 16)
    table[186] = int("0x2", 16)
    table[187] = int("0x3e", 16)

    table[188] = int("0x71", 16)
    table[189] = int("0x4c", 16)
    table[190] = int("0x71", 16)
    table[191] = int("0x70", 16)
    table[192] = int("0x73", 16)
    table[193] = int("0x5", 16)
    table[194] = int("0x72", 16)
    table[195] = int("0x38", 16)
    table[196] = int("0x40", 16)
    table[197] = int("0x3e", 16)

    table[198] = int("0x40", 16)
    table[199] = int("0x3f", 16)
    table[200] = int("0x42", 16)
    table[201] = int("0x35", 16)
    table[203] = int("0x48", 16)
    table[204] = int("0x30", 16)
    table[205] = int("0x64", 16)
    table[207] = int("0x4c", 16)
    table[210] = 39
    table[211] = 39
    table[212] = int("0x39", 16)
    table[213] = int("0x15", 16)
    table[214] = int("0x16", 16)

    table[215] = int("0x17", 16)
    table[216] = int("0x18", 16)
    table[217] = int("0x19", 16)  # modified 29/7/9
    table[218] = int("0x1a", 16)
    table[219] = int("0x1b", 16)
    table[220] = int("0x1c", 16)
    table[221] = int("0x2f", 16)
    table[222] = int("0x1d", 16)
    table[223] = int("0x1e", 16)
    table[224] = int("0x1f", 16)
    table[225] = int("0x20", 16)
    table[226] = int("0x21", 16)
    table[227] = int("0x22", 16)

    table[228] = int("0x23", 16)
    table[229] = int("0x24", 16)
    table[230] = int("0x25", 16)
    table[231] = int("0x26", 16)
    table[232] = int("0x27", 16)
    table[233] = int("0x28", 16)
    table[234] = int("0x2a", 16)
    table[235] = int("0x2b", 16)
    table[236] = int("0x2c", 16)
    table[237] = int("0x2d", 16)

    table[238] = int("0x2e", 16)
    table[239] = int("0x2f", 16)
    table[240] = int("0x30", 16)
    table[241] = int("0x32", 16)
    table[242] = int("0x35", 16)
    table[243] = int("0x5c", 16)
    table[244] = int("0x36", 16)
    table[245] = int("0x59", 16)
    table[246] = int("0x5a", 16)
    table[247] = int("0x5b", 16)

    table[248] = int("0x5e", 16)
    table[249] = int("0x28", 16)
    table[250] = int("0x13", 16)
    table[251] = int("0x25", 16)
    table[252] = int("0x1a", 16)
    table[253] = int("0x74", 16)  # modified 29/7/9
    table[254] = int("0x39", 16)
    table[255] = int("0x33", 16)

    # table[122] =int("0x4d",16)
    table[123] = int("0x4d", 16)
    table[124] = int("0x4d", 16)
    table[125] = int("0x4d", 16)
    table[126] = int("0x4d", 16)
    table[165] = int("0x4d", 16)
    table[183] = int("0x4d", 16)
    table[201] = int("0x4d", 16)
    table[204] = int("0x4d", 16)

    if (satluj != 206) and (table[satluj]) > 0:
        # {
        unicode[len] = table[satluj]
        len += 1
        unicode[len] = end_table[satluj]
        len += 1
    # }
    for i in range(0, 256):
        table[i] = 0
    table[10] = 10
    table[161] = int("0x2", 16)
    table[166] = int("0x70", 16)
    table[170] = int("0x2", 16)
    table[171] = int("0x41", 16)
    table[172] = int("0x42", 16)
    table[180] = int("0x4d", 16)
    table[187] = int("0x2", 16)
    table[196] = int("0x2", 16)
    table[249] = int("0x42", 16)
    table[251] = int("0x41#modified", 16)
    table[252] = int("0x41#modified", 16)
    #	table[253] =int("0x1#modified",16) 29/7/9
    #	table[254] =int("0x39#modified",16) 29/7/9
    #	table[253] =int("0x1",16)  #modified 29/7/9
    table[254] = int("0x48", 16)  # modified 29/7/9

    # table[122] =int("0x30",16)
    table[123] = int("0x1a", 16)
    table[124] = int("0x1f", 16)
    table[125] = int("0x24", 16)
    table[126] = int("0x39", 16)
    table[183] = int("0x39", 16)
    table[201] = int("0x35", 16)
    table[204] = int("0x30", 16)

    if table[satluj] > 0:
        # {
        unicode[len] = table[satluj]
        len += 1
        unicode[len] = end_table[satluj]
        len += 1
    # }
    if satluj == 249:
        # {
        unicode[len] = int("0x70", 16)
        len += 1
        unicode[len] = 10
        len += 1
    # }
    elif satluj == 180:
        # {
        unicode[len] = int("0x30", 16)
        len += 1
        unicode[len] = 10
        len += 1
    # }

    return len
def anmol_to_satluj(anmol, anmol_len, satluj):
            table=[0]*256
            satluj_len=0

            for  i in range(0,256):
                table[i] = i
            table[62] = 0
            table[ord('u')] = 0
            table[33] = 33
            table[34] = 85
            table[35] = 35
            table[37] = 37
            table[38] = 248
            table[39] = 211
            table[48] = 64
            table[49] = 65
            table[50] = 66
            table[51] = 67
            table[52] = 68
            table[53] = 69
            table[54] = 70
            table[55] = 71
            table[56] = 72
            table[57] = 73
            table[60] = 253
            table[65] = 193
            table[66] = 237
            table[67] = 219
            table[68] = 232
            table[69] = 250
            table[70] = 227
            table[71] = 216
            table[72] = 183
            table[73] = 198
            table[74] = 222
            table[75] = 214
            table[76] = 241
            table[77] = 191
            table[78] = 186
            table[79] = 189
            table[80] = 235
            table[81] = 230
            table[82] = 204
            table[83] = 244
            table[84] = 225
            table[85] = 177
            table[86] = 243
            table[87] = 187
            table[88] = 239
            table[89] = 203
            table[90] = 246
            table[91] = 142
            table[92] = 223
            table[93] = 163
            table[94] = 245
            table[95] = 151
            table[96] = 181
            table[97] = 192
            table[98] = 236
            table[99] = 218
            table[100] = 231
            table[101] = 194
            table[102] = 226
            table[103] = 215
            table[104] = 212
            table[105] = 199
            table[106] = 220
            table[107] = 213
            table[108] = 241
            table[109] = 238
            table[110] = 233
            table[111] = 175
            table[112] = 234
            table[113] = 229
            table[114] = 240
            table[115] = 195
            table[116] = 224
            table[117] = 176
            table[118] = 242
            table[119] = 197
            table[120] = 228
            table[121] = 182
            table[122] = 247
            table[124] = 217
            table[126] = 181
            table[131] = 249
            table[134] = 124
            table[145] = 210
            table[146] = 211
            table[147] = 84
            table[148] = 85
            table[156] = 125
            table[161] = 253
            table[164] = 181
            table[206] = 221
            table[210] = 168
            table[241] = 49
            table[242] = 50
            table[243] = 51
            table[244] = 52
            table[245] = 53
            table[246] = 54
            table[247] = 55
            table[248] = 56
            table[249] = 57
            table[250] = 48

            j=0
            for  i in range(0,anmol_len):
                if  table[anmol[i]] > 0:
                    satluj[j] = table[anmol[i]]
                    j+=1
            satluj_len = j
            return satluj_len

def str2Byte(str1):
            data=[0]*(len(str1)* 2)
            len = 0
            for  t in range(0,len(str1)):
                ch = str1[t]
                code = ch
                data[len] = (code % 256)
                len+=1
                data[len] = (code / 256)
                len+=1
            return data
def strcat(str1, str2):
            len1 = strlen(str1)
            len2 = strlen(str2)
            j = len1
            for  t in range(0,len2):
                str1[j] = str2[t]
                j+=1
            str1[j] = 0
def printMSG(s):
            global MSG
            MSG += "\n" + s
def printMSG2(s, v):
            global MSG
            MSG += "\n" + s + v


def G2S():
    i = 0
    global isActive
    global similar_word_count
    if not isActive:
        isActive = True
        QTS = [0] * 1
        QTS[0] = 0

        for i in range(5000):
            wordlist.append(wlist())
            wordlist[i].word = [0] * 40
            wordlist[i].count = 0
        total_merged_words = [0] * 10

        for i in range(SIMILAR_SIZE):
            sd.append(similar_dictionary())
            sd[i].original = [0] * 24
            sd[i].similar = [0] * 24
        read_urdu_gurmukhi_dict()
        similar_word_count = read_similar_dict(sd)
def func(matchobj):
    m = matchobj.group(0)
    return start(m)

def startReg(input):
    G2S()
    global isDacritic
    isDacritic=False
    generatedWord = ''
    patt=(r'([ਂ-ੳ]\s*[' + re.escape(string.punctuation) + ']*[।]*)+')
    generatedWord = re.sub(patt, func, input)
    return generatedWord

