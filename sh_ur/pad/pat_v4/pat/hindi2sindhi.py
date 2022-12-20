import numpy as np
import os.path
import re
import string
import os, sys

class similar_dictionary:
    original=[]
    similar=[]
class broken_dictionary:
    urdu=[]
    broken=[]
class urdu_hindi():
    urdu_start=[]
    urdu_end=[]
    hindi_start=[]
    hindi_end=[]
    urdu_word_count=0

class urdu_corpus:   
    original_word=[]
    freq=0

class trigram_index:
    normalised_word=[]
    index=0
class unicode:
    urdu=0
    hindi=0

class bistruct:
    urdu=[]
    hindi1=[]
    hindi2=[]
    freq=0
class normalised_corpus:
    original_word=[]
    normalised_word=[]
    freq=0

class bigram_index:
    normalised_word=[]
    index=0
class bigram_corpus:
    first_word=[]
    second_word=[]
    freq=0
    unigram_freq=0


class wlist:
    word=[]
    count=0

class urdu_bigram:  
    urdu1=[]
    urdu2=[]
    hindi=[]
class trigram_corpus:
    first_word=[]
    second_word=[]
    third_word=[]
    freq=0


class trigram:
    first_word=[]
    second_word=[]
    third_word=[]

class tunion:
    uc=[0]*2
    ui=0


class ligature:
    char_count = 0
    lig=[]

class lig_class:
    ligature_count=0


