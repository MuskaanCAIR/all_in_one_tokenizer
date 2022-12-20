import numpy as np
import os.path
import re
import string
import os, sys

class unicode:
        urdu=0
        punjabi=0

class urdu_punjabi:
            urdu_start=[]
            urdu_end=[]
            punjabi_start=[]
            punjabi_end=[]
            urdu_word_count=0

class biclass:
            urdu=[]
            punjabi1=[]
            punjabi2=[]
            freq=0
class normalised_corpus:
            original_word=[]
            normalised_word=[]
            freq=0

class urdu_corpus:   
            original_word=[]
            freq=0

class bigram_index:
            normalised_word=[]
            index=0

class trigram_index:
            normalised_word=[]
            index=0

class bigram_corpus:
            first_word=[]
            second_word=[]
            freq=0
            unigram_freq=0

class bigram_corpus1:
            first_word=[]
            second_word=[]
            freq=0


class wlist:
            word=[]
            count=0



class urdu_bigram_str:
            urdu1=[]
            urdu2=[]
            punjabi=[]

class trigram_corpus:
    first_word=[]
    second_word=[]
    third_word=[]
    freq=0



class trigram:
            first_word=[]
            second_word=[]
            third_word=[]

class bigram_index1_str:
            normalised_word=[]
            index=0
class tunion:
    uc=[0]*2
    ui = 0