class Sindhi2HindiReverse:
    appPath=''
    QTS=[]
    MSG = "Started:"
    isActive =  False
    isDic =  False
    isDicSimilar =  False
    isBinCorpus =  False
    isPreBinCorpus =  False
    isPostBinCorpus =  False
    isUrduBigram = True
    offTriGram = True

    
    FILESIZE = 125000
    CORPUS = 250000
    CORPUS_FILESIZE = 6400
    DICSIZE = 120000
    BISIZE = 4000
    BIGRAM_SIZE = 20000
    INDEX_SIZE = 8000
    URDU_BIGRAM_SIZE = 3000
    URDUCORPUS = 0
    SIMILAR_SIZE = 20730
    BROKEN_SIZE = 56
    
    wordlist = []
    word_total = 0
    word_found = 0
    bi_word_found = 0
    word_not_found = 0
    hindi_trigram_found = 0
    broken_count = 0
    PROTECTOLDA = 0
    olda = 0
    remove_diactric = 1
    
    pre_bigram = []
    post_bigram = []  
    pre_bigram_index = []
    post_bigram_index = []  
    corpus_words = []  
    corpus_word_count = 0
    corpus_found = 0
    multi_count = 0
    dict_word_count = 0
    pre_bigram_total = 0
    post_bigram_total = 0
    pre_bigram_index_count = 0
    post_bigram_index_count = 0
    urdu_bigram_total = 0
    extra_word_count = 0
    Hindi_dict = []
    urdu_dict = []  
    corpus_flag = 0
    conversion_level = 3
    urdu_bigram = []  
    average_joint_count = 0.0
    urdu_corpus_words = []  
    urdu_corpus_total = 0
    similar_word_count = 0
    broken_word_count = 0
    sd = []  
    bd = []  


    def __init__(self):
            i = 0
            if  not self.isActive:
                self.isActive = True
                QTS=[0]*1
                QTS[0]=0
    
                self.corpus_words=np.empty((self.CORPUS), dtype="object")
                for  i in range(0,len(self.corpus_words)):
                    self.corpus_words[i]=normalised_corpus()
                    self.corpus_words[i].original_word=[0]*16
                    self.corpus_words[i].normalised_word=[0]*16
                    self.corpus_words[i].freq=0
                self.Hindi_dict=np.empty((self.DICSIZE), dtype="object")
                self.urdu_dict=np.empty((self.DICSIZE), dtype="object")
                for  i in range(0,self.DICSIZE):
                    self.Hindi_dict[i]=[0]*26
                    self.urdu_dict[i]=[0]*26
                self.sd=np.empty((self.SIMILAR_SIZE), dtype="object")
                for  i in range(0,self.SIMILAR_SIZE):
                    self.sd[i]=similar_dictionary()
                    self.sd[i].original=[0]*24
                    self.sd[i].similar=[0]*24
                self.bd=np.empty((self.BROKEN_SIZE), dtype="object")
                for  i in range(0,self.BROKEN_SIZE):
                    self.bd[i]=broken_dictionary()
                    self.bd[i].urdu=[0]*45
                    self.bd[i].broken=[0]*45
                self.wordlist=np.empty((30000), dtype="object")
                for  i in range(0,len(self.wordlist)):
                    self.wordlist[i]=wlist()
                    self.wordlist[i].word=[0]*40
                    self.wordlist[i].count=0
    
    
                self.appPath = pathname = os.getcwd()  
                self.appPath = os.path.join(self.appPath,'sindhi2hindi')
                
                self.read_urdu_hindi_dict()
                self.similar_word_count=self.read_similar_dict(self.sd, self.similar_word_count)
    
        
    
    
    
    
    
    def startReg(self, input):
        generatedWord = ''
        patt = r'(\s*[ऀ-ॿ]\s*[' + re.escape(string.punctuation) + ']*)+'
        generatedWord = re.sub(patt, self.func, input)
        return generatedWord
    
    def func(self, matchobj):
        m = matchobj.group(0)
        return self.start(m)
    
    def start(self, input):
            file_length_in = 0
            file_length_out = 0
            urdu=[0]*self.FILESIZE
            Hindi=[0]*self.FILESIZE
            if len(input)== 0:
                return "Empty String...."
            inputbytes=self.str2Byte(input)
            if len(inputbytes)+ 1 > len(Hindi):
                return "TOO MUCH DATA"
            for  i in range(0,len(inputbytes)):
                Hindi[i]=inputbytes[i]
            file_length_in = len(inputbytes)
    
    
            file_length_out=self.convert_Hindi_to_urdu(Hindi,  file_length_in,  urdu, file_length_out)
    
    
            tej_urdu = self.byte2Str(urdu, (file_length_out + 2), True)
            return tej_urdu
    def convert_Hindi_to_urdu(self, Hindi, size, urdu, urdu_size):
            temp_roman_word = [0]*5000
            Hindi_word = [0]*100
            urdu_word = [0]*100
            urdu_word1 = [0]*100
            Hindi_strip = [0]*25
            broken_urdu_word = [0]*80
            urdu8 = [0]*40
            final_word = [0]*40
            urdu_word2 = [0]*100
            urdu_word_size = 0
            Hindi_word_size = 0
            temp_roman_word_size = 0
            cword = 0
            broken_word_size = 0
            size1 = 0
            size2 = 0
            freq1 = 0
            freq2 = 0
    
            urdu_size = 0
            Hindi_ptr = 0
            while  Hindi_ptr <= size:
                ch = Hindi[Hindi_ptr];
                ch1 = Hindi[Hindi_ptr + 1];
    
                if  self.check_punctuation(ch, ch1) > 0:
    
                    cword+=1
    
                    if  cword == 499:
                        cword+=1
                    flag = 0;
                    if ((Hindi_word_size > 4) and (Hindi_word[Hindi_word_size - 2] == 71)):
                        for  i in range(0,40):
                            urdu_word1[i] = urdu_word[i] = 0;
                        flag, size1 = self.Hindi_word_to_urdu(Hindi_word,  Hindi_word_size,  urdu_word, flag)
                        self.UnicodeTo8(urdu_word, self.strlen(urdu_word), urdu8)
                        freq1 = self.check_urdu_corpus(urdu8, final_word)
                        freq2 = 0
                        if  freq1 < 1:
                            flag, size2 = self.Hindi_word_to_urdu(Hindi_word,  Hindi_word_size - 2,  urdu_word1, flag)
                            self.UnicodeTo8(urdu_word1, self.strlen(urdu_word1), urdu8)
                            freq2 = self.check_urdu_corpus(urdu8, final_word)
                            freq2 = 0
                        if  freq1 >= freq2:
                            urdu_word_size = size1
    
                        else:
                            for  i in range(0,size2):
                                urdu_word1[i]=[]
                            urdu_word_size = size2
    
                    else:
                       flag, urdu_word_size = self.Hindi_word_to_urdu(Hindi_word,  Hindi_word_size,  urdu_word, flag)
                    broken_word_size, returnedFlag=self.check_broken_word_dictionary(urdu_word, urdu_word_size, broken_urdu_word, broken_word_size)
                    if  (flag != 1) and urdu_word_size > 0 and returnedFlag > 0:
                        for  i in range(0,broken_word_size):
                            broken_urdu_word[i]=[]
                        urdu_word_size = broken_word_size
                        self.broken_count+=1
    
    
                    for  i in range(0,urdu_word_size):
                        if  urdu_word[i] == 251:
                            urdu[(urdu_size)] = ord('-')
                            urdu_size+=1
                            urdu[(urdu_size)] = 0
                            urdu_size+=1
                            i+=1
                        else:
                            if  urdu_word[i] == 255:
                                urdu[(urdu_size)] = ord(' ')
                                urdu_size+=1
                                urdu[(urdu_size)] = 0
                                urdu_size+=1
                                i+=1
                            else:
                                urdu[(urdu_size)] = urdu_word[i]
                                urdu_size += 1
                    Hindi_word_size = 0
                    flag = 0
                    while  self.check_punctuation(ch, ch1) > 0 or flag > 0:
                        temp_roman_word_size=self.convert_Hindi_punctuation_to_urdu(ch,  ch1,  temp_roman_word, temp_roman_word_size)
                        for  i in range(0,temp_roman_word_size):
                            urdu[(urdu_size)] = temp_roman_word[i]
                            urdu_size += 1
                        Hindi_ptr += 2
                        if  Hindi_ptr >= size: break
                        ch = Hindi[Hindi_ptr];
                        ch1 = Hindi[Hindi_ptr + 1];
                        flag = 0
                        if  ch == 45 and not (ch1 != 0) and not (Hindi_word_size != 0): flag = 1
                else:
                    Hindi_word[Hindi_word_size] = ch
                    Hindi_word_size+=1
                    Hindi_word[Hindi_word_size] = ch1
                    Hindi_word_size+=1
                    Hindi_ptr += 2
            
            return urdu_size
    
    def convert_Hindi_punctuation_to_urdu(self, ch, ch1, roman, roman_size):
            urdu_to_roman=[0]*256
            roman_ptr = 0
            if  (ch == 0) and (ch1 == 0):
                roman_size = 0
                return roman_size 
            for  i in range(0,256):
                urdu_to_roman[i] = i
            for  i in range(128,256):
                urdu_to_roman[i] = 0
            urdu_to_roman[ord(',')] =12
            urdu_to_roman[ord(';')] =27
            urdu_to_roman[ord('?')] =31
            urdu_to_roman[ord('%')] =106
            urdu_to_roman[ord('*')] =109
            urdu_to_roman[255] = 0
            if  (ch == 255) and (ch1 == 254):
                roman[roman_ptr] = ch
                roman_ptr+=1
                roman[roman_ptr] = ch1
                roman_ptr+=1
            else:
                if  ch1 == 9:
                    if  ch ==100:
                        roman[roman_ptr] =212
                        roman_ptr+=1
                        roman[roman_ptr] = 6
                        roman_ptr+=1
                    elif ch ==101:
                        roman[roman_ptr] =212
                        roman_ptr+=1
                        roman[roman_ptr] = 6
                        roman_ptr+=1
                        roman[roman_ptr] =212
                        roman_ptr+=1
                        roman[roman_ptr] = 6
                        roman_ptr+=1
    
                else:
                    if  ch1 == 10:
                        if  (ch >=102) and (ch <=111):
                            roman[roman_ptr] = (ord('0') + ch -102)
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
    
    def check_broken_word_dictionary(self, urdu_word, urdu_word_size, broken_urdu_word, broken_word_size):
        high = self.broken_word_count - 1
        low = 0
        mid = 0
        read_word=[0]*80
        urdu_strip=[0]*80
        temp=[0]*80
        self.UnicodeTo8(urdu_word, urdu_word_size, urdu_strip)
        broken_word_size = urdu_word_size
        while  low <= high:
            mid = int((low + high) / 2)
            self.strcpy(read_word, self.bd[mid].urdu)
            if  not (self.strcmp(read_word, urdu_strip) != 0):
                self.strcpy(temp, self.bd[mid].broken)
                k=0
                for  i in range(0,self.strlen(temp)):
                    if  temp[i] == 255:
                        if  i < self.strlen(temp) - 1:
                            broken_urdu_word[k] = 32
                            k+=1
                            broken_urdu_word[k] = 0
                            k+=1
                        else:
                            continue
                    else:
                        broken_urdu_word[k] = temp[i]
                        k+=1
                        broken_urdu_word[k] = 6
                        k+=1
                broken_word_size = k
                return broken_word_size, mid + 1
            if  self.strcmp(read_word, urdu_strip) < 0:
                low = mid + 1
            else:
                high = mid - 1
        return broken_word_size, 0
    def check_urdu_hyphen_dictionary(self, Hindi_word, urdu_word):
        Hindi_strip=[0]*40
        urdu_strip=[0]*40
        ulen = 0
        urdu_len = 0
        if  self.strlen(Hindi_word) < 3: return 0
        j = 0
        for  i in range(0,self.strlen(Hindi_word)):
            if  Hindi_word[i] == 251:
                Hindi_strip[j] = 0
                j+=1
                ulen = self.check_urdu_word_dictionary(Hindi_strip, urdu_strip)
                if (ulen) > 0:
                    for  k in range(0,ulen):
                        urdu_word[urdu_len] = urdu_strip[k]
                        urdu_len+=1
                    urdu_word[urdu_len] =32
                    urdu_len+=1
                    urdu_word[urdu_len] = 0
                    urdu_len+=1
                else: return 0
                j = 0
            else:
                if  Hindi_word[i] == 252:
                    Hindi_strip[j] = 252
                    j+=1
                    Hindi_strip[j] = 0
                    j+=1
                    ulen = self.check_urdu_word_dictionary(Hindi_strip, urdu_strip)
                    if  (ulen) > 0:
                        for  k in range(0,ulen):
                            urdu_word[urdu_len] = urdu_strip[k]
                            urdu_len+=1
                        return urdu_len
                    else:
                        Hindi_strip[j - 2] = 0
                        ulen = self.check_urdu_word_dictionary(Hindi_strip, urdu_strip)
                        if  (ulen) > 0:
                            for  k in range(0,ulen):
                                urdu_word[urdu_len] = urdu_strip[k]
                                urdu_len+=1
                            while  Hindi_word[i] == 252:
                                i+=1
                                urdu_word[urdu_len] =212
                                urdu_len+=1
                                urdu_word[urdu_len] = 6
                                urdu_len+=1
                            
                            return urdu_len
                    return 0
                    j = 0
    
                else:
                    if  Hindi_word[i] == 251:
                        Hindi_strip[j] = 0
                        j+=1
                        ulen = self.check_urdu_word_dictionary(Hindi_strip, urdu_strip)
                        if  (ulen) > 0:
                            for  k in range(0,ulen):
                                urdu_word[urdu_len] = urdu_strip[k]
                                urdu_len+=1
                            urdu_word[urdu_len] =32
                            urdu_len+=1
                            urdu_word[urdu_len] = 0
                            urdu_len+=1
                            urdu_word[urdu_len] =72
                            urdu_len+=1
                            urdu_word[urdu_len] = 6
                            urdu_len+=1
                        else: return 0
                        j = 0
                    else:
                        if  Hindi_word[i] == 253:
                            Hindi_strip[j] = 0
                            j+=1
                            ulen = self.check_urdu_word_dictionary(Hindi_strip, urdu_strip)
                            if  (ulen) > 0:
                                for  k in range(0,ulen):
                                    urdu_word[urdu_len] = urdu_strip[k]
                                    urdu_len+=1
                                if  self.checkendMATRA(urdu_word[urdu_len - 2]):
                                    if  urdu_word[urdu_len - 2] ==193:
                                        urdu_word[urdu_len - 2] =194
                                    else:
                                        urdu_word[urdu_len] =116
                                        urdu_len+=1
                                        urdu_word[urdu_len] = 6
                                        urdu_len+=1
                               
                                urdu_word[urdu_len] =32
                                urdu_len+=1
                                urdu_word[urdu_len] = 0
                                urdu_len+=1
                            else: return 0
                            j = 0
                        else:
                            Hindi_strip[j] = Hindi_word[i]
                            j+=1
        if  j > 0:
            Hindi_strip[j] = 0
            j+=1
            ulen = self.check_urdu_word_dictionary(Hindi_strip, urdu_strip)
            if  (ulen) > 0:
                for  k in range(0,ulen):
                    urdu_word[urdu_len] = urdu_strip[k]
                    urdu_len+=1
            else: urdu_len = 0
        return urdu_len
    def check_punctuation(self, ch, ch1):
            if  ch1 == 9:
                if  (ch >=100) and (ch <=101):
                    return 1
                return 0
            if  ch1 == 10:
                if  (ch >=102) and (ch <=111): return 1
            if  (ch1 == 32) and ((ch >= 11) and (ch <= 13)):
                return 0
            if  (ch1 == 0) and (ch ==45):
                return 1
            if  (ch1 == 0) and (ch == ord('.')):
                return 0
            if  (ch1 == 0) and (ch == 173):
                return 0
            if  ch1 != 10: return 1
            return 0
    def checkendMATRA(self, u):
            return (u ==34 or u ==39 or u ==80 or u ==79 or u ==193 or u ==210)
    def improve_urdu_word(self, urdu, urdu_size):
            for  i in range(2,urdu_size):
                if  (urdu[i - 2] ==38) and (urdu[i] ==38):
                    urdu[i] =204
                if  (urdu[i] ==36):
                    urdu_size += 2
                    for  j in range(urdu_size,i,-1):
                        urdu[j] = urdu[j - 1]
                    for  j in range(urdu_size,i,-1):
                        urdu[j] = urdu[j - 1]
                    urdu[i] =38
                    urdu[i + 2] =72
                    urdu[i + 1] = urdu[i + 3] = 6
            if  urdu_size > 4:
                i = urdu_size - 2
                if  (urdu[i] ==36):
                    urdu[i] =38
                    urdu[i + 2] =72
                    urdu[i + 3] = 6
                    urdu_size += 2
                if  (urdu[i] ==193):
                    urdu[i] =190
            return urdu_size
    def Hindi_word_to_urdu(self, Hindi_word, Hindi_word_size, urdu_word, flag):
        Hindi_strip=[0]*40
        similar=[0]*40
        urdu_subword=[0]*40
        sub_similar=[0]*40
        urdu8=[0]*40
        print_hindi_word=[0]*40
        final_word=[0]*40
        urdu_word_size = 0
        urdu_subword_size = 0
        scnt = 0
        urdu_len = 0
        ulen = 0
        
        for  i in range(0,40):
            urdu_word[i] = 0
        if  Hindi_word_size <= 0:
            return flag,  0
        self.UnicodeTo8(Hindi_word, Hindi_word_size, Hindi_strip)
        self.normalise_Hindi_dot(Hindi_strip)
        urdu_word_size = self.check_urdu_word_dictionary(Hindi_strip, urdu_word)
        if  (urdu_word_size) > 0:
            self.word_found+=1
            urdu_word_size=self.improve_urdu_word(urdu_word, urdu_word_size)
            flag = 1
            return flag,  urdu_word_size
        urdu_word_size = self.check_urdu_hyphen_dictionary(Hindi_strip, urdu_word)
        if  (urdu_word_size) > 0:
            self.word_found+=1
            flag = 1
            return flag,  urdu_word_size
        if  not (self.check_similar_word_dictionary(Hindi_strip, similar) != 0):
            flag, returnedFlag= self.check_urdu_hyphen_word(Hindi_strip,  urdu_word, flag)
            return flag, returnedFlag
        else:
            scnt = 0
            self.strcpy(Hindi_strip, similar)
            scnt+=1
            if  not scnt > 3:
                while self.check_similar_word_dictionary(Hindi_strip, similar) > 0:
                    self.strcpy(Hindi_strip, similar)
                    scnt += 1
                    if scnt > 3: break
                    
            urdu_word_size = self.check_urdu_word_dictionary(similar, urdu_word)
            if  (urdu_word_size) > 0:
                
                self.corpus_found+=1
                urdu_word_size=self.improve_urdu_word(urdu_word, urdu_word_size)
                flag = 1
                return flag,  urdu_word_size
            j = 0
            for  i in range(0,self.strlen(similar)+1):
                if  (similar[i] < 254) and (similar[i]) > 0:
                    Hindi_strip[j] = similar[i]
                    j+=1
                else:
                    Hindi_strip[j] = 0
                    j+=1
                    j = 0
                    if  self.check_similar_word_dictionary(Hindi_strip, sub_similar) > 0:
                        self.strcpy(Hindi_strip, sub_similar)
                    urdu_subword_size = self.check_urdu_word_dictionary(Hindi_strip, urdu_subword)
                    if  (urdu_subword_size) > 0:
                        self.word_found+=1
                        urdu_subword_size=self.improve_urdu_word(urdu_subword, urdu_subword_size)
                        flag = 1
                    else:
                        self.normalise_Hindi_word(Hindi_strip)
                        self.rule_based_Hindi_word_to_urdu(Hindi_strip, urdu_subword)
                        ulen = self.strlen(urdu_subword)
                        ulen=self.improve_urdu_word(urdu_subword, ulen)
                        self.UnicodeTo8(urdu_subword, self.strlen(urdu_subword), urdu8)
                        if  self.check_urdu_corpus(urdu8, final_word) > 0:
                            urdu_subword_size = 0
                            for  k in range(0,self.strlen(final_word)):
                                urdu_subword[urdu_subword_size] = final_word[k]
                                urdu_subword_size+=1
                                urdu_subword[urdu_subword_size] = 6
                                urdu_subword_size+=1
                            self.corpus_found+=1
                            urdu_subword[urdu_subword_size] = 0
                            urdu_subword_size+=1
                            k = self.strlen(Hindi_strip)
                            j = 0
                            for  k in range(0,self.strlen(Hindi_strip)):
                                print_hindi_word[j] = Hindi_strip[k]
                                j+=1
                                print_hindi_word[j] = 9
                                j+=1
                            flag = 2
                        urdu_subword_size = self.strlen(urdu_subword)
                        if  urdu_subword_size > 2 and flag != 2:
                            self.word_not_found+=1
                            k = self.strlen(Hindi_strip)
                            j = 0
                            for  k in range(0,self.strlen(Hindi_word)):
                                print_hindi_word[j] = Hindi_word[k]
                                j+=1
                                print_hindi_word[j] = 9
                                j+=1
                        else:
                            self.word_found+=1
                        j = 0
                        for  k in range(0,self.strlen(Hindi_word)):
                            print_hindi_word[j] = Hindi_strip[k]
                            j+=1
                            print_hindi_word[j] = 9
                            j+=1
                        print_hindi_word[j] = 0
                        j+=1
                        self.add_frequency(print_hindi_word, self.strlen(print_hindi_word))
                        flag = 0
                    if  similar[i] == 255:
                        urdu_subword[urdu_subword_size] = 32
                        urdu_subword_size+=1
                        urdu_subword[urdu_subword_size] = 0
                        urdu_subword_size+=1
                    else:
                        if  similar[i] == 251:
                            urdu_subword[urdu_subword_size] = ord('-')
                            urdu_subword_size+=1
                            urdu_subword[urdu_subword_size] = 0
                            urdu_subword_size+=1
                    for  k in range(0,urdu_subword_size):
                        urdu_word[urdu_word_size] = urdu_subword[k]
                        urdu_word_size+=1
                    urdu_subword_size = 0
            return flag,  urdu_word_size
    def check_urdu_corpus(self, urdu_int, final_word):
        multi = 0
        urdu_word=[0]*20
        first_urdu_word=[0]*16
        rest_urdu_word=[0]*16
        self.normalise_urdu_word(urdu_int, urdu_word)
        if  self.strlen(urdu_int) < 2: return 0
        pos = self.search_corpus(self.corpus_words, self.corpus_word_count, urdu_word)
        if  pos < 0: return 0
        low = high = pos
        self.strcpy(final_word, self.corpus_words[pos].original_word)
        return self.corpus_words[pos].freq
    def search_corpus(self, corpus_words, total, urdu_word):
            high = total - 1
            low = 0
            mid = 0
            read_word=[0]*16
            while  low <= high:
                mid = int((low + high) / 2)
                self.strcpy(read_word, corpus_words[mid].normalised_word)
                if  not (self.strcmp(read_word, urdu_word) != 0):
                    return mid
                if  self.strcmp(read_word, urdu_word) < 0:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1
    def normalise_urdu_word(self, t_urdu_word, urdu_word):
        extra = 0
        table=[0]*256
        for  i in range(0,256):
            table[i] = i
        table[45] =193
        table[43] = table[53] =51
        table[44] = table[48] = table[54] = table[56] =50
        table[66] =169
        table[41] = table[195] = table[55] =42
        table[175] =58
        table[57] =39
        j = 0
        for  i in range(0,self.strlen(t_urdu_word)):
            if  (t_urdu_word[i] ==57) and (t_urdu_word[i + 1] ==39):
                urdu_word[j] =39
                j+=1
                i+=1
                continue
            if  (t_urdu_word[i] ==204) and (t_urdu_word[i + 1] ==112):
                urdu_word[j] =39
                j+=1
                i+=1
                continue
            if  (t_urdu_word[i] ==39) and (t_urdu_word[i + 1] ==75):
                urdu_word[j] =70
                j+=1
                i+=1
                continue
            if  (t_urdu_word[i] ==169) and (t_urdu_word[i + 1] ==190):
                urdu_word[j] =46
                j+=1
                i+=1
                continue
            if  (t_urdu_word[i] ==126) and (t_urdu_word[i + 1] ==190):
                urdu_word[j] =65
                j+=1
                i+=1
                continue
            if  (t_urdu_word[i] >=75) and (t_urdu_word[i] <=82):
                continue
            if  i == self.strlen(t_urdu_word) - 1:
                if  t_urdu_word[i] ==193:
                    urdu_word[j] =39
                    j+=1
                    continue
            if  not (table[t_urdu_word[i]] != 0): continue
            urdu_word[j] = table[t_urdu_word[i]]
            j+=1
        urdu_word[j] = 0
    def convert_Hindi_urdu_char(self, u, pos, fc, sc):
            table=[0]*256
            for  i in range(0,255):
                table[i] = 0
            table[1] =int("0x46",16)
            table[2] =int("0x46",16)
            table[5] =int("0x27",16)
            table[int("0x11",16)] = table[6] =int("0x22",16)
            table[7] =int("0x27",16)
            table[8] =int("0x27",16)
            table[9] =int("0x27",16)
            table[10] =int("0x27",16)
            table[11] =int("0x31",16)
            table[15] =int("0x27",16)
            table[14] = table[16] =39
            table[18] = table[19] =39
            table[20] =39
            table[56] =51
            table[57] =193
            table[21] =169
            table[22] =169
            table[23] =175
            table[24] =175
            table[25] =70
            table[26] =134
            table[27] =134
            table[28] =44
            table[29] =44
            table[30] =131
            table[31] =125
            table[32] =121
            table[33] =136
            table[33] =138
            table[34] =136
            table[35] =70
            table[36] =42
            table[37] =42
            table[38] =47
            table[39] =47
            table[40] =70
            table[42] =126
            table[43] =126
            table[44] =40
            table[45] =40
            table[46] =69
            table[47] =204
            table[48] =49
            table[50] =68
            table[53] =72
            table[92] =145
            table[54] =52
            table[55] =52
            table[88] =66
            table[89] =46
            table[90] =58
            table[91] =50
            table[94] =65
            table[51] =68
            table[73] = table[62] =39
            table[63] =80
            table[64] =204
            table[65] =79
            table[66] =72
            table[75] =72
            table[76] =72
            table[71] =204
            table[72] =204
            table[112] =70
            table[113] =81
            table[117] =190
            table[102] =96
            table[103] =97
            table[104] =98
            table[105] =99
            table[106] =100
            table[107] =101
            table[108] =102
            table[109] =103
            table[110] =104
            table[111] =105
            table[252] =212
            table[254] = 254
            table[93] =145
            table[93] =153
            table[45] =128
            table[43] =166
            table[127] =123
            table[37] =127
            table[32] =122
            table[124] =132
            table[27] =135
            table[39] =140
            table[126] =143
            table[34] =141
            table[92] =153
            table[123] =179
            table[25] =177
            table[35] =187
            table[57] =190
            table[47] =74
            table[71] =74
            table[72] =74
            table[64] =74
            table[21] =170
            table[125] =74
            if  pos > 0:
                table[5] =int("0x26",16)
                table[6] =int("0x26",16)
                table[7] =int("0x26",16)
                table[8] =int("0x26",16)
                table[9] =int("0x26",16)
                table[10] =int("0x24",16)
                table[19] =36
                table[20] =36
                table[15] =int("0x4a",16)
                table[16] =74
            if  pos == 2:
                table[5] =33
                table[7] =33
                table[9] =33
                table[15] =38
            fc = table[u]
            for  i in range(0,255):
                table[i] = 0
            table[7] =int("0x50",16)
            table[8] =int("0x26",16)
            table[9] =int("0x4f",16)
            table[10] =int("0x48",16)
            table[15] =int("0xd2",16)
            table[16] =210
            table[19] =72
            table[20] =72
            table[24] =190
            table[29] =190
            table[93] =190
            table[8] =int("0x4a",16)
            if  pos > 0:
                table[6] =int("0x27",16)
                
                table[7] = 0
                table[9] = 0
                table[10] = 0
                table[19] = 0
                table[20] = 0
                table[16] = 0
            if  pos == 2:
                table[15] =int("0x54",16)
                table[5] =78
                table[7] =80
                table[9] =79
                table[15] =74
                table[47] =71
                table[125] =193
            sc = table[u]
            return fc, sc
    def rule_based_Hindi_word_to_urdu(self, Hindi, urdu):
        a = 0
        pos = 0
        fc = 0
        sc = 0
        cp = -1
        urdu_size = 0
        Hindi_size = self.strlen(Hindi)
        self.olda = 0
        urdu_size = 0
        cp+=1
        while cp < Hindi_size:
            a = Hindi[cp]
            if  cp > 0:
                prev = Hindi[cp - 1]
            if  cp > 0:
                pos = 1
            if  cp == 0: pos = 0
            if  cp == Hindi_size - 1: pos = 2
            if  (a ==2) and (cp == Hindi_size - 2) and (Hindi[cp + 1] ==5): pos = 2
            fc, sc=self.convert_Hindi_urdu_char(a,  pos, fc, sc)
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
    def normalise_Hindi_word(self, Hindi_word):
            Hindi_int_size = self.strlen(Hindi_word)
            t_Hindi_word=[0]*60
            zer_flag = self.remove_diactric
            i = j = 0
            while  i < Hindi_int_size:
                if  (i < Hindi_int_size - 1) and (Hindi_word[i] == 28) and (Hindi_word[i + 1] == 77) and (Hindi_word[i + 2] == 30):
                    t_Hindi_word[j] =23
                    j+=1
                    t_Hindi_word[j] =47
                    i+=1
                    i+=1
                else:
                    if  (i < Hindi_int_size - 1) and (Hindi_word[i] ==21) and (Hindi_word[i + 1] == 77) and (Hindi_word[i + 2] ==54):
                        t_Hindi_word[j] =21
                        j+=1
                        t_Hindi_word[j] =54
                        i+=1
                        i+=1
                    else:
                        if  (i < Hindi_int_size - 1) and ((Hindi_word[i] == 35) or (Hindi_word[i] ==46)) and (Hindi_word[i + 1] == 77):
                            t_Hindi_word[j] =2
                            i+=1
                        else:
                            if  (i < Hindi_int_size - 1) and (Hindi_word[i] != Hindi_word[i + 2]) and (Hindi_word[i + 1] == 77):
                                t_Hindi_word[j] = Hindi_word[i]
                                i+=1
                            else:
                                if  (i < Hindi_int_size - 1) and (Hindi_word[i] ==54) and (Hindi_word[i + 1] == 77) and (Hindi_word[i + 2] ==48):
                                    t_Hindi_word[j] =54
                                    j+=1
                                    t_Hindi_word[j] =48
                                    i+=1
                                    i+=1
                                else:
                                    if  (i < Hindi_int_size - 1) and (Hindi_word[i] ==22) and (Hindi_word[i + 1] == 77) and (Hindi_word[i + 2] ==60):
                                        t_Hindi_word[j] =89
                                        j+=1
                                        t_Hindi_word[j] =77
                                        i+=1
                                        i+=1
                                    else:
                                        if  (i < Hindi_int_size - 1) and (Hindi_word[i] ==77) and (Hindi_word[i + 1] ==46):
                                            t_Hindi_word[j] =2
                                            j+=1
                                            i+=1
                                        else:
                                            if  (i < Hindi_int_size - 1) and (Hindi_word[i] ==23) and (Hindi_word[i + 1] == 77) and (Hindi_word[i + 2] ==60):
                                                t_Hindi_word[j] =90
                                                j+=1
                                                t_Hindi_word[j] =77
                                                i+=1
                                                i+=1
                                            else:
                                                if  (i < Hindi_int_size - 1) and (Hindi_word[i] ==36) and (Hindi_word[i + 1] == 77) and (Hindi_word[i + 2] ==48):
                                                    t_Hindi_word[j] =36
                                                    j+=1
                                                    t_Hindi_word[j] =48
                                                    i+=1
                                                    i+=1
                                                else:
                                                    if  (i > 0) and (Hindi_word[i] == 60) and (t_Hindi_word[j - 1] == 28):
                                                        t_Hindi_word[j - 1] =91
                                                        j-=1
                                                    else:
                                                        if  (i > 0) and (Hindi_word[i] == 60) and (t_Hindi_word[j - 1] ==43):
                                                            t_Hindi_word[j - 1] =94
                                                            j-=1
                                                        else:
                                                            if  (i > 0) and (Hindi_word[i] == 60) and (t_Hindi_word[j - 1] ==22):
                                                                t_Hindi_word[j - 1] =89
                                                                j-=1
                                                            else:
                                                                if  (i > 0) and (Hindi_word[i] == 60) and (t_Hindi_word[j - 1] ==23):
                                                                    t_Hindi_word[j - 1] =90
                                                                    j-=1
                                                                else:
                                                                    if  (i == 0) and (i < Hindi_int_size - 1) and (Hindi_word[i] == 21) and (Hindi_word[i + 1] == 77) and (Hindi_word[i + 2] == 55):
                                                                        i+=1
                                                                        j-=1
                                                                    else:
                                                                        if  (i > 1) and (Hindi_word[i - 2] ==5) and (Hindi_word[i - 1] ==int("0x28",16)) and (Hindi_word[i] ==int("0x41",16)):
                                                                            t_Hindi_word[j] =66
                                                                        else:
                                                                            if  Hindi_word[i] ==73:
                                                                                t_Hindi_word[j] =62
                                                                            else:
                                                                                if  Hindi_word[i] ==67:
                                                                                    t_Hindi_word[j] =48
                                                                                else:
                                                                                    if  Hindi_word[i] ==17:
                                                                                        t_Hindi_word[j] =6
                                                                                    else:
                                                                                        if  (Hindi_word[i] ==21) and (Hindi_word[i + 1] ==77) and (Hindi_word[i + 2] ==22):
                                                                                            i+=1
                                                                                            j-=1
                                                                                        else:
                                                                                            if  (Hindi_word[i] ==38) and (Hindi_word[i + 1] ==77) and (Hindi_word[i + 2] ==39):
                                                                                                i+=1
                                                                                                j-=1
                                                                                            else:
                                                                                                if  (Hindi_word[i] ==26) and (Hindi_word[i + 1] ==77) and (Hindi_word[i + 2] ==27):
                                                                                                    i+=1
                                                                                                    j-=1
                                                                                                else:
                                                                                                    if  (Hindi_word[i] ==31) and (Hindi_word[i + 1] ==77) and (Hindi_word[i + 2] ==32):
                                                                                                        i+=1
                                                                                                        j-=1
                                                                                                    else:
                                                                                                        if  (Hindi_word[i] ==36) and (Hindi_word[i + 1] ==77) and (Hindi_word[i + 2] ==37):
                                                                                                            i+=1
                                                                                                            j-=1
                                                                                                        else:
                                                                                                            if  (i > 0) and (Hindi_word[i] ==77) and (Hindi_word[i - 1] == Hindi_word[i + 1]):
                                                                                                                i+=1
                                                                                                                j-=1
                                                                                                            else:
                                                                                                                if  (Hindi_word[i] ==56) and (Hindi_word[i + 1] ==60):
                                                                                                                    t_Hindi_word[j] =54
                                                                                                                    i+=1
                                                                                                                else:
                                                                                                                    if  (Hindi_word[i] ==33) and (Hindi_word[i + 1] ==60):
                                                                                                                        t_Hindi_word[j] =92
                                                                                                                        i+=1
                                                                                                                    else:
                                                                                                                        if  (Hindi_word[i] ==34) and (Hindi_word[i + 1] ==60):
                                                                                                                            t_Hindi_word[j] =93
                                                                                                                            i+=1
                                                                                                                        else:
                                                                                                                            if  (Hindi_word[i] ==50) and (Hindi_word[i + 1] ==60):
                                                                                                                                t_Hindi_word[j] =51
                                                                                                                                i+=1
                                                                                                                            else:
                                                                                                                                if  (i > 0) and (Hindi_word[i - 1] ==64) and (Hindi_word[i] ==47):
                                                                                                                                    j-=1
                                                                                                                                else:
                                                                                                                                    if  (Hindi_word[i] ==21) and (Hindi_word[i + 1] ==60):
                                                                                                                                        t_Hindi_word[j] =88
                                                                                                                                        i+=1
                                                                                                                                    else:
                                                                                                                                        if  (Hindi_word[i] ==22) and (Hindi_word[i + 1] ==60):
                                                                                                                                            t_Hindi_word[j] =89
                                                                                                                                            i+=1
                                                                                                                                        else:
                                                                                                                                            if  (Hindi_word[i] ==23) and (Hindi_word[i + 1] ==60):
                                                                                                                                                t_Hindi_word[j] =90
                                                                                                                                                i+=1
                                                                                                                                            else:
                                                                                                                                                if  (Hindi_word[i] ==28) and (Hindi_word[i + 1] ==60):
                                                                                                                                                    t_Hindi_word[j] =91
                                                                                                                                                    i+=1
                                                                                                                                                else:
                                                                                                                                                    if  (Hindi_word[i] ==43) and (Hindi_word[i + 1] ==60):
                                                                                                                                                        t_Hindi_word[j] =94
                                                                                                                                                        i+=1
                                                                                                                                                    else:
                                                                                                                                                        if  Hindi_word[i] ==113:
                                                                                                                                                            t_Hindi_word[j] = Hindi_word[i + 1]
                                                                                                                                                            t_Hindi_word[j + 1] = Hindi_word[i]
                                                                                                                                                            i+=1
                                                                                                                                                            j+=1
                                                                                                                                                        else:
                                                                                                                                                            if  (i > 0) and ((Hindi_word[i - 1] ==int("0x3e",16)) or (Hindi_word[i - 1] ==6)) and (Hindi_word[i] ==7) and (Hindi_word[i + 1] ==6):
                                                                                                                                                                t_Hindi_word[j] =47
                                                                                                                                                                t_Hindi_word[j + 1] =62
                                                                                                                                                                j+=1
                                                                                                                                                                i+=1
                                                                                                                                                            else:
                                                                                                                                                                if  (i > 0) and (Hindi_word[i - 1] ==8) and (Hindi_word[i] ==6):
                                                                                                                                                                    t_Hindi_word[j] =62
                                                                                                                                                                else:
                                                                                                                                                                    if  (i > 0) and (Hindi_word[i] ==7) and (Hindi_word[i + 1] ==6):
                                                                                                                                                                        t_Hindi_word[j] =47
                                                                                                                                                                        t_Hindi_word[j + 1] =62
                                                                                                                                                                        j+=1
                                                                                                                                                                        i+=1
                                                                                                                                                                    else:
                                                                                                                                                                        if  (Hindi_word[i] ==56) and (Hindi_word[i + 1] ==60):
                                                                                                                                                                            t_Hindi_word[j] =54
                                                                                                                                                                            i+=1
                                                                                                                                                                        else:
                                                                                                                                                                            if  (Hindi_word[i] ==21) and (Hindi_word[i + 1] ==60):
                                                                                                                                                                                t_Hindi_word[j] =88
                                                                                                                                                                                i+=1
                                                                                                                                                                            else:
                                                                                                                                                                                if  (Hindi_word[i] ==22) and (Hindi_word[i + 1] ==60):
                                                                                                                                                                                    t_Hindi_word[j] =89
                                                                                                                                                                                    i+=1
                                                                                                                                                                                else:
                                                                                                                                                                                    if  (Hindi_word[i] ==23) and (Hindi_word[i + 1] ==60):
                                                                                                                                                                                        t_Hindi_word[j] =90
                                                                                                                                                                                        i+=1
                                                                                                                                                                                    else:
                                                                                                                                                                                        if  (Hindi_word[i] ==28) and (Hindi_word[i + 1] ==60):
                                                                                                                                                                                            t_Hindi_word[j] =91
                                                                                                                                                                                            i+=1
                                                                                                                                                                                        else:
                                                                                                                                                                                            if  (Hindi_word[i] ==43) and (Hindi_word[i + 1] ==60):
                                                                                                                                                                                                t_Hindi_word[j] =94
                                                                                                                                                                                                i+=1
                                                                                                                                                                                            else:
                                                                                                                                                                                                if  (Hindi_word[i] ==50) and (Hindi_word[i + 1] ==60):
                                                                                                                                                                                                    t_Hindi_word[j] =51
                                                                                                                                                                                                    i+=1
                                                                                                                                                                                                else:
                                                                                                                                                                                                    if  (i > 0) and (Hindi_word[i] ==int("0x3f",16)) and (Hindi_word[i + 1] ==6):
                                                                                                                                                                                                        t_Hindi_word[j] =47
                                                                                                                                                                                                        t_Hindi_word[j + 1] =62
                                                                                                                                                                                                        j+=1
                                                                                                                                                                                                        i+=1
                                                                                                                                                                                                    else:
                                                                                                                                                                                                        if  (i > 0) and (Hindi_word[i] ==112) and (Hindi_word[i + 1] ==40):
                                                                                                                                                                                                            t_Hindi_word[j] =40
                                                                                                                                                                                                            t_Hindi_word[j + 1] =113
                                                                                                                                                                                                            i+=1
                                                                                                                                                                                                            j+=1
                                                                                                                                                                                                        else:
                                                                                                                                                                                                            if  (i > 0) and (Hindi_word[i] ==2) and (Hindi_word[i + 1] ==int("0x2a",16)):
                                                                                                                                                                                                                t_Hindi_word[j] =46
                                                                                                                                                                                                                t_Hindi_word[j + 1] =42
                                                                                                                                                                                                                i+=1
                                                                                                                                                                                                                j+=1
                                                                                                                                                                                                            else:
                                                                                                                                                                                                                if  (i > 0) and (Hindi_word[i] ==int("0x3f",16)) and ((Hindi_word[i + 1] ==int("0x13",16)) or (Hindi_word[i + 1] ==9)):
                                                                                                                                                                                                                    t_Hindi_word[j] =47
                                                                                                                                                                                                                    t_Hindi_word[j + 1] =75
                                                                                                                                                                                                                    i+=1
                                                                                                                                                                                                                    j+=1
                                                                                                                                                                                                                else:
                                                                                                                                                                                                                    if  (i > 0) and (Hindi_word[i] ==7) and ((Hindi_word[i + 1] ==int("0x13",16)) or (Hindi_word[i + 1] ==9)):
                                                                                                                                                                                                                        t_Hindi_word[j] =7
                                                                                                                                                                                                                        t_Hindi_word[j + 1] =47
                                                                                                                                                                                                                        t_Hindi_word[j + 2] =75
                                                                                                                                                                                                                        i+=1
                                                                                                                                                                                                                        j+=1
                                                                                                                                                                                                                        j+=1
                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                        if  (i > 0) and (Hindi_word[i] ==8) and ((Hindi_word[i + 1] ==int("0x0f",16)) or (Hindi_word[i + 1] ==int("0x0f",16))):
                                                                                                                                                                                                                            t_Hindi_word[j] =8
                                                                                                                                                                                                                            t_Hindi_word[j + 1] =71
                                                                                                                                                                                                                            i+=1
                                                                                                                                                                                                                            j+=1
                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                            if  (i > 0) and (Hindi_word[i] ==7) and (Hindi_word[i + 1] ==10):
                                                                                                                                                                                                                                t_Hindi_word[j] =7
                                                                                                                                                                                                                                t_Hindi_word[j + 1] =47
                                                                                                                                                                                                                                t_Hindi_word[j + 2] =66
                                                                                                                                                                                                                                i+=1
                                                                                                                                                                                                                                j+=1
                                                                                                                                                                                                                                j+=1
                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                if  (i > 0) and (Hindi_word[i] ==int("0x41",16)) and (Hindi_word[i + 1] ==6):
                                                                                                                                                                                                                                    t_Hindi_word[j] =65
                                                                                                                                                                                                                                    t_Hindi_word[j + 1] =53
                                                                                                                                                                                                                                    t_Hindi_word[j + 2] =62
                                                                                                                                                                                                                                    i+=1
                                                                                                                                                                                                                                    j+=1
                                                                                                                                                                                                                                    j+=1
                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                    if  (i > 0) and (Hindi_word[i] ==int("0x3f",16)) and (Hindi_word[i + 1] ==10):
                                                                                                                                                                                                                                        t_Hindi_word[j] =63
                                                                                                                                                                                                                                        t_Hindi_word[j + 1] =47
                                                                                                                                                                                                                                        t_Hindi_word[j + 2] =66
                                                                                                                                                                                                                                        i+=1
                                                                                                                                                                                                                                        j+=1
                                                                                                                                                                                                                                        j+=1
                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                        if  (i > 0) and (Hindi_word[i] ==6) and not ((Hindi_word[i - 1] ==int("0x21",16)) or (Hindi_word[i - 1] ==int("0x26",16)) or (Hindi_word[i - 1] ==int("0x27",16)) or (Hindi_word[i - 1] ==int("0x30",16)) or (Hindi_word[i - 1] ==int("0x3f",16)) or (Hindi_word[i - 1] ==int("0x5b",16)) or (Hindi_word[i - 1] ==int("0x4b",16)) or (Hindi_word[i - 1] ==int("0x4c",16)) or (Hindi_word[i - 1] ==int("0x42",16)) or (Hindi_word[i - 1] ==int("0x5c",16))):
                                                                                                                                                                                                                                            t_Hindi_word[j] =62
                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                            if  ((Hindi_word[i] ==16) or (Hindi_word[i] ==15)) and (i != Hindi_int_size - 1):
                                                                                                                                                                                                                                                t_Hindi_word[j] =8
                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                if  (Hindi_word[i] ==72) and (i == Hindi_int_size - 1):
                                                                                                                                                                                                                                                    t_Hindi_word[j] =71
                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                    if  i > 0 and (Hindi_word[i - 1] ==62) and (Hindi_word[i] ==47) and (i == Hindi_int_size - 1):
                                                                                                                                                                                                                                                        t_Hindi_word[j] =15
                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                        if  (Hindi_word[i] ==112) and ((Hindi_word[i + 1] ==46)):  
                                                                                                                                                                                                                                                            t_Hindi_word[j] =46
                                                                                                                                                                                                                                                            j+=1
                                                                                                                                                                                                                                                            t_Hindi_word[j] =113
                                                                                                                                                                                                                                                            i+=1
                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                            t_Hindi_word[j] = Hindi_word[i]
                i+=1
                j+=1
            t_Hindi_word[j] = 0
            self.strcpy(Hindi_word, t_Hindi_word)
            if  zer_flag > 0:
                Hindi_int_size = self.strlen(Hindi_word)
                i = j = 0
                while  i < Hindi_int_size:
                    if  (i < Hindi_int_size) and ((Hindi_word[i] ==63) or (Hindi_word[i] ==65) or (Hindi_word[i] ==113)): 
                        i+=1
                    else:
                        if  (i == 0) and ((Hindi_word[i] ==7) or (Hindi_word[i] ==9)):
                            t_Hindi_word[j] =5
                            j+=1
                            i+=1
                        else:
                            t_Hindi_word[j] = Hindi_word[i]
                            i+=1
                            j+=1
                t_Hindi_word[j] = 0
                self.strcpy(Hindi_word, t_Hindi_word)
    def check_urdu_hyphen_word(self, Hindi_word, urdu_word, flag1):
        Hindi_strip=[0]*40
        urdu_strip=[0]*40
        final_word=[0]*40
        urdu8=[0]*30
        print_hindi_word=[0]*40
        ulen = 0
        urdu_len = 0
        flag = 0
        found = 0
        usize = 0
        flag1 = 0
        j = 0
        for  i in range(0,self.strlen(Hindi_word)):
            if  (Hindi_word[i] == 253) or (Hindi_word[i] == 251):
                if  Hindi_word[i] == 253: flag = 0
                else: flag = 1
                Hindi_strip[j] = 0
                j+=1
                ulen = self.check_urdu_word_dictionary(Hindi_strip, urdu_strip)
                if  (ulen) > 0:
                    for  k in range(0,ulen):
                        urdu_word[urdu_len] = urdu_strip[k]
                        urdu_len+=1
                    if  Hindi_word[i] == 253:
                        if  self.checkendMATRA(urdu_word[urdu_len - 2]):
                            if  urdu_word[urdu_len - 2] ==193:
                                urdu_word[urdu_len - 2] =194
                            else:
                                urdu_word[urdu_len] =116
                                urdu_len+=1
                                urdu_word[urdu_len] = 6
                                urdu_len+=1
                        
                        urdu_word[urdu_len] =32
                        urdu_len+=1
                        urdu_word[urdu_len] = 0
                        urdu_len+=1
                   
                    self.word_found+=1
                    flag1 = 1
                else:
                    self.normalise_Hindi_word(Hindi_strip)
                    self.rule_based_Hindi_word_to_urdu(Hindi_strip, urdu_strip)
                    usize = self.strlen(urdu_strip)
                    usize=self.improve_urdu_word(urdu_strip, usize)
                    self.UnicodeTo8(urdu_strip, self.strlen(urdu_strip), urdu8)
                    if  self.check_urdu_corpus(urdu8, final_word) > 0:
                        found = 1
                        for  k in range(0,self.strlen(final_word)):
                            urdu_word[urdu_len] = final_word[k]
                            urdu_len+=1
                            urdu_word[urdu_len] = 6
                            urdu_len+=1
                        self.corpus_found+=1
                        urdu_word[urdu_len] = 0
                        k = self.strlen(Hindi_strip)
                        j = 0
                        for  k in range(0,self.strlen(Hindi_word)):
                            print_hindi_word[j] = Hindi_word[k]
                            j+=1
                            print_hindi_word[j] = 9
                            j+=1
                        flag1 = 2
                    else:
                        for  k in range(0,self.strlen(urdu_strip)):
                            urdu_word[urdu_len] = urdu_strip[k]
                            urdu_len+=1
                    if  not (flag != 0):
                        if  self.checkendMATRA(urdu_word[urdu_len - 2]):
                            if  urdu_word[urdu_len - 2] ==193:
                                urdu_word[urdu_len - 2] =194
                            else:
                                urdu_word[urdu_len] =116
                                urdu_len+=1
                                urdu_word[urdu_len] = 6
                                urdu_len+=1
                       
                        urdu_word[urdu_len] =32
                        urdu_len+=1
                        urdu_word[urdu_len] = 0
                        urdu_len+=1
                    else:
                        urdu_word[urdu_len] =32
                        urdu_len+=1
                        urdu_word[urdu_len] = 0
                        urdu_len+=1
                    if  not (found != 0) and self.strlen(urdu_strip) > 2:
                        self.word_not_found+=1
                        k = self.strlen(Hindi_strip)
                        j = 0
                        for  k in range(0,self.strlen(Hindi_word)):
                            print_hindi_word[j] = Hindi_word[k]
                            j+=1
                            print_hindi_word[j] = 9
                            j+=1
                    else:
                        self.word_found+=1
                    if  not (found != 0):
                        j = 0
                        for k in range(0, self.strlen(Hindi_word)):
                            print_hindi_word[j] = Hindi_strip[k]
                            j+=1
                            print_hindi_word[j] = 9
                            j+=1
                        print_hindi_word[j] = 0
                        j+=1
                        self.add_frequency(print_hindi_word, self.strlen(print_hindi_word))
                        flag1 = 0
                j = 0
            else:
                Hindi_strip[j] = Hindi_word[i]
                j+=1
        if  j > 0:
            ulen = self.check_urdu_word_dictionary(Hindi_strip, urdu_strip)
            if (ulen) > 0:
                ulen=self.improve_urdu_word(urdu_strip, ulen)
                for  k in range(0,ulen):
                    urdu_word[urdu_len] = urdu_strip[k]
                    urdu_len+=1
                self.word_found+=1
                flag1 = 1
            else:
                Hindi_strip[j] = 0
                j+=1
                self.normalise_Hindi_word(Hindi_strip)
                for  i in range(0,30):
                    urdu_strip[i] = 0
                self.rule_based_Hindi_word_to_urdu(Hindi_strip, urdu_strip)
                ulen = self.strlen(urdu_strip)
                ulen=self.improve_urdu_word(urdu_strip, ulen)
                self.UnicodeTo8(urdu_strip, self.strlen(urdu_strip), urdu8)
                if  self.check_urdu_corpus(urdu8, final_word) > 0:
                    for  i in range(0,self.strlen(final_word)):
                        urdu_word[urdu_len] = final_word[i]
                        urdu_len+=1
                        urdu_word[urdu_len] = 6
                        urdu_len+=1
                    self.corpus_found+=1
                    urdu_word[urdu_len] = 0
                    i = self.strlen(Hindi_strip)
                    j = 0
                    for i in range(0, self.strlen(Hindi_word)):
                        print_hindi_word[j] = Hindi_word[i]
                        j+=1
                        print_hindi_word[j] = 9
                        j+=1
                    flag1 = 2
                    return flag1, urdu_len
                else:
                    for  k in range(0,self.strlen(urdu_strip)):
                        urdu_word[urdu_len] = urdu_strip[k]
                        urdu_len+=1
                if  self.strlen(urdu_strip) > 2:
                    self.word_not_found+=1
                    j = 0
                    for k in range(0, self.strlen(Hindi_word)):
                        print_hindi_word[j] = Hindi_word[k]
                        j+=1
                        print_hindi_word[j] = 9
                        j+=1
                else:
                    self.word_found+=1
                flag1 = 0
                j = 0
                for i in range(0, self.strlen(Hindi_word)):
                    print_hindi_word[j] = Hindi_word[i]
                    j+=1
                    print_hindi_word[j] = 9
                    j+=1
                print_hindi_word[j] = 0
                j+=1
                self.add_frequency(print_hindi_word, self.strlen(print_hindi_word))
        return flag1, urdu_len
    def UnicodeTo8(self, UnicodeString, UnicodePos, szOut):
        len = 0
        j = 0
        for  i in range(0,UnicodePos,2):
            if  not (UnicodeString[i + 1] != 0) and ((UnicodeString[i] == ord('-')) or (UnicodeString[i] == 173)):
                szOut[j] = 251
                j+=1
            else:
                if  (not (UnicodeString[i + 1] != 0)) and (UnicodeString[i] == ord('.')):
                    szOut[j] = 252
                    j+=1
                else:
                    if  UnicodeString[i + 1] == 32:
                        continue
                    else:
                        szOut[j] = UnicodeString[i]
                        j+=1
        szOut[j] = 0
        j+=1
        return
    def normalise_Hindi_dot(self, Hindi_word):
            t_Hindi_word=[0]*40
            j = 0
            i = 0
            while  Hindi_word[i] > 0:
                if  (Hindi_word[i] == 251) and (Hindi_word[i + 1] ==15) and (Hindi_word[i + 2] == 251):
                    t_Hindi_word[j] = 253
                    i+=1
                    i+=1
                else:
                    if  (Hindi_word[i] == 251) and (Hindi_word[i + 1] == 19) and (Hindi_word[i + 2] == 251): 
                        t_Hindi_word[j] = 251
                        i+=1
                        i+=1
                    else:
                        if  (Hindi_word[i] ==56) and (Hindi_word[i + 1] ==60):
                            t_Hindi_word[j] =54
                            i+=1
                        else:
                            if  (Hindi_word[i] ==50) and (Hindi_word[i + 1] ==60):
                                t_Hindi_word[j] =51
                                i+=1
                            else:
                                if  (Hindi_word[i] ==21) and (Hindi_word[i + 1] ==60):
                                    t_Hindi_word[j] =88
                                    i+=1
                                else:
                                    if  (Hindi_word[i] ==22) and (Hindi_word[i + 1] ==60):
                                        t_Hindi_word[j] =89
                                        i+=1
                                    else:
                                        if  (Hindi_word[i] ==23) and (Hindi_word[i + 1] ==60):
                                            t_Hindi_word[j] =90
                                            i+=1
                                        else:
                                            if  (Hindi_word[i] ==33) and (Hindi_word[i + 1] ==60):
                                                t_Hindi_word[j] =92
                                                i+=1
                                            else:
                                                if  (Hindi_word[i] ==34) and (Hindi_word[i + 1] ==60):
                                                    t_Hindi_word[j] =93
                                                    i+=1
                                                else:
                                                    if  (Hindi_word[i] ==28) and (Hindi_word[i + 1] ==60):
                                                        t_Hindi_word[j] =91
                                                        i+=1
                                                    else:
                                                        if  (Hindi_word[i] ==43) and (Hindi_word[i + 1] ==60):
                                                            t_Hindi_word[j] =94
                                                            i+=1
                                                        else:
                                                            t_Hindi_word[j] = Hindi_word[i]
                i+=1
                j+=1
            self.strcpy(Hindi_word, t_Hindi_word)
    
    def check_urdu_word_dictionary(self, Hindi_strip, urdu):
        len = 0
        hword=[0]*50
        len = self.check_urdu_word_dictionary1(Hindi_strip, urdu)
        if  (len) > 0:
            return len
        self.remove_end_Hindi_dai(Hindi_strip, hword)
        len = self.check_urdu_word_dictionary1(hword, urdu)
        if  (len) > 0:
            return len
        self.remove_end_Hindi_a(Hindi_strip, hword)
        if  self.strlen(hword) > 0:
            len = self.check_urdu_word_dictionary1(hword, urdu)
            if  (len) > 0:
                urdu[len] =33
                len+=1
                urdu[len] = 6
                len+=1
                urdu[len] =78
                len+=1
                urdu[len] = 6
                len+=1
                return len
        self.remove_end_Hindi_i(Hindi_strip, hword)
        if  self.strlen(hword) > 0:
            len = self.check_urdu_word_dictionary1(hword, urdu)
            if  (len) > 0:
                urdu[len] =33
                len+=1
                urdu[len] = 6
                len+=1
                urdu[len] =80
                len+=1
                urdu[len] = 6
                len+=1
                return len
        self.remove_end_Hindi_u(Hindi_strip, hword)
        if  self.strlen(hword) > 0:
            len = self.check_urdu_word_dictionary1(hword, urdu)
            if  (len) > 0:
                c = hword[self.strlen(hword) - 1]
                if  c >=62 and c <=76:
                    urdu[len] =33
                    len+=1
                else:
                    urdu[len] =36
                    len+=1
                urdu[len] = 6
                len+=1
                urdu[len] =79
                len+=1
                urdu[len] = 6
                len+=1
                return len
        self.remove_end_Hindi_vnoon(Hindi_strip, hword)
        if  self.strlen(hword) > 0:
            len = self.check_urdu_word_dictionary1(hword, urdu)
            if (len) > 0:
                urdu[len] =36
                len+=1
                urdu[len] = 6
                len+=1
                urdu[len] =70
                len+=1
                urdu[len] = 6
                len+=1
                return len
        self.remove_end_Hindi_ni(Hindi_strip, hword)
        if  self.strlen(hword) > 0:
            len = self.check_urdu_word_dictionary1(hword, urdu)
            if (len) > 0:
                urdu[len] =70
                len+=1
                urdu[len] = 6
                len+=1
                return len
        self.remove_all_Hindi_dai(Hindi_strip, hword)
        len = self.check_urdu_word_dictionary1(hword, urdu)
        if (len) > 0:
            return len
        self.similar_Hindi(Hindi_strip, hword)
        return (self.check_urdu_word_dictionary1(hword, urdu))
    
    
    def remove_end_Hindi_a(self, Hindi_strip, hword):
        len = self.strlen(Hindi_strip)
        hw=[0]*50
        if  len > 49:
            len = 49
        for  i in range(0,50):
            hw[i] = 0
        i = 0
        for  i in range(0,len-1):
            hw[i] = Hindi_strip[i]
        if i != 0:
            i += 1
        if  Hindi_strip[i] ==5:
            hw[i] = 0
        else:
            hw[0] = 0
        self.strcpy(hword, hw)
    
    def remove_end_Hindi_i(self, Hindi_strip, hword):
        len = self.strlen(Hindi_strip)
        hw=[0]*50
        if  len > 49:
            len = 49
        for  i in range(0,50):
            hw[i] = 0
        i = 0
        for  i in range(0,len-1):
            hw[i] = Hindi_strip[i]
        if i != 0:
            i += 1
        if  Hindi_strip[i] ==7:
            hw[i] = 0
        else:
            hw[0] = 0
        self.strcpy(hword, hw)
    
    
    def remove_end_Hindi_u(self, Hindi_strip, hword):
        len = self.strlen(Hindi_strip)
        hw=[0]*50
        if  len > 49:
            len = 49
        for  i in range(0,50):
            hw[i] = 0
        i = 0
        for  i in range(0,len-1):
            hw[i] = Hindi_strip[i]
        if i != 0:
            i += 1
        if  Hindi_strip[i] ==9:
            hw[i] = 0
        else:
            hw[0] = 0
        self.strcpy(hword, hw)
    
    def remove_end_Hindi_vnoon(self, Hindi_strip, hword):
        len = self.strlen(Hindi_strip)
        hw=[0]*50
        if  len > 49:
            len = 49
        for  i in range(0,50):
            hw[i] = 0

        i = 0
        for  i in range(0,len-2):
            hw[i] = Hindi_strip[i]
        if i != 0:
            i += 1
        if  Hindi_strip[i] ==10 and Hindi_strip[i + 1] ==2:
            hw[i] = 0
        else:
            hw[0] = 0
        self.strcpy(hword, hw)
    
    def remove_end_Hindi_ni(self, Hindi_strip, hword):
        len = self.strlen(Hindi_strip)
        hw=[0]*50
        if  len > 49:
            len = 49
        for  i in range(0,50):
            hw[i] = 0
        i = 0
        for  i in range(0,len-2):
            hw[i] = Hindi_strip[i]
        if i != 0:
            i += 1
        if  Hindi_strip[i] ==40 and Hindi_strip[i + 1] ==63:
            hw[i] = 0
        else:
            hw[0] = 0
        self.strcpy(hword, hw)
    def remove_end_Hindi_dai(self, Hindi_strip, hword):
        len = self.strlen(Hindi_strip)
        hw=[0]*50
        if  len > 49:
            len = 49
        for  i in range(0,50):
            hw[i] = 0
        i=0
        for  i in range(0,len-1):
            hw[i] = Hindi_strip[i]
        if i!=0:
            i+=1
        
        if  Hindi_strip[i] ==63 or Hindi_strip[i] ==65:
            hw[i] = 0
        else:
            hw[0] = 0
        self.strcpy(hword, hw)
    def remove_all_Hindi_dai(self, Hindi_strip, hword):
        j = 0
        len = self.strlen(Hindi_strip)
        hw=[0]*50
        if  len > 49:
            len = 49
            
        i=0
        for i in range(0,len):
            if  Hindi_strip[i] ==63 or Hindi_strip[i] ==65: continue
            else:
                hw[j] = Hindi_strip[i]
                j+=1
        if i!=0:
            i+=1
            
        if  i == j:
            hw[0] = 0
        else:
            hw[j] = 0
        self.strcpy(hword, hw)
    def similar_Hindi(self, Hindi_strip, hword):
        j = 0
        len = self.strlen(Hindi_strip)
        flag = 0
        hw=[0]*50
        if  len > 49:
            len = 49
        for  i in range(0,len):
            if  Hindi_strip[i] ==23:
                hw[j] =90
                j+=1
                flag+=1
                continue
            if  Hindi_strip[i] ==21:
                hw[j] =88
                j+=1
                flag+=1
                continue
            if  Hindi_strip[i] ==22:
                hw[j] =89
                j+=1
                flag+=1
                continue
            if  Hindi_strip[i] ==43:
                hw[j] =94
                j+=1
                flag+=1
                continue
            else:
                hw[j] = Hindi_strip[i]
                j+=1
        hw[j] = 0
        if  flag == 0:
            hw[0] = 0
        self.strcpy(hword, hw)
    def check_urdu_word_dictionary1(self, Hindi_strip, urdu):
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
        Hindi=[0]*40
        temp1=[0]*40
        if  not (self.strlen(Hindi_strip) != 0):
            return 0
        self.strcpy(Hindi, Hindi_strip)
        self.normalise_Hindi_kdot(Hindi)
        high = self.dict_word_count - 1
        while  low <= high:
            mid = int((low + high) / 2)
            self.strcpy(read_word, self.Hindi_dict[mid])
            si = self.strcmp(read_word, Hindi)
            if  si == 0 or si == -1 or si == 1:
                si = 1 * si
            if  not (self.strcmp(read_word, Hindi) != 0):
                self.strcpy(temp, self.urdu_dict[mid])
                self.convert_urdu_sindhi(temp, temp1)
                self.strcpy(temp, temp1)
                k = 0
                for  i in range(0,self.strlen(temp)):
                        if  temp[i] == 255:
                            if  i < self.strlen(temp) - 1:
                                urdu[k] = 32
                                k+=1
                                urdu[k] = 0
                                k+=1
                            else:
                                continue
                        else:
                            if  temp[i] == 251:
                                urdu[k] = ord('-')
                                k+=1
                                urdu[k] = 0
                                k+=1
                            else:
                                urdu[k] = temp[i]
                                k+=1
                                urdu[k] = 6
                                k+=1
                return k
            if  self.strcmp(read_word, Hindi) < 0:
                low = mid + 1
            else:
                high = mid - 1
        return 0
    def convert_urdu_sindhi(self, urdu, sindhi):
            len = self.strlen(urdu)
            i=j = 0
            while i <= len:
                if  urdu[i] ==204:
                    sindhi[j] =74
                    j+=1
                else:
                    if  urdu[i] ==210:
                        sindhi[j] =74
                        j+=1
                    else:
                        if  urdu[i] ==186:
                            sindhi[j] =70
                            j+=1
                        else:
                            if  urdu[i] ==136:
                                sindhi[j] =138
                                j+=1
                            else:
                                if  urdu[i] ==145:
                                    sindhi[j] =153
                                    j+=1
                                else:
                                    if  urdu[i] ==193 and i != len - 1:
                                        sindhi[j] =71
                                        j+=1
                                    else:
                                        if  urdu[i] ==169 and urdu[i + 1] ==190:
                                            sindhi[j] =169
                                            j+=1
                                            i+=1
                                        else:
                                            if  urdu[i] ==193 and urdu[i + 1] ==190:
                                                sindhi[j] =71
                                                j+=1
                                                i+=1
                                            else:
                                                if  urdu[i] ==121 and urdu[i + 1] ==190:
                                                    sindhi[j] =122
                                                    j+=1
                                                    i+=1
                                                else:
                                                    if  urdu[i] ==136 and urdu[i + 1] ==190:
                                                        sindhi[j] =141
                                                        j+=1
                                                        i+=1
                                                    else:
                                                        if  urdu[i] ==42 and urdu[i + 1] ==190:
                                                            sindhi[j] =127
                                                            j+=1
                                                            i+=1
                                                        else:
                                                            if  urdu[i] ==193 and urdu[i + 1] ==190:
                                                                sindhi[j] =71
                                                                j+=1
                                                                i+=1
                                                            else:
                                                                if  urdu[i] ==121 and urdu[i + 1] !=190:
                                                                    sindhi[j] =125
                                                                    j+=1
                                                                else:
                                                                    sindhi[j] = urdu[i]
                                                                    j += 1
                i+=1
    def normalise_Hindi_kdot(self, Hindi_word):
            t_Hindi_word=[0]*40
            j = 0
            i = 0
            while  Hindi_word[i] > 0:
                if  (Hindi_word[i] == 251) and (Hindi_word[i + 1] ==15) and (Hindi_word[i + 2] == 251):
                    t_Hindi_word[j] = 253
                    i+=1
                    i+=1
                else:
                    if  (Hindi_word[i] ==88):
                        t_Hindi_word[j] =21
                    else:
                        if  (Hindi_word[i] ==22) and (Hindi_word[i + 1] ==60):
                            t_Hindi_word[j] =89
                            i+=1
                        else:
                            if  (Hindi_word[i] == 28) and (Hindi_word[i + 1] == 77) and (Hindi_word[i + 2] ==60):
                                t_Hindi_word[j] =91
                                i+=1
                                i+=1
                            else:
                                if  (Hindi_word[i] ==22) and (Hindi_word[i + 1] == 77) and (Hindi_word[i + 2] ==60):
                                    t_Hindi_word[j] =89
                                    i+=1
                                    i+=1
                                else:
                                    if  (Hindi_word[i] ==21) and (Hindi_word[i + 1] == 77) and (Hindi_word[i + 2] ==60):
                                        t_Hindi_word[j] =88
                                        i+=1
                                        i+=1
                                    else:
                                        if  (Hindi_word[i] ==43) and (Hindi_word[i + 1] == 77) and (Hindi_word[i + 2] ==60):
                                            t_Hindi_word[j] =94
                                            i+=1
                                            i+=1
                                        else:
                                            if  (Hindi_word[i] ==23) and (Hindi_word[i + 1] == 77) and (Hindi_word[i + 2] ==60):
                                                t_Hindi_word[j] =90
                                                i+=1
                                                i+=1
                                            else:
                                                if  (Hindi_word[i] ==23) and (Hindi_word[i + 1] ==60):
                                                    t_Hindi_word[j] =90
                                                    i+=1
                                                else:
                                                    if  (Hindi_word[i] ==33) and (Hindi_word[i + 1] ==60):
                                                        t_Hindi_word[j] =92
                                                        i+=1
                                                    else:
                                                        if  (Hindi_word[i] ==34) and (Hindi_word[i + 1] ==60):
                                                            t_Hindi_word[j] =93
                                                            i+=1
                                                        else:
                                                            if  (Hindi_word[i] ==28) and (Hindi_word[i + 1] ==60):
                                                                t_Hindi_word[j] =91
                                                                i+=1
                                                            else:
                                                                if  (Hindi_word[i] ==43) and (Hindi_word[i + 1] ==60):
                                                                    t_Hindi_word[j] =94
                                                                    i+=1
                                                                else:
                                                                    t_Hindi_word[j] = Hindi_word[i]
                i+=1
                j+=1
            self.strcpy(Hindi_word, t_Hindi_word)
    def check_similar_word_dictionary(self, Hindi, similar):
            low = 0
            read_word=[0]*40
            high = self.similar_word_count - 1
            self.strcpy(similar, Hindi)
            while  low <= high:
                mid = int((low + high) / 2)
                self.strcpy(read_word, self.sd[mid].original)
                if  not (self.strcmp(read_word, Hindi) != 0):
                    self.strcpy(similar, self.sd[mid].similar)
                    return 1
                if  self.strcmp(read_word, Hindi) < 0:
                    low = mid + 1
                else:
                    high = mid - 1
            return 0
    def add_frequency(self, urdu, urdu_size):
        read_word=[0]*80
        Urdu_UTF8=[0]*40
        temp=[0]*80
        total = 0
        if  urdu_size <= 2: return 1
        for  i in range(0,self.word_total):
            if  not (self.strcmp(self.wordlist[i].word, urdu) != 0):
                self.wordlist[i].count+=1
                return 1
        self.wordlist[self.word_total].count = 1
        self.strcpy(self.wordlist[self.word_total].word, urdu)
        self.word_total+=1
        return 0
    
    
    def read_urdu_hindi_dict(self):
        dic_word=[0]*40
        freq=[0]*8
        
        
        FILE_NAME = os.path.join(self.appPath,"dict1.bin")
        
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return
        
        r = open(FILE_NAME, 'rb')
        self.dict_word_count = int.from_bytes(r.read(4), 'little')
        for i in range(0, self.dict_word_count):
            rawBytes = r.read(len(self.Hindi_dict[i]))
            for j, byte in enumerate(rawBytes):
                self.Hindi_dict[i][j] = byte
            
            rawBytes = r.read(len(self.urdu_dict[i]))
            for j, byte in enumerate(rawBytes):
                self.urdu_dict[i][j] = byte
        r.close()
        self.isDic = True
    
    
    def read_similar_dict(self, similar_words, similar_word_count):
        FILE_NAME = os.path.join(self.appPath,"similar.bin")
        
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return
        
        r = open(FILE_NAME, 'rb')
        self.similar_word_count = int.from_bytes(r.read(4), 'little')
        for i in range(0, self.similar_word_count):
            rawBytes = r.read(len(similar_words[i].original))
            for j, byte in enumerate(rawBytes):
                similar_words[i].original[j] = byte
            
            rawBytes = r.read(len(similar_words[i].similar))
            for j, byte in enumerate(rawBytes):
                similar_words[i].similar[j] = byte
        r.close()
        self.isDicSimilar = True
        return self.similar_word_count
    
    
    def strcpy(self, str1, str2):
        t = 0
        len2 = self.strlen(str2)
        for t in range(0, len2 + 1):
            if t < len(str1):
                try:
                    str1[t] = str2[t]
                except IndexError:
                    str1[t] = 0
                    break
            else:
                str1[len(str1 - 1)] = 0
                break
    
    
    def strcmp(self, str1, str2):
        len1 = self.strlen(str1)
        len2 = self.strlen(str2)
        if len1 > len2:
            len = len1
        else:
            len = len2
        for t in range(0, len):
            if str1[t] < str2[t]: return -1
            if str1[t] > str2[t]: return 1
        return 0
    
    
    def strlen(self, source):
        if len(source) == 0: return 0
        size = len(source)
        length = 0
        for t in range(0, size):
            if source[t] != 0:
                length += 1
            else:
                break
        return length
    
    
    def strcat(self, str1, str2):
        len1 = self.strlen(str1)
        len2 = self.strlen(str2)
        j = len1
        for t in range(0, len2):
            str1[j] = str2[t]
            j += 1
        str1[j] = 0
    
    
    def byte2Str(self, data, length, SKIPFIRST2BYTES):
        s = ""
        b1 = 10
        b2 = 111
        c1 = b1 * 256 + b2
        c = (c1)
        sala=1545
        if SKIPFIRST2BYTES:
            for t in range(2, length-2, 2):
                b1 = data[t]
                b2 = data[t + 1]
                c1 = b1 + (b2 * 256)
                c=c1
                if c == 1545 or c == 65279:
                    continue
                s = s + chr(c)
        else:
            for t in range(0, length-2, 2):
                b1 = data[t]
                b2 = data[t + 1]
                c1 = b1 + (b2 * 256)
                c=c1
                s = s + chr(c)
        return s
    
    
    def str2Byte(self, str1):
        data = [0] * (len(str1) * 2 + 2)
        length = 0
        data[length] = 255
        length += 1
        data[length] = 254
        length += 1
        for t in range(0, len(str1)):
            ch = ord(str1[t])
            code = ch
            data[length] = int(code % 256)
            length += 1
            data[length] = int(code / 256)
            length += 1
        return data
    
    
    def printMSG(self, s):
        #self.MSG = self.MSG + self.separator + s
        self.MSG = self.MSG  + s
    
    def printMSG2(self, s, v):
        #self.MSG = self.MSG + self.separator + s + v
        self.MSG = self.MSG  + s + v
    
    def convertToByte(self, u):
        u = u % 256
        return u
    
    def splitStr(self, txt, seps):
        default_sep = seps[0]
    
        for sep in seps[1:]:
            txt = txt.replace(sep, default_sep)
        return [i.strip() for i in txt.split(default_sep)]