class S2G:
    counting=0
    separator='\n'
    FILESIZE = 250000
    CORPUS = 270000
    CORPUS_FILESIZE = 6400
    DICSIZE = 50000
    BISIZE = 4000
    TRISIZE_PRE = 165000
    TRISIZE_MID = 161400
    TRISIZE_POST = 23600
    BIGRAM_SIZE = 220000
    INDEX_SIZE = 8000
    URDU_BIGRAM_SIZE = 3000
    IGNORE = 1000
    URDUCORPUS = 140000
    BISIZE1 = 750000
    INDEX_SIZE1 = 60000
    OUTDEV = False
    word_total = 0
    word_found = 0
    bi_word_found = 0
    word_not_found = 0
    punjabi_trigram_found = 0
    PROTECTOLDA = 0
    olda = 0
    urdu=[]
    roman=[]
    bigram_index1=[]
    bigrams=[]
    pre_bigram=[]
    post_bigram=[]
    pre_bigram_index=[]
    post_bigram_index=[]
    pre_trigram_index=[]
    post_trigram_index=[]
    mid_trigram_index=[]
    corpus_words=[]


    corpus_word_count = 0
    corpus_found = 0
    multi_count = 0

    dict_word_count = 0
    pre_bigram_total=0
    post_bigram_total=0
    pre_bigram_index_count=0
    post_bigram_index_count=0
    urdu_bigram_total=0
    pre_trigram_index_count=0
    mid_trigram_index_count=0
    post_trigram_index_count=0
    pre_trigram_total=0
    mid_trigram_total=0
    post_trigram_total=0
    ignore_word_count=0
    prefix_word_count=0
    suffix_word_count=0
    bigram_index_count=0
    bigram_total=0

    corpus_flag = 0
    conversion_level = 3
    max_joint = 0
    total_joint = 0
    merged_word_count = 0
    average_joint_count = 0.0

    urdu_corpus_total = 0
    urdu_corpus_word_count=0
    tej_urdu=''
    tej_punjabi=''
    appPath=''
    QTS=[]
    MSG = "Started:"
    isActive =  False
    isDic =  False
    isBinCorpus =  False
    isPreBinCorpus =  False
    isPostBinCorpus =  False
    isUrduBigram = True

    offTriGram =  False

    def __init__(self):
                i = 0
                if  not self.isActive:
                    QTS=[0]*1
                    QTS[0] = 0

                    self.pre_bigram=np.empty((self.BIGRAM_SIZE), dtype="object")
                    self.post_bigram = np.empty((self.BIGRAM_SIZE), dtype="object")
                    for  i in range(self.BIGRAM_SIZE):
                        self.pre_bigram[i]=bigram_corpus()
                        self.post_bigram[i]=bigram_corpus()
                        self.pre_bigram[i].first_word=np.zeros((16),dtype='i')
                        self.pre_bigram[i].second_word=np.zeros((16),dtype='i')
                        self.post_bigram[i].first_word=np.zeros((16),dtype='i')
                        self.post_bigram[i].second_word=np.zeros((16),dtype='i')
                    self.bigrams = np.empty((self.BISIZE1), dtype="object")
                    for  i in range(self.BISIZE1):
                        self.bigrams[i]=bigram_corpus1()
                        self.bigrams[i].first_word=np.zeros((10),dtype='i')
                        self.bigrams[i].second_word=np.zeros((10),dtype='i')
                    self.bigram_index1 =np.empty((self.INDEX_SIZE1), dtype="object")
                    for  i in range(self.INDEX_SIZE1):
                        self.bigram_index1[i]=bigram_index1_str()
                        self.bigram_index1[i].normalised_word=np.zeros((10),dtype='i')
                        self.bigram_index1[i].index = 0
                    
                    self.pre_bigram_index = np.empty((self.INDEX_SIZE), dtype="object")
                    self.post_bigram_index = np.empty((self.INDEX_SIZE), dtype="object")
                    self.pre_trigram_index = np.empty((self.INDEX_SIZE), dtype="object")
                    self.post_trigram_index = np.empty((self.INDEX_SIZE), dtype="object")
                    self.mid_trigram_index = np.empty((self.INDEX_SIZE), dtype="object")
                    for  i in range(self.INDEX_SIZE):
                        self.pre_bigram_index[i]=bigram_index()
                        self.post_bigram_index[i]=bigram_index()
                        self.pre_trigram_index[i]=trigram_index()
                        self.post_trigram_index[i]=trigram_index()
                        self.mid_trigram_index[i]=trigram_index()
                        self.pre_bigram_index[i].normalised_word=np.zeros((16),dtype='i')
                        self.post_bigram_index[i].normalised_word=np.zeros((16),dtype='i')
                        self.pre_trigram_index[i].normalised_word=np.zeros((16),dtype='i')
                        self.post_trigram_index[i].normalised_word=np.zeros((16),dtype='i')
                        self.mid_trigram_index[i].normalised_word=np.zeros((16),dtype='i')
                    self.urdu_bigram = np.empty((self.URDU_BIGRAM_SIZE), dtype="object")
                    for  i in range(self.URDU_BIGRAM_SIZE):
                        self.urdu_bigram[i]=urdu_bigram_str()
                        self.urdu_bigram[i].urdu1=np.zeros((16),dtype='i')
                        self.urdu_bigram[i].urdu2=np.zeros((16),dtype='i')
                        self.urdu_bigram[i].punjabi=np.zeros((30),dtype='i')
                    self.corpus_words = np.empty((self.CORPUS), dtype="object")
                    for  i in range(self.CORPUS):
                        self.corpus_words[i]=normalised_corpus()
                        self.corpus_words[i].original_word=np.zeros((16),dtype='i')
                        self.corpus_words[i].normalised_word=np.zeros((16),dtype='i')
                        self.corpus_words[i].freq = 0
                    self.roman_dict=np.zeros((self.DICSIZE,20), dtype="i")
                    self.urdu_dict=np.zeros((self.DICSIZE,20), dtype="i")

                    self.wordlist = np.empty((20000), dtype="object")
                    for i in range(20000):
                        self.wordlist[i]=wlist()
                        self.wordlist[i].word=np.zeros((60),dtype='i')
                        self.wordlist[i].count = 0
                    if  not self.offTriGram:
                        self.pre_trigram = np.empty((self.TRISIZE_PRE),dtype='object')
                        self.mid_trigram = np.empty((self.TRISIZE_MID),dtype='object')
                        self.post_trigram = np.empty((self.TRISIZE_POST),dtype='object')
                        for  i in range(self.TRISIZE_PRE):
                            self.pre_trigram[i]=trigram_corpus()
                            self.pre_trigram[i].first_word=np.zeros((16),dtype='i')
                            self.pre_trigram[i].second_word=np.zeros((16),dtype='i')
                            self.pre_trigram[i].third_word=np.zeros((16),dtype='i')
                            self.pre_trigram[i].freq = 0
                        for  i in range(self.TRISIZE_MID):
                            self.mid_trigram[i]=trigram_corpus()
                            self.mid_trigram[i].first_word=np.zeros((16),dtype='i')
                            self.mid_trigram[i].second_word=np.zeros((16),dtype='i')
                            self.mid_trigram[i].third_word=np.zeros((16),dtype='i')
                            self.mid_trigram[i].freq = 0
                        for  i in range(self.TRISIZE_POST):
                            self.post_trigram[i]=trigram_corpus()
                            self.post_trigram[i].first_word=np.zeros((16),dtype='i')
                            self.post_trigram[i].second_word=np.zeros((16),dtype='i')
                            self.post_trigram[i].third_word=np.zeros((16),dtype='i')
                            self.post_trigram[i].freq = 0
                    
                    
                    self.appPath = pathname = os.getcwd()#os.path.dirname(sys.argv[0])                    
                    self.appPath = os.path.join(self.appPath,'s2g')
                    
                    self.urdu_corpus_words = np.empty((self.URDUCORPUS),dtype='object')
                    for  i in range(self.URDUCORPUS):
                        self.urdu_corpus_words[i]=urdu_corpus()
                        self.urdu_corpus_words[i].original_word=np.zeros((25),dtype='i')
                        self.urdu_corpus_words[i].freq = 0
                    self.ignore=np.zeros((self.IGNORE,10),dtype='i')
                    self.prefix=np.zeros((20,10),dtype='i')
                    self.suffix=np.zeros((20,10),dtype='i')
                    self.noon_freq=np.zeros((120,120),dtype='i')


                    self.read_urdu_punjabi_dict()
                    self.corpus_word_count=self.read_binary_corpus(self.corpus_words)
                    self.read_ignore_words()
                    self.pre_bigram_total,self.pre_bigram_index_count=self.read_pre_bigram_corpus(self.pre_bigram, self.pre_bigram_index)
                    self.post_bigram_total,self.post_bigram_index_count=self.read_post_bigram_corpus(self.post_bigram, self.post_bigram_index)
                    if  not self.offTriGram:
                        self.pre_trigram_total,self.pre_trigram_index_count=self.read_pre_trigram_corpus(self.pre_trigram, self.pre_trigram_index)
                        self.post_trigram_total,self.post_trigram_index_count=self.read_post_trigram_corpus(self.post_trigram, self.post_trigram_index)
                        self.mid_trigram_total,self.mid_trigram_index_count=self.read_mid_trigram_corpus(self.mid_trigram , self.mid_trigram_index)
                    else:
                        self.pre_trigram_index_count = 0
                        self.post_trigram_index_count = 0
                        self.mid_trigram_index_count = 0
                    self.read_urdu_bigram()
                    self.bigram_total,self.bigram_index_count=self.read_bigram_corpus(self.bigrams, self.bigram_index1)
                    self.read_noon_freq()
                    self.isActive = True

    def startReg(self,input):
        try:
            generatedWord=''
            patt=r'([’]*\s*[؀-ۿ]\s*['+ re.escape(string.punctuation)+']*[‘]*)+'
            generatedWord = re.sub(patt, self.func, input)
            return generatedWord
        except TypeError:
            return ""

    def func(self,matchobj):
        m = matchobj.group(0)
        # print(m)
        return self.start(m)

    def start(self,input):
                # print('in S2G file inside start function\n')
                out_file_len = 0
                file_length_in = 0
                file_length_out = 0
                itotalLength = len(input)* 3
                
                if len(input)< 20:
                    itotalLength = 140
                urdu=np.zeros((itotalLength),dtype='i')
                roman=np.zeros((itotalLength),dtype='i')
                input = input.replace('�', ' ')
                if len(input)== 0:
                    return "Empty String...."
                inputbytes = self.str2Byte(input)
                
                if len(inputbytes)+ 1 > len(urdu):
                    return "TOO MUCH DATA"
                for i in range(len(inputbytes)):
                    urdu[i]=np.array(inputbytes[i])
                    # print(f'{inputbytes[i]}----->{urdu[i]}')
                
                # print(f'string to byte array of shahmukhi character(urdu before):\n{urdu}')
                
                file_length_in = len(inputbytes)

                out_file_len=self.normalise_text(urdu, file_length_in, roman)
                # print(out_file_len)
                
                for  i in range(0,out_file_len):
                    urdu[i] = roman[i]
                # print(f'\nurdu array updated:\n {urdu}')
                # print(f'\nroman: {roman}') urdu = roman

                file_length_in = out_file_len
                file_length_out=self.convert_urdu_to_punjabi(urdu, file_length_in, roman)
                # print(f'\nroman after conversion from urdu to punjabi:\n {roman}') #urdu = roman
                # print(f'\nfile_length_out: {file_length_out}')
                self.write_frequency()
                self.word_found += (self.corpus_found + self.multi_count + self.bi_word_found)
                # print(f'\nword_found: {self.word_found}')
                self.total_words = self.word_found + self.word_not_found
                try:
                    self.printMSG("<hr>Status Check: Dic=" + str(self.isDic) + "|BinCorpus=" + str(self.isBinCorpus) + "|PreBC=" + str(self.isPreBinCorpus) + "|PostBC=" + str(self.isPostBinCorpus) + "|UrduBi=" + str(self.isUrduBigram))
                    self.printMSG2("Total Words in File=", str(self.total_words))
                    self.printMSG2("Words found", str(self.word_found))
                    self.printMSG2("%age=", str((self.word_found * 100.0) / self.total_words))
                    self.printMSG2("Words in Dictionary", str(self.word_found - self.corpus_found - self.multi_count))
                    self.printMSG2("%age=", str(((self.word_found - self.corpus_found - self.multi_count) * 100.0) / self.total_words))
                    self.printMSG2("Words in Bigram table", str(self.bi_word_found))
                    self.printMSG2("%age=", str((self.bi_word_found * 100.0) / self.total_words))
                    self.printMSG2("Words in Corpus =", str(self.corpus_found))
                    self.printMSG2("%age=", str((self.corpus_found * 100.0) / self.total_words))
                    self.printMSG2("Multi words are:", str(self.multi_count))
                    self.printMSG2("%age=", str((self.multi_count * 100.0) / self.total_words))
                    if self.OUTDEV:
                        # print('i am inside if.self.OUTDEV')
                        roman=self.convertGurmukhiToDevanagariText(roman)
                    # print(f'before byte to str: {roman}')
                    self.tej_punjabi = self.byte2Str(roman, file_length_out, True)
                    return self.tej_punjabi
                except ZeroDivisionError:
                    return ('','')

    def convert_unicodefile_to_UTF8(self, urdu, size, roman, roman_size):
        urdu_word = [0] * 50
        roman_word = [0] * 16
        UTF8_string = [0] * 60
        urdu_word_size = 0
        roman_word_size = 0
        urdu_ptr = 2
        roman_ptr = 0
        while urdu_ptr < size:
            ch = urdu[urdu_ptr]
            ch1 = urdu[urdu_ptr + 1]
            if self.check_punctuation(ch, ch1) > 0:
                for i in range(0, self.strlen(UTF8_string)):
                    roman[roman_ptr] = UTF8_string[i]
                    roman_ptr += 1
                roman_word_size = self.convert_urdu_punctuation_to_roman(ch, ch1, roman_word)  
                for i in range(0, roman_word_size):
                    roman[roman_ptr] = roman_word[i]
                    roman_ptr += 1
                for i in range(0, urdu_word_size):
                    urdu_word[i] = 0
                urdu_word_size = 0
                urdu_ptr += 2
            else:
                urdu_word[urdu_word_size] = ch
                urdu_word_size += 1
                urdu_word[urdu_word_size] = ch1
                urdu_word_size += 1
                urdu_ptr += 2
        if urdu_word_size > 0:
            for i in range(0, self.strlen(UTF8_string)):
                roman[roman_ptr] = UTF8_string[i]
                roman_ptr += 1
        roman_size = roman_ptr
        return 0

    def check_for_vao_in_line(self, punjabi, line_size):
        punjabi_ptr = 0
        temp_size = 0
        if line_size == 0: return line_size
        while punjabi_ptr < line_size:
            if (punjabi_ptr < line_size - 6) and (punjabi[punjabi_ptr] == 32) and (punjabi[punjabi_ptr + 1] == 0) and (
                    punjabi[punjabi_ptr + 2] == 19) and (punjabi[punjabi_ptr + 3] == 10) and (
                    punjabi[punjabi_ptr + 4] == ord('-')) and (punjabi[punjabi_ptr + 5] == 0):
                punjabi[temp_size] = ord('-')
                temp_size += 1
                punjabi[temp_size] = 0
                temp_size += 1
                punjabi[temp_size] = 19
                temp_size += 1
                punjabi[temp_size] = 10
                temp_size += 1
                punjabi[temp_size] = ord('-')
                temp_size += 1
                punjabi[temp_size] = 0
                temp_size += 1
                punjabi_ptr += 8
            elif (punjabi_ptr < line_size - 8) and (punjabi[punjabi_ptr] == ord('-')) and (
                    punjabi[punjabi_ptr + 1] == 0) and (punjabi[punjabi_ptr + 2] == 15) and (
                    punjabi[punjabi_ptr + 3] == 10) and (punjabi[punjabi_ptr + 4] == ord('-')) and (
                    punjabi[punjabi_ptr + 5] == 0) and (punjabi[punjabi_ptr + 6] == ord(' ')) and (
                    punjabi[punjabi_ptr + 7] == 0):
                punjabi[temp_size] = ord('-')
                temp_size += 1
                punjabi[temp_size] = 0
                temp_size += 1
                punjabi[temp_size] = 15
                temp_size += 1
                punjabi[temp_size] = 10
                temp_size += 1
                punjabi[temp_size] = ord('-')
                temp_size += 1
                punjabi[temp_size] = 0
                temp_size += 1
                punjabi_ptr += 8
            else:
                if temp_size != punjabi_ptr:
                    punjabi[temp_size] = punjabi[punjabi_ptr]
                    temp_size += 1
                    punjabi_ptr += 1
                    punjabi[temp_size] = punjabi[punjabi_ptr]
                    temp_size += 1
                    punjabi_ptr += 1
                else:
                    punjabi_ptr += 2
                    temp_size = punjabi_ptr
            
        line_size = temp_size
        return line_size

    def check_for_broken_words(self,punjabi, line_size):
        return line_size

    def get_line_word_count(self, punjabi, line_size):

        len = 0
        i = 0
        punjabi_ptr = 0
        wc = 0
        while  punjabi_ptr < line_size:
            ch = punjabi[punjabi_ptr]
            ch1 = punjabi[punjabi_ptr + 1]
            if  (ch == 255) and (ch1 == 254):
                punjabi_ptr += 2
                continue
            while  self.check_punjabi_punctuation(ch, ch1) > 0:
                if  punjabi_ptr >= line_size:
                    return wc
                ch = punjabi[punjabi_ptr]
                punjabi_ptr+=1
                ch1 = punjabi[punjabi_ptr]
                punjabi_ptr+=1
            len = 0
            while  not(self.check_punjabi_punctuation(ch, ch1) != 0):
                if  punjabi_ptr >= line_size:
                    return wc
                ch = punjabi[punjabi_ptr]
                punjabi_ptr+=1
                ch1 = punjabi[punjabi_ptr]
                punjabi_ptr+=1
                len+=1
                if  len == 2: wc+=1
        return wc

    def post_process(self, punjabi, line_size):
        # print('inside post_process() function\n')
        i = 0
        punjabi_ptr = 0
        punjabi_word_size = 0
        word_size1 = 0
        word_size2 = 0
        word_size3 = 0
        temp_size = 0
        word_size4 = 0
        word_size5 = 0
        start1 = 0
        end1 = 0
        start2 = 0
        end2 = -1
        start3 = 0
        end3 = -1
        end4 = -1
        end5 = -1
        start4 = 0
        start5 = 0
        flag = 0
        punjabi_word=[0]*20
        punc1=[0]*5000
        punc2=[0]*5000
        word1=[0]*20
        word2=[0]*20
        word3=[0]*20
        word4=[0]*20
        word5=[0]*20
        temp=[0]*20000
        if  line_size == 0: return line_size
        if  self.get_line_word_count(punjabi, line_size) < 5:
            return line_size
        self.strcpy(word1, self.QTS)
        self.strcpy(word2, self.QTS)
        self.strcpy(word3, self.QTS)
        self.strcpy(word4, self.QTS)
        self.strcpy(word5, self.QTS)
        while  punjabi_ptr < line_size:
            ch = punjabi[punjabi_ptr]
            ch1 = punjabi[punjabi_ptr + 1]
            if  (ch == 255) and (ch1 == 254):
                punjabi_ptr += 2
                continue
            if  flag > 0 or self.check_punjabi_punctuation(ch, ch1) > 0:
                if  punjabi_word_size > 0:
                    start1 = start2
                    end1 = end2
                    start2 = start3
                    end2 = end3
                    start3 = start4
                    end3 = end4
                    start4 = start5
                    end4 = end5
                    start5 = punjabi_ptr
                    for  i in range(0,word_size2):
                        word1[i] = word2[i]
                    word_size1 = word_size2
                    for  i in range(0,word_size3):
                        word2[i] = word3[i]
                    word_size2 = word_size3
                    for  i in range(0,word_size4):
                        word3[i] = word4[i]
                    word_size3 = word_size4
                    for  i in range(0,word_size5):
                        word4[i] = word5[i]
                    word_size4 = word_size5
                    for  i in range(0,punjabi_word_size):
                        word5[i] = punjabi_word[i]
                    word_size5 = punjabi_word_size
                    while  self.check_punjabi_punctuation(ch, ch1) > 0:
                        punjabi_ptr += 2
                        ch = punjabi[punjabi_ptr]
                        ch1 = punjabi[punjabi_ptr + 1]
                        if  punjabi_ptr >= line_size:
                            break
                    end5 = punjabi_ptr - 1
                    if  not(flag != 0):
                        punjabi_ptr -= 2
                    word1[word_size1] = 0
                    word2[word_size2] = 0
                    word3[word_size3] = 0
                    word4[word_size4] = 0
                    word5[word_size5] = 0
                    if  punjabi_ptr == 624:
                        i = 0
                    if temp_size >= 84:
                        temp_size = temp_size
                    if  self.check_punjabi_trigram(word1, word2, word3, word4, word5) > 0:
                        for  i in range(0,self.strlen(word3)):
                            temp[temp_size] = word3[i]
                            temp_size+=1
                            temp[temp_size] = 10
                            temp_size+=1
                        for  i in range(start3,end3+1):
                            temp[temp_size] = punjabi[i]
                            temp_size+=1
                        self.punjabi_trigram_found+=1
                    else:
                        if  self.check_punjabi_bigram(word2, word3, word4) > 0:
                            for  i in range(0,self.strlen(word3)):
                                temp[temp_size] = word3[i]
                                temp_size+=1
                                temp[temp_size] = 10
                                temp_size+=1
                            for  i in range(start3,end3+1):
                                temp[temp_size] = punjabi[i]
                                temp_size+=1
                    flag = 0
                    punjabi_word_size = 0
            else:
                punjabi_word[punjabi_word_size] = ch
                punjabi_word_size+=1
                if  punjabi_word_size > 18: flag = 1
            punjabi_ptr += 2
        if  punjabi_word_size > 0:
            start1 = start2
            end1 = end2
            start2 = start3
            end2 = end3
            start3 = start4
            end3 = end4
            start4 = start5
            end4 = end5
            start5 = punjabi_ptr
            for  i in range(0,word_size2):
                word1[i] = word2[i]
            word_size1 = word_size2
            for  i in range(0,word_size3):
                word2[i] = word3[i]
            word_size2 = word_size3
            for  i in range(0,word_size4):
                word3[i] = word4[i]
            word_size3 = word_size4
            for  i in range(0,word_size5):
                word4[i] = word5[i]
            word_size4 = word_size5
            for  i in range(0,punjabi_word_size):
                word5[i] = punjabi_word[i]
            word_size5 = punjabi_word_size
            word4[word_size4] = 0
            word5[word_size5] = 0
        word2[word_size2] = 0
        word3[word_size3] = 0
        if  self.check_punjabi_trigram(word2, word3, word4, word5, self.QTS) > 0:
            for  i in range(0,self.strlen(word4)):
                temp[temp_size] = word4[i]
                temp_size+=1
                temp[temp_size] = 10
                temp_size+=1
            for  i in range(start4,end4+1):
                temp[temp_size] = punjabi[i]
                temp_size+=1
            self.punjabi_trigram_found+=1
        else:
            self.check_punjabi_bigram(word3, word4, word5)
            for  i in range(0,self.strlen(word4)):
                temp[temp_size] = word4[i]
                temp_size+=1
                temp[temp_size] = 10
                temp_size+=1
            for  i in range(start4,end4+1):
                temp[temp_size] = punjabi[i]
                temp_size+=1
        if  self.check_punjabi_trigram(word3, word4, word5, self.QTS, self.QTS) > 0:
            for  i in range(0,self.strlen(word5)):
                temp[temp_size] = word5[i]
                temp_size+=1
                temp[temp_size] = 10
                temp_size+=1
            for  i in range(start5,end5+1):
                temp[temp_size] = punjabi[i]
                temp_size+=1
        else:
            self.check_punjabi_bigram(word4, word5, self.QTS)
            for  i in range(0,self.strlen(word5)):
                temp[temp_size] = word5[i]
                temp_size+=1
                temp[temp_size] = 10
                temp_size+=1
            for  i in range(start5,end5+1):
                temp[temp_size] = punjabi[i]
                temp_size+=1
        for  i in range(0,temp_size):
            punjabi[i] = temp[i]
        line_size = temp_size
        line_size=self.check_for_vao_in_line(punjabi,line_size)
        line_size=self.check_for_broken_words(punjabi, line_size)
        return line_size

    def check_punjabi_bigram(self, word1, word2, word3):
        normalise=[0]*20
        temp_word=[0]*20
        temp_word1=[0]*20
        norm1=[0]*20
        norm2=[0]*20
        punjabi_int = np.zeros((20),dtype='i')
        start = 0
        end = 0
        pre_freq = -0.1
        post_freq = -0.1
        if  self.strlen(word2) == 0: return 0
        if  (self.strlen(word1) > 14) or (self.strlen(word2) > 14) or (self.strlen(word3) > 14):
            return 0
        for  k in range(0,self.strlen(word2)):
            punjabi_int[k] = word2[k]
        self.normalise_punjabi_word(punjabi_int, self.strlen(word2), normalise)
        temp_word[0] = temp_word1[0] = 0
        for  k in range(0,self.strlen(word1)):
            punjabi_int[k] = word1[k]
        self.normalise_punjabi_word(punjabi_int, self.strlen(word1), norm1)
        for  k in range(0,self.strlen(word3)):
            punjabi_int[k] = word3[k]
        self.normalise_punjabi_word(punjabi_int, self.strlen(word3), norm2)
        start, end,flag = self.search_word_pre_bigram_index(normalise,start,end)
        if  flag > 0:
            pre_freq = self.search_word_pre_bigram(norm2, start, end, temp_word)
        start, end, flag = self.search_word_post_bigram_index(normalise, start, end)
        if  flag > 0:
            post_freq = self.search_word_post_bigram(norm1, start, end, temp_word1)
        if  pre_freq + post_freq <= 0.0: return 3
        if  pre_freq > post_freq:
            self.strcpy(word2, temp_word)
            return 1
        if  post_freq >= pre_freq:
            self.strcpy(word2, temp_word1)
            return 2
        return 3

    def check_punjabi_trigram(self, word1, word2, word3, word4, word5):
        normalise=[0]*20
        norm1=[0]*20
        norm2=[0]*20
        temp_word=[0]*20
        temp_word1=[0]*20
        temp_word2=[0]*20
        punjabi_int = np.zeros((20),dtype='i')
        start = 0
        end = 0
        pre_freq = 0
        mid_freq = 0
        post_freq = 0
        if  self.strlen(word2) == 0: return 0
        if  self.strlen(word3) == 0: return 0
        if  (self.strlen(word1) > 14) or (self.strlen(word2) > 14) or (self.strlen(word3) > 14) or (self.strlen(word4) > 14) or (self.strlen(word5) > 14):
            return 0
        for  k in range(0,self.strlen(word3)):
            punjabi_int[k] = word3[k]
        self.normalise_punjabi_word(punjabi_int, self.strlen(word3), normalise)
        temp_word[0] = temp_word1[0] = 0
        pre_freq = mid_freq = post_freq = 0
        start,end,flag=self.search_word_pre_trigram_index(normalise,start, end) 
        if  flag > 0:
            for  k in range(0,self.strlen(word4)):
                punjabi_int[k] = word4[k]
            self.normalise_punjabi_word(punjabi_int, self.strlen(word4), norm1)
            for  k in range(0,self.strlen(word5)):
                punjabi_int[k] = word5[k]
            self.normalise_punjabi_word(punjabi_int, self.strlen(word5), norm2)
            pre_freq = self.search_word_pre_trigram(norm1, norm2, start, end, temp_word)
        start,end,flag=self.search_word_mid_trigram_index(normalise, start,end)

        if  flag > 0:
            for  k in range(0,self.strlen(word2)):
                punjabi_int[k] = word2[k]
            self.normalise_punjabi_word(punjabi_int, self.strlen(word2), norm1)
            for  k in range(0,self.strlen(word4)):
                punjabi_int[k] = word4[k]
            self.normalise_punjabi_word(punjabi_int, self.strlen(word4), norm2)
            mid_freq = self.search_word_mid_trigram(norm1, norm2, start, end, temp_word1)
        start,end,flag=self.search_word_post_trigram_index(normalise,start,end)
        if  flag > 0:
            for  k in range(0,self.strlen(word1)):
                punjabi_int[k] = word1[k]
            self.normalise_punjabi_word(punjabi_int, self.strlen(word1), norm1)
            for  k in range(0,self.strlen(word2)):
                punjabi_int[k] = word2[k]
            self.normalise_punjabi_word(punjabi_int, self.strlen(word2), norm2)
            post_freq = self.search_word_post_trigram(norm1, norm2, start, end, temp_word2)
        if  mid_freq + pre_freq + post_freq == 0: return 0
        if  mid_freq > pre_freq:
            self.strcpy(word3, temp_word1)
            if  mid_freq < post_freq:
                self.strcpy(word3, temp_word2)
            else:
                pass
        else:
            self.strcpy(word3, temp_word)
            if  pre_freq < post_freq:
                self.strcpy(word3, temp_word2)
            else:
                pass
        return 1

    def check_broken_punc(self, roman_word, roman_word_size):
        if  roman_word_size > 2: return 0
        if  roman_word[0] != 32: return 0
        if  roman_word[1] != 0: return 0
        return 1

    def shah_tokens_b2s(one_word_array):
        print('inside shah token')
        s = ''
        for i in range(0,len(one_word_array),2):
            b=one_word_array[i]
            b1=one_word_array[i+1]
            if b==0 and b1==0:
                print(s)
                with open ("tokens.txt","a") as f:
                    f.write(s)
                    f.write('\n')
                return s
            c = (b1 * 256)+b
            # print(c)
            s = s+ chr(c)
            

    def convert_urdu_to_punjabi(self, urdu, size, roman):
        # print('inside convert_urdu_to_punjabi() function\n')
        count = 1
        shah_tokens = []
        urdu_word=[0]*100
        p_urdu_word=[0]*100
        pp_urdu_word=[0]*100
        roman_word=[0]*10000
        punjabi_word=[0]*100
        p_roman_word=[0]*10000
        pp_roman_word=[0]*10000
        temp_roman_word=[0]*5000
        punjabi_line=[0]*10000
        urdu_word_size = 0
        p_urdu_word_size = 0
        pp_urdu_word_size = 0
        roman_word_size = 0
        p_roman_word_size = 0
        pp_roman_word_size = 0
        urdu_ptr = 0
        roman_ptr = 0
        temp_roman_word_size = 0
        line_ptr = 0
        first_word = 1
        last_word = 0
        end_of_line = 0
        first_punc = 1
        cword = 0
        punjabi_line[line_ptr] = roman[roman_ptr] = urdu[urdu_ptr]
        urdu_ptr+=1
        roman_ptr+=1
        line_ptr+=1
        punjabi_line[line_ptr] = roman[roman_ptr] = urdu[urdu_ptr]
        urdu_ptr+=1
        roman_ptr+=1
        line_ptr+=1
        while  urdu_ptr <= size:
            if urdu_ptr>=88:
                pass
            #extract the first byte in ch and second byte(language code) in ch1
            ch = urdu[urdu_ptr]
            ch1 = urdu[urdu_ptr + 1]
            # print(f'ch: {ch}        ch1: {ch1}')
            if  not(ch != 0) and not(ch1 != 0) and not(urdu_word_size != 0):  
                urdu_ptr += 2
                continue
            #will enter this part if punctuation
            if  self.check_punctuation(ch, ch1) > 0:
                
                if  (first_punc > 0) and not(urdu_word_size != 0):
                    # print('ignoring first punctuation')   
                    roman_ptr += 2
                    urdu_ptr += 2
                    continue
                
                count += 1
                # print(f"\t\t\t\t\t\t\t\tThis is {count} token\n\t\t\t\t\t\t\t\t{S2G.shah_tokens_b2s(urdu_word)}")
                first_punc = 0
                roman_word_size = 0
                self.olda = -1
                if  last_word > 0:
                    first_word = 1
                    last_word = 0
                if  ch1 == 6:
                    # print("last word")
                    last_word = 1
                    first_word = 0
                cword+=1
                if  cword == 2508:
                    i = 2373
                if  self.post_trigram_index[2].normalised_word[1] == 0: 
                    end_of_line = cword
                # print(f'end_of_line: {end_of_line}\n')

                # print(f'pp_urdu_word status:\n{pp_urdu_word}\n\np_urdu_word status:\n{p_urdu_word}')
                # print(f'roman_word status:\n{roman_word[:50]}\n\npp_roman_word status:\n{pp_roman_word[:50]}\n\np_roman_word:\n{p_roman_word[:50]}\n\n\n')

                urdu_word_size=self.normalise_urdu_word(urdu_word,urdu_word_size)
                post_found = 0

                #if reached this line it means word before one space is extracted
                #checking if the word contains multiple word
                roman_word_size, found = self.urdu_word_to_punjabi(urdu_word, p_urdu_word, pp_urdu_word, urdu_word_size, p_urdu_word_size, pp_urdu_word_size, punjabi_word,roman_word_size, self.check_broken_punc(pp_roman_word, pp_roman_word_size))
                # print(f'\nroman_word_size: {roman_word_size}')

                for  i in range(0,roman_word_size):
                    punjabi_line[line_ptr] = punjabi_word[i]
                    line_ptr+=1
                # print(f'urdu word = {urdu_word[:200]}\n')
                # shah_tokens.append(S2G.shah_tokens_b2s(urdu_word))
                # print(f'punjabi_word = {punjabi_word[:200]}')
                roman_word_size = 0
                if  first_word > 0: first_word = 0
                end_of_line = 0
                
                #to check if we have reached end of the line or not
                while  self.check_punctuation(ch, ch1) > 0:
                    temp_roman_word_size=self.convert_urdu_punctuation_to_roman(ch, ch1, temp_roman_word)
                    # print(f'temp_roman_word:\n{temp_roman_word[:100]}\n\n')
                    if  roman_word_size < 9900:
                        for  i in range(0,temp_roman_word_size):
                            roman_word[roman_word_size] = temp_roman_word[i]
                            roman_word_size+=1
                    urdu_ptr += 2
                    if  urdu_ptr >= size: break
                    ch = urdu[urdu_ptr]
                    ch1 = urdu[urdu_ptr + 1]
                    if  (ch == 13) and (ch1 == 0):
                        end_of_line = 0
                if  post_found > 0:
                    urdu_word_size = 0
                    roman_word_size = 0
                if  found == 2:
                    p_urdu_word_size = 0
                    pp_roman_word_size = p_roman_word_size
                    for  i in range(0,pp_roman_word_size):
                        pp_roman_word[i] = p_roman_word[i]
                    p_roman_word_size = 0
                if  found == 3:
                    pp_urdu_word_size = p_urdu_word_size = urdu_word_size = 0
                    pp_roman_word_size = p_roman_word_size = roman_word_size = 0
                if  pp_roman_word_size - 2 >= 0 and self.check_urdu_line_end(pp_roman_word[pp_roman_word_size - 2], pp_roman_word[pp_roman_word_size - 1]) > 0: 
                    end_of_line = 1
                if  self.check_urdu_line_end(pp_roman_word[0], pp_roman_word[1]) > 0:
                    end_of_line = 1
                for  i in range(0,pp_roman_word_size):
                    punjabi_line[line_ptr] = pp_roman_word[i]
                    line_ptr+=1
                pp_roman_word_size = p_roman_word_size
                for  i in range(0,pp_roman_word_size):
                    pp_roman_word[i] = p_roman_word[i]
                p_roman_word_size = roman_word_size
                for  i in range(0,p_roman_word_size):
                    p_roman_word[i] = roman_word[i]
                for  i in range(0,roman_word_size):
                    roman_word[i] = 0
                pp_urdu_word_size = p_urdu_word_size
                for  i in range(0,pp_urdu_word_size):
                    pp_urdu_word[i] = p_urdu_word[i]
                p_urdu_word_size = urdu_word_size
                for  i in range(0,p_urdu_word_size):
                    p_urdu_word[i] = urdu_word[i]
                for  i in range(0,urdu_word_size):
                    urdu_word[i] = 0
                urdu_word_size = 0
                if  end_of_line > 0 or (line_ptr >= 9000):
                    line_ptr=self.post_process(punjabi_line,line_ptr)
                    for  i in range(0,line_ptr):
                        roman[roman_ptr] = punjabi_line[i]
                        roman_ptr+=1
                    line_ptr = 0
               
            else:
                urdu_word[urdu_word_size] = ch
                urdu_word_size+=1
                urdu_word[urdu_word_size] = ch1
                urdu_word_size+=1
                if  urdu_word_size > 80: urdu_word_size = 80
                urdu_ptr += 2
                # print(urdu_word)
        # print('before')
        # print(f'urdu_word:\n{roman[:50]}\n\npp_urdu_word:\n{pp_urdu_word[:50]}\n\np_urdu_word:\n{p_urdu_word[:50]}')
        # print(f'roman_word:\n{roman_word[:50]}\n\npp_roman_word:\n{pp_roman_word[:50]}\n\np_roman_word:\n{p_roman_word[:50]}')
        if  pp_urdu_word_size == 0 and p_urdu_word_size > 0:
            roman_word_size = urdu_word_size = 0
            pp_roman_word_size = p_roman_word_size
            for  i in range(0,pp_roman_word_size):
                pp_roman_word[i] = p_roman_word[i]
            p_roman_word_size = roman_word_size
            for  i in range(0,p_roman_word_size):
                p_roman_word[i] = roman_word[i]
            for  i in range(0,roman_word_size):
                roman_word[i] = 0
            pp_urdu_word_size = p_urdu_word_size
            for  i in range(0,pp_urdu_word_size):
                pp_urdu_word[i] = p_urdu_word[i]
            p_urdu_word_size = urdu_word_size
        while  pp_urdu_word_size > 0:

            roman_word_size = 0
            punjabi_word_size = 0
            p_urdu_word_size, post_found = self.check_post_word(urdu_word, p_urdu_word, urdu_word_size, p_urdu_word_size)
            punjabi_word_size, found = self.urdu_word_to_punjabi(urdu_word, p_urdu_word, pp_urdu_word, urdu_word_size, p_urdu_word_size, pp_urdu_word_size, punjabi_word, punjabi_word_size,self.check_broken_punc(pp_roman_word, pp_roman_word_size)) 
            for  i in range(0,punjabi_word_size):
                punjabi_line[line_ptr] = punjabi_word[i]
                line_ptr+=1

            if  post_found > 0:
                urdu_word_size = 0
                p_roman_word_size = 0
            for  i in range(0,pp_roman_word_size):
                punjabi_line[line_ptr] = pp_roman_word[i]
                line_ptr+=1
            if  found == 2:
                p_urdu_word_size = 0
                pp_roman_word_size = p_roman_word_size
                for  i in range(0,pp_roman_word_size):
                    pp_roman_word[i] = p_roman_word[i]
                p_roman_word_size = 0
            if  found == 3:
                pp_urdu_word_size = p_urdu_word_size = urdu_word_size = 0
                pp_roman_word_size = p_roman_word_size = roman_word_size = 0
            roman_word_size = 0
            pp_roman_word_size = p_roman_word_size
            for  i in range(0,pp_roman_word_size):
                pp_roman_word[i] = p_roman_word[i]
            p_roman_word_size = roman_word_size
            for  i in range(0,p_roman_word_size):
                p_roman_word[i] = roman_word[i]
            for  i in range(0,roman_word_size):
                roman_word[i] = 0
            pp_urdu_word_size = p_urdu_word_size
            for  i in range(0,pp_urdu_word_size):
                pp_urdu_word[i] = p_urdu_word[i]
            p_urdu_word_size = urdu_word_size
            for  i in range(0,p_urdu_word_size):
                p_urdu_word[i] = urdu_word[i]
            for  i in range(0,urdu_word_size):
                urdu_word[i] = 0
            urdu_word_size = 0
        line_ptr=self.post_process(punjabi_line,line_ptr)
        # print('after')
        # print(f'urdu_word:\n{urdu_word[:50]}\n\npp_urdu_word:\n{pp_urdu_word[:50]}\n\np_urdu_word:\n{p_urdu_word[:50]}')
        # print(f'roman_word:\n{roman_word[:50]}\n\npp_roman_word:\n{pp_roman_word[:50]}\n\np_roman_word:\n{p_roman_word[:50]}')
        for  i in range(0,line_ptr):
            roman[roman_ptr] = punjabi_line[i]
            roman_ptr+=1
        roman_size = roman_ptr
        # print(f'array after post process:\n{roman}')
        # print(shah_tokens)
        return roman_size

    def check_punjabi_punctuation(self, ch, ch1):
        if  ch1 != 10: return 1
        if  (ch >96) and (ch <112): return 1
        return 0

    def check_punctuation(self, ch, ch1):
        # print('inside check_punctuation() function')
        if  (ch1 == 0) or (ch1 == 32): return 1
        if  ch1 == 6:
            if  ch ==255:
                return 1
            if  ch <=31:
                return 1
            if  (ch ==212) or (ch ==31) or (ch ==12) or (ch ==13) or (ch ==27) or (ch ==106) or (ch ==109) or (ch ==107):
                return 1
            if  (ch >=96) and (ch <=105):
                return 1
            if  (ch >=240) and (ch <=249):
                return 1
            if  ch ==64:
                return 1
        if  ch1 ==32:
            if  (ch ==24) or (ch ==25) or (ch ==29) or (ch ==28):
                return 1
        if  ch1 == 254: return 0
        if  ch1 >32: return 1
        return 0

    def convert_urdu_punctuation_to_roman(self, ch, ch1, roman):
        # print('inside convert_urdu_punctuation_to_roman() function')
        urdu_to_roman=[0]*256
        roman_ptr = 0
        for  i in range(0,256):
            urdu_to_roman[i] = i
        for  i in range(0,32):
            urdu_to_roman[i] = 0
        for  i in range(128,256):
            urdu_to_roman[i] = 0
        urdu_to_roman[33] = ord(' ')
        urdu_to_roman[12] = ord(',')
        urdu_to_roman[13] = ord(',')
        urdu_to_roman[27] = ord(';')
        urdu_to_roman[31] = ord('?')
        urdu_to_roman[64] = ord(' ')
        urdu_to_roman[212] = ord('.')
        urdu_to_roman[12] = ord(',')
        urdu_to_roman[13] = ord('/')
        urdu_to_roman[27] = ord(';')
        urdu_to_roman[106] = ord('/')
        urdu_to_roman[107] = ord(',')
        urdu_to_roman[109] = ord('*')
        urdu_to_roman[255] = 0
        urdu_to_roman[20] = 0
        if  (ch1 == 6) and (ch == 16):
            roman[roman_ptr] = ord('(')
            roman_ptr+=1
            roman[roman_ptr] = 0
            roman_ptr+=1
            roman[roman_ptr] =56
            roman_ptr+=1
            roman[roman_ptr] = 10
            roman_ptr+=1
            roman[roman_ptr] =50
            roman_ptr+=1
            roman[roman_ptr] = 10
            roman_ptr+=1
            roman[roman_ptr] = ord('.')
            roman_ptr+=1
            roman[roman_ptr] = 0
            roman_ptr+=1
            roman[roman_ptr] = ord(')')
            roman_ptr+=1
            roman[roman_ptr] = 0
            roman_ptr+=1
        else:
            if  (ch1 == 6) and (ch == 17):
                roman[roman_ptr] = ord('(')
                roman_ptr+=1
                roman[roman_ptr] = 0
                roman_ptr+=1
                roman[roman_ptr] = 5
                roman_ptr+=1
                roman[roman_ptr] = 10
                roman_ptr+=1
                roman[roman_ptr] =50
                roman_ptr+=1
                roman[roman_ptr] = 10
                roman_ptr+=1
                roman[roman_ptr] =72
                roman_ptr+=1
                roman[roman_ptr] = 10
                roman_ptr+=1
                roman[roman_ptr] = ord('.')
                roman_ptr+=1
                roman[roman_ptr] = 0
                roman_ptr+=1
                roman[roman_ptr] = ord(')')
                roman_ptr+=1
                roman[roman_ptr] = 0
                roman_ptr+=1
            else:
                if  (ch1 == 6) and (ch ==18):
                    roman[roman_ptr] = ord('(')
                    roman_ptr+=1
                    roman[roman_ptr] = 0
                    roman_ptr+=1
                    roman[roman_ptr] =48
                    roman_ptr+=1
                    roman[roman_ptr] = 10
                    roman_ptr+=1
                    roman[roman_ptr] =57
                    roman_ptr+=1
                    roman[roman_ptr] = 10
                    roman_ptr+=1
                    roman[roman_ptr] =63
                    roman_ptr+=1
                    roman[roman_ptr] = 10
                    roman_ptr+=1
                    roman[roman_ptr] = ord('.')
                    roman_ptr+=1
                    roman[roman_ptr] = 0
                    roman_ptr+=1
                    roman[roman_ptr] = ord(')')
                    roman_ptr+=1
                    roman[roman_ptr] = 0
                    roman_ptr+=1
                else:
                    if  (ch1 == 6) and (ch ==19):
                        roman[roman_ptr] = ord('(')
                        roman_ptr+=1
                        roman[roman_ptr] = 0
                        roman_ptr+=1
                        roman[roman_ptr] =48
                        roman_ptr+=1
                        roman[roman_ptr] = 10
                        roman_ptr+=1
                        roman[roman_ptr] =91
                        roman_ptr+=1
                        roman[roman_ptr] = 10
                        roman_ptr+=1
                        roman[roman_ptr] =64
                        roman_ptr+=1
                        roman[roman_ptr] = 10
                        roman_ptr+=1
                        roman[roman_ptr] = ord('.')
                        roman_ptr+=1
                        roman[roman_ptr] = 0
                        roman_ptr+=1
                        roman[roman_ptr] = ord(')')
                        roman_ptr+=1
                        roman[roman_ptr] = 0
                        roman_ptr+=1
                    else:
                        if  (ch >=96) and (ch <=105) and (ch1 == 6):
                            roman[roman_ptr] = (ch + 6)
                            roman_ptr+=1
                            roman[roman_ptr] = 10
                            roman_ptr+=1
                        else:
                            if  (ch >=240) and (ch <=249) and (ch1 == 6):
                                roman[roman_ptr] = (ch -138)
                                roman_ptr+=1
                                roman[roman_ptr] = 10
                                roman_ptr+=1
                            else:
                                if  (ch ==212) and (ch1 == 6):
                                    roman[roman_ptr] =100
                                    roman_ptr+=1
                                    roman[roman_ptr] = 9
                                    roman_ptr+=1
                                else:
                                    if  ch1 != 6:
                                        if  (ch1 ==32) and (ch ==24):
                                            roman[roman_ptr] = 39
                                            roman_ptr+=1
                                        else:
                                            if  (ch1 ==32) and (ch ==25):
                                                roman[roman_ptr] = 39
                                                roman_ptr+=1
                                            else:
                                                if  ch > 128: ch = 0
                                                roman[roman_ptr] = ch
                                                roman_ptr+=1
                                    else:
                                        roman[roman_ptr] = urdu_to_roman[ch]
                                        roman_ptr+=1
                                    roman[roman_ptr] = 0
                                    roman_ptr+=1
        # print(f'urdu_to_roman_punctuation: {urdu_to_roman}')
        # print(roman)
        roman_size = roman_ptr
        return roman_size

        
    def write_frequency(self, ):
        pass

    def check_urdu_word_trigram(self, urdu, p_urdu, pp_urdu, urdu_size, p_urdu_size, pp_urdu_size, roman):
        return 0

    def check_urdu_word_bigram(self, urdu, p_urdu, urdu_size, p_urdu_size, roman, roman_size):
        # print('\t\tinside bigram check function\n')
        low = 0
        mid = 0
        last = 0
        found = 0
        high = self.urdu_bigram_total
        read_word=[0]*50
        Urdu_UTF8=[0]*50
        Urdu1_UTF8=[0]*50
        temp=[0]*50
        self.UnicodeTo8(p_urdu, p_urdu_size, Urdu_UTF8)
        while  low <= high:
            mid = int((low + high) / 2)
            self.strcpy(read_word, self.urdu_bigram[mid].urdu1)
            while  not(self.strcmp(self.urdu_bigram[mid].urdu1, Urdu_UTF8) != 0):
                found = 1
                self.UnicodeTo8(urdu, urdu_size, Urdu1_UTF8)
                if  not(self.strcmp(self.urdu_bigram[mid].urdu2, Urdu1_UTF8) != 0):
                    self.strcpy(temp, self.urdu_bigram[mid].punjabi)
                    k=0
                    for  i in range(0,self.strlen(temp)):
                        if  temp[i] == 255:
                            if  i < self.strlen(temp) - 1:
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
                                if  temp[i] == 253:
                                    roman[k] = ord('.')
                                    k+=1
                                    roman[k] = 0
                                    k+=1
                                else:
                                    roman[k] = temp[i]
                                    k+=1
                                    roman[k] = 10
                                    k+=1
                    roman_size = k
                    return roman_size, 1
                if  self.strcmp(self.urdu_bigram[mid].urdu2, Urdu1_UTF8) > 0:
                    mid-=1
                    if last > 0:
                        mid = -1
                    last = -1
                else:
                    mid+=1
                    if  last < 0:
                        mid = -1
                    last = 1
                if  (mid < 0) or (mid >= self.urdu_bigram_total): return roman_size, 0
            if  found > 0: return roman_size, 0
            if  self.strcmp(read_word, Urdu_UTF8) < 0:
                low = mid + 1
            else:
                high = mid - 1
     
        return roman_size, 0

    def check_invalid_first_char(self, c):
        r = ((c ==33) or (c ==36) or (c ==37) or (c ==38) or (c ==80) or (c ==81) or (c ==82) or (c ==84) or (c ==85) or (c ==88) or (c ==116) or
            (c ==194) or (c ==195) or (c ==210) or (c ==211))
        if  r: return 1
        else: return 0

    def check_invalid_combination(self, urdu1, urdu2):
        n = self.strlen(urdu1) - 1
        if  self.check_matra(urdu1[n]) > 0 and self.check_matra(urdu2[0]) > 0:
            return 1
        if  (urdu1[n] ==186) and (urdu2[0] !=175):
            return 1
        if  (urdu2[0] == 34) and (urdu2[1] != 40):
            return 1
        if  urdu1[0] == 33:
            return 1
        return 0

    def check_joining_combination(self, urdu1, urdu2):
        if  self.check_invalid_first_char(urdu2[0]) > 0:
            return 1
        return 0

    def check_definte_join_word(self, urdu2):
                post_dict=np.zeros((20,10),dtype='i')
                Urdu_UTF8=np.zeros((40),dtype='i')
                total = 8
                post_dict[2][0] = post_dict[1][0] = post_dict[0][0] =175
                post_dict[5][0] = post_dict[4][0] = post_dict[3][0] =42
                post_dict[0][1] =210
                post_dict[3][1] =210
                post_dict[3][1] =11
                post_dict[1][1] =204
                post_dict[4][1] =204
                post_dict[2][1] =39
                post_dict[5][1] =39
                post_dict[5][2] = post_dict[4][2] = post_dict[3][2] = post_dict[2][2] = post_dict[1][2] = post_dict[0][2] = 0
                post_dict[6][0] = post_dict[7][0] =47
                post_dict[6][1] = post_dict[7][1] =39
                post_dict[6][2] = post_dict[7][2] =49
                post_dict[6][3] = post_dict[7][4] = 0
                post_dict[7][3] =204
                for  i in range(0,total):
                    if  not(self.strcmp(post_dict[i], urdu2) != 0):
                        return 1
                return 0

    def get_bigram_freq(self, word1, word2):
        punjabi_int =np.zeros((20),dtype='i')
        start = 0
        end = 0
        freq = 0
        normalise=[0]*20
        temp_word=[0]*20
        temp_word1=[0]*20
        norm1=[0]*20
        norm2=[0]*20
        pre_freq = 0
        if  self.strlen(word2) == 0: return 0
        if  (self.strlen(word1) > 9) or (self.strlen(word2) > 9):
            return 0
        for  k in range(0,self.strlen(word1)):
            punjabi_int[k] = word1[k]
        self.normalise_punjabi_word(punjabi_int, self.strlen(word1), norm1)
        for  k in range(0,self.strlen(word2)):
            punjabi_int[k] = word2[k]
        self.normalise_punjabi_word(punjabi_int, self.strlen(word2), norm2)
        start,end,flag=self.search_word_pre_bigram_index(norm1,start, end)
        if  flag > 0:
            pre_freq = self.search_word_pre_int_bigram(norm2, start, end, temp_word)
            if  pre_freq > freq + 1:
                freq = pre_freq

        start,end,flag=self.search_word_post_bigram_index(norm2,start, end) 
        if  flag > 0:
            pre_freq = self.search_word_post_int_bigram(norm1, start, end, temp_word)
            if  pre_freq > freq + 1:
                freq = pre_freq
        start,end,flag=self.search_word_bigram_index(word1,start,end)
        if  flag > 0:
            pre_freq = self.search_word_bigram(word2, start, end)
            if  pre_freq > freq + 1:
                freq = pre_freq
        return freq

    def check_equivalence(self, combine, combine_size, punjabi1, punjabi_size1, punjabi2, punjabi_size2):
        if  punjabi_size1 + punjabi_size2 != combine_size:
            return 0
        for  i in range(0,punjabi_size1):
            if  combine[i] != punjabi1[i]: return 0
        for  i in range(0,punjabi_size2):
            if  i == 0:
                if  (punjabi2[i] == 6) and (combine[i + punjabi_size1] ==62):
                    continue
                if  (punjabi2[i] == 8) and (combine[i + punjabi_size1] ==64):
                    continue
                if  (punjabi2[i] == 8) and (combine[i + punjabi_size1] ==71):
                    continue
            if  combine[i + punjabi_size1] != punjabi2[i]: return 0
        return 1

    def check_urdu_broken_word(self, urdu, p_urdu, urdu_size, p_urdu_size, punjabi, punjabi_size):
        # print('\t\tinside broken word function\n ')
        total = 10000
        min_limit = 10000
        punjabi_int = np.zeros((40),dtype='i')
        urdu_int = np.zeros((30),dtype='i')
        temp_size = 0
        temp_size1 = 0
        mult = 1

        final_word=[0]*130
        Urdu_UTF8=[0]*130
        Urdu1_UTF8=[0]*130
        temp=[0]*150
        temp1=[0]*150
        urdu1=[0]*150
        c = 0
        definte_join = 0
        self.UnicodeTo8(urdu, urdu_size, Urdu_UTF8)
        self.UnicodeTo8(p_urdu, p_urdu_size, Urdu1_UTF8)
        if  self.check_invalid_combination(Urdu1_UTF8, Urdu_UTF8) > 0:
            punjabi_size = 0
            return punjabi_size, 0
        for  i in range(0,p_urdu_size):
            urdu1[i] = p_urdu[i]
        for  i in range(0,urdu_size):
            urdu1[i + p_urdu_size] = urdu[i]
        c+=1
        if  c == 2438:
            c+=1
        punjabi_size, freq = self.get_word_freq(urdu1, urdu_size + p_urdu_size, punjabi,punjabi_size, definte_join)
        if  freq > 0 and self.check_joining_combination(Urdu1_UTF8, Urdu_UTF8) > 0:
            return punjabi_size, freq
        definte_join = self.check_definte_join_word(Urdu_UTF8)
        if  definte_join > 0:
            temp_size = temp_size1 = 0
            temp_size, freq2 = self.get_word_freq(p_urdu, p_urdu_size, temp,temp_size, 0)
            temp_size1, freq1 = self.get_word_freq(urdu, urdu_size, temp1, temp_size1,0)
            if  not(temp_size != 0):
                punjabi_size = 0
                return punjabi_size, 0
            r1 = (freq * 1.0) / total
            r2 = (1.0 * freq1) / (total)
            r3 = (1.0 * freq2) / (total)
            r4 = r2 * r3
            if  (freq > 10) and (r4 < r1):
                return punjabi_size, freq
            punjabi_size = temp_size + temp_size1
            for  i in range(0,temp_size):
                punjabi[i] = temp[i]
            for  i in range(0,temp_size1):
                punjabi[i + temp_size] = temp1[i]
            return punjabi_size, 1
        if  freq < 3:
            punjabi_size = 0
            return punjabi_size, 0
        temp_size, freq2 = self.get_word_freq(p_urdu, p_urdu_size, temp, temp_size,0)
        temp_size1, freq1 = self.get_word_freq(urdu, urdu_size, temp1, temp_size1,0)
        if  freq1 == 0:
            temp_size1 = 0
        if  freq2 == 0:
            temp_size = 0
        if  (freq1 < 1) or (freq2 < 1):
            return punjabi_size, freq
        self.UnicodeTo8(temp, temp_size, Urdu_UTF8)
        self.UnicodeTo8(temp1, temp_size1, Urdu1_UTF8)
        freq3 = self.get_bigram_freq(Urdu_UTF8, Urdu1_UTF8)
        con1 = self.check_equivalence(punjabi, punjabi_size, temp, temp_size, temp1, temp_size1)
        if  ((freq > 8) and (freq3 <= 0)) or (con1) > 0:
            mult = 1
            if  freq1 + freq2 < 10000: con = 1
            else: con = 0
            if  con1 > 0 and (temp1[0] == 38) and (temp_size1 == 4): con = 1
            if  (freq3 * mult < freq) and con > 0:
                return punjabi_size, freq
        else:
            mult = 8

        r1 = (freq * 1.0) / total
        r2 = (1.0 * freq1) / (total)
        r3 = (1.0 * freq2) / (total)
        r4 = r2 * r3
        if  (r4 > r1) or (freq3 * mult > freq):
            punjabi_size = 0
            return punjabi_size, 0
        print(punjabi_size)
        return punjabi_size, freq


    def get_word_freq(self, urdu, urdu_size, punjabi, punjabi_size,dummy):
        mid = 0
        last = 0
        found = 0
        high = self.urdu_bigram_total
        punjabi_int = np.zeros((40),dtype='i')
        punjabi_int_size = 0
        urdu_int = np.zeros((30),dtype='i')
        final_word=[0]*30
        Urdu_UTF8=[0]*30
        Urdu1_UTF8=[0]*30
        temp=[0]*50
        urdu1=[0]*40

        punjabi_size, flag=self.check_urdu_word_dictionary(urdu, urdu_size, punjabi,punjabi_size)
        if  flag > 0:
            j=0
            for  i in range(0,punjabi_size,2):
                punjabi_int[j] = punjabi[i]
                j+=1
            punjabi_int_size = int(punjabi_size / 2)
            punjabi_int_size, freq = self.check_punjabi_corpus(punjabi_int, punjabi_int_size, final_word)
            return punjabi_size, freq
        urdu_ptr = urdu_int_ptr = 0
        while  urdu_ptr < urdu_size:
            ch = urdu[urdu_ptr]
            ch1 = urdu[urdu_ptr + 1]
            int1 = ch1
            int1 <<= 8
            int1 += ch
            urdu_ptr += 2
            urdu_int[urdu_int_ptr] = int1
            urdu_int_ptr+=1
        punjabi_int_size=self.rule_based_urdu_word_to_punjabi(urdu_int, int(urdu_size / 2), punjabi_int)
        punjabi_int_size=self.improve_punjabi_word(punjabi_int,punjabi_int_size)
        punjabi_int_size, freq = self.check_punjabi_corpus(punjabi_int,punjabi_int_size, final_word)
        if  freq > 0:
            punjabi_size = 0
            self.check_urdu_nukta_dictionary(urdu, urdu_size, final_word)
            for  i in range(0,self.strlen(final_word)):
                if  final_word[i] ==118:
                    punjabi[(punjabi_size)] = ord('-')
                    punjabi_size+=1
                    punjabi[punjabi_size] = 0
                    punjabi_size+=1
                    continue
                punjabi[(punjabi_size)] = final_word[i]
                punjabi_size+=1
                punjabi[(punjabi_size)] = 10
                punjabi_size+=1
            return punjabi_size, freq
        else: return punjabi_size, 0
        return punjabi_size, 0

    def check_urdu_word_dictionary(self, urdu, urdu_size, roman, roman_size):
        # print('\t\tinside word dictionary function\n')
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
        self.UnicodeTo8(urdu, urdu_size, Urdu_UTF8)
        high = self.dict_word_count - 1
        while  low <= high:
            mid = int((low + high) / 2)
            self.strcpy(read_word, self.urdu_dict[mid])
            if  not(self.strcmp(read_word, Urdu_UTF8) != 0):
                self.strcpy(temp, self.roman_dict[mid])
                self.check_urdu_nukta_dictionary(urdu, urdu_size, temp)
                k=0
                for  i in range(0,self.strlen(temp)):
                    if  temp[i] == 255:
                        if  i < self.strlen(temp) - 1:
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
                            if  temp[i] == 253:
                                roman[k] = ord('.')
                                k+=1
                                roman[k] = 0
                                k+=1
                            else:
                                roman[k] = temp[i]
                                k+=1
                                roman[k] = 10
                                k+=1
                    # print(f'\t\t\t\troman_update: {roman}')
                roman_size = k
                return roman_size, 1
            if  self.strcmp(read_word, Urdu_UTF8) < 0:
                low = mid + 1
            else:
                high = mid - 1
        return roman_size, 0

    def check_post_word(self, urdu, p_urdu, urdu_size, p_urdu_size):
        # print('inside check_post_word() function\n ')
        post_dict=np.zeros((20,20),dtype='i')
        Urdu_UTF8=[0]*40
        if  urdu_size == 0: return p_urdu_size, 0
        total = 8
        post_dict[2][0] = post_dict[1][0] = post_dict[0][0] =175
        post_dict[5][0] = post_dict[4][0] = post_dict[3][0] =42
        post_dict[0][1] =210
        post_dict[3][1] =11
        post_dict[1][1] =204
        post_dict[4][1] =204
        post_dict[2][1] =39
        post_dict[5][1] =39
        post_dict[5][2] = post_dict[4][2] = post_dict[3][2] = post_dict[2][2] = post_dict[1][2] = post_dict[0][2] = 0
        post_dict[6][0] = post_dict[7][0] =47
        post_dict[6][1] = post_dict[7][1] =39
        post_dict[6][2] = post_dict[7][2] =49
        post_dict[6][3] = post_dict[7][4] = 0
        post_dict[7][3] =204
        self.UnicodeTo8(urdu, urdu_size, Urdu_UTF8)
        for  i in range(0,total):
            if  not(self.strcmp(post_dict[i], Urdu_UTF8) != 0):
                k = p_urdu_size
                for  i in range(0,urdu_size):
                    p_urdu[k] = urdu[i]
                    k+=1
                p_urdu_size += urdu_size
                return p_urdu_size, 1
        if  p_urdu_size == 0: return p_urdu_size, 0
        total = 1
        post_dict[0][0] =40
        post_dict[0][1] =210
        post_dict[0][2] = 0
        self.UnicodeTo8(p_urdu, p_urdu_size, Urdu_UTF8)
        for  i in range(0,total):
            if  not(self.strcmp(post_dict[i], Urdu_UTF8) != 0):
                k=p_urdu_size
                for  i in range(0,urdu_size):
                    p_urdu[k] = urdu[i]
                    k+=1
                p_urdu_size += urdu_size
                return p_urdu_size, 2
        return p_urdu_size, 0

    def add_frequency(self, urdu, urdu_size):
                read_word=[0]*80
                Urdu_UTF8=[0]*40
                temp=[0]*80
                if  urdu_size <= 2: return 1
                self.UnicodeToUtf8(urdu, urdu_size, Urdu_UTF8)
                if  self.word_total >= 20000:
                    self.word_total = 20000
                for  i in range(0,self.word_total):
                    if  not(self.strcmp(self.wordlist[i].word, Urdu_UTF8) != 0):
                        self.wordlist[i].count+=1
                        return 1
                self.wordlist[self.word_total].count = 1
                self.strcpy(self.wordlist[self.word_total].word, Urdu_UTF8)
                self.word_total+=1
                return 0

    def strcmp_unicode(self, str1, str2, size):
                for  i in range(0,size):
                    if  str1[i] < str2[i]: return -1
                    if  str1[i] > str2[i]: return 1
                return 0

    def strcpy_unicode(self, str1, str2, size):
                for  i in range(0,size):
                    str2[i] = str1[i]
                return 0

    def normalise_urdu(self, urdu, urdu_size):
                for  i in range(0,urdu_size,2):
                    if  (urdu[i] ==73) or (urdu[i] ==74):
                        urdu[i] =204

    def normalise_urdu_word(self, urdu, urdu_size):
                # print('inside normalise_urdu_word() function\n')
                temp_urdu=[0]*100
                j=0
                for  i in range(0,urdu_size,2):
                    if  (urdu[i] ==81) and (urdu[i + 2] ==81):
                        continue
                    else:
                        if  (urdu[i] ==39) and (urdu[i + 2] ==83):
                            temp_urdu[j] =34
                            j+=1
                            i += 2
                        else:
                            if  ((urdu[i] ==78) or (urdu[i] ==79) or (urdu[i] ==80) or (urdu[i] ==81)) and (urdu[i + 2] ==190):
                                temp_urdu[j] = urdu[i + 2]
                                j+=1
                                temp_urdu[j] = 6
                                j+=1
                                temp_urdu[j] = urdu[i]
                                j+=1
                                i += 2
                            else:
                                if  (i == urdu_size - 2) and (urdu[i] ==38):
                                    temp_urdu[j] =204
                                    j+=1
                                    temp_urdu[j] = 6
                                    j+=1
                                    temp_urdu[j] =84
                                    j+=1
                                else:
                                    if  (urdu[i] ==211):
                                        temp_urdu[j] =210
                                        j+=1
                                        temp_urdu[j] = 6
                                        j+=1
                                        temp_urdu[j] =84
                                        j+=1
                                    else:
                                        if  (urdu[i] ==74) or (urdu[i] ==73):
                                            temp_urdu[j] =204
                                            j+=1
                                        else:
                                            if  ((urdu[i] ==133) or (urdu[i] ==134)) and (urdu[i + 1] ==254):
                                                temp_urdu[j] =36
                                                j+=1
                                            else:
                                                temp_urdu[j] = urdu[i]
                                                j+=1
                    temp_urdu[j] = 6
                    j+=1
                for  i in range(0,j):
                    urdu[i] = temp_urdu[i]
                # print(urdu)
                urdu_size = j
                return urdu_size

    def normalise_text(self, urdu, urdu_size, temp_urdu):
                i = j = 0
                while i < urdu_size:
                    if  (urdu[i + 1] == 6):
                        if  (urdu[i] ==39) and (urdu[i + 2] ==83) and (urdu[i + 3] == 6):
                            temp_urdu[j] =34
                            j+=1
                            temp_urdu[j] = 6
                            j+=1
                            i += 2
                        else:
                            if  (urdu[i] ==72) and ((urdu[i + 2] ==116) or (urdu[i + 2] ==84)) and (urdu[i + 3] == 6):  
                                temp_urdu[j] =36
                                j+=1
                                temp_urdu[j] = 6
                                j+=1
                                i += 2
                            else:
                                if  (urdu[i] ==67):
                                    temp_urdu[j] =169
                                    j+=1
                                    temp_urdu[j] = 6
                                    j+=1
                                else:
                                    if  (urdu[i] ==67):
                                        temp_urdu[j] =84
                                        j+=1
                                        temp_urdu[j] = 6
                                        j+=1
                                    else:
                                        if  (urdu[i] ==211):
                                            temp_urdu[j] =210
                                            j+=1
                                            temp_urdu[j] = 6
                                            j+=1
                                            temp_urdu[j] =84
                                            j+=1
                                            temp_urdu[j] = 6
                                            j+=1
                                        else:
                                            if  (urdu[i] ==74) or (urdu[i] ==73):
                                                temp_urdu[j] =204
                                                j+=1
                                                temp_urdu[j] = 6
                                                j+=1
                                            else:
                                                temp_urdu[j] = urdu[i]
                                                j+=1
                                                temp_urdu[j] = urdu[i + 1]
                                                j+=1
                    else:
                        if  (urdu[i + 1] == 32):
                            if  (urdu[i] ==12):
                                temp_urdu[j] = 32
                                j+=1
                                temp_urdu[j] = 0
                                j+=1
                            elif  (urdu[i] ==24) or (urdu[i] ==25):
                                temp_urdu[j] = 39
                                j+=1
                                temp_urdu[j] = 0
                                j+=1
                            else:
                                temp_urdu[j] = urdu[i]
                                j+=1
                                temp_urdu[j] = 0
                                j+=1
                        else:
                            if  urdu[i + 1] ==254:
                                if  (urdu[i] ==133) or (urdu[i] ==134):
                                    temp_urdu[j] =36
                                    j+=1
                                    temp_urdu[j] = 6
                                    j+=1
                                else:
                                    temp_urdu[j] = urdu[i]
                                    j+=1
                                    temp_urdu[j] = urdu[i + 1]
                                    j+=1
                            else:
                                temp_urdu[j] = urdu[i]
                                j+=1
                                temp_urdu[j] = urdu[i + 1]
                                j+=1
                    i+=2
                roman_size = j
                # print(f'\nroman size: {roman_size}')
                # print(f'\narray after normalization:\n {temp_urdu}')
                return roman_size

    def check_gurmukhi_nukta(self, urdu, gurmukhi, start):
                for  i in range(start,self.strlen(gurmukhi)):
                    if  ((urdu ==50) or (urdu ==54) or (urdu ==56)) and (gurmukhi[i + 1] !=60):
                        if  gurmukhi[i] ==28:
                            gurmukhi[i] =91
                            start = i + 1
                            return start, 1
                    if  urdu ==58:
                        if  (gurmukhi[i] ==23) and (gurmukhi[i + 1] !=60):
                            gurmukhi[i] =90
                            start = i + 1
                            return start, 1
                    if  urdu ==65:
                        if  (gurmukhi[i] ==43) and (gurmukhi[i + 1] !=60):
                            gurmukhi[i] =94
                            start = i + 1
                            return start, 1
                    if  urdu ==46:
                        if  (gurmukhi[i] ==22) and (gurmukhi[i + 1] !=60):
                            gurmukhi[i] =89
                            start = i + 1
                            return start, 1
                return start, 0

    def urdu_nukta(self, urdu):
                if  (urdu ==50) or (urdu ==54) or (urdu ==56) or (urdu ==58) or (urdu ==65) or (urdu ==46):
                    return 1
                else:
                    return 0

    def check_urdu_nukta_dictionary(self, urdu, urdu_size, gurmukhi):
                # print('\t\t\t\tinside check_urdu_nukta_dictionary() function\n')
                start = 0
                for  i in range(0,urdu_size):
                    if  self.urdu_nukta(urdu[i]) > 0:
                        start,flag_returned=self.check_gurmukhi_nukta(urdu[i], gurmukhi,start)

    def urdu_word_to_punjabi(self, urdu_word, p_urdu, pp_urdu, urdu_word_size, p_urdu_size, pp_urdu_size, roman, roman_size, punc_flag):
        # print('inside urdu_word_to_punjabi() function\n')
        urdu=[0]*256
        next_ch1 = 0
        next_ch2 = 0
        next_next_ch1 = 0
        next_next_ch2 = 0
        final_word=[0]*16
        urdu_ptr = 0
        roman_ptr = 0
        flag = 0
        urdu_int_ptr = 0
        urdu_int = np.zeros((128),dtype='i')
        punjabi_int = np.zeros((128),dtype='i')
        punjabi_int_size = 0
        urdu_size = pp_urdu_size
        roman2=[0]*6
        for  i in range(0,len(roman2)):
            roman2[i]=[0]*40
        troman=[0]*60
        roman_size2 = np.zeros((6),dtype='i')
        # print(f'pp_urdu: {pp_urdu}\n')
        # print(f'\t\tlength of pp_urdu: {pp_urdu_size}')
        if  urdu_size == 0:
            roman_size = 0
            # print(f'\t\tlength of pp_urdu: {pp_urdu_size}\n\t\treturning -1')
            return roman_size,-1
        # print(f'pp_urdu:\n{pp_urdu}\n\np_urdu: \n{p_urdu}')    
        for  i in range(0,urdu_size):
            urdu[i] = pp_urdu[i]
        # print(f'urdu array:\n{urdu}')
            
        
        #if word found in the begining that is in bigram or broken word
        if  self.conversion_level > 0:
            flag = self.check_urdu_word_trigram(urdu_word, p_urdu, pp_urdu, urdu_word_size, p_urdu_size, pp_urdu_size, roman)  
            if  flag > 0:
                self.word_found+=1
                return roman_size, 3
            if  self.conversion_level > 2:
                roman_size,flag=self.check_urdu_word_bigram(p_urdu,  pp_urdu,  p_urdu_size,  pp_urdu_size,  roman, roman_size) 
                if  flag>0:
                    self.bi_word_found+=1
                    # print('word found inside bigram\n')
                    # print(f'final_word: {roman[:50]}\n')
                    return roman_size, 2
            if  self.conversion_level > 2:
                if punc_flag > 0:
                    roman_size,flag=self.check_urdu_broken_word(p_urdu,  pp_urdu,  p_urdu_size,  pp_urdu_size,  roman, roman_size) 
                    if  flag>0:
                        self.bi_word_found+=1
                        # print('word found inside broken word\n')
                        # print(f'final_word: {roman[:50]}\n')
                        return roman_size, 2

            
            #if word not found in bigrams then check urdu dictionary
            # print(f'\t\turdu_before_tranliterate: {urdu[:20]}\n')
            # print(f'\t\troman: {roman[:20]}\n')
            roman_size, flag=self.check_urdu_word_dictionary(urdu,  urdu_size,  roman, roman_size) 
            # print(f'\t\tflag:{flag}\n')
            if  flag>0:
                self.word_found+=1
                roman[(roman_size)] = 0
                j=0
                # print(f'\t\tword:{roman[:20]}\n')
                for  i in range(0,roman_size):
                    if  roman[i] == 0: j+=1
                if  j > 0:
                    j+=1
                    if  j > 4:
                        j = 4
                    self.multi_count += j
                    self.merged_word_count+=1
                # print(f"\t\tmergerd word count: {self.merged_word_count}\n")
                # print(f'final_word: {roman[:50]}\n')
                return roman_size, 1
        
        
        #if still not found in bigram and urdu dict then check punjabi dict
        urdu_int_ptr = 0
        # print('\t\tword not found in urdu dict\n')
        while  urdu_ptr < urdu_size:
            ch = urdu[urdu_ptr]
            ch1 = urdu[urdu_ptr + 1]
            int1 = ch1
            #-----------------------creation of urdu_int---------------
            int1 <<= 8
            int1 += ch
            urdu_ptr += 2
            urdu_int[urdu_int_ptr] = int1
            urdu_int_ptr+=1
        self.olda = 0
        self.corpus_flag = 1
        # print(f'\t\turdu_int_before: {urdu_int[:20]}\n')
        # print(f'punjabi_int_before: {punjabi_int[:20]}\n')
        punjabi_int_size=self.rule_based_urdu_word_to_punjabi(urdu_int, int(urdu_size / 2), punjabi_int)
        punjabi_int_size=self.improve_punjabi_word(punjabi_int, punjabi_int_size)
        if  self.conversion_level < 2: self.corpus_flag = 0
        else: self.corpus_flag = 1

        if self.corpus_flag > 0:
            punjabi_int_size, flag=self.check_punjabi_corpus(punjabi_int ,punjabi_int_size, final_word)
            if  flag > 0:
                final_word[15] = 0
                self.check_urdu_nukta_dictionary(urdu, urdu_size, final_word)
                for  i in range(0,self.strlen(final_word)):
                    if  final_word[i] ==118:
                        roman[(roman_size)] = ord('-')
                        roman_size+=1
                        roman[roman_size] = 0
                        roman_size+=1
                        continue
                    if  (i > 0) and (final_word[i - 1] == 33) and (final_word[i] == 60):
                        continue
                    roman[(roman_size)] = final_word[i]
                    roman_size+=1
                    roman[roman_size] = 10
                    roman_size+=1
                self.corpus_found+=1
                roman[(roman_size)] = 0
                # print(f'final_word: {roman[:50]}\n')
                return roman_size, 0
        
        
        #if still not found
        words_found = 0
        # print('-------------------------------------------------------------------------------------------------------------------------------------------------\n')
        words_found=self.split_and_check_word_latest(urdu,  urdu_size,  roman2,  roman_size2) 
        if  self.corpus_flag > 0 and words_found>0:
            j=0
            for  i in range(int(urdu_size/2)):
                troman[j] = (urdu_int[i] % 256)
                j+=1
                troman[j] = int(urdu_int[i] / 256)
                j+=1
            j=0
            for  i in range(0,punjabi_int_size):
                troman[j] = (punjabi_int[i] % 256)
                j+=1
                troman[j] = int(punjabi_int[i] / 256)
                j+=1
            for  i in range(0,words_found):
                for  j in range(0,roman_size2[i]):
                    roman[(roman_size)] = roman2[i][j]
                    roman_size+=1
                if  i < words_found - 1:
                    roman[(roman_size)] = ord(' ')
                    roman_size+=1
                    roman[(roman_size)] = 0
                    roman_size+=1
               
            self.multi_count += words_found
            return roman_size, 5
        if  urdu_size >= 2:
            self.word_not_found+=1
        self.add_frequency(urdu, urdu_size)
        urdu_int_ptr = 0
        while  urdu_int_ptr < punjabi_int_size:
            int1 = punjabi_int[urdu_int_ptr]
            urdu_int_ptr+=1
            ch = (int1 % 256)
            ch1 = int(int1 / 256)
            urdu_ptr += 2                           
            if  ch ==118:
                ch = ord('-')
                ch1 = 0
            roman[(roman_size)] = ch
            roman_size+=1
            roman[(roman_size)] = ch1
            roman_size+=1
        # print(f'final_word: {roman[:50]}\n')
        return roman_size, 0

    def improve_punjabi_word(self, punjabi_int, punjabi_int_size):
                # print('\t\tinside improve_punjabi_word() function\n')
                h = 10
                temp = np.zeros((30),dtype='i')
                for  i in range(0,punjabi_int_size):
                    if  i == 0:
                        if  not(self.check_punjabi_full_matra((punjabi_int[i] % 256)) != 0):
                            h <<= 8
                            punjabi_int[i]=h + self.toggle_punjabi_matra(punjabi_int[i])
                        continue
                    if  (self.check_punjabi_matra((punjabi_int[i - 1] % 256))) and (self.check_punjabi_matra((punjabi_int[i] % 256))):
                        if  not(self.check_punjabi_full_matra((punjabi_int[i] % 256)) != 0):
                            h <<= 8
                            punjabi_int[i]=h + self.toggle_punjabi_matra(punjabi_int[i])
                for  i in range(1,punjabi_int_size-1):
                    if  (punjabi_int[i] ==2607) and (punjabi_int[i + 1] ==2622):
                        punjabi_int[i] =2623
                        punjabi_int[i + 1] =2566
                        break
                return punjabi_int_size

    def improve_punjabi_word_matra(self, punjabi, punjabi_size):
                for  i in range(2,punjabi_size,2):
                    if  (self.check_punjabi_matra(punjabi[i - 2])) and (self.check_punjabi_matra(punjabi[i])):
                        if  not(self.check_punjabi_full_matra(punjabi[i]) != 0):
                            punjabi[i] = self.toggle_punjabi_matra(punjabi[i])

    def check_punjabi_full_matra(self, u):
                r = ((u > 3) and (u <11)) or ((u >12) and (u <21))
                if  r: return 1
                else: return 0

    def toggle_punjabi_matra(self, u):
                u=self.convertToByte(u)
                toggle_table=[0]*256
                for  i in range(0,256):
                    toggle_table[i] = i
                toggle_table[6] = 62
                toggle_table[7] = 63
                toggle_table[8] = 64
                toggle_table[9] = 65
                toggle_table[10] = 66
                toggle_table[15] = 71
                toggle_table[16] = 72
                toggle_table[19] = 75
                toggle_table[20] = 76
                toggle_table[62] = 6
                toggle_table[63] = 7
                toggle_table[64] = 8
                toggle_table[65] = 9
                toggle_table[66] = 10
                toggle_table[71] = 15
                toggle_table[72] = 16
                toggle_table[75] = 19
                toggle_table[76] = 20
                return toggle_table[u]

    def rule_based_urdu_word_to_punjabi(self, urdu_int, urdu_size, punjabi_int):
                # print(f'\t\tinside rule_based_urdu_word_to_punjabi() function\n')
                cp = -1
                punjabi_size = 0
                bb = 0
                b = 0
                self.olda = 0
                punjabi_int_size = 0

                for  i in range(1,urdu_size):
                    if  urdu_int[i] ==1617:
                        urdu_int[i] = urdu_int[i - 1]
                        urdu_int[i - 1] =1617
                for  i in range(1,urdu_size-1):
                    if  ((urdu_int[i] ==1616) or (urdu_int[i] ==1615)) and (urdu_int[i + 1] ==1726):
                        urdu_int[i + 1] = urdu_int[i]
                        urdu_int[i] =1726
                cp+=1
                while  cp < urdu_size:
                    a = urdu_int[cp]
                    if  (cp >= 0) and a ==1791:
                        self.olda = 0
                        cp += 1
                        continue
                    if  a ==1614:
                        self.olda = a
                        cp += 1
                        continue
                    elif  a ==1648 and self.olda ==1608:  
                        self.olda =1648
                        cp += 1
                        continue
                    if  a ==1726:
                        bb = urdu_int[cp + 1]
                        punjabi_size-=1
                        if self.olda == 1576:
                            if  bb ==1617:   
                                punjabi_int[punjabi_size] =2605
                                punjabi_size+=1
                                punjabi_int[punjabi_size] =2637
                                punjabi_size+=1
                            b =2605

                        elif self.olda == 1681:
                            punjabi_int[punjabi_size] =2652
                            punjabi_size+=1
                            punjabi_int[punjabi_size] =2637
                            punjabi_size+=1
                            b =2617

                        elif self.olda ==1662:
                            if  bb ==1617:
                                punjabi_int[punjabi_size] =2603
                                punjabi_size+=1
                                punjabi_int[punjabi_size] =2637
                                punjabi_size+=1
                            b =2603

                        elif self.olda == 1578:
                            if  bb ==1617:  
                                urdu_size,punjabi_size,punjabi_int[punjabi_size] = self.UtoH(1578, urdu_int, urdu_size, urdu_size,punjabi_int,punjabi_size)
                                punjabi_size+=1
                                punjabi_int[punjabi_size] =77
                                punjabi_size+=1
                            b =2597

                        elif self.olda == 1672:
                            if  bb ==1617:
                                punjabi_int[punjabi_size] =2594
                                punjabi_size+=1
                                punjabi_int[punjabi_size] =2637
                                punjabi_size+=1
                            b =2594

                        elif self.olda == 1580:
                            if  bb ==1617:
                                urdu_size,punjabi_size,punjabi_int[punjabi_size] = self.UtoH(1580, urdu_int, urdu_size, urdu_size,punjabi_int,punjabi_size)
                                punjabi_size+=1
                                punjabi_int[punjabi_size] =2637
                                punjabi_size+=1
                            b =2589

                        elif self.olda == 1670:
                            if  bb ==1617:
                                urdu_size,punjabi_size,punjabi_int[punjabi_size] = self.UtoH(1670, urdu_int, urdu_size, urdu_size,punjabi_int,punjabi_size)
                                punjabi_size+=1
                                punjabi_int[punjabi_size] =2637
                                punjabi_size+=1
                            b =2587

                        elif self.olda == 1583:
                            if  bb ==1617:
                                urdu_size,punjabi_size,punjabi_int[punjabi_size] = self.UtoH(1583, urdu_int, urdu_size, urdu_size,punjabi_int,punjabi_size)
                                punjabi_int[punjabi_size] =2637
                                punjabi_size+=1
                            b =2599

                        elif self.olda == 1657:
                            if  bb ==1617:
                                punjabi_int[punjabi_size] =2592
                                punjabi_size+=1
                                punjabi_int[punjabi_size] =2637
                                punjabi_size+=1
                            b =2592

                        elif self.olda == 1705:
                            if  bb ==1617:
                                urdu_size,punjabi_size,punjabi_int[punjabi_size] = self.UtoH(1705, urdu_int, urdu_size, urdu_size,punjabi_int,punjabi_size)
                                punjabi_size+=1
                                punjabi_int[punjabi_size] =2637
                                punjabi_size+=1
                            b =2582

                        elif self.olda == 1711:
                            if  bb ==1617:
                                punjabi_int[punjabi_size] =2584
                                punjabi_size+=1
                                punjabi_int[punjabi_size] =2637
                                punjabi_size+=1
                            b =2584

                        else:
                            b =2617
                            punjabi_size+=1


                    else:
                        if  (cp == urdu_size - 1) and (cp > 2) and ((a == 1616) or (a ==1730) or (a ==1747) or (a ==1728) or (a ==1620) or (a ==1569)): 
                            punjabi_int[punjabi_size] =118
                            punjabi_size+=1
                            punjabi_int[punjabi_size] =2575
                            punjabi_size+=1
                            b =118
                        else:
                            cp,punjabi_size,b = self.UtoH(a, urdu_int, urdu_size, cp, punjabi_int,punjabi_size)
                            
                    if  b == 0:
                        b = a
                    if  punjabi_size >= 0:
                        punjabi_int[punjabi_size] = b
                        punjabi_size+=1
                    if  a ==1688:   
                        b =2364
                        punjabi_int[punjabi_size] = b
                        punjabi_size+=1
                    if  self.PROTECTOLDA == 0:
                        self.olda = a
                    else:
                        self.PROTECTOLDA = 0
                    cp += 1
                punjabi_int_size = punjabi_size
                return punjabi_int_size

    def UnicodeTo8(self, UnicodeString, UnicodePos, szOut):
                j = 0
                self.normalise_urdu(UnicodeString, UnicodePos)
                j=0
                # print(UnicodeString)
                for  i in range(0,UnicodePos,2):
                    szOut[j] = UnicodeString[i]
                    j+=1
                szOut[j] = 0
                j+=1
                return

    def UtoH(self, u, urdu_int, urdu_size, urdu_ptr, punjabi_int, punjabi_ptr):
                punjabi_chr = 0
                if  urdu_ptr >= 2:
                    oolda = urdu_int[urdu_ptr - 2]
                else:
                    oolda = -1
                if  urdu_ptr >= 1:
                    self.olda = urdu_int[urdu_ptr - 1]
                else:
                    self.olda = -1
                if  u ==1570:   
                    return urdu_ptr, punjabi_ptr,2566
                if  punjabi_ptr > 0:
                    punjabi_chr = punjabi_int[(punjabi_ptr) - 1]
                if  u ==1615:
                    urdu_ptr,punjabi_ptr,flag=self.PESH_RULE(urdu_int, urdu_ptr, punjabi_ptr)
                    return urdu_ptr, punjabi_ptr,flag
                if  u ==1608: 
                    urdu_ptr, punjabi_ptr, flag = self.VAO_RULE(urdu_int,urdu_ptr, punjabi_int,punjabi_ptr)
                    return urdu_ptr, punjabi_ptr,flag
                if  u ==1746: 
                    urdu_ptr, punjabi_ptr, flag= self.BADI_YEH_RULE(urdu_int,urdu_ptr, punjabi_ptr)  
                    return urdu_ptr, punjabi_ptr,flag
                if  u ==1740 or u ==1610:
                    urdu_ptr, punjabi_ptr,flag = self.CHOTI_YEH_RULE(urdu_int,urdu_ptr, urdu_size, punjabi_int,punjabi_ptr)  
                    return urdu_ptr, punjabi_ptr,flag
                if  u ==1729: 
                    urdu_ptr, punjabi_ptr,flag = self.CHOTI_HEH_RULE(urdu_int,urdu_ptr, punjabi_int, punjabi_ptr)  
                    return urdu_ptr, punjabi_ptr,flag
                if  u ==1593:
                    urdu_ptr, punjabi_ptr,flag = self.EIN_RULE(urdu_int,urdu_ptr, punjabi_int,punjabi_ptr)  
                    return urdu_ptr, punjabi_ptr,flag
                if  u ==1648:
                    urdu_ptr, punjabi_ptr,flag = self.KHARA_ZABAR_RULE(urdu_int,urdu_ptr, punjabi_int,punjabi_ptr)  
                    return urdu_ptr, punjabi_ptr,flag
                if  u ==1611:
                    urdu_ptr, punjabi_ptr,flag = self.DO_ZABAR_RULE(urdu_int,urdu_ptr, punjabi_int,punjabi_ptr)  
                    return urdu_ptr, punjabi_ptr,flag
                if  u ==1622:
                    urdu_ptr, punjabi_ptr,flag = self.KHARAZER_RULE(urdu_int,urdu_ptr, punjabi_int,punjabi_ptr)  
                    return urdu_ptr, punjabi_ptr,flag
                if  u ==1572 or u ==1574 or u ==1620 or u ==1747 or u ==1730 or u ==1569:
                    urdu_ptr, punjabi_ptr,flag = self.HAMZA_RULE(u, urdu_int, urdu_size,urdu_ptr, punjabi_int,punjabi_ptr)  
                    return urdu_ptr, punjabi_ptr,flag
                if  u ==1606:  
                    urdu_ptr,punjabi_ptr,tmp = self.NUN_RULE(urdu_int, urdu_ptr, punjabi_int,punjabi_ptr)
                    if  tmp != -1:
                        return urdu_ptr, punjabi_ptr,tmp
                if u == 1627:
                    return urdu_ptr, punjabi_ptr,self.JAZM_CONJUNCT_RULE()
                if  self.checkMATRA(u) > 0:
                    consonant_flag = ((punjabi_chr ==2607) or (punjabi_chr ==2613))
                    if  (not consonant_flag) and (((self.olda ==1722) and self.checkMATRA(oolda) > 0) or (self.olda ==32 or self.olda ==1748 or self.olda ==58 or self.olda ==8216 or self.olda ==8217 or self.olda ==46 or self.olda ==40 or self.olda ==34 or self.olda ==10 or self.olda ==45 or self.olda ==1548 or self.olda ==47 or self.olda ==92 or self.olda ==8216 or self.olda <= 0) or self.checkMATRA(self.olda) > 0): 

                        if u==1570: return urdu_ptr, punjabi_ptr,2566
                        elif u==1575:
                            if  self.olda ==1740:
                                return urdu_ptr, punjabi_ptr,2566
                            elif (oolda <= 0):
                                return urdu_ptr, punjabi_ptr,2565
                            else:
                                return urdu_ptr, punjabi_ptr,2622
                        elif u==1616:
                            if  self.olda ==1575:  
                                punjabi_ptr-=1
                            return urdu_ptr, punjabi_ptr,2567
                        elif u==1615: return urdu_ptr, punjabi_ptr,2569
                    else:      

                        if u==1570: return urdu_ptr, punjabi_ptr,2622
                        elif u==1575: return urdu_ptr, punjabi_ptr,2622
                        elif u==1616: return urdu_ptr, punjabi_ptr,2623
                        elif u==1615: return urdu_ptr, punjabi_ptr,2625

                return urdu_ptr, punjabi_ptr, self.convert_urdu_punjabi_char(u)

    def convert_urdu_punjabi_char(self, u):
                c = (u % 256)
                c1 = int(u / 256)
                table=[0]*256
                for  i in range(0,255):
                    table[i] = i
                if  (u < 10) or (u ==64):
                    return 32
                table[82] = 0
                table[34] =6
                table[40] =44
                table[126] =42
                table[42] =36
                table[121] =31
                table[127] =31
                table[43] =56
                table[43] =56
                table[44] =28
                table[134] =26
                table[45] =57
                table[46] =89
                table[47] =38
                table[136] =33
                table[144] =33
                table[48] =91
                table[49] =48
                table[145] =92
                table[153] =92
                table[50] =91
                table[152] =29
                table[60] =56
                table[52] =54
                table[53] =56
                table[54] =91
                table[55] =36
                table[56] =91
                table[58] =90
                table[65] =94
                table[66] =88
                table[169] =21
                table[175] =23
                table[68] =50
                table[69] =46
                table[70] =40
                table[72] =53
                table[193] =57
                table[204] =47
                table[51] =56
                table[240] =102
                table[241] =103
                table[242] =104
                table[243] =105
                table[244] =106
                table[245] =107
                table[246] =108
                table[247] =109
                table[248] =110
                table[249] =111
                table[31] =63
                table[212] =100
                table[186] =2
                table[12] =44
                table[66] =21
                table[118] =9
                table[255] =57
                table[81] =113
                table[152] =91
                table[187] =35
                for  i in range(96,105+1):
                    table[i] = i + 6
                for  i in range(240,249+1):
                    table[i] = (i -138)
                table[71] = table[133] =57
                if  c1 == 6:
                    h = 10
                else:
                    h = 0
                h <<= 8
                h += table[c]
                return h

    def checkMATRA(self, u):
                r = (u ==1570 or u ==1575 or u ==1616 or u ==1615 or u ==1614 or u == 1740)
                if  r: return 1
                else: return 0

    def check_matra(self, c):
                r = (c ==34 or c ==39 or c ==73 or c ==74 or c ==204 or c ==210)
                if  r: return 1
                else: return 0

    def PESH_RULE(self, urdu_int, urdu_ptr, punjabi_ptr):
                a = urdu_int[(urdu_ptr) + 1]
                if  a ==1608: 
                    b = urdu_int[urdu_ptr + 2]
                    if  b ==1614: 
                        return urdu_ptr, punjabi_ptr,2613
                    if  self.olda ==1575: 
                        punjabi_ptr-=1
                        return urdu_ptr, punjabi_ptr,2570
                    else:
                        return urdu_ptr, punjabi_ptr,2626
                self.corpus_flag = 0
                if self.olda == 1575:
                    punjabi_ptr-=1
                    return urdu_ptr, punjabi_ptr,2569
                else:
                    return urdu_ptr, punjabi_ptr,2625

    def VAO_RULE(self, urdu_int, urdu_ptr, punjabi_int, punjabi_ptr):
        if  urdu_ptr >= 2:
            oolda = urdu_int[urdu_ptr - 2]
        else:
            oolda = -1
        if  self.olda ==1614: 
            if  oolda ==1575:    
                punjabi_ptr-=1
                return urdu_ptr,punjabi_ptr,2580
            else:
                return urdu_ptr,punjabi_ptr,2636
        if  self.olda <= 0 or self.olda ==32 or self.olda ==1608 or self.olda ==1748 or self.olda ==58 or self.olda ==8216 or self.olda ==8217 or self.olda ==46 or self.olda ==40 or self.olda ==34 or self.olda ==10 or self.olda ==47 or self.olda ==92 or self.olda ==45 or self.olda ==8216:
            return urdu_ptr,punjabi_ptr,2613
        elif  (self.checkMATRA(self.olda) > 0 and self.olda !=1615 and self.olda !=1614 and self.olda !=1575): 

            return urdu_ptr,punjabi_ptr,2613
        elif  self.olda ==1740 or self.olda ==1610 or self.olda ==1746:  
            return urdu_ptr,punjabi_ptr,2613
        else:  
            b = urdu_int[urdu_ptr + 1]
            if  b ==1615: 
                self.olda = b
                self.PROTECTOLDA = 1
            if  b ==1614:
                return urdu_ptr,punjabi_ptr,2613
            elif  b ==1593 or b ==1746 or self.checkMATRA(b) > 0: 
                self.olda = b
                return urdu_ptr,punjabi_ptr,2613
            elif  b ==1740 or b ==1610:  
                return urdu_ptr,punjabi_ptr,2613
            if  (punjabi_ptr > 0) and (punjabi_int[punjabi_ptr - 1] !=2622) and (self.olda ==1575 or self.olda ==1593): 
                punjabi_ptr-=1

                return urdu_ptr,punjabi_ptr,2580
            else:
                if  (punjabi_ptr > 0) and (punjabi_int[punjabi_ptr - 1] !=2622) and (self.olda ==1615): 
                    punjabi_ptr-=1

                    if  (punjabi_int[punjabi_ptr] ==2570) or (punjabi_int[punjabi_ptr] ==2569):
                        return urdu_ptr,punjabi_ptr,2570
                    else:
                        return urdu_ptr,punjabi_ptr,2626
                else:
                    if  (punjabi_ptr > 0) and (punjabi_int[punjabi_ptr - 1] ==2622): 
                        return urdu_ptr,punjabi_ptr,2613
                    else:
                        return urdu_ptr,punjabi_ptr,2635

    def BADI_YEH_RULE(self, urdu_int, urdu_ptr, punjabi_ptr):
        if  urdu_ptr >= 2:
            oolda = urdu_int[urdu_ptr - 2]
        else:
            oolda = -1
        b = urdu_int[(urdu_ptr) + 1]
        c = urdu_int[(urdu_ptr) + 2]
        if  self.olda ==1614:     
            if  b ==1569:  
                urdu_ptr+=1
                return urdu_ptr, punjabi_ptr,2575
            if  b ==1614:  
                urdu_ptr+=1
                return urdu_ptr, punjabi_ptr,2607
            if  oolda ==1575:  
                punjabi_ptr-=1
                return urdu_ptr, punjabi_ptr,2576
            return urdu_ptr, punjabi_ptr,2632
        elif  self.olda ==1575:  
            punjabi_ptr-=1
            return urdu_ptr, punjabi_ptr,2575
        elif  self.olda ==32 or self.olda ==1593 or self.olda ==1740 or self.olda ==1610 or self.checkMATRA(self.olda) > 0:  
            return urdu_ptr, punjabi_ptr,2575
        if  (b == 1575) and (c == 1722):
            return urdu_ptr, punjabi_ptr,2623
        if  self.checkMATRA(b) > 0  :  
            return urdu_ptr, punjabi_ptr,2607
        elif  b ==1746: 
            return urdu_ptr, punjabi_ptr,2607
        return urdu_ptr, punjabi_ptr,2631

    def CHOTI_YEH_RULE(self, urdu_int, urdu_ptr, urdu_size, punjabi_int, punjabi_ptr):
        if  urdu_ptr >= 2:
            oolda = urdu_int[urdu_ptr - 2]
        else:
            oolda = -1
        b = urdu_int[(urdu_ptr) + 1]
        if  urdu_ptr + 1 == urdu_size: b = 0
        if  self.olda ==1575 and (b ==1575 or b ==1729):   
            return urdu_ptr, punjabi_ptr,2607
        if  self.olda ==1575:
            if  punjabi_ptr < 2:
                punjabi_ptr-=1
            return urdu_ptr, punjabi_ptr,2576
        if  self.olda == 1616:    
            punjabi_ptr-=1
            return urdu_ptr, punjabi_ptr,2624
        if  self.olda <= 0 or self.olda ==32 or self.olda ==1748 or self.olda ==58 or self.olda ==8216 or self.olda ==8217 or self.checkMATRA(self.olda) > 0 or self.olda ==46 or self.olda ==40 or self.olda ==10 or self.olda ==34 or self.olda ==47 or self.olda ==92 or self.olda ==45 or self.olda ==8216:  
            return urdu_ptr, punjabi_ptr,2607
        if  self.olda ==1648:
            return urdu_ptr, punjabi_ptr,2568
        if  self.olda ==1729:
            return urdu_ptr, punjabi_ptr,2624
        if  self.checkMATRA(b) > 0 or b ==1648 or self.olda <= 0 or self.olda ==32 or self.olda ==1748 or self.olda ==58 or self.olda ==8216 or self.olda ==8217 or self.olda ==46 or self.olda ==40 or self.olda ==34 or self.olda ==1548 or self.olda ==10 or self.olda ==47 or self.olda ==92 or self.olda ==45 or self.olda ==8216:   
            if  b == 1575:
                punjabi_int[punjabi_ptr] =2607
                punjabi_ptr+=1
                urdu_ptr+=1
                return urdu_ptr, punjabi_ptr,2622
            else:
                return urdu_ptr, punjabi_ptr,2607
        if  self.olda ==1605 and (oolda <= 0 or oolda ==32 or oolda ==1748 or oolda ==58 or oolda ==8216 or oolda ==8217 or oolda ==46 or oolda ==40 or oolda ==34 or oolda ==10 or oolda ==47 or oolda ==92 or oolda ==45 or oolda ==8216 or oolda ==1548) and b ==1722: 
            return urdu_ptr, punjabi_ptr,2631
        if  (self.olda ==1581 or self.olda ==1729) and oolda ==32 and b ==1722: 
            return urdu_ptr, punjabi_ptr,2632
        return urdu_ptr, punjabi_ptr,2624

    def CHOTI_HEH_RULE(self, urdu_int, urdu_ptr, punjabi_int, punjabi_ptr):    
        b = urdu_int[(urdu_ptr) + 1]
        if  urdu_ptr >= 2:
            oolda = urdu_int[urdu_ptr - 2]
        else:
            oolda = -1
        if  self.checkMATRA(self.olda) > 0 or self.olda ==1608 or self.olda ==1593 or self.olda ==1740 or self.olda ==1610 or self.olda ==32 or self.olda ==1748 or self.olda ==58 or self.olda ==8216 or self.olda ==8217 or self.olda ==46 or self.olda ==40 or self.olda ==34 or self.olda ==10 or self.olda ==47 or self.olda ==92 or self.olda ==45 or self.olda ==8216 or (self.checkMATRA(b) > 0 and b > 0):  
            return urdu_ptr, punjabi_ptr,2617
        if  b ==1615:  
            urdu_ptr+=1
            punjabi_int[(punjabi_ptr)] =2617
            punjabi_ptr+=1
            return urdu_ptr, punjabi_ptr,2626
        if  b ==1622:  
            urdu_ptr+=1
            punjabi_int[punjabi_ptr] = 2617
            punjabi_ptr+=1
            return urdu_ptr, punjabi_ptr,2624

        if  self.olda ==1705 and oolda ==32:  
            return urdu_ptr, punjabi_ptr,2631
        if  not(b != 0) or b ==32 or b ==1748 or b ==58 or b ==8216 or b ==8217 or b ==46 or b ==40 or b ==34 or b ==10 or b ==47 or b ==92 or b ==45 or b ==8216 or b ==1548:   
            return urdu_ptr, punjabi_ptr,2622
        return urdu_ptr, punjabi_ptr,2617

    def EIN_RULE(self, urdu_int, urdu_ptr, punjabi_int, punjabi_ptr):
        b = urdu_int[(urdu_ptr) + 1]
        bb = urdu_int[(urdu_ptr) + 2]
        if  urdu_ptr >= 2:
            oolda = urdu_int[urdu_ptr - 2]
        else:
            oolda = -1
        if  self.olda ==1575 and (b ==1740 or b ==1610): 
            urdu_ptr+=1
            return urdu_ptr, punjabi_ptr,2568
        if  self.olda ==1575 and b ==1575:    
            urdu_ptr+=1
            return urdu_ptr, punjabi_ptr,2566
        if  (oolda <= 0 or oolda ==32) and self.olda ==1575: 
            punjabi_ptr-=1
            return urdu_ptr, punjabi_ptr,2566
        if  (self.checkMATRA(self.olda) > 0 or self.olda ==1740) and b ==1575: 
            urdu_ptr+=1
            return urdu_ptr, punjabi_ptr,2566
        if  (b ==1614 and (bb !=1608 and bb !=1746)) or (self.checkMATRA(self.olda) > 0 or self.olda == 1574): 
            return urdu_ptr, punjabi_ptr,2565
        if  b ==1740 or b ==1610: 
            urdu_ptr+=1
            return urdu_ptr, punjabi_ptr,2568
        if  (self.olda ==1740 or self.olda ==1610) and oolda ==32: 
            punjabi_ptr-=1
            return urdu_ptr, punjabi_ptr,2607
        if  self.olda ==1740 or self.olda ==1610:   
            punjabi_ptr-=1
            return urdu_ptr, punjabi_ptr,2624
        if  b ==1616:      
            urdu_ptr+=1
            return urdu_ptr, punjabi_ptr,2567
        if  b ==1746:     
            urdu_ptr+=1
            return urdu_ptr, punjabi_ptr,2631
        if  b ==1614 and bb ==1746: 
            urdu_ptr+=1
            urdu_ptr+=1
            return urdu_ptr, punjabi_ptr,2576
        if  ((self.checkMATRA(oolda) > 0 or oolda <= 0 or oolda ==32 or oolda ==1748 or oolda ==58 or oolda ==8216 or oolda ==8217 or oolda ==46 or oolda ==40 or oolda ==34 or oolda ==10 or oolda ==47 or oolda ==92 or oolda ==45 or oolda ==8216) and self.olda ==1575) or ((self.olda <= 0 or self.olda ==32 or self.olda ==1748 or self.olda ==58 or (self.olda <= 0) or self.olda ==8216 or self.olda ==8217 or self.olda ==46 or self.olda ==40 or self.olda ==34 or self.olda ==10 or self.olda ==47 or self.olda ==92 or self.olda ==1575 or self.olda ==1740 or self.checkMATRA(self.olda) > 0) and b ==1575):   
            if  self.olda ==1575: 
                punjabi_ptr-=1
            if  b ==1575 and (bb ==1740 or bb ==1610): 
                urdu_ptr+=1
                urdu_ptr+=1
                punjabi_int[punjabi_ptr] =2566
                punjabi_ptr+=1
                return urdu_ptr, punjabi_ptr,2607
            if  b ==1575:      
                urdu_ptr+=1
                if  self.olda <= 0:
                    return urdu_ptr, punjabi_ptr,2566
                punjabi_int[(punjabi_ptr)] =2622
                punjabi_ptr+=1
                return urdu_ptr, punjabi_ptr,2565
            return urdu_ptr, punjabi_ptr,2566
        if  b ==1608 and bb ==1615: 
            urdu_ptr+=1
            urdu_ptr+=1
            return urdu_ptr, punjabi_ptr,2570
        if  oolda ==1608 and self.olda ==1615: 
            punjabi_ptr-=1
            return urdu_ptr, punjabi_ptr,2626
        if  b ==1615:  
            urdu_ptr+=1
            return urdu_ptr, punjabi_ptr,2569
        if  b ==1614 and bb ==1608: 
            urdu_ptr+=1
            urdu_ptr+=1
            return urdu_ptr, punjabi_ptr,2580
            return urdu_ptr, punjabi_ptr,2324
        if  (self.olda > 0) and (b ==1729 or b ==1575):   
            urdu_ptr+=1
            return urdu_ptr, punjabi_ptr,2622
        if  self.olda ==1608:
            return urdu_ptr, punjabi_ptr,2622
        if  self.olda <= 0 or self.olda ==32 or self.olda ==1748 or self.olda ==58 or self.olda ==8216 or self.olda ==8217 or self.olda ==46 or self.olda ==40 or self.olda ==34 or self.olda ==10 or self.olda ==47 or self.olda ==92 or self.olda ==45 or self.olda ==8216:  
            return urdu_ptr, punjabi_ptr,2565
        return urdu_ptr, punjabi_ptr,2622

    def KHARA_ZABAR_RULE(self, urdu_int, urdu_ptr, punjabi_int, punjabi_ptr):
        b = urdu_int[(urdu_ptr) + 1]
        if  urdu_ptr >= 2:
            oolda = urdu_int[urdu_ptr - 2]
        else:
            oolda = -1
        if  (self.olda ==1746 or self.olda ==1740 or self.olda ==1610) and (b ==32 or not(b != 0)): 
            punjabi_ptr-=1
            return urdu_ptr, punjabi_ptr,2622
        if  not(self.checkMATRA(self.olda) != 0) and self.olda !=1746: 
            return urdu_ptr, punjabi_ptr,2622
        return urdu_ptr, punjabi_ptr,2622

    def NUN_RULE(self, urdu_int, urdu_ptr, punjabi_int, punjabi_ptr):
        b = urdu_int[urdu_ptr + 1]
        if  b ==1624:   
            urdu_ptr+=1
            return urdu_ptr,punjabi_ptr,2562
        return urdu_ptr,punjabi_ptr,-1

    def JAZM_CONJUNCT_RULE(self):
        return 2637

    def DO_ZABAR_RULE(self, urdu_int, urdu_ptr, punjabi_int, punjabi_ptr):
        punjabi_ptr-=1
        return urdu_ptr, punjabi_ptr,2600

    def HAMZA_RULE(self, u, urdu_int, urdu_size, urdu_ptr, punjabi_int, punjabi_ptr):
        k = 0
        b = urdu_int[(urdu_ptr) + 1]
        if  urdu_ptr >= 2:
            oolda = urdu_int[urdu_ptr - 2]
        else:
            oolda = -1
        if  urdu_ptr >= 1:
            self.olda = urdu_int[urdu_ptr - 1]
        else:
            self.olda = -1

        if  u ==1620:
            return urdu_ptr, punjabi_ptr,2565
        if  (u ==1572) and (self.olda ==1608):
            return urdu_ptr, punjabi_ptr,2579
        punjabi_ptr-=1
        if  self.olda ==1570 or self.olda ==1575:  
            if  (oolda ==32) or (oolda <= 0):
                if  self.olda ==1570:
                    k =2566
                elif  self.olda ==1575:
                    k =2566
                elif  self.olda ==1729:
                    k =2617
            else:
                k =2622
        elif  (self.olda ==1608) and (oolda > 0):     
            if  oolda ==1615:   
                k =2626
            elif  oolda ==1614:  
                k =2636
            elif  oolda ==1740: 
                k =2613
            else:
                k =2635
        elif  self.olda ==1740 or self.olda ==1610:    
            if  oolda ==1575:
                punjabi_ptr-=1
                k =2568
            else:
                k =2624
        elif  self.olda ==1746:        
            if  oolda ==1614:   
                k =2632
            else:
                k =2631
        if  (k != 0) and (punjabi_ptr >= 0):
            punjabi_int[(punjabi_ptr)] = k
            punjabi_ptr+=1
        urdu_ptr+=1
        if  k == 0:
            punjabi_ptr+=1
        if  (self.olda ==1740 or self.olda ==1610) and b ==1746:   
            return urdu_ptr, punjabi_ptr,2575
        bb = urdu_int[urdu_ptr]
        if  (b ==1740 or b ==1610) and bb ==1575: 
            return urdu_ptr, punjabi_ptr,2607
        if  b ==1616:       
            return urdu_ptr, punjabi_ptr,2567
        if  b ==1740:       
            return urdu_ptr, punjabi_ptr,2568
        if  b ==1608:       
            return urdu_ptr, punjabi_ptr,2569
        if  b ==1746:       
            return urdu_ptr, punjabi_ptr,2575
        if  b ==1610:       
            return urdu_ptr, punjabi_ptr,2568
        if  u ==1730:
            punjabi_int[(punjabi_ptr)] =2622
            punjabi_ptr+=1
            punjabi_int[punjabi_ptr] =2673
            punjabi_ptr+=1
            punjabi_int[(punjabi_ptr)] =2575
            punjabi_ptr+=1
            return urdu_ptr, punjabi_ptr,2673
        if  k != 0:
            urdu_ptr-=1
            if  u ==1572:    
                return urdu_ptr, punjabi_ptr,2579
            return urdu_ptr, punjabi_ptr,2567
        else:
            urdu_ptr, punjabi_ptr,flag = self.UtoH(b, urdu_int, urdu_size,urdu_ptr, punjabi_int,punjabi_ptr)  
            return  urdu_ptr, punjabi_ptr,flag

    def KHARAZER_RULE(self, urdu_int, urdu_ptr, punjabi_int, punjabi_ptr):
        if  urdu_ptr >= 2:
            oolda = urdu_int[urdu_ptr - 2]
        else:
            oolda = -1
        if  (self.olda ==1740 or self.olda ==1610) and oolda ==1575:
            punjabi_ptr-=1
            punjabi_ptr-=1
            return urdu_ptr, punjabi_ptr,2568
        else:
            return urdu_ptr, punjabi_ptr,2624

    def print_word(self, word, file_type, end_line, append):
        pass

    def read_binary_corpus(self, corpus_words):
        FILE_NAME = os.path.join(self.appPath,"fcorpus.bin")
        if not os.path.exists(FILE_NAME):

            return

        r = open(FILE_NAME, 'rb')
        corpus_word_count = int.from_bytes(r.read(4), 'little')
        for i in range(0, corpus_word_count):
            rawBytes = r.read(16)
            for j, byte in enumerate(rawBytes):
                corpus_words[i].original_word[j] = byte
            rawBytes = r.read(16)
            for j, byte in enumerate(rawBytes):
                corpus_words[i].normalised_word[j] = byte
            corpus_words[i].freq = int.from_bytes(r.read(4), 'little')  
        r.close()
        self.isBinCorpus = True
        return corpus_word_count

    def read_ignore_words(self):
        i = 0
        FILE_NAME = os.path.join(self.appPath,"ignore.bin")
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return

        r = open(FILE_NAME, 'rb')
        self.ignore_word_count = int.from_bytes(r.read(4), 'little')
        for i in range(0,self.ignore_word_count):
            rawBytes = r.read(len(self.ignore[i]))
            for j,byte in enumerate(rawBytes):
                self.ignore[i][j] = byte
        r.close()

        FILE_NAME = os.path.join(self.appPath,"prefix.bin")
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return

        r = open(FILE_NAME, 'rb')
        self.prefix_word_count = int.from_bytes(r.read(4), 'little')
        for i in range(0, self.prefix_word_count):
            rawBytes = r.read(len(self.prefix[i]))
            for j, byte in enumerate(rawBytes):
                self.prefix[i][j] = byte
        r.close()


        FILE_NAME = os.path.join(self.appPath,"suffix.bin")
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return

        r = open(FILE_NAME, 'rb')
        self.prefix_word_count = int.from_bytes(r.read(4), 'little')
        for i in range(0, self.prefix_word_count):
            rawBytes = r.read(len(self.suffix[i]))
            for j, byte in enumerate(rawBytes):
                self.suffix[i][j] = byte
        r.close()

    def read_pre_bigram_corpus(self, pre_bigram, pre_bigram_index):
        corpus_word=[0]*200
        freq=[0]*8
        word=[0]*20
        word[0] = 0
        FILE_NAME = os.path.join(self.appPath,"pre_bigram.bin")
        # print(FILE_NAME)
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return

        r = open(FILE_NAME, 'rb')
        pre_bigram_total = int.from_bytes(r.read(4), 'little')
        for i in range(0, pre_bigram_total):

            rawBytes = r.read(len(pre_bigram[i].first_word))
            for j, byte in enumerate(rawBytes):
                pre_bigram[i].first_word[j] = byte

            rawBytes = r.read(len(pre_bigram[i].second_word))
            for j, byte in enumerate(rawBytes):
                pre_bigram[i].second_word[j] = byte

            pre_bigram[i].freq = int.from_bytes(r.read(4), 'little')
            pre_bigram[i].unigram_freq = int.from_bytes(r.read(4), 'little')

        r.close()
        FILE_NAME = os.path.join(self.appPath,"pre_normal_bigram.bin")
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return

        r = open(FILE_NAME, 'rb')
        pre_bigram_index_count = int.from_bytes(r.read(4), 'little')
        pre_bigram_index_count = 0
        for  i in range(0,pre_bigram_total):        

            try:
                rawBytes = r.read(len(pre_bigram_index[i].normalised_word))
                for j, byte in enumerate(rawBytes):
                    pre_bigram_index[i].normalised_word[j] = byte
                readValue=r.read(4)
                pre_bigram_index[i].index = int.from_bytes(readValue, 'little')
                if readValue:
                    pre_bigram_index_count+=1
                else:
                    break
            except:
                break
        r.close()
        return pre_bigram_total, pre_bigram_index_count

    def read_pre_trigram_corpus(self, pre_trigram, pre_trigram_index):
        FILE_NAME = os.path.join(self.appPath,"pre_trigram.bin")
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return

        r = open(FILE_NAME, 'rb')
        pre_trigram_total = int.from_bytes(r.read(4), 'little')
        for i in range(0, pre_trigram_total):
            rawBytes = r.read(len(pre_trigram[i].first_word))
            for j, byte in enumerate(rawBytes):
                pre_trigram[i].first_word[j] = byte

            rawBytes = r.read(len(pre_trigram[i].second_word))
            for j, byte in enumerate(rawBytes):
                pre_trigram[i].second_word[j] = byte

            rawBytes = r.read(len(pre_trigram[i].third_word))
            for j, byte in enumerate(rawBytes):
                pre_trigram[i].third_word[j] = byte

            pre_trigram[i].freq = int.from_bytes(r.read(4), 'little')

        r.close()

        FILE_NAME = os.path.join(self.appPath,"pre_normal_trigram.bin")
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return

        r = open(FILE_NAME, 'rb')
        pre_trigram_index_count = int.from_bytes(r.read(4), 'little')
        pre_trigram_index_count=0
        for i in range(0, pre_trigram_total):
            try:
                rawBytes = r.read(len(pre_trigram_index[i].normalised_word))
                for j, byte in enumerate(rawBytes):
                    pre_trigram_index[i].normalised_word[j] = byte
                readValue=r.read(4)
                pre_trigram_index[i].index = int.from_bytes(readValue, 'little')
                if readValue:
                    pre_trigram_index_count += 1
                else:
                    break
            except:
                break

        r.close()
        return pre_trigram_total,pre_trigram_index_count

    def read_mid_trigram_corpus(self, mid_trigram, mid_trigram_index ):
        pre_count = 0
        corpus_word=[0]*200
        freq=[0]*8
        word=[0]*20

        FILE_NAME = os.path.join(self.appPath,"mid_trigram.bin")
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return

        r = open(FILE_NAME, 'rb')
        mid_trigram_total = int.from_bytes(r.read(4), 'little')
        for i in range(0, mid_trigram_total):

            rawBytes = r.read(len(mid_trigram[i].first_word))
            for j, byte in enumerate(rawBytes):
                mid_trigram[i].first_word[j] = byte

            rawBytes = r.read(len(mid_trigram[i].second_word))
            for j, byte in enumerate(rawBytes):
                mid_trigram[i].second_word[j] = byte

            rawBytes = r.read(len(mid_trigram[i].third_word))
            for j, byte in enumerate(rawBytes):
                mid_trigram[i].third_word[j] = byte
            mid_trigram[i].freq = int.from_bytes(r.read(4), 'little')
        r.close()

        FILE_NAME = os.path.join(self.appPath,"mid_normal_trigram.bin")
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return

        r = open(FILE_NAME, 'rb')
        mid_trigram_index_count = int.from_bytes(r.read(4), 'little')
        mid_trigram_index_count = 0

        for i in range(0, mid_trigram_total):
            try:
                rawBytes = r.read(len(mid_trigram_index[i].normalised_word))
                for j, byte in enumerate(rawBytes):
                    mid_trigram_index[i].normalised_word[j] = byte
                readValue=r.read(4)
                mid_trigram_index[i].index = int.from_bytes(readValue, 'little')
                if readValue:
                    mid_trigram_index_count += 1
                else:
                    break

            except:
                break
        r.close()
        return mid_trigram_total, mid_trigram_index_count

    def read_post_bigram_corpus(self, post_bigram, post_bigram_index ):

        post_count = 0
        corpus_word = [0] * 200
        freq = [0] * 8
        word = [0] * 20

        word[0] = 0
        FILE_NAME = os.path.join(self.appPath,"post_bigram.bin")
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return

        r = open(FILE_NAME, 'rb')
        post_bigram_total = int.from_bytes(r.read(4), 'little')
        for i in range(0, post_bigram_total):

            rawBytes = r.read(len(post_bigram[i].first_word))
            for j, byte in enumerate(rawBytes):
                post_bigram[i].first_word[j] = byte

            rawBytes = r.read(len(post_bigram[i].second_word))
            for j, byte in enumerate(rawBytes):
                post_bigram[i].second_word[j] = byte

            post_bigram[i].freq = int.from_bytes(r.read(4), 'little')
            post_bigram[i].unigram_freq = int.from_bytes(r.read(4), 'little')

        r.close()

        FILE_NAME = os.path.join(self.appPath,"post_normal_bigram.bin")
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return

        r = open(FILE_NAME, 'rb')
        post_bigram_index_count = int.from_bytes(r.read(4), 'little')
        post_bigram_index_count = 0

        for i in range(0, post_bigram_total):
            try:
                rawBytes = r.read(len(post_bigram_index[i].normalised_word))
                for j, byte in enumerate(rawBytes):
                    post_bigram_index[i].normalised_word[j] = byte
                readValue=r.read(4)
                post_bigram_index[i].index = int.from_bytes(readValue, 'little')
                if readValue:
                    post_bigram_index_count += 1
                else:
                    break
            except:
                break

        r.close()
        return  post_bigram_total,post_bigram_index_count

    def read_post_trigram_corpus(self, post_trigram, post_trigram_index):
        pre_count = 0
        corpus_word=[0]*200
        freq=[0]*8
        word=[0]*20
        word[0] = 0
        FILE_NAME = os.path.join(self.appPath,"post_trigram.bin")
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return 0,0

        r = open(FILE_NAME, 'rb')
        post_trigram_total = int.from_bytes(r.read(4), 'little')
        for i in range(0, post_trigram_total):
            rawBytes = r.read(len(post_trigram[i].first_word))
            for j,byte in enumerate(rawBytes):
                post_trigram[i].first_word[j] = byte

            rawBytes = r.read(len(post_trigram[i].second_word))
            for j, byte in enumerate(rawBytes):
                post_trigram[i].second_word[j] = byte

            rawBytes = r.read(len(post_trigram[i].third_word))
            for j, byte in enumerate(rawBytes):
                post_trigram[i].third_word[j] = byte

            post_trigram[i].freq = int.from_bytes(r.read(4), 'little')

        r.close()
        FILE_NAME = os.path.join(self.appPath,"post_normal_trigram.bin")
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return 0,0

        r = open(FILE_NAME, 'rb')
        post_trigram_index_count = int.from_bytes(r.read(4), 'little')
        post_trigram_index_count = 0
        for i in range(0, post_trigram_total):
            try:
                rawBytes = r.read(len(post_trigram_index[i].normalised_word))
                for j, byte in enumerate(rawBytes):
                    post_trigram_index[i].normalised_word[j] = byte
                readValue=r.read(4)
                post_trigram_index[i].index = int.from_bytes(readValue, 'little')
                if readValue:
                    post_trigram_index_count += 1
                else:
                    break
            except:
                break
        return post_trigram_total,post_trigram_index_count

    def read_urdu_punjabi_dict(self):

        FILE_NAME = os.path.join(self.appPath,"dict.bin")

        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return

        r = open(FILE_NAME, 'rb')
        self.dict_word_count = int.from_bytes(r.read(4), 'little')
        for i in range(0, self.dict_word_count):
            rawBytes = r.read(len(self.urdu_dict[i]))
            for j,byte in enumerate(rawBytes):
                self.urdu_dict[i][j] = byte

            rawBytes = r.read(len(self.roman_dict[i]))
            for j,byte in enumerate(rawBytes):
                self.roman_dict[i][j] = byte
        r.close()
        self.isDic = True

    def read_urdu_bigram(self):
        FILE_NAME = os.path.join(self.appPath,"BigramUrdu.bin")
        
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return

        r = open(FILE_NAME, 'rb')
        self.urdu_bigram_total = int.from_bytes(r.read(4), 'little')

        for  i in range(0,self.urdu_bigram_total):
            rawBytes = r.read(len(self.urdu_bigram[i].urdu1))
            for j, byte in enumerate(rawBytes):
                self.urdu_bigram[i].urdu1[j] = byte

            rawBytes = r.read(len(self.urdu_bigram[i].urdu2))
            for j, byte in enumerate(rawBytes):
                self.urdu_bigram[i].urdu2[j] = byte

            rawBytes = r.read(len(self.urdu_bigram[i].punjabi))
            for j, byte in enumerate(rawBytes):
                self.urdu_bigram[i].punjabi[j] = byte

        r.close()
    
    def read_noon_freq(self):
        FILE_NAME = os.path.join(self.appPath,"noon.bin")
        
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return

        r = open(FILE_NAME, 'rb')             
        for  i in range(0,120):
            for  j in range(0,120):
                row = int.from_bytes(r.read(1), 'little')
                col = int.from_bytes(r.read(1), 'little')
                corpus_word = int.from_bytes(r.read(1), 'little')
                self.noon_freq[row][col] = corpus_word
        r.close()
				
    def get_corpus_pos(self, corpus_words, count, punjabi_word):
        for  i in range(count - 1,-1,-1):
            if  self.strcmp(corpus_words[i].normalised_word, punjabi_word) <= 0:
                return i
        return 0

    def search_corpus(self, corpus_words, total, punjabi_word):
        high = total - 1
        low = 0
        mid = 0
        read_word=[0]*16
        while  low <= high:
            mid = int((low + high) / 2)
            self.strcpy(read_word, corpus_words[mid].normalised_word)
            if  not(self.strcmp(read_word, punjabi_word) != 0):
                return mid
            if  self.strcmp(read_word, punjabi_word) < 0:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def search_ignore_word_list(self, word):
        high = self.ignore_word_count - 1
        low = 0
        mid = 0
        read_word=[0]*16
        while  low <= high:
            mid = int((low + high) / 2)
            self.strcpy(read_word, self.ignore[mid])
            if  not(self.strcmp(read_word, word) != 0):
                return mid
            if  self.strcmp(read_word, word) < 0:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def search_avoid_prefix(self, word, word_size):
        high = self.prefix_word_count - 1
        low = 0
        mid = 0
        read_word=[0]*16
        temp=[0]*16
        self.UnicodeTo8(word, word_size, temp)
        while  low <= high:
            mid = int((low + high) / 2)
            self.strcpy(read_word,self.prefix[mid])
            if  not(self.strcmp(read_word, temp) != 0):
                return mid + 1
            if  self.strcmp(read_word, temp) < 0:
                low = mid + 1
            else:
                high = mid - 1
        return 0

    def search_suffix(self, word, word_size):
        high = self.suffix_word_count - 1
        low = 0
        mid = 0
        read_word=[0]*16
        temp=[0]*16
        self.UnicodeTo8(word, word_size, temp)
        while  low <= high:
            mid = int((low + high) / 2)
            self.strcpy(read_word, self.suffix[mid])
            if  not(self.strcmp(read_word, temp) != 0):
                return mid + 1
            if  self.strcmp(read_word, temp) < 0:
                low = mid + 1
            else:
                high = mid - 1
        return 0

    def merge_words_corpus_struct(self, corpus_words, corpus_word_count, punjabi_words, word_count):
        punjabi_word=[0]*16
        punjabi_int = [0]*16
        for  i in range(0,word_count):
            found = 0
            for  j in range(0,self.corpus_word_count):
                if  not(self.strcmp(corpus_words[j].original_word, punjabi_words[i]) != 0):
                    found = 1
                    break
            if  not(found != 0):
                for  k in range(0,self.strlen(punjabi_words[i])):
                    punjabi_int[k] = punjabi_words[i][k]
                self.normalise_punjabi_word(punjabi_int, self.strlen(punjabi_words[i]), punjabi_word)
                j = self.corpus_word_count
                self.strcpy(corpus_words[j].original_word, punjabi_words[i])
                self.strcpy(corpus_words[j].normalised_word, punjabi_word)
                self.corpus_word_count+=1
        return 0

    def generate_words(self, punjabi, size, punjabi_words, word_count):
        ptr = 0
        punjabi_ptr = 0
        flag = 0
        punjabi_word=[0]*16
        punjabi_word_size = 0
        word_count = 0
        if  not(punjabi_word_size != 0):
            for  i in range(0,15):
                punjabi_word[i] = 0
        while  punjabi_ptr < size:
            ch = punjabi[punjabi_ptr]
            ch1 = punjabi[punjabi_ptr + 1]
            if  flag > 0 or self.check_punjabi_punctuation(ch, ch1) > 0:
                if  punjabi_word_size > 0:
                    for  i in range(0,punjabi_word_size+1):
                        punjabi_words[word_count][i] = punjabi_word[i]
                    word_count+=1
                    punjabi_word_size = 0
                    for  i in range(0,15):
                        punjabi_word[i] = 0
                    flag = 0
            else:
                punjabi_word[punjabi_word_size] = ch
                punjabi_word_size+=1
                if  punjabi_word_size > 13: flag = 1
            punjabi_ptr += 2
        return 0

    def get_freq_corpus(self, punjabi_int, punjabi_int_size, corpus_pos):
        multi = 0
        punjabi_word=[0]*30
        first_punjabi_word=[0]*30
        rest_punjabi_word=[0]*30
        self.normalise_punjabi_word(punjabi_int, punjabi_int_size, punjabi_word)
        multi =self.break_word_for_corpus (punjabi_word, first_punjabi_word, rest_punjabi_word)
        if  multi > 0:
            self.normalise_punjabi_word(punjabi_int, multi, first_punjabi_word)
        pos = self.search_corpus(self.corpus_words, self.corpus_word_count, first_punjabi_word)
        if  pos < 0: return 0
        corpus_pos = pos
        low = high = pos
        return self.corpus_words[pos].freq

    def get_word_corpus(self, punjabi_int, punjabi_int_size, final_word):
        multi = 0
        punjabi_word=[0]*30
        first_punjabi_word=[0]*30
        rest_punjabi_word=[0]*30
        final_word[0] = 0
        self.normalise_punjabi_word(punjabi_int, punjabi_int_size, punjabi_word)
        multi = self.break_word_for_corpus(punjabi_word, first_punjabi_word, rest_punjabi_word)
        if  multi > 0:
            self.normalise_punjabi_word(punjabi_int, multi, first_punjabi_word)
        pos = self.search_corpus(self.corpus_words, self.corpus_word_count, first_punjabi_word)
        if  pos < 0: return punjabi_int_size,0
        self.strcpy(final_word, self.corpus_words[pos].original_word)
        if  multi > 0:
            self.strcat(final_word, rest_punjabi_word)
        return punjabi_int_size, 1

    def check_punjabi_corpus(self, punjabi_int, punjabi_int_size, final_word):
        # print('\t\t\t\t\t inside check_punjabi_corpus() function\n')
        multi = 0
        punjabi_word=[0]*30
        first_punjabi_word=[0]*30
        rest_punjabi_word=[0]*30
        self.normalise_punjabi_word(punjabi_int, punjabi_int_size, punjabi_word)
        multi = self.break_word_for_corpus(punjabi_word, first_punjabi_word, rest_punjabi_word)
        if  multi > 0:
            self.normalise_punjabi_word(punjabi_int, multi, first_punjabi_word)
        pos = self.search_corpus(self.corpus_words, self.corpus_word_count, first_punjabi_word)
        if  pos < 0: return punjabi_int_size, 0
        low = high = pos
        self.strcpy(final_word, self.corpus_words[pos].original_word)
        if  multi > 0:
            self.strcat(final_word, rest_punjabi_word)
        return punjabi_int_size, self.corpus_words[pos].freq

    def check_urdu_corpus(self, urdu1, urdu_size):
        low = 0
        high = self.urdu_corpus_word_count - 1
        read_word=[0]*25
        self.urdu=[0]*30
        self.UnicodeTo8(urdu1, urdu_size, self.urdu)
        while  low <= high:
            mid = int((low + high) / 2)
            self.strcpy(read_word, self.urdu_corpus_words[mid].original_word)
            if  not(self.strcmp(read_word, self.urdu) != 0):
                return self.urdu_corpus_words[mid].freq
            if  self.strcmp(read_word, self.urdu) < 0:
                low = mid + 1
            else:
                high = mid - 1
        return 0

    def break_word_for_corpus(self, punjabi_word, first_punjabi_word, rest_punjabi_word):
        found=0
        for  i in range(0,self.strlen(punjabi_word)+1):
            if  punjabi_word[i] ==118:
                first_punjabi_word[i] = 0
                found = i
                break
            else:
                first_punjabi_word[i] = punjabi_word[i]
        if  found > 0:
            j=i
            for  i in range(i,self.strlen(punjabi_word)+1):
                if  punjabi_word[i] == 7:
                    rest_punjabi_word[i - j] = 15
                else:
                    rest_punjabi_word[i - j] = punjabi_word[i]
        return found

    def check_punjabi_matra(self, u):
        return (((u > 3) and (u <11)) or ((u >12) and (u <21)) or ((u >61) and (u <67)) or ((u >69) and (u <77)))

    def check_punjabi_diactric(self, u):
        return ((u >61) and (u <77))

    def split_and_check_word_latest(self, urdu, urdu_size, roman, roman_size):
        # print('\t\tinside split_and_check_word_latest() function\n')
        start = 0
        end = urdu_size - 1
        pos = [0]*6
        f_pos = [0]*6
        t_roman_size =[0]*6
        join_pt = [0]*20
        roman1=[0]*40
        p_urdu=[0]*40
        t_roman=[0]*6
        # print(f'\t\t\t\turdu_word before update: {urdu}\n')
        # print(f'\t\t\t\troman before update: {roman}\n')
        for  i in range(0,len(t_roman)):
            t_roman[i]=[0]*100
        roman_size1 = 0
        p_size = 0
        count = 0
        jcount = 0
        cflag = 0
        flag = 0
        freq = [0]*6
        total_freq = 4250000.0
        sp = [0]*6
        ep = [0]*6
        total = 0
        if  flag > 0:
            total_freq /= 7
        
        #part1
        if  urdu_size > 79:
            # print(f'split_word: {roman}\n')
            return 0

        #part 2
        for  i in range(0,urdu_size,2):
            if  (urdu[i] ==34) or (urdu[i] ==36) or (urdu[i] ==39) or (urdu[i] ==47) or (urdu[i] ==48) or (urdu[i] ==49) or (urdu[i] ==50) or (urdu[i] ==72) or (urdu[i] ==136) or (urdu[i] ==145) or (urdu[i] ==210):
                end = i + 1
                if  urdu[i + 2] ==80:
                    start = i + 4
                else:
                    start = i + 2
                p_size = 0
                for  j in range(i + 2,urdu_size):
                    p_urdu[p_size] = urdu[j]
                    p_size+=1
                # print(f'split_word: {p_urdu}\n')
                # S2G.shah_tokens_b2s(p_urdu)
                roman_size1,flag = self.check_urdu_word_bigram(p_urdu, urdu, p_size, start, roman1, roman_size1)   
                # print(f'flag:{flag}')
                if flag> 0:
                    total = 1
                    roman_size[0] = roman_size1
                    for  j in range(0,roman_size1):
                        roman[0][j] = roman1[j]
                    return 1

        #part 3
        jcount = 0
        for  i in range(0,20):
            join_pt[jcount] = -1
        jcount+=1
        for  i in range(0,urdu_size,2):
            if (((urdu[i] ==34) or (urdu[i] ==36) or (urdu[i] ==39) or (urdu[i] ==47) or (urdu[i] ==48) or (urdu[i] ==49) or (urdu[i] ==50) or (urdu[i] ==72) or (urdu[i] ==136) or (urdu[i] ==145) or (urdu[i] ==210) or (urdu[i] ==186)
                or (urdu[i] ==19) or (urdu[i] ==77) or (urdu[i] ==75) or (urdu[i] ==16)) and
                ((urdu[i + 2] != 186) and (urdu[i + 2] != 190) and (urdu[i + 2] != 33) and (urdu[i + 2] != 35) and (urdu[i + 2] != 36) and (urdu[i + 2] != 37) and (urdu[i + 2] != 38)
                  and (urdu[i + 2] !=41) and (urdu[i + 2] !=192) and (urdu[i + 2] !=81) and (urdu[i + 2] !=17) and (urdu[i + 2] !=3) and (urdu[i + 2] !=213) and (urdu[i + 2] !=117) and (urdu[i + 2] !=118) and (urdu[i + 2] !=190) and (urdu[i + 2] !=210))):
                join_pt[jcount] = i + 1
                jcount+=1
                if  urdu[i + 2] ==80:
                    join_pt[jcount - 1] += 2
                if  jcount > 16: 
                    # print(f'joint count: {jcount}\n')
                    return 0


        #part 4
        if  join_pt[jcount - 1] != urdu_size - 1:
            # print('1\n')
            join_pt[jcount] = urdu_size - 1
            jcount+=1
        max_freq = 0
        if  flag > 0:
            # print('2\n')
            total_freq = urdu_size
        if  jcount == 12:
            # print('3\n')
            max_freq = 0
       
        pos[0] = 0
        sp[0] = join_pt[pos[0]] + 1

        while pos[0] < jcount - 1:
            # print('4\n')
            ep[0] = join_pt[pos[0] + 1]
            # print(f'urdu 1: {urdu}\n')
            t_roman_size[0],freq[0] = self.check_freq_corpus(urdu,  sp[0],  ep[0],  t_roman[0], t_roman_size[0],  flag)
            # print(f't_roman_size: {t_roman_size}\n')
            if  freq[0] == 0:
                # print('5\n')
                pos[0]+=1
                continue
            if  flag > 0:
                # print('6\n')
                freq[0] = ep[0] - sp[0] + 1
            if  flag == 2:
                # print('7\n')
                freq[0] = freq[0] * freq[0]
            if  freq[0] == -1:
                # print('8\n')
                freq[0] = 1
            else:
                # print('9\n')
                freq[0] = freq[0] / total_freq
            if  ep[0] >= urdu_size - 1:
                # print('10\n')
                cfreq = freq[0]
                if  cfreq > max_freq:
                    # print('11\n')
                    total = 1
                    for  i in range(0,1):
                        roman_size[i] = t_roman_size[i]
                        for  j in range(0,roman_size[i]):
                            roman[i][j] = t_roman[i][j]
                    max_freq = cfreq
                    for  i in range(0,6):
                        f_pos[i] = pos[i]
            pos[1] = pos[0] + 1
            sp[1] = join_pt[pos[1]] + 1
            freq[1] = 1
            while pos[1] < jcount - 1:

                ep[1] = join_pt[pos[1] + 1]
                # print(f'urdu 1: {urdu}\n')
                t_roman_size[1],freq[1] = self.check_freq_corpus(urdu,  sp[1],  ep[1],  t_roman[1],  t_roman_size[1], flag)
                # print(f't_roman_size: {t_roman_size}\n')
                if  freq[1] == 0:
                    # print('12\n')
                    pos[1]+=1
                    continue
                if  flag > 0:
                    # print('13\n')
                    freq[1] = ep[1] - sp[1] + 1
                if  flag == 2:
                    # print('14\n')
                    freq[1] = freq[1] * freq[1]
                if  freq[1] == -1:
                    # print('15\n')
                    freq[1] = 1
                else:
                    # print('16\n')
                    freq[1] = freq[1] / total_freq
                if  ep[1] >= urdu_size - 1:
                    # print('17\n')
                    cfreq = 1.0 * (freq[0] * freq[1])
                    if  flag == 2:
                        # print('18\n')
                        cfreq = 1.0 * (freq[0] + freq[1])
                    if  cfreq > max_freq:
                        # print('19\n')
                        total = 2
                        for  i in range(0,2):
                            roman_size[i] = t_roman_size[i]
                            for  j in range(0,roman_size[i]):
                                roman[i][j] = t_roman[i][j]
                        max_freq = cfreq
                        for  i in range(0,6):
                            f_pos[i] = pos[i]
                pos[2] = pos[1] + 1
                sp[2] = join_pt[pos[2]] + 1
                freq[2] = 1
                while pos[2] < jcount - 1:
                    # print(f'urdu 2: {urdu}\n')
                    ep[2] = join_pt[pos[2] + 1]
                    t_roman_size[2],freq[2] = self.check_freq_corpus(urdu,  sp[2],  ep[2],  t_roman[2],  t_roman_size[2],flag)
                    # print(f't_roman_size: {t_roman_size}\n')
                    if  freq[2] == 0:
                        # print('20\n')
                        pos[2]+=1
                        continue
                    if  flag > 0:
                        # print('21\n')
                        freq[2] = ep[2] - sp[2] + 1
                    if  flag == 2:
                        # print('22\n')
                        freq[2] = freq[2] * freq[2]
                    if  freq[2] == -1:
                        # print('23\n')
                        freq[2] = 1
                    else:
                        # print('24\n')
                        freq[2] = freq[2] / total_freq
                    if  ep[2] >= urdu_size - 1:
                        # print('25\n')
                        cfreq = 1.0 * (freq[0] * freq[1] * freq[2])
                        if  flag == 2:
                            # print('26\n')
                            cfreq = 1.0 * (freq[0] + freq[1] + freq[2])
                        if  cfreq > max_freq:
                            # print('27\n')
                            total = 3
                            for  i in range(0,3):
                                roman_size[i] = t_roman_size[i]
                                for  j in range(0,roman_size[i]):
                                    roman[i][j] = t_roman[i][j]
                            max_freq = cfreq
                    pos[3] = pos[2] + 1
                    sp[3] = join_pt[pos[3]] + 1
                    freq[3] = 1
                    while pos[3] < jcount - 1:
                        # print(f'urdu 3: {urdu}\n')
                        ep[3] = join_pt[pos[3] + 1]
                        t_roman_size[3],freq[3] = self.check_freq_corpus(urdu,  sp[3],  ep[3],  t_roman[3],  t_roman_size[3],flag)
                        # print(f't_roman_size: {t_roman_size}\n')
                        if  freq[3] == 0:
                            # print('28\n')
                            pos[3]+=1
                            continue
                        if  flag > 0:
                            # print('29\n')
                            freq[3] = ep[3] - sp[3] + 1
                        if  flag == 2:
                            # print('30\n')
                            freq[3] = freq[3] * freq[3]
                        if  freq[3] == -1:
                            # print('31\n')
                            freq[3] = 1
                        else:
                            # print('32\n')
                            freq[3] = freq[3] / total_freq
                        if  ep[3] >= urdu_size - 1:
                            # print('33\n')
                            cfreq = 1.0 * (freq[0] * freq[1] * freq[2] * freq[3])
                            if  flag == 2:
                                # print('34\n')
                                cfreq = 1.0 * (freq[0] + freq[1] + freq[2] + freq[3])
                            if  cfreq > max_freq:
                                # print('35\n')
                                max_freq = cfreq
                                total = 4
                                for  i in range(0,4):
                                    roman_size[i] = t_roman_size[i]
                                    for  j in range(0,roman_size[i]):
                                        roman[i][j] = t_roman[i][j]
                        pos[4] = pos[3] + 1
                        sp[4] = join_pt[pos[4]] + 1
                        freq[4] = freq[5] = 1
                        while pos[4] < jcount - 1:
                            # print(f'urdu 3: {urdu}\n')
                            ep[4] = join_pt[pos[4] + 1]
                            t_roman_size[4], freq[4] = self.check_freq_corpus(urdu,  sp[4],  ep[4],  t_roman[4],  t_roman_size[4],flag)
                            # print(f't_roman_size: {t_roman_size}\n')
                            if  freq[4] == 0:
                                # print('36\n')
                                pos[4]+=1
                                continue
                            if  flag > 0:
                                # print('37\n')
                                freq[4] = ep[4] - sp[4] + 1
                            if  flag == 2:
                                # print('38\n')
                                freq[4] = freq[4] * freq[4]
                            if  freq[4] == -1:
                                # print('39\n')
                                freq[4] = 1
                            else:
                                # print('40\n')
                                freq[4] = freq[4] / total_freq
                            if  ep[4] >= urdu_size - 1:
                                # print('41\n')
                                cfreq = 1.0 * (freq[0] * freq[1] * freq[2] * freq[3] * freq[4])
                                if  flag == 2:
                                    # print('42\n')
                                    cfreq = 1.0 * (freq[0] + freq[1] + freq[2] + freq[3] + freq[4])
                                if  cfreq > max_freq:
                                    # print('43\n')
                                    total = 5
                                    max_freq = cfreq
                                    roman_size[4] = roman_size1
                                    for  i in range(0,5):
                                        roman_size[i] = t_roman_size[i]
                                        for  j in range(0,roman_size[i]):
                                            roman[i][j] = t_roman[i][j]
                            pos[5] = pos[4] + 1
                            if  pos[5] >= jcount - 1:
                                # print('44\n')
                                freq[5] = 1
                                j = 0
                            else:
                                # print('45\n')
                                sp[5] = join_pt[pos[5]] + 1
                                ep[5] = join_pt[jcount - 1]
                                t_roman_size[5],freq[5] = self.check_freq_corpus(urdu,  sp[5],  ep[5],  t_roman[5],t_roman_size[5],  flag)
                                if  flag > 0:
                                    # print('46\n')
                                    freq[5] = ep[5] - sp[5] + 1
                                if  flag == 2:
                                    # print('47\n')
                                    freq[5] = freq[5] * freq[5]
                                if  freq[5] == -1:
                                    # print('48\n')
                                    freq[5] = 1
                                    j = 0
                                else:
                                    # print('49\n')
                                    freq[5] = freq[5] / total_freq
                                    j = 1
                            cfreq = 1.0 * (freq[0] * freq[1] * freq[2] * freq[3] * freq[4] * freq[5])
                            if  flag == 2:
                                # print('50\n')
                                cfreq = 1.0 * (freq[0] + freq[1] + freq[2] + freq[3] + freq[4] + freq[5])
                            if  cfreq > max_freq:
                                # print('51\n')
                                max_freq = cfreq
                                if  j > 1:
                                    # print('52\n')
                                    j = 1
                                total = 5 + j
                                roman_size[5] = roman_size1
                                for  i in range(0,6):
                                    roman_size[i] = t_roman_size[i]
                                    for  j in range(0,roman_size[i]):
                                        roman[i][j] = t_roman[i][j]
                            pos[4]+=1
                        pos[3]+=1
                    pos[2]+=1
                pos[1]+=1
            pos[0]+=1
            
            # print(f'split_word: {roman}\n')
            
        if  total > 1:
            self.merged_word_count+=1
            self.total_joint += (jcount - 1)
            if (self.max_joint < (jcount - 1)):
                max_joint= jcount - 1
            self.average_joint_count = (1.0 * self.total_joint) / self.merged_word_count
        # print(f'total: {total}\n')
        return total

    def check_freq_corpus(self, urdu, start, end, punjabi, punjabi_size, flag):
        full = 0
        urdu_size = end - start + 1
        urdu1=[0]*80
        final_word=[0]*80
        normalise=[0]*80
        urdu2=[0]*30
        urdu_ptr = 0
        roman_ptr = 0
        urdu_int_ptr = 0
        urdu_int = [0]*128
        punjabi_int = [0]*128
        punjabi_int_size = 0
        if  start >= end: return punjabi_size,-1
        if  (urdu_size <= 2) and (urdu[start] !=34):
            return punjabi_size,0
        j= k = 0

        for  i in range(start, end+1):
            urdu1[j] = urdu[i]
            j+=1
            if  (i % 2) > 0: continue
            urdu2[k] = urdu[i]
            k+=1
        urdu2[k] = 0
        k+=1
        if  flag > 0:
            freq,flag_returned = self.check_urdu_corpus(urdu1, urdu_size)
            if  flag_returned > 0:
                punjabi_size,flag_returned=self.check_urdu_word_dictionary(urdu1,  urdu_size,  punjabi, punjabi_size)
                if  flag_returned > 0:
                    return punjabi_size,freq
                urdu_int_ptr = 0
                while  urdu_ptr < urdu_size:
                    ch = urdu1[urdu_ptr]
                    ch1 = urdu1[urdu_ptr + 1]
                    int1 = ch1
                    int1 <<= 8
                    int1 += ch
                    urdu_ptr += 2
                    urdu_int[urdu_int_ptr] = int1
                    urdu_int_ptr+=1
                punjabi_int_size=self.rule_based_urdu_word_to_punjabi(urdu_int,  int(urdu_size / 2),  punjabi_int)
                punjabi_int_size=self.improve_punjabi_word(punjabi_int,punjabi_int_size)
                punjabi_int_size,j = self.check_punjabi_corpus(punjabi_int, punjabi_int_size, final_word)
                self.check_urdu_nukta_dictionary(urdu1, urdu_size, final_word)
                if  not(j != 0):
                    punjabi_size = 0
                    for  i in range(0,punjabi_int_size):
                        punjabi[(punjabi_size)] = punjabi_int[i]
                        punjabi_size+=1
                        punjabi[punjabi_size] = 10
                        punjabi_size+=1
                    return punjabi_size,freq
                else:
                    punjabi_size = 0
                    self.check_urdu_nukta_dictionary(urdu1, urdu_size, final_word)
                    for  i in range(0,self.strlen(final_word)):
                        if  final_word[i] ==118:
                            punjabi[punjabi_size] = ord('-')
                            punjabi_size+=1
                            punjabi[punjabi_size] = 0
                            punjabi_size+=1
                            continue
                        punjabi[(punjabi_size)] = final_word[i]
                        punjabi_size+=1
                        punjabi[(punjabi_size)] = 10
                        punjabi_size+=1
                    return punjabi_size,freq
            else:
                return punjabi_size,0
        if  self.search_ignore_word_list(urdu2) >= 0:
            return punjabi_size,0
        original_size = urdu_size
        for  k in range(0,urdu_size-2,2):
            if  (k > 0) and (urdu1[k] ==210) and (urdu1[k - 2] !=38): 
                urdu1[k] =204
        for  k in range(0,23+1):
            urdu_size = original_size
            full = 0
            if  k == 1:
                if  (urdu_size > 9) and (urdu1[urdu_size - 2] ==186) and ((urdu1[urdu_size - 4] ==36) or (urdu1[urdu_size - 4] ==72)) and (urdu1[urdu_size - 6] ==204) and (urdu1[urdu_size - 8] !=38):
                    if  urdu1[urdu_size - 4] ==36: full = 1
                    urdu_size -= 4
                else:
                    continue
            if  k == 2:
                if  (urdu_size > 9) and (urdu1[urdu_size - 2] ==186) and ((urdu1[urdu_size - 4] ==36) or (urdu1[urdu_size - 4] ==72)) and (urdu1[urdu_size - 6] ==204):
                    if  urdu1[urdu_size - 8] ==38:
                        full = 1
                        urdu_size += 2
                    urdu_size -= 6
                else:
                    continue
            if  k == 3:  
                if  (urdu_size > 7) and (urdu1[urdu_size - 2] ==186) and ((urdu1[urdu_size - 4] ==39) and (urdu1[urdu_size - 6] ==72)):
                    urdu_size -= 6
                else:
                    continue
            if  k == 4:  
                if  (urdu_size > 13) and (urdu1[urdu_size - 2] ==210) and (urdu1[urdu_size - 4] ==47) and (urdu1[urdu_size - 6] ==70) and (urdu1[urdu_size - 8] ==72):
                    if  urdu1[urdu_size - 10] ==38:
                        if  urdu1[urdu_size - 12] ==39:
                            full = 1
                            urdu_size -= 2
                        urdu_size -= 10
                    else:
                        if  urdu1[urdu_size - 10] ==39:
                            full = 1
                            urdu_size -= 2
                        urdu_size -= 8
                else:
                    continue
            if  k == 5:  
                if  (urdu_size > 9) and (urdu1[urdu_size - 2] ==186) and (urdu1[urdu_size - 4] ==39) and (urdu1[urdu_size - 6] ==204) and (urdu1[urdu_size - 8] !=38):
                    if  urdu1[urdu_size - 4] ==36:
                        full = 1
                    urdu_size -= 4
                else:
                    continue
            if  k == 6:
                if  (urdu_size > 9) and (urdu1[urdu_size - 2] ==50):  
                    urdu_size -= 2
                else:
                    continue
            if  k == 7:
                if  (urdu_size > 9) and (urdu1[urdu_size - 2] ==51):  
                    urdu_size -= 2
                else:
                    continue
            if  k == 8:
                if  (urdu_size > 9) and (urdu1[urdu_size - 2] ==70) and (urdu1[urdu_size - 4] ==72) and (urdu1[urdu_size - 6] ==38) and (urdu1[urdu_size - 8] ==39):  
                    urdu_size -= 8
                else:
                    continue
            if  k == 9:
                if  (urdu_size > 7) and (urdu1[urdu_size - 2] ==39) and (urdu1[urdu_size - 4] ==70):  
                    urdu_size -= 4
                else:
                    continue
            if  k == 10:
                if  (urdu_size > 7) and (urdu1[urdu_size - 2] ==210) and (urdu1[urdu_size - 4] ==72):  
                    urdu_size -= 4
                else:
                    continue
            if  k == 11:
                if  (urdu_size > 7) and (urdu1[urdu_size - 2] ==70) and (urdu1[urdu_size - 4] ==72): 
                    urdu_size -= 4
                else:
                    continue
            if  k == 12:
                if  (urdu_size > 7) and (urdu1[urdu_size - 2] ==204) and (urdu1[urdu_size - 4] ==42):  
                    urdu_size -= 4
                else:
                    continue
            if  k == 13:
                if  (urdu_size > 7) and (urdu1[urdu_size - 2] ==204) and (urdu1[urdu_size - 4] ==70):  
                    urdu_size -= 4
                else:
                    continue
            if  k == 14:
                if  (urdu_size > 7) and (urdu1[urdu_size - 2] ==39) and (urdu1[urdu_size - 4] ==72):  
                    urdu_size -= 4
                else:
                    continue
            if  k == 15:
                if  (urdu_size > 7) and (urdu1[urdu_size - 2] ==70) and (urdu1[urdu_size - 4] ==126):  
                    urdu_size -= 4
                else:
                    continue
            if  k == 16:
                if  (urdu_size > 9) and (urdu1[urdu_size - 2] ==49) and (urdu1[urdu_size - 4] ==39) and (urdu1[urdu_size - 6] ==47):  
                    urdu_size -= 6
                else:
                    continue
            if  k == 17:
                if  (urdu_size > 7) and (urdu1[urdu_size - 4] ==193) and (urdu1[urdu_size - 2] ==121):  
                    urdu_size -= 4
                else:
                    continue
            if  k == 18:
                if  (urdu_size > 7) and (urdu1[urdu_size - 4] ==175) and (urdu1[urdu_size - 2] ==39):  
                    urdu_size -= 4
                else:
                    continue
            if  k == 19:
                if  (urdu_size > 7) and (urdu1[urdu_size - 4] ==175) and (urdu1[urdu_size - 2] ==204):  
                    urdu_size -= 4
                else:
                    continue
            if  k == 20:
                if  (urdu_size > 7) and (urdu1[urdu_size - 4] ==175) and (urdu1[urdu_size - 2] ==210):  
                    urdu_size -= 4
                else:
                    continue
            if  k == 21:  
                if  (urdu_size > 9) and (urdu1[urdu_size - 8] !=38) and (urdu1[urdu_size - 6] ==210) and (urdu1[urdu_size - 4] ==39) and (urdu1[urdu_size - 2] ==186):
                    urdu1[urdu_size - 6] =39
                    urdu_size -= 4
                else:
                    continue
            if  k == 22:  
                if  (urdu_size > 9) and (urdu1[urdu_size - 8] ==38) and (urdu1[urdu_size - 6] ==210) and (urdu1[urdu_size - 4] ==39) and (urdu1[urdu_size - 2] ==186):
                    urdu1[urdu_size - 6] =204
                    full = 1
                    urdu_size -= 4
                else:
                    continue
            if  k == 23:  
                if  (urdu_size > 7) and (urdu1[urdu_size - 2] ==186) and (urdu1[urdu_size - 4] ==39):
                    if  urdu1[urdu_size - 6] ==38: full = 1
                    urdu_size -= 4
                else:
                    continue
            punjabi_size,flag_returend=self.check_urdu_word_dictionary(urdu1,  urdu_size,  punjabi, punjabi_size) 
            if flag_returend> 0:
                if  k == 1:
                    punjabi_size -= 2
                    punjabi[(punjabi_size)] =63
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =19
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =2
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                if  k == 2:
                    if  full > 0:
                        punjabi_size -= 2
                        punjabi[(punjabi_size)] =7
                        punjabi_size+=1
                        punjabi[(punjabi_size)] = 10
                        punjabi_size+=1
                    punjabi[(punjabi_size)] =47
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =75
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =2
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                if  k == 3:
                    punjabi[(punjabi_size)] =53
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =62
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =2
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                if  k == 4:  
                    if  full > 0:
                        punjabi[(punjabi_size)] =62
                        punjabi_size+=1
                        punjabi[(punjabi_size)] = 10
                        punjabi_size+=1
                    punjabi[(punjabi_size)] =9
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =2
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =38
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =71
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                if  k == 5:
                    punjabi[(punjabi_size)] =6
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =2
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                if  k == 6:
                    punjabi[(punjabi_size)] =91
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                if  k == 7:
                    punjabi[(punjabi_size)] =56
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                if  k == 8:  
                    punjabi[(punjabi_size)] =62
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =9
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =35
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                if  k == 9:  
                    punjabi[(punjabi_size)] =40
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =62
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                if  k == 10:  
                    punjabi[(punjabi_size)] =53
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =71
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                if  k == 11:  
                    punjabi[(punjabi_size)] =9
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =35
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                if  k == 12:  
                    punjabi[(punjabi_size)] =36
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =64
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                if  k == 13:  
                    punjabi[(punjabi_size)] =40
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =64
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                if  k == 14:  
                    punjabi[(punjabi_size)] =53
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =62
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                if  k == 15:  
                    punjabi[(punjabi_size)] =42
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =40
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                if  k == 16:  
                    punjabi[(punjabi_size)] =38
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =62
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =48
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                if  k == 17:  
                    punjabi[(punjabi_size)] =57
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =31
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                if  k == 18:  
                    punjabi[(punjabi_size)] =23
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =62
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                if  k == 19:  
                    punjabi[(punjabi_size)] =23
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =64
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                if  k == 20:  
                    punjabi[(punjabi_size)] =23
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =71
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                if  k == 21:
                    punjabi_size -= 2
                    punjabi[(punjabi_size)] =63
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =6
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =2
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                if  (k == 22) or (k == 23):  
                    if  full > 0:
                        punjabi[(punjabi_size)] =6
                        punjabi_size+=1
                        punjabi[(punjabi_size)] = 10
                        punjabi_size+=1
                    else:
                        punjabi[(punjabi_size)] =62
                        punjabi_size+=1
                        punjabi[(punjabi_size)] = 10
                        punjabi_size+=1
                    punjabi[(punjabi_size)] =2
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                j = 0
                for  i in range(0,punjabi_size,2):
                    punjabi_int[j] = punjabi[i]
                    j+=1
                punjabi_int_size = int(punjabi_size / 2)
                punjabi_int_size,freq =self.check_punjabi_corpus(punjabi_int,punjabi_int_size,  final_word)
                self.check_urdu_nukta_dictionary(urdu1, urdu_size, final_word)
                self.improve_punjabi_word_matra(punjabi, punjabi_size)
                if  freq < 1: freq = 1
                return punjabi_size,freq
            urdu_ptr = urdu_int_ptr = 0
            while  urdu_ptr < urdu_size:
                ch = urdu1[urdu_ptr]
                ch1 = urdu1[urdu_ptr + 1]
                int1 = ch1
                int1 <<= 8
                int1 += ch
                urdu_ptr += 2
                urdu_int[urdu_int_ptr] = int1
                urdu_int_ptr+=1
            punjabi_int_size=self.rule_based_urdu_word_to_punjabi(urdu_int,  int(urdu_size / 2),  punjabi_int)
            punjabi_int_size=self.improve_punjabi_word(punjabi_int,punjabi_int_size)
            final_word[0] = 0
            punjabi_int_size,freq=self.check_punjabi_corpus(punjabi_int,punjabi_int_size,  final_word)
            if  (k == 0) and (freq < 5) and (self.strlen(final_word) < 5) and (original_size < 10):
                return punjabi_size,0
            if  (k == 0) and (original_size < 4):
                return punjabi_size,0
            if  freq > 0:
                punjabi_size = 0
                for  i in range(0,self.strlen(final_word)):
                    if  final_word[i] ==118:
                        punjabi[(punjabi_size)] = ord('-')
                        punjabi_size+=1
                        punjabi[(punjabi_size)] = 0
                        punjabi_size+=1
                        continue
                    if  (i > 0) and (final_word[i - 1] == 33) and (final_word[i] == 60):
                        continue
                    punjabi[(punjabi_size)] = final_word[i]
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                if  k == 1:
                    punjabi_size -= 2
                    punjabi[(punjabi_size)] =63
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =19
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =2
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    freq = 1
                if  k == 2:
                    if  full > 0:
                        punjabi_size -= 2
                        punjabi[(punjabi_size)] =8
                        punjabi_size+=1
                        punjabi[(punjabi_size)] = 10
                        punjabi_size+=1
                    punjabi[(punjabi_size)] =19
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =2
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    freq = 1
                if  k == 3:
                    punjabi[(punjabi_size)] =53
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =62
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =2
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    freq = 1
                if  k == 4:
                    if  full > 0:
                        punjabi[(punjabi_size)] =62
                        punjabi_size+=1
                        punjabi[(punjabi_size)] = 10
                        punjabi_size+=1
                    punjabi[(punjabi_size)] =9
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =2
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =38
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =71
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    freq = 1
                if  k == 5:
                    punjabi[(punjabi_size)] =6
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =2
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    freq = 1
                if  k == 6:
                    punjabi[(punjabi_size)] =91
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    freq = 1
                if  k == 7:
                    punjabi[(punjabi_size)] =56
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    freq = 1
                if  k == 8:  
                    punjabi[(punjabi_size)] =62
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =9
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =35
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    freq = 1
                if  k == 9:  
                    punjabi[(punjabi_size)] =40
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =62
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    freq = 1
                if  k == 10:  
                    punjabi[(punjabi_size)] =53
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =71
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    freq = 1
                if  k == 11:  
                    punjabi[(punjabi_size)] =9
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =35
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    freq = 1
                if  k == 12:  
                    punjabi[(punjabi_size)] =36
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =64
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    freq = 1
                if  k == 13:  
                    punjabi[(punjabi_size)] =40
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =64
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    freq = 1
                if  k == 14:  
                    punjabi[(punjabi_size)] =53
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =62
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    freq = 1
                if  k == 15:  
                    punjabi[(punjabi_size)] =42
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =40
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    freq = 1
                if  k == 16:  
                    punjabi[(punjabi_size)] =38
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =62
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =48
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    freq = 1
                if  k == 17:  
                    punjabi[(punjabi_size)] =57
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =31
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    freq = 1
                if  k == 18:  
                    punjabi[(punjabi_size)] =23
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =62
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    freq = 1
                if  k == 19:  
                    punjabi[(punjabi_size)] =23
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =64
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    freq = 1
                if  k == 20:  
                    punjabi[(punjabi_size)] =23
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =71
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    freq = 1
                if  k == 21:
                    punjabi_size -= 2
                    punjabi[(punjabi_size)] =63
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =6
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    punjabi[(punjabi_size)] =2
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    freq = 1
                if  (k == 22) or (k == 23):  
                    if  full > 0:
                        punjabi[(punjabi_size)] =6
                        punjabi_size+=1
                        punjabi[(punjabi_size)] = 10
                        punjabi_size+=1
                    else:
                        punjabi[(punjabi_size)] =62
                        punjabi_size+=1
                        punjabi[(punjabi_size)] = 10
                        punjabi_size+=1
                    punjabi[(punjabi_size)] =2
                    punjabi_size+=1
                    punjabi[(punjabi_size)] = 10
                    punjabi_size+=1
                    freq = 1
                self.improve_punjabi_word_matra(punjabi, punjabi_size)
                return punjabi_size, freq
        return punjabi_size, 0

    def get_word_freq_corpus(self, urdu, start, end, roman, roman_size):
        urdu_size = end - start + 1
        urdu1=[0]*50
        final_word=[0]*50
        urdu_ptr = 0
        roman_ptr = 0
        urdu_int_ptr = 0
        urdu_int = [0]*128
        punjabi_int = [0]*128
        punjabi_int_size = 0
        if  urdu_size <= 1: return -1
        if  start >= end: return -1
        j=0
        for  i in range(start,end+1):
            urdu1[j] = urdu[i]
            j+=1
        urdu_int_ptr = 0
        while  urdu_ptr < urdu_size:
            ch = urdu1[urdu_ptr]
            ch1 = urdu1[urdu_ptr + 1]
            int1 = ch1
            int1 <<= 8
            int1 += ch
            urdu_ptr += 2
            urdu_int[urdu_int_ptr] = int1
            urdu_int_ptr+=1
        punjabi_int_size=self.rule_based_urdu_word_to_punjabi(urdu_int,  int(urdu_size / 2),  punjabi_int)
        punjabi_int_size=self.improve_punjabi_word(punjabi_int,punjabi_int_size)
        punjabi_int_size=self.get_word_corpus(punjabi_int,punjabi_int_size,  final_word)
        roman_size = 0
        for  i in range(0,self.strlen(final_word)):
            if  final_word[i] ==118:
                roman[(roman_size)] = ord('-')
                roman_size+=1
                roman[(roman_size)] = 0
                roman_size+=1
                continue
            roman[(roman_size)] = final_word[i]
            roman_size+=1
            roman[(roman_size)] = 10
            roman_size+=1
        return 0

    def UnicodeToUtf8(self, UnicodeString, UnicodePos, szOut):
        len = 0
        j = 0
        uc1 = tunion()
        self.normalise_urdu(UnicodeString, UnicodePos)
        for  i in range(0,UnicodePos,2):
            uc1.uc[0] = UnicodeString[i]
            uc1.uc[1] = UnicodeString[i + 1]
            if  uc1.ui <128:
                szOut[j] = UnicodeString[i]
                j+=1
            elif  uc1.ui <2048:
                szOut[j] = 192 | ((uc1.ui) >> 6)
                j+=1
                szOut[j] = 128 | ((uc1.ui) & 63)
                j+=1
            else:
                szOut[j] = 224 | ((uc1.ui) >> 12)
                j+=1
                szOut[j] = 128 | (((uc1.ui) >> 6) & 63)
                j+=1
                szOut[j] = 128 | ((uc1.ui) & 63)
                j+=1
        szOut[j] = 0
        return

    def check_long_punjabi_matra(self, u):
        r = (((u > 3) and (u <11)) or ((u >12) and (u <21)) or (u ==62) or (u ==64) or (u ==66) or ((u >69) and (u <77)))
        if  r: return 1
        else: return 0

    def check_urdu_line_end(self, ch, ch1):
        # print('inside check_urdu_line_end() function\n')
        if  ch1 == 0:
            if  (ch == ord('.')) or (ch == ord('?')) or (ch == 0) or (ch == 10) or (ch == 13): return 1
        if  ch1 == 6:
            if  (ch ==31) or (ch ==212) or (ch ==64):
                return 1
        if  ch1 == 9:
            if  ch == 100:
                return 1
        return 0

    def search_word_pre_bigram(self, word, low, high, selected_word):
        read_word=[0]*20
        while  low <= high:
            mid = int((low + high) / 2)
            self.strcpy(read_word, self.pre_bigram[mid].second_word)
            if  not (self.strcmp(read_word, word) != 0):
                self.strcpy(selected_word, self.pre_bigram[mid].first_word)
                return (1.0 * self.pre_bigram[mid].freq / self.pre_bigram[mid].unigram_freq)
            if  self.strcmp(read_word, word) < 0:
                low = mid + 1
            else:
                high = mid - 1
        return 0

    def search_word_pre_trigram(self, word1, word2, low, high, selected_word):
        first = low
        last = high
        read_word=[0]*20
        while  low <= high:
            mid = int((low + high) / 2)
            self.strcpy(read_word, self.pre_trigram[mid].second_word)
            if  not(self.strcmp(read_word, word1) != 0):
                if  self.strcmp(self.pre_trigram[mid].third_word, word2) > 0:
                    dir = -1
                else: dir = +1
                while  not(self.strcmp(self.pre_trigram[mid].second_word, word1) != 0):
                    if  not(self.strcmp(self.pre_trigram[mid].third_word, word2) != 0):
                        self.strcpy(selected_word, self.pre_trigram[mid].first_word)
                        return self.pre_trigram[mid].freq
                    mid += dir
                    if  (mid < low) or (mid > high):
                        return 0
                    if  dir < 0:
                        if  self.strcmp(self.pre_trigram[mid].third_word, word2) < 0: return 0
                    if  dir > 0:
                        if  self.strcmp(self.pre_trigram[mid].third_word, word2) > 0: return 0
                return 0
            if  self.strcmp(read_word, word1) < 0:
                low = mid + 1
            else:
                high = mid - 1
        return 0

    def search_word_post_bigram(self, word, low, high, selected_word):
        read_word=[0]*20
        while  low <= high:
            mid = int((low + high) / 2)
            self.strcpy(read_word, self.post_bigram[mid].first_word)
            if  not(self.strcmp(read_word, word) != 0):
                self.strcpy(selected_word, self.post_bigram[mid].second_word)
                return ((1.0 * self.post_bigram[mid].freq) / self.post_bigram[mid].unigram_freq)
            if  self.strcmp(read_word, word) < 0:
                low = mid + 1
            else:
                high = mid - 1
        return 0

    def search_word_mid_trigram(self, word1, word2, low, high, selected_word):
        first = low
        last = high
        read_word=[0]*20
        while  low <= high:
            mid = int((low + high) / 2)
            self.strcpy(read_word, self.mid_trigram[mid].first_word)
            if  not(self.strcmp(read_word, word1) != 0):
                if  self.strcmp(self.mid_trigram[mid].third_word, word2) > 0:
                    dir = -1
                else: dir = +1
                while  not(self.strcmp(self.mid_trigram[mid].first_word, word1) != 0):
                    if  not(self.strcmp(self.mid_trigram[mid].third_word, word2) != 0):
                        self.strcpy(selected_word, self.mid_trigram[mid].second_word)
                        return self.mid_trigram[mid].freq
                    mid += dir
                    if  (mid < low) or (mid > high):
                        return 0
                    if  dir < 0:
                        if  self.strcmp(self.mid_trigram[mid].third_word, word2) < 0: return 0
                    if  dir > 0:
                        if  self.strcmp(self.mid_trigram[mid].third_word, word2) > 0: return 0
                return 0
            if  self.strcmp(read_word, word1) < 0:
                low = mid + 1
            else:
                high = mid - 1
        return 0

    def search_word_post_trigram(self, word1, word2, low, high, selected_word):
        first = low
        last = high
        read_word=[0]*20
        while  low <= high:
            mid = int((low + high) / 2)
            self.strcpy(read_word, self.post_trigram[mid].first_word)
            if  not(self.strcmp(read_word, word1) != 0):
                if  self.strcmp(self.post_trigram[mid].second_word, word2) > 0:
                    dir = -1
                else: dir = +1
                while  not(self.strcmp(self.post_trigram[mid].first_word, word1) != 0):
                    if  not(self.strcmp(self.post_trigram[mid].second_word, word2) != 0):
                        self.strcpy(selected_word, self.post_trigram[mid].third_word)
                        return self.post_trigram[mid].freq
                    mid += dir
                    if  (mid < low) or (mid > high):
                        return 0
                    if  dir < 0:
                        if  self.strcmp(self.post_trigram[mid].second_word, word2) < 0: return 0
                    if  dir > 0:
                        if  self.strcmp(self.post_trigram[mid].second_word, word2) > 0: return 0
                return 0
            if  self.strcmp(read_word, word1) < 0:
                low = mid + 1
            else:
                high = mid - 1
        return 0

    def search_word_pre_bigram_index(self, word,start,end):
        read_word=[0]*20
        high = self.pre_bigram_index_count - 1
        low = 0
        while  low <= high:
            mid = int((low + high) / 2)
            self.strcpy(read_word, self.pre_bigram_index[mid].normalised_word)
            if  not(self.strcmp(read_word, word) != 0):
                if  mid == 0:
                    start = 0
                else:
                    start = self.pre_bigram_index[mid - 1].index + 1
                end = self.pre_bigram_index[mid].index
                return start,end, 1
            if  self.strcmp(read_word, word) < 0:
                low = mid + 1
            else:
                high = mid - 1
        return start,end, 0

    def search_word_pre_trigram_index(self, word,start, end):
        read_word=[0]*20
        high = self.pre_trigram_index_count - 1
        low = 0
        while  low <= high:
            mid = int((low + high) / 2)
            self.strcpy(read_word, self.pre_trigram_index[mid].normalised_word)
            if  not(self.strcmp(read_word, word) != 0):
                if  mid == 0:
                    start = 0
                else:
                    start = self.pre_trigram_index[mid - 1].index + 1
                end = self.pre_trigram_index[mid].index
                return start, end,1
            if  self.strcmp(read_word, word) < 0:
                low = mid + 1
            else:
                high = mid - 1
        return start, end,0

    def search_word_mid_trigram_index(self, word, start, end):
        read_word=[0]*20
        high = self.mid_trigram_index_count - 1
        low = 0
        while  low <= high:
            mid = int((low + high) / 2)
            self.strcpy(read_word, self.mid_trigram_index[mid].normalised_word)
            if  not(self.strcmp(read_word, word) != 0):
                if  mid == 0:
                    start = 0
                else:
                    start = self.mid_trigram_index[mid - 1].index + 1
                end = self.mid_trigram_index[mid].index
                return  start,end, 1
            if  self.strcmp(read_word, word) < 0:
                low = mid + 1
            else:
                high = mid - 1
        return  start,end, 0

    def search_word_post_bigram_index(self, word, start, end):
        read_word=[0]*20
        high = self.post_bigram_index_count - 1
        low = 0
        while  low <= high:
            mid = int((low + high) / 2)

            self.strcpy(read_word, self.post_bigram_index[mid].normalised_word)
            if  not(self.strcmp(read_word, word) != 0):
                if  mid == 0:
                    start = 0
                else:
                    start = self.post_bigram_index[mid - 1].index + 1
                end = self.post_bigram_index[mid].index
                return start, end,1
            if  self.strcmp(read_word, word) < 0:
                low = mid + 1
            else:
                high = mid - 1
        return start, end,0

    def search_word_post_trigram_index(self, word, start, end):
        read_word=[0]*20
        high = self.post_trigram_index_count - 1
        low = 0
        while  low <= high:
            mid = int((low + high) / 2)
            self.strcpy(read_word, self.post_trigram_index[mid].normalised_word)
            if  not(self.strcmp(read_word, word) != 0):
                if  mid == 0:
                    start = 0
                else:
                    start = self.post_trigram_index[mid - 1].index + 1
                end = self.post_trigram_index[mid].index
                return start,end, 1
            if  self.strcmp(read_word, word) < 0:
                low = mid + 1
            else:
                high = mid - 1
        return start,end, 0

    def get_freq(self, word):
        low = 0
        mid = 0
        high = self.corpus_word_count - 1
        punjabi_int = [0]*20
        normalise=[0]*20
        read_word=[0]*20
        for  k in range(0,self.strlen(word)):
            punjabi_int[k] = word[k]
        self.normalise_punjabi_word(punjabi_int, self.strlen(word), normalise)
        while  low <= high:
            mid = int((low + high) / 2)
            self.strcpy(read_word, self.corpus_words[mid].normalised_word)
            if  not(self.strcmp(read_word, normalise) != 0):
                if  not(self.strcmp(self.corpus_words[mid].original_word, word) != 0):
                    return self.corpus_words[mid].freq
                else:
                    return 0
            if  self.strcmp(read_word, normalise) < 0:
                low = mid + 1
            else:
                high = mid - 1
        return 0

    def normalise_punjabi_word(self, punjabi_int, punjabi_int_size, punjabi_word):
        extra = 0
        table=[0]*256
        t_punjabi_word=[0]*30
        i = j = 0
        extra+=1
        extra-=1
        while  i < punjabi_int_size:
            int1 = punjabi_int[i]
            ch = (int1 % 256)
            if  (ch == 28) and (i < punjabi_int_size - 1) and ((punjabi_int[i + 1] % 256) == 60):
                t_punjabi_word[j] =91
                j+=1
                i+=1
                extra+=1
            else:
                if  (ch == 15) and (i < punjabi_int_size - 1) and ((punjabi_int[i + 1] % 256) == 6):
                    t_punjabi_word[j] =62
                    j+=1
                    t_punjabi_word[j] =47
                    j+=1
                    t_punjabi_word[j] =62
                    j+=1
                    i+=1
                    extra-=1
                else:
                    t_punjabi_word[j] = ch
                    j+=1
            i+=1
        punjabi_int_size -= extra
        i = 0
        while  i < punjabi_int_size - 1:  
            ch = t_punjabi_word[i]
            ch1 = t_punjabi_word[i + 1]
            if  (ch ==63) and (ch1 ==19):
                t_punjabi_word[i] =47
                t_punjabi_word[i + 1] =75
                i+=1
            i+=1
        i = 0
        while  i < punjabi_int_size - 1: 
            ch = t_punjabi_word[i]
            ch1 = t_punjabi_word[i + 1]
            if  (ch ==63) and (ch1 ==6):
                t_punjabi_word[i] =47
                t_punjabi_word[i + 1] =62
                i+=1
            i+=1
        i = 0
        while  i < punjabi_int_size - 1: 
            ch = t_punjabi_word[i]
            ch1 = t_punjabi_word[i + 1]
            if  (ch ==63) and (ch1 ==10):
                t_punjabi_word[i] =47
                t_punjabi_word[i + 1] =66
                i+=1
            i+=1
        i = 0
        while  i < punjabi_int_size - 1: 
            ch = t_punjabi_word[i]
            ch1 = t_punjabi_word[i + 1]
            if  ((ch ==112) or (ch ==2)) and ((ch1 ==42) or (ch1 ==44) or (ch1 ==45)):
                t_punjabi_word[i] =46
                t_punjabi_word[i + 1] = ch1
                i+=1
            i+=1
        i = 0
        while  i < punjabi_int_size - 1: 
            ch = t_punjabi_word[i]
            ch1 = t_punjabi_word[i + 1]
            if  (ch ==112) and ((ch1 ==46) or (ch1 ==40)):
                t_punjabi_word[i] =113
                t_punjabi_word[i + 1] = ch1
                i+=1
            i+=1
        for  i in range(0,256):
            table[i] = i
        table[7] = 5
        table[8] = 16
        table[9] = 5
        table[10] = 5
        table[15] = 7
        table[16] = 5
        table[19] = 5
        table[20] = 5
        table[55] = 54
        table[51] =50
        table[60] = 0
        table[63] = 0
        table[65] = 0
        table[69] = table[77] = 0
        table[88] =21
        table[89] =22
        table[90] =23
        table[93] =92
        table[94] =43
        table[72] =47
        table[64] =47
        table[71] =47
        table[67] =48
        table[1] = table[35] = table[2] =40
        table[47] =71
        table[6] =62
        table[73] =62
        table[17] =62
        table[13] =15
        table[113] = 0
        table[9] = table[10] = table[19] = table[20] =10
        table[66] = table[75] = table[76] =53
        table[112] =40
        table[16] = 8
        table[47] = 47
        table[16] = 16
        table[34] =33
        table[29] =28
        j=0
        for  i in range(0,punjabi_int_size):
            if  (i > 0) and ((t_punjabi_word[i - 1] ==62) or (t_punjabi_word[i - 1] ==6)) and (t_punjabi_word[i] ==47) and (t_punjabi_word[i + 1] ==71):
                punjabi_word[j] =15
                j+=1
                i+=1
                continue
            if  (i == 0) and ((t_punjabi_word[i] ==47) or (t_punjabi_word[i] ==53)):
                punjabi_word[j] = t_punjabi_word[i]
                j+=1
                continue
            if  i == 0:
                if  (t_punjabi_word[i] ==19) or (t_punjabi_word[i] ==20) or (t_punjabi_word[i] ==10):
                    punjabi_word[j] =19
                    j+=1
                    continue
                else:
                    if  (t_punjabi_word[i] ==5) and (t_punjabi_word[i + 1] ==53):
                        punjabi_word[j] =19
                        j+=1
                        i+=1
                        continue
                    else:
                        if  (t_punjabi_word[i] ==8) or (t_punjabi_word[i] ==16):
                            punjabi_word[j] =8
                            j+=1
                            continue
                        else:
                            if  t_punjabi_word[i] ==34:
                                punjabi_word[j] =34
                                j+=1
                                continue
                            else:
                                if  t_punjabi_word[i] ==29:
                                    punjabi_word[j] =29
                                    j+=1
                                    continue
                                else:
                                    if  (t_punjabi_word[i] ==5) and (t_punjabi_word[i + 1] ==47):
                                        punjabi_word[j] =8
                                        j+=1
                                        i+=1
                                        continue
                                    else:
                                        if  (t_punjabi_word[i] ==7) or (t_punjabi_word[i] ==9) or (t_punjabi_word[i] ==5) or (t_punjabi_word[i] ==255):
                                            punjabi_word[j] =5
                                            j+=1
                                            continue
            if  (i > 0) and (t_punjabi_word[i - 1] ==113):
                punjabi_word[j] = t_punjabi_word[i]
                j+=1
                continue
            if  ((t_punjabi_word[i] ==63) or (t_punjabi_word[i] == 7)) and (t_punjabi_word[i + 1] == 6):
                punjabi_word[j] =47
                j+=1
                punjabi_word[j] =62
                j+=1
                i+=1
                continue
            if  (i == punjabi_int_size - 1) and (t_punjabi_word[i] ==64):
                punjabi_word[j] = t_punjabi_word[i]
                j+=1
                continue
            if  (i > 0) and (i == punjabi_int_size - 1) and (t_punjabi_word[i] ==57) and (t_punjabi_word[i - 1] !=53):
                punjabi_word[j] =62
                j+=1
                continue
            if  (i == punjabi_int_size - 1) and (t_punjabi_word[i] ==65):
                punjabi_word[j] =66
                j+=1
                continue
            if  (t_punjabi_word[i] == 2) and ((t_punjabi_word[i + 1] ==42) or (t_punjabi_word[i + 1] ==44) or (t_punjabi_word[i + 1] ==45)):
                punjabi_word[j] =46
                j+=1
                continue
            if  (t_punjabi_word[i + 1] == 77) and (t_punjabi_word[i + 2] == t_punjabi_word[i] + 1) and (t_punjabi_word[i] <47):
                continue
            if  (i > 2) and (t_punjabi_word[i - 1] == 77):
                if  t_punjabi_word[i - 2] == t_punjabi_word[i]: continue
            if  i == punjabi_int_size - 1:
                if  t_punjabi_word[i] ==112:
                    t_punjabi_word[i] = 2
                if  (t_punjabi_word[i] == 2) or (t_punjabi_word[i] == 15) or (t_punjabi_word[i] ==71) or (t_punjabi_word[i] ==72) or (t_punjabi_word[i] ==8):
                    punjabi_word[j] = t_punjabi_word[i]
                    j+=1
                    continue
            if  t_punjabi_word[i] ==60:
                if  i > 0 and t_punjabi_word[i - 1] ==56:
                    punjabi_word[j] = t_punjabi_word[i]
                    j+=1
                    continue
            if  (t_punjabi_word[i] ==65) or (t_punjabi_word[i] ==65):
                if  (t_punjabi_word[i + 1] >=4) and (t_punjabi_word[i + 1] <=6):
                    punjabi_word[j] =66
                    j+=1
                    continue
            if  not(table[t_punjabi_word[i]] != 0): continue
            punjabi_word[j] = table[t_punjabi_word[i]]
            j+=1
        punjabi_word[j] = 0

    def search_word_bigram(self, word, low, high):
        read_word=[0]*12
        while  low <= high:
            mid = int((low + high) / 2)
            self.strcpy(read_word, self.bigrams[mid].second_word)
            if  not(self.strcmp(read_word, word) != 0):
                return (self.bigrams[mid].freq)
            if  self.strcmp(read_word, word) < 0:
                low = mid + 1
            else:
                high = mid - 1
        return 0

    def search_word_bigram_index(self, word, start, end):
        read_word=[0]*20
        high = self.bigram_index_count - 1
        low = 0
        while  low <= high:
            mid = int((low + high) / 2)
            self.strcpy(read_word, self.bigram_index1[mid].normalised_word)
            if  not(self.strcmp(read_word, word) != 0):
                if  mid == 0:
                    start = 0
                else:
                    start = self.bigram_index1[mid - 1].index + 1
                end = self.bigram_index1[mid].index
                return start, end, 1
            if  self.strcmp(read_word, word) < 0:
                low = mid + 1
            else:
                high = mid - 1
        return start, end, 0

    def read_bigram_corpus(self, bigrams, bigram_index1 ):

        FILE_NAME = os.path.join(self.appPath,"normal_bigrams.bin")
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return

        FILE_NAME1 = os.path.join(self.appPath,"bigrams.bin")
        if not os.path.exists(FILE_NAME1):
            self.printMSG("File not exists! " + FILE_NAME1)
            return

        r1 = open(FILE_NAME1, 'rb')
        bigram_total = int.from_bytes(r1.read(4), 'little')
        for  i in range(0,bigram_total):
            try:
                rawBytes = r1.read(10)
                for j, byte in enumerate(rawBytes):
                    bigrams[i].first_word[j] = byte
                rawBytes = r1.read(10)
                for j, byte in enumerate(rawBytes):
                    bigrams[i].second_word[j] = byte
                b = int.from_bytes(r1.read(1), 'little')
                bigrams[i].freq = b
            except Exception as e:
                    self.printMSG("read_bigram_corpus() " + e)
                    break
        r1.close()

        r = open(FILE_NAME, 'rb')
        bigram_index_count = int.from_bytes(r.read(4), 'little')
        bigram_index_count = 0
        for  i in range(0,bigram_total):
            try:
                rawBytes = r.read(len(bigram_index1[i].normalised_word))
                for j, byte in enumerate(rawBytes):
                    bigram_index1[i].normalised_word[j] = byte
                readValue = r.read(4)
                bigram_index1[i].index = int.from_bytes(readValue, 'little')
                if readValue:
                    bigram_index_count += 1
                else:
                    break
            except: 
                break
        r.close()
        return bigram_total, bigram_index_count

    def search_word_post_int_bigram(self, word, low, high, selected_word):
        read_word=[0]*20
        while  low <= high:
            mid = int((low + high) / 2)
            self.strcpy(read_word, self.post_bigram[mid].first_word)
            if  not(self.strcmp(read_word, word) != 0):
                self.strcpy(selected_word, self.post_bigram[mid].second_word)
                return (self.post_bigram[mid].freq)
            if  self.strcmp(read_word, word) < 0:
                low = mid + 1
            else:
                high = mid - 1
        return 0

    def search_word_pre_int_bigram(self, word, low, high, selected_word):
        read_word=[0]*20
        while  low <= high:
            mid = int((low + high) / 2)
            self.strcpy(read_word, self.pre_bigram[mid].second_word)
            if  not(self.strcmp(read_word, word) != 0):
                self.strcpy(selected_word, self.pre_bigram[mid].first_word)
                return (self.pre_bigram[mid].freq)
            if  self.strcmp(read_word, word) < 0:
                low = mid + 1
            else:
                high = mid - 1
        return 0

    def strcpy(self, str1, str2):
        t = 0
        len2 = self.strlen(str2)
        for  t in range(0,len2+1):
            if  t < len(str1):
                try:
                    str1[t] = str2[t]
                except IndexError:
                    str1[t] = 0
                    break
            else:
                str1[len(str1- 1)] = 0
                break

    def strcmp(self, str1, str2):
        len1 = self.strlen(str1)
        len2 = self.strlen(str2)
        if  len1 > len2: len = len1
        else: len = len2
        for  t in range(0,len):
            if  str1[t] < str2[t]: return -1
            if  str1[t] > str2[t]: return 1
        return 0

    def strlen(self, source):
        if  len(source) == 0: return 0
        size = len(source)
        length = 0
        for  t in range(0,size):
            if  source[t] != 0:
                length+=1
            else: break
        return length

    def strcat(self, str1, str2):
        len1 = self.strlen(str1)
        len2 = self.strlen(str2)
        j = len1
        for  t in range(0,len2):
            str1[j] = str2[t]
            j+=1
        str1[j] = 0

    def byte2Str_off(self, data, len, SKIPFIRST2BYTES):
        s = ""
        b1 =10
        b2 =111
        c1 = b1 * 256 + b2
        c = c1
        if  SKIPFIRST2BYTES:
            for  t in range(2,2,2):
                b1 = data[t]
                b2 = data[t + 1]
                c1 = b1 + (b2 * 256)
                c = c1
                s = s + c
        else:
            for  t in range(0,2,2):
                b1 = data[t]
                b2 = data[t + 1]
                c1 = b1 + (b2 * 256)
                c = c1
                s = s + c
        
        return s

    def byte2Str(self, data, length, SKIPFIRST2BYTES):
        # print("inside shamukhi's byte2str\n" )
        s = ""
        b1 =10
        b2 =111
        c1 = b1 * 256 + b2
        c = (c1)
        # print(data)
        # print(SKIPFIRST2BYTES)
        
        if  SKIPFIRST2BYTES:
            for  t in range(0,length,2):
                b1 = data[t]
                b2 = data[t + 1]
                if  b1 == 255 and b2 == 254: continue
                c1 = b1 + (b2 * 256)
               
                if  c1 != 0:
                    c = chr(c1)
                    # print(f'{c1}---->{c}')
                    s = s + c
        else:
            for  t in range(0,length,2):
                b1 = data[t]
                b2 = data[t + 1]
                if  b1 == 255 and b2 == 254: continue
                c1 = b1 + (b2 * 256)
                if  c1 != 0:
                    c = c1
                    # print(f'{c1}---->{c}')
                    s = s + c
        # print(s)
        return s

    def str2Byte(self, str1):
        # print(f'{str1}\n')
        data=[0]*(len(str1)* 2 + 2)
        length = 0
        data[length] = 255
        length+=1
        data[length] = 254
        length+=1
        # print('string to byte shahmukhi\n')
        for  t in range(0,len(str1)):
            #character to decimal for convertion
            ch = ord(str1[t])
            # print(f'{str1[t]}--->{ch}')
            code = ch
            #normalization
            data[length] = int(code % 256)
            length+=1
            data[length] = int(code / 256)
            length+=1
        # print(f'\ndata of shahmukhi characters:\n {data}')
        return data

    def printMSG(self, s):
        self.MSG = self.MSG + self.separator + s
        # print(self.MSG,'\n\n')

    def printMSG2(self, s, v):
        self.MSG = self.MSG + self.separator + s + v
        # print(self.MSG)

    def convertToByte(self,u):
        u=u%256
        return u

    def convertGurmukhiToDevanagariText(self,gurmukhiText):
        dev =9
        gur =10
        halant =77
        if  gurmukhiText[0]:
            gurUnicodeBytes = gurmukhiText
            devUnicodeBytes = [0]*(len(gurUnicodeBytes)* 2)
            devptr = 0
            for  i in range(0,len(gurUnicodeBytes)):
                b1 = gurUnicodeBytes[i]
                b2 = 0
                if  i < len(gurUnicodeBytes)- 2:
                    b2 = gurUnicodeBytes[i + 2]
                if  b1 == 255 or b1 == 254: continue
                if  gurUnicodeBytes[i] == gur:
                    devUnicodeBytes[devptr] = dev
                    devptr+=1
                elif  gurUnicodeBytes[i] ==112:
                    devUnicodeBytes[devptr] =2
                    devptr+=1
                elif  gurUnicodeBytes[i] ==113:
                    devUnicodeBytes[devptr] = b2
                    devptr+=1
                    devUnicodeBytes[devptr] = dev
                    devptr+=1
                    devUnicodeBytes[devptr] = halant
                    devptr+=1
                else:
                    devUnicodeBytes[devptr] = gurUnicodeBytes[i]
                    devptr+=1
        return devUnicodeBytes