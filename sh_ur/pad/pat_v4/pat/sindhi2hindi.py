import numpy as np
import os.path
import re
import string
import os, sys

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
class Sindhi2Hindi:
    FILESIZE = 50000
    CORPUS = 260860
    CORPUS_FILESIZE = 6400
    DICSIZE = 99000
    BISIZE = 4000
    TRISIZE_PRE = 81500
    TRISIZE_MID = 140550
    TRISIZE_POST = 83900
    BIGRAM_SIZE = 202550
    INDEX_SIZE = 8000
    URDU_BIGRAM_SIZE = 12800
    EXTRA_SIZE = 3568
    URDUCORPUS = 100500
    IGNORE = 340
    BISIZE1 = 461200
    INDEX_SIZE1 = 40000
    SEQSIZE =220

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

    wordlist=[]
    cs=[] 
    word_total = 0
    word_found = 0
    bi_word_found = 0
    word_not_found = 0
    hindi_trigram_found = 0
    PROTECTOLDA = 0
    olda = 0
    swc = 0
    max_c = 0
    min_c = 0
    average_c = 0
    urdu_corpus_count = 0
    pre_bigram=[]
    post_bigram=[]
    pre_bigram_index=[]
    post_bigram_index=[]
    bigrams=[]
    bigram_index1=[]
    pre_trigram_index=[]
    post_trigram_index=[]
    mid_trigram_index=[]
    corpus_words=[]
    urdu_bigram=[]
    roman_dict=[] 
    urdu_dict=[] 
    ignore=[] 
    pre_trigram=[]
    mid_trigram=[]
    post_trigram=[]
    corpus_word_count = 0
    corpus_found = 0
    multi_count = 0
    dict_word_count = 0
    pre_bigram_total= 0
    post_bigram_total= 0
    pre_bigram_index_count= 0
    post_bigram_index_count= 0
    urdu_bigram_total= 0
    pre_trigram_index_count= 0
    mid_trigram_index_count= 0
    post_trigram_index_count= 0
    pre_trigram_total= 0
    mid_trigram_total= 0
    post_trigram_total= 0
    extra_word_count= 0
    ignore_word_count= 0
    bigram_total= 0
    bigram_index_count=0
    prev_number = 0
    corpus_flag = 0
    conversion_level = 5
    extra_words=[] 
    tej_urdu=''
    tej_hindi=''
    max_joint = 0
    total_joint = 0
    merged_word_count = 0
    total_merged_words=[]
    average_joint_count = 0.0
    urdu_corpus_words=[]
    urdu_corpus_total = 0
    urdu_corpus_word_count = 0
    merged_words_searched = 0
    merged_words_found = 0
    single_words_found = 0
    izafat_flag = 0

    def __init__(self):
        i = 0
        if not self.isActive:
            QTS = [0] * 1
            QTS[0] = 0
            self.pre_bigram = np.empty((self.BIGRAM_SIZE), dtype="object")
            self.post_bigram = np.empty((self.BIGRAM_SIZE), dtype="object")
            for i in range(self.BIGRAM_SIZE):
                self.pre_bigram[i] = bigram_corpus()
                self.post_bigram[i] = bigram_corpus()
                self.pre_bigram[i].first_word = np.zeros((16), dtype='i')
                self.pre_bigram[i].second_word = np.zeros((16), dtype='i')
                self.post_bigram[i].first_word = np.zeros((16), dtype='i')
                self.post_bigram[i].second_word = np.zeros((16), dtype='i')
            self.bigrams = np.empty((self.BISIZE1), dtype="object")
            for i in range(self.BISIZE1):
                self.bigrams[i] = bigram_corpus() 
                self.bigrams[i].first_word = np.zeros((10), dtype='i')
                self.bigrams[i].second_word = np.zeros((10), dtype='i')
            self.bigram_index1 = np.empty((self.INDEX_SIZE1), dtype="object")
            for i in range(self.INDEX_SIZE1):
                self.bigram_index1[i] = bigram_index()
                self.bigram_index1[i].normalised_word = np.zeros((10), dtype='i')
                self.bigram_index1[i].index = 0
            self.pre_bigram_index = np.empty((self.INDEX_SIZE), dtype="object")
            self.post_bigram_index = np.empty((self.INDEX_SIZE), dtype="object")
            self.pre_trigram_index = np.empty((self.INDEX_SIZE), dtype="object")
            self.post_trigram_index = np.empty((self.INDEX_SIZE), dtype="object")
            self.mid_trigram_index = np.empty((self.INDEX_SIZE), dtype="object")
            for i in range(self.INDEX_SIZE):
                self.pre_bigram_index[i] = bigram_index()
                self.post_bigram_index[i] = bigram_index()
                self.pre_trigram_index[i] = trigram_index()
                self.post_trigram_index[i] = trigram_index()
                self.mid_trigram_index[i] = trigram_index()
                self.pre_bigram_index[i].normalised_word = np.zeros((16), dtype='i')
                self.post_bigram_index[i].normalised_word = np.zeros((16), dtype='i')
                self.pre_trigram_index[i].normalised_word = np.zeros((16), dtype='i')
                self.post_trigram_index[i].normalised_word = np.zeros((16), dtype='i')
                self.mid_trigram_index[i].normalised_word = np.zeros((16), dtype='i')
            self.urdu_bigram = np.empty((self.URDU_BIGRAM_SIZE), dtype="object")
            for i in range(self.URDU_BIGRAM_SIZE):
                self.urdu_bigram[i] = urdu_bigram()
                self.urdu_bigram[i].urdu1 = np.zeros((20), dtype='i')
                self.urdu_bigram[i].urdu2 = np.zeros((20), dtype='i')
                self.urdu_bigram[i].hindi = np.zeros((40), dtype='i')
            self.corpus_words = np.empty((self.CORPUS), dtype="object")
            for i in range(self.CORPUS):
                self.corpus_words[i] = normalised_corpus()
                self.corpus_words[i].original_word = np.zeros((16), dtype='i')
                self.corpus_words[i].normalised_word = np.zeros((16), dtype='i')
                self.corpus_words[i].freq = 0
            self.roman_dict = np.zeros((self.DICSIZE, 20), dtype="i")
            self.urdu_dict = np.zeros((self.DICSIZE, 20), dtype="i")
            
            self.wordlist = np.empty((40000), dtype="object")
            for i in range(40000):
                self.wordlist[i] = wlist()
                self.wordlist[i].word = np.zeros((40), dtype='i')
                self.wordlist[i].count = 0
            if not self.offTriGram:
                self.pre_trigram = np.empty((self.TRISIZE_PRE), dtype='object')
                self.mid_trigram = np.empty((self.TRISIZE_MID), dtype='object')
                self.post_trigram = np.empty((self.TRISIZE_POST), dtype='object')
                for i in range(self.TRISIZE_PRE):
                    self.pre_trigram[i] = trigram_corpus()
                    self.pre_trigram[i].first_word = np.zeros((16), dtype='i')
                    self.pre_trigram[i].second_word = np.zeros((16), dtype='i')
                    self.pre_trigram[i].third_word = np.zeros((16), dtype='i')
                    self.pre_trigram[i].freq = 0
                for i in range(self.TRISIZE_MID):
                    self.mid_trigram[i] = trigram_corpus()
                    self.mid_trigram[i].first_word = np.zeros((16), dtype='i')
                    self.mid_trigram[i].second_word = np.zeros((16), dtype='i')
                    self.mid_trigram[i].third_word = np.zeros((16), dtype='i')
                    self.mid_trigram[i].freq = 0
                for i in range(self.TRISIZE_POST):
                    self.post_trigram[i] = trigram_corpus()
                    self.post_trigram[i].first_word = np.zeros((16), dtype='i')
                    self.post_trigram[i].second_word = np.zeros((16), dtype='i')
                    self.post_trigram[i].third_word = np.zeros((16), dtype='i')
                    self.post_trigram[i].freq = 0

            self.extra_words = np.zeros((self.EXTRA_SIZE, 5), dtype='i')
            self.appPath = pathname = os.getcwd()
            self.appPath = os.path.join(self.appPath,'sindhi2hindi')
            #self.appPath += '\\'
            self.urdu_corpus_words = np.empty((self.URDUCORPUS), dtype='object')
            for i in range(self.URDUCORPUS):
                self.urdu_corpus_words[i] = urdu_corpus()
                self.urdu_corpus_words[i].original_word = np.zeros((25), dtype='i')
                self.urdu_corpus_words[i].freq = 0
            self.ignore = np.zeros((self.IGNORE, 10), dtype='i')
            self.read_sindhi_hindi_dict()
            self.read_ignore_words()
            self.corpus_word_count=self.read_binary_corpus(self.corpus_words,self.corpus_word_count)
            self.pre_bigram_total, self.pre_bigram_index_count = self.read_pre_bigram_corpus(self.pre_bigram,  self.pre_bigram_total, self.pre_bigram_index,self.pre_bigram_index_count)  
            self.post_bigram_total, self.post_bigram_index_count = self.read_post_bigram_corpus(self.post_bigram,self.post_bigram_total, self.post_bigram_index,self.post_bigram_index_count)  
            if  not self.offTriGram:
                self.pre_trigram_total,self.pre_trigram_index_count=self.read_pre_trigram_corpus(self.pre_trigram,self.pre_trigram_total, self.pre_trigram_index,self.pre_trigram_index_count)
                self.post_trigram_total,self.post_trigram_index_count=self.read_post_trigram_corpus(self.post_trigram,self.post_trigram_total, self.post_trigram_index,self.post_trigram_index_count)
                self.mid_trigram_total,self.mid_trigram_index_count=self.read_mid_trigram_corpus(self.mid_trigram,self.mid_trigram_total, self.mid_trigram_index,self.mid_trigram_index_count)
            else:                
                self.pre_trigram_index_count = 0
                self.post_trigram_index_count = 0
                self.mid_trigram_index_count = 0
            self.isActive = True
    def startReg(self, input):
        generatedWord = ''
        patt = r'(\s*[؀-ۿ]\s*[' + re.escape(string.punctuation) + ']*)+'
        generatedWord = re.sub(patt, self.func, input)
        return generatedWord

    def func(self, matchobj):
        m = matchobj.group(0)
        return self.start(m)

    def start(self, input):
            out_file_len = 0
            file_length_in = 0
            file_length_out = 0
            urdu = np.zeros((self.FILESIZE), dtype='i')
            roman = np.zeros((self.FILESIZE), dtype='i')
            
            wsp = (' ', '\r', '\n', '\t')
            wCount = 10
            wCount += len((self.splitStr(input, wsp)))
            self.total_merged_words = [0]*wCount
            if len(input)== 0:
                return "Empty String...."
            inputbytes = self.str2Byte(input)
            if len(inputbytes)+ 1 > len(urdu):
                return "TOO MUCH DATA"
            for  i in range(0,len(inputbytes)): 
                urdu[i]=inputbytes[i]
            file_length_in = len(inputbytes)


            out_file_len=self.normalise_text(urdu, file_length_in, roman, out_file_len)
            for  i in range(0,out_file_len): 
                urdu[i] = roman[i]
            file_length_in = out_file_len
            file_length_out=self.convert_urdu_to_hindi(urdu, file_length_in, roman,file_length_out)


            self.word_found += (self.corpus_found + self.multi_count + self.bi_word_found)
            total_words = self.word_found + self.word_not_found

            self.tej_hindi = self.byte2Str(roman, file_length_out, True)
            return self.tej_hindi
    def convert_unicodefile_to_UTF8(self, urdu, size, roman, roman_size):
        urdu_word = [0] * 50
        roman_word = [0] * 15
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
                roman_word_size = self.convert_urdu_punctuation_to_roman(ch, ch1, roman_word,roman_word_size)
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
        return roman_size

    def get_line_word_count(self, hindi, line_size):
        len = 0
        i = 0
        hindi_ptr = 0
        wc = 0
        while hindi_ptr < line_size:
            ch = hindi[hindi_ptr]
            ch1 = hindi[hindi_ptr + 1]
            if (ch == 255) and (ch1 == 254):
                hindi_ptr += 2
                continue
            while self.check_hindi_punctuation(ch, ch1) > 0:
                if hindi_ptr >= line_size:
                    return wc
                ch = hindi[hindi_ptr]
                hindi_ptr += 1
                ch1 = hindi[hindi_ptr]
                hindi_ptr += 1
            len = 0
            while not (self.check_hindi_punctuation(ch, ch1) != 0):
                if hindi_ptr >= line_size:
                    return wc
                ch = hindi[hindi_ptr]
                hindi_ptr += 1
                ch1 = hindi[hindi_ptr]
                hindi_ptr += 1
                len += 1
                if len == 2: wc += 1
        return wc

    def check_for_vao_in_line(self, hindi, line_size):
        hindi_ptr = 0
        temp_size = 0
        if line_size == 0: return line_size
        while hindi_ptr < line_size:
            if (hindi_ptr < line_size - 6) and (hindi[hindi_ptr] == 32) and (hindi[hindi_ptr + 1] == 0) and (
                    hindi[hindi_ptr + 2] == 19) and (hindi[hindi_ptr + 3] == 9) and (
                    hindi[hindi_ptr + 4] == ord('-')) and (hindi[hindi_ptr + 5] == 0):
                hindi[temp_size] = ord('-')
                temp_size += 1
                hindi[temp_size] = 0
                temp_size += 1
                hindi[temp_size] = 19
                temp_size += 1
                hindi[temp_size] = 9
                temp_size += 1
                hindi[temp_size] = ord('-')
                temp_size += 1
                hindi[temp_size] = 0
                temp_size += 1
                hindi_ptr += 8
            elif (hindi_ptr < line_size - 8) and (hindi[hindi_ptr] == ord('-')) and (
                    hindi[hindi_ptr + 1] == 0) and (hindi[hindi_ptr + 2] == 15) and (
                    hindi[hindi_ptr + 3] == 9) and (hindi[hindi_ptr + 4] == ord('-')) and (
                    hindi[hindi_ptr + 5] == 0) and (hindi[hindi_ptr + 6] == ord(' ')) and (
                    hindi[hindi_ptr + 7] == 0):
                hindi[temp_size] = ord('-')
                temp_size += 1
                hindi[temp_size] = 0
                temp_size += 1
                hindi[temp_size] = 15
                temp_size += 1
                hindi[temp_size] = 9
                temp_size += 1
                hindi[temp_size] = ord('-')
                temp_size += 1
                hindi[temp_size] = 0
                temp_size += 1
                hindi_ptr += 8
            else:
                if temp_size != hindi_ptr:
                    hindi[temp_size] = hindi[hindi_ptr]
                    temp_size += 1
                    hindi_ptr += 1
                    hindi[temp_size] = hindi[hindi_ptr]
                    temp_size += 1
                    hindi_ptr += 1
                else:
                    hindi_ptr += 2
                    temp_size = hindi_ptr

        line_size = temp_size
        return line_size
    def convert_urdu_to_hindi(self, urdu, size, roman, roman_size):
        urdu_word=[0]*100
        p_urdu_word=[0]*100
        pp_urdu_word=[0]*100
        roman_word=[0]*9000
        hindi_word=[0]*100
        p_roman_word=[204]*9000
        pp_roman_word=[204]*9000
        temp_roman_word=[0]*5000
        hindi_line=[0]*10000
        urdu_word_size = 0
        p_urdu_word_size = 0
        pp_urdu_word_size = 0
        roman_word_size = 0
        p_roman_word_size = 0
        pp_roman_word_size = 0
        post_found = 0
        urdu_ptr = 0
        roman_ptr = 0
        temp_roman_word_size = 0
        line_ptr = 0
        first_word = 1
        last_word = 0
        end_of_line = 0
        first_punc = 1
        cword = 0
        urduHindi=urdu_hindi()
        urduHindi.hindi_end = np.zeros((100), dtype='i')
        urduHindi.hindi_start = np.zeros((100), dtype='i')
        urduHindi.urdu_end = np.zeros((100), dtype='i')
        urduHindi.urdu_start = np.zeros((100), dtype='i')

        hindi_line[line_ptr] = roman[roman_ptr] = urdu[urdu_ptr]
        line_ptr+=1
        roman_ptr += 1
        urdu_ptr += 1

        hindi_line[line_ptr] = roman[roman_ptr] = urdu[urdu_ptr]
        line_ptr += 1
        roman_ptr += 1
        urdu_ptr += 1

        urduHindi.urdu_word_count = 0
        urduHindi.urdu_start[urduHindi.urdu_word_count] = -1

        count=0
        while  urdu_ptr <= size:
            count+=1
            ch = urdu[urdu_ptr]
            ch1 = urdu[urdu_ptr + 1]
            if  not(ch != 0) and not(ch1 != 0) and not(urdu_word_size != 0):
                urdu_ptr += 2
                continue
            if  self.check_punctuation(ch, ch1) > 0:
                if  (first_punc > 0) and not(urdu_word_size != 0):
                    roman_ptr += 2
                    urdu_ptr += 2
                    continue
                first_punc = 0
                roman_word_size = 0
                self.olda = -1
                if  last_word > 0:
                    first_word = 1
                    last_word = 0
                if  ch1 == 6:
                    last_word = 1
                    first_word = 0
                cword+=1
                if  cword == 2315:
                   end_of_line = cword
                urdu_word_size=self.normalise_urdu_word(urdu_word,urdu_word_size)
                post_found = 0
                
                
               
                    
                roman_word_size, found = self.urdu_word_to_hindi(urdu_word, p_urdu_word, pp_urdu_word, urdu_word_size, p_urdu_word_size, pp_urdu_word_size, hindi_word,roman_word_size, self.check_broken_punc(pp_roman_word, pp_roman_word_size))

                urduHindi.urdu_end[urduHindi.urdu_word_count] = urdu_ptr - 1
                if urduHindi.urdu_word_count > 1:
                    urduHindi.hindi_start[urduHindi.urdu_word_count - 2] = line_ptr
                    urduHindi.hindi_end[urduHindi.urdu_word_count - 2] = line_ptr + roman_word_size - 1

                urduHindi.urdu_word_count += 1
                if urduHindi.urdu_word_count > 98:
                    urduHindi.urdu_word_count -= 1

                for  i in range(0,roman_word_size):
                    hindi_line[line_ptr] = hindi_word[i]
                    line_ptr+=1
                roman_word_size = 0
                if  first_word > 0: first_word = 0
                end_of_line = 0
                while  self.check_punctuation(ch, ch1) > 0:
                    temp_roman_word_size=self.convert_urdu_punctuation_to_roman(ch, ch1, temp_roman_word,temp_roman_word_size)

                    for  i in range(0,temp_roman_word_size):
                        roman_word[roman_word_size] = temp_roman_word[i]
                        roman_word_size+=1
                    urdu_ptr += 2
                    if  urdu_ptr >= size: break
                    ch = urdu[urdu_ptr]
                    ch1 = urdu[urdu_ptr + 1]
                    if  (ch == 13) and (ch1 == 0):
                        end_of_line = 0
                urduHindi.urdu_start[urduHindi.urdu_word_count] = urdu_ptr
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
                self.check_prev_number(pp_roman_word, pp_roman_word_size)
                if  pp_roman_word_size - 2 >= 0 and self.check_urdu_line_end(pp_roman_word[pp_roman_word_size - 2], pp_roman_word[pp_roman_word_size - 1]) > 0:
                    end_of_line = 1
                if  self.check_urdu_line_end(pp_roman_word[0], pp_roman_word[1]) > 0:
                    end_of_line = 1
                for  i in range(0,pp_roman_word_size):
                    hindi_line[line_ptr] = pp_roman_word[i]
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
                    line_ptr=self.post_process(hindi_line,line_ptr)
                    for  i in range(0,line_ptr):
                        roman[roman_ptr] = hindi_line[i]
                        roman_ptr+=1
                    line_ptr = 0
                    urduHindi.urdu_word_count = 2
            else:
                if ((urduHindi.urdu_word_count == 0) and  (urduHindi.urdu_start[urduHindi.urdu_word_count] == -1)):
                    urduHindi.urdu_start[urduHindi.urdu_word_count] = urdu_ptr
                urdu_word[urdu_word_size] = ch
                urdu_word_size+=1
                urdu_word[urdu_word_size] = ch1
                urdu_word_size+=1
                if  urdu_word_size > 80: urdu_word_size = 80
                urdu_ptr += 2
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
            hindi_word_size = 0
            hindi_word_size, found = self.urdu_word_to_hindi(urdu_word, p_urdu_word, pp_urdu_word, urdu_word_size, p_urdu_word_size, pp_urdu_word_size, hindi_word, hindi_word_size,self.check_broken_punc(pp_roman_word, pp_roman_word_size))
            for  i in range(0,hindi_word_size):
                hindi_line[line_ptr] = hindi_word[i]
                line_ptr+=1

            if  post_found > 0:
                urdu_word_size = 0
                p_roman_word_size = 0
            for  i in range(0,pp_roman_word_size):
                hindi_line[line_ptr] = pp_roman_word[i]
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
        line_ptr=self.post_process(hindi_line,line_ptr)
        for  i in range(0,line_ptr):
            roman[roman_ptr] = hindi_line[i]
            roman_ptr+=1
        roman_size = roman_ptr
        return roman_size

    def check_hindi_punctuation(self, ch, ch1):
            if  ch1 != 9: return 1
            if ch==125: return 1
            if (ch >96) and (ch<=112): return 1 
            return 0
    def check_prev_number(self, num, pp_roman_word_size):
        for i in range(0,pp_roman_word_size,2):
            if self.check_number(num[i], num[i+1])>0:
                self.prev_number=1
                return
        self.prev_number=0
        return

    def check_number(self, ch, ch1):
        if (ch>=ord('0') and ch <=ord('9')) and not (ch1!=0):
            return 1
        if (ch >=240) and (ch <=249) and (ch1==6):
            return 1
        return 0
    def check_punctuation(self, ch, ch1):
            if (ch>=ord('0') and ch <=ord('9')) and not (ch1!=0):
                self.prev_number=1 
            if  (ch1 == 0) or (ch1 == 32): return 1
            if  ch1 == 6:
                if  ch ==255:
                    return 1
                if  ch ==27:
                    return 1
                if  ch ==31:
                    return 1
                if  ch <=15:
                    return 1
                if  (ch ==212) or (ch ==31) or (ch ==12) or (ch ==13) or (ch ==27) or (ch ==106) or (ch ==109) or (ch ==107):
                    return 1
                if  (ch >=96) and (ch <=109):
                    return 1
                if  (ch >=240) and (ch <=249):
                    return 1
                if  ch ==64:
                    return 1
            if  ch1 ==32:
                if  (ch ==24) or (ch ==25) or (ch ==29) or (ch ==28):
                    return 1
            if (ch==255) and (ch1==254): return 1 
            if  ch1 == 254: return 0
            if  ch1 >32: return 1
            return 0
    def convert_urdu_punctuation_to_roman(self, ch, ch1, roman, roman_size):
        urdu_to_roman = [0] * 256
        urdu_ptr = 0
        roman_ptr = 0
        for i in range(0, 256):
            urdu_to_roman[i] = i
        for i in range(0, 32):
            urdu_to_roman[i] = 0
        for i in range(128, 256):
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

        if (ch1 == 6) and (ch == 16):
            roman[roman_ptr] = ord('(')
            roman_ptr += 1
            roman[roman_ptr] = 0
            roman_ptr += 1
            roman[roman_ptr] = 56
            roman_ptr += 1
            roman[roman_ptr] = 9
            roman_ptr += 1
            roman[roman_ptr] = 50
            roman_ptr += 1
            roman[roman_ptr] = 9
            roman_ptr += 1
            roman[roman_ptr] = ord('.')
            roman_ptr += 1
            roman[roman_ptr] = 0
            roman_ptr += 1
            roman[roman_ptr] = ord(')')
            roman_ptr += 1
            roman[roman_ptr] = 0
            roman_ptr += 1
        else:
            if (ch1 == 6) and (ch == 1):
                roman[roman_ptr] = 32
                roman_ptr += 1
                roman[roman_ptr] = 0
                roman_ptr += 1
                roman[roman_ptr] = 8
                roman_ptr += 1
                roman[roman_ptr] = 9
                roman_ptr += 1
                roman[roman_ptr] = 3
                roman_ptr += 1
                roman[roman_ptr] = 9
                roman_ptr += 1
            else:
                if (ch1 == 6) and (ch == 17):
                    roman[roman_ptr] = ord('(')
                    roman_ptr += 1
                    roman[roman_ptr] = 0
                    roman_ptr += 1
                    roman[roman_ptr] = 5
                    roman_ptr += 1
                    roman[roman_ptr] = 9
                    roman_ptr += 1
                    roman[roman_ptr] = 50
                    roman_ptr += 1
                    roman[roman_ptr] = 9
                    roman_ptr += 1
                    roman[roman_ptr] = 72
                    roman_ptr += 1
                    roman[roman_ptr] = 9
                    roman_ptr += 1
                    roman[roman_ptr] = ord('.')
                    roman_ptr += 1
                    roman[roman_ptr] = 0
                    roman_ptr += 1
                    roman[roman_ptr] = ord(')')
                    roman_ptr += 1
                    roman[roman_ptr] = 0
                    roman_ptr += 1
                else:
                    if (ch1 == 6) and (ch == 18):
                        roman[roman_ptr] = ord('(')
                        roman_ptr += 1
                        roman[roman_ptr] = 0
                        roman_ptr += 1
                        roman[roman_ptr] = 48
                        roman_ptr += 1
                        roman[roman_ptr] = 9
                        roman_ptr += 1
                        roman[roman_ptr] = 57
                        roman_ptr += 1
                        roman[roman_ptr] = 9
                        roman_ptr += 1
                        roman[roman_ptr] = 63
                        roman_ptr += 1
                        roman[roman_ptr] = 9
                        roman_ptr += 1
                        roman[roman_ptr] = ord('.')
                        roman_ptr += 1
                        roman[roman_ptr] = 0
                        roman_ptr += 1
                        roman[roman_ptr] = ord(')')
                        roman_ptr += 1
                        roman[roman_ptr] = 0
                        roman_ptr += 1
                    else:
                        if (ch1 == 6) and (ch == 19):
                            roman[roman_ptr] = ord('(')
                            roman_ptr += 1
                            roman[roman_ptr] = 0
                            roman_ptr += 1
                            roman[roman_ptr] = 48
                            roman_ptr += 1
                            roman[roman_ptr] = 9
                            roman_ptr += 1
                            roman[roman_ptr] = 91
                            roman_ptr += 1
                            roman[roman_ptr] = 9
                            roman_ptr += 1
                            roman[roman_ptr] = 64
                            roman_ptr += 1
                            roman[roman_ptr] = 9
                            roman_ptr += 1
                            roman[roman_ptr] = ord('.')
                            roman_ptr += 1
                            roman[roman_ptr] = 0
                            roman_ptr += 1
                            roman[roman_ptr] = ord(')')
                            roman_ptr += 1
                            roman[roman_ptr] = 0
                            roman_ptr += 1
                        else:
                            if (ch >= 96) and (ch <= 105) and (ch1 == 6):
                                roman[roman_ptr] = (ch + 6)
                                roman_ptr += 1
                                roman[roman_ptr] = 9
                                roman_ptr += 1
                            else:
                                if (ch >= 240) and (ch <= 249) and (ch1 == 6):
                                    roman[roman_ptr] = (ch - 138)
                                    roman_ptr += 1
                                    roman[roman_ptr] = 9
                                    roman_ptr += 1
                                    self.prev_number = 1;
                                else:
                                    if (ch == 212) and (ch1 == 6):
                                        roman[roman_ptr] = 100
                                        roman_ptr += 1
                                        roman[roman_ptr] = 9
                                        roman_ptr += 1
                                    else:
                                        if ch1 != 6:
                                            if (ch1 == 32) and (ch == 24):
                                                roman[roman_ptr] = 39
                                                roman_ptr += 1
                                            else:
                                                if (ch1 == 32) and (ch == 25):
                                                    roman[roman_ptr] = 39
                                                    roman_ptr += 1
                                                else:
                                                    if ch > 128: ch = 0
                                                    roman[roman_ptr] = ch
                                                    roman_ptr += 1
                                        else:
                                            roman[roman_ptr] = urdu_to_roman[ch]
                                            roman_ptr += 1
                                        roman[roman_ptr] = 0
                                        roman_ptr += 1
        roman_size = roman_ptr
        return roman_size

    def check_urdu_word_trigram(self, urdu, p_urdu, pp_urdu, urdu_size, p_urdu_size, pp_urdu_size, roman, roman_size):
            return roman_size,0


           


    def check_urdu_word_bigram(self, urdu, p_urdu, urdu_size, p_urdu_size, roman, roman_size):
        low = 0
        mid = 0
        last = 0
        found = 0
        high = self.urdu_bigram_total
        read_word = [0] * 20
        Urdu_UTF8 = [0] * 20
        Urdu1_UTF8 = [0] * 20
        temp = [0] * 50
        self.UnicodeTo8(p_urdu, p_urdu_size, Urdu_UTF8)
        while low <= high:
            mid = int((low + high) / 2)
            self.strcpy(read_word, self.urdu_bigram[mid].urdu1)
            while not (self.strcmp(self.urdu_bigram[mid].urdu1, Urdu_UTF8) != 0):
                found = 1
                self.UnicodeTo8(urdu, urdu_size, Urdu1_UTF8)
                if not (self.strcmp(self.urdu_bigram[mid].urdu2, Urdu1_UTF8) != 0):
                    self.strcpy(temp, self.urdu_bigram[mid].hindi)
                    k = 0
                    for i in range(0, self.strlen(temp)):
                        if temp[i] == 255:
                            if i < self.strlen(temp) - 1:
                                roman[k] = 32
                                k += 1
                                roman[k] = 0
                                k += 1
                            else:
                                continue
                        else:
                            if temp[i] == 254:
                                roman[k] = ord('-')
                                k += 1
                                roman[k] = 0
                                k += 1
                            else:
                                roman[k] = temp[i]
                                k += 1
                                roman[k] = 9
                                k += 1
                    roman_size = k
                    return roman_size, 1
                if self.strcmp(self.urdu_bigram[mid].urdu2, Urdu1_UTF8) > 0:
                    mid -= 1
                    if last > 0:
                        mid = -1
                    last = -1
                else:
                    mid += 1
                    if last < 0:
                        mid = -1
                    last = 1
                if (mid < 0) or (mid >= self.urdu_bigram_total): return roman_size, 0
            if found == 0: return roman_size, 0
            if self.strcmp(read_word, Urdu_UTF8) < 0:
                low = mid + 1
            else:
                high = mid - 1
        return roman_size, 0

    def check_urdu_word_dictionary(self, urdu, urdu_size, roman, roman_size):
            urdu_ptr = 0
            roman_ptr = 0
            flag = 0
            low = 0
            kk = 0
            break_flag = 0
            file_length_in = 0
            ccount = 0
            temp = [0] * 40
            read_word = [0] * 40
            Urdu_UTF8 = [0] * 40
            sindhi = [0] * 40
            self.UnicodeTo8(urdu, urdu_size, Urdu_UTF8)
            high = self.dict_word_count - 1
            while low <= high:
                mid = int((low + high) / 2)
                self.strcpy(read_word, self.urdu_dict[23502])
                self.strcpy(read_word, self.urdu_dict[mid])
                if not (self.strcmp(read_word, Urdu_UTF8) != 0):
                    self.strcpy(temp, self.roman_dict[mid])                    
                    k = 0
                    for i in range(0, self.strlen(temp)):
                        if temp[i] == 255:
                            if i < self.strlen(temp) - 1:
                                roman[k] = 32
                                k += 1
                                roman[k] = 0
                                k += 1
                            else:
                                continue
                        else:
                            if temp[i] == 254:
                                roman[k] = ord('-')
                                k += 1
                                roman[k] = 0
                                k += 1
                            else:
                                if temp[i] == 253:
                                    roman[k] = ord('.')
                                    k += 1
                                    roman[k] = 0
                                    k += 1
                                else:
                                    if  temp[i] == 249:
                                        roman[k] = ord('(')
                                        k+=1
                                        roman[k] = 0
                                        k+=1
                                    else:
                                        if  temp[i] == 250:
                                            roman[k] = ord(')')
                                            k+=1
                                            roman[k] = 0
                                            k+=1
                                        else:
                                            roman[k] = temp[i]
                                            k+=1
                                            roman[k] = 9
                                            k+=1
                    roman_size = k
                    return roman_size, 1
                if self.strcmp(read_word, Urdu_UTF8) < 0:
                    low = mid + 1
                else:
                    high = mid - 1
            

            self.convert_sindhi_urdu(Urdu_UTF8, sindhi)
            self.strcpy(Urdu_UTF8, sindhi)
            high = self.dict_word_count-1
            low=0
            while low <= high:
                mid = int((low+high)/2)
                self.strcpy(read_word, self.urdu_dict[mid])
                if  not (self.strcmp(read_word, Urdu_UTF8) != 0):
                    self.strcpy(temp, self.roman_dict[mid])
                    k=0
                    for i in range(0,self.strlen(temp)):
                        if temp[i]==255:
                            if i<self.strlen(temp)-1:
                                roman[k]=32
                                k+=1
                                roman[k] = 0
                                k+=1
                            else:
                                continue
                        else:
                            if temp[i]==254:
                                roman[k]=ord('-')
                                k+=1
                                roman[k] = 0
                                k+=1
                            else:
                                if temp[i]==253:
                                    roman[k]=ord('.')
                                    k+=1
                                    roman[k] = 0
                                    k+=1
                                else:
                                    if temp[i]==249:
                                        roman[k]=ord('(')
                                        k+=1
                                        roman[k] = 0
                                        k+=1
                                    else:
                                        if temp[i]==250:
                                            roman[k]=ord(')')
                                            k+=1
                                            roman[k] = 0
                                            k+=1
                                        else:
                                            roman[k]= temp[i]
                                            k+=1
                                            roman[k] = 9
                                            k+=1
                    roman_size = k
                    return roman_size, 1
                if self.strcmp(read_word, Urdu_UTF8)<0:
                  low=mid+1
                else:
                  high=mid-1
            return roman_size,0
    def check_post_word(self, urdu, p_urdu, urdu_size, p_urdu_size):
            post_dict=[0]*20
            for  i in range(0,len(post_dict)): 
                post_dict[i]=[0]*10
            Urdu_UTF8=[0]*40


            if  urdu_size == 0: return p_urdu_size,0
            total = 6
            post_dict[2][0] = post_dict[1][0] = post_dict[0][0] =175
            post_dict[5][0] = post_dict[4][0] = post_dict[3][0] =42
            post_dict[0][1] =210
            post_dict[3][1] =210
            post_dict[1][1] =204
            post_dict[4][1] =204
            post_dict[2][1] =39
            post_dict[5][1] =39
            post_dict[5][2] = post_dict[4][2] = post_dict[3][2] = post_dict[2][2] = post_dict[1][2] = post_dict[0][2] = 0
            self.UnicodeTo8(urdu, urdu_size, Urdu_UTF8)
            for  i in range(0,total): 
                if  not (self.strcmp(post_dict[i], Urdu_UTF8) != 0):
                    k=p_urdu_size
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
                if  not (self.strcmp(post_dict[i], Urdu_UTF8) != 0):
                    k = p_urdu_size
                    for i in range(0, urdu_size):
                        p_urdu[k] = urdu[i]
                        k+=1
                    p_urdu_size += urdu_size
                    return p_urdu_size, 2
            return p_urdu_size, 0

    def add_frequency(self, urdu, urdu_size):

            read_word=[0]*80
            Urdu_UTF8=[0]*40
            temp=[0]*80
            total = 0
            if  urdu_size <= 2: return 1
            self.UnicodeToUtf8(urdu, urdu_size, Urdu_UTF8)
            for  i in range(0,self.word_total): 
                if  not (self.strcmp(self.wordlist[i].word, Urdu_UTF8) != 0):
                    self.wordlist[i].count+=1
                    return 1
            self.wordlist[self.word_total].count = 1
            self.strcpy(self.wordlist[self.word_total].word, Urdu_UTF8)
            self.word_total+=1
            return 0
        

        
        
    def normalise_urdu(self, urdu, urdu_size):
            for  i in range(0,urdu_size,2): 
                if  (urdu[i] ==73) or (urdu[i] ==74):
                    urdu[i] =204

    def normalise_urdu_word(self, urdu, urdu_size):
            i=j = urdu_size
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
                        if  (urdu[i] ==193) and ((urdu[i + 2] ==84) or (urdu[i + 2] ==116)):
                            temp_urdu[j] =194
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
            urdu_size = j
            return urdu_size
    def normalise_text(self, urdu, urdu_size, temp_urdu, roman_size):
            


            j = 0

            for  i in range(0,urdu_size,2):
                if  (urdu[i] == 242) and (urdu[i + 1] == 253):
                    temp_urdu[j] = 68
                    j+=1
                    temp_urdu[j] = 6
                    j+=1
                    temp_urdu[j] = 68
                    j+=1
                    temp_urdu[j] = 6
                    j+=1
                    temp_urdu[j] = 193
                    j+=1
                    temp_urdu[j] = 6
                    j+=1
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
                                            if  (urdu[i] ==204) and (urdu[i + 2] ==84):
                                                temp_urdu[j] =38
                                                j+=1
                                                temp_urdu[j] = 6
                                                j+=1
                                                i += 2
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
            
            roman_size = j
            return roman_size


    def urdu_word_to_hindi(self, urdu_word, p_urdu, pp_urdu, urdu_word_size, p_urdu_size, pp_urdu_size, roman, roman_size, punc_flag):
        urdu = [0] * 256
        final_word = [0] * 16
        next_ch1 = 0
        next_ch2 = 0
        next_next_ch1 = 0
        next_next_ch2 = 0
        urdu_ptr = 0
        roman_ptr = 0
        flag = 0
        urdu_int_ptr = 0
        hindi_int_size = 0
        urdu_size = pp_urdu_size
        urdu_int = [0] * 128
        hindi_int = [0] * 128
        roman2 = [0] * 6
        for i in range(0, len(roman2)):
            roman2[i] = [0] * 40
        troman = [0] * 60
        hindi8 = [0] * 80
        refined = [0] * 40
        
    
        roman_size2 = [0] * 6
        wordc = 0
    
        if urdu_size == 0:
            roman_size = 0
            return roman_size,-1
    
        for i in range(0, urdu_size):
            urdu[i] = pp_urdu[i]
    
        if (urdu_size < 3) or (self.check_urdu_corpus(urdu, urdu_size)) > 0:
            self.urdu_corpus_count += 1
        if True:
            wordc += 1
            if wordc == 120:
                i = 0
            roman_size,returendFlag=self.check_urdu_word_trigram(urdu_word, p_urdu, pp_urdu, urdu_word_size, p_urdu_size, pp_urdu_size, roman, roman_size)
            if  returendFlag> 0:  
                self.word_found += 1
                return roman_size,3
            
            roman_size,returendFlag=self.check_urdu_word_bigram(p_urdu, pp_urdu, p_urdu_size, pp_urdu_size, roman, roman_size)
            if  returendFlag> 0:  
                self.bi_word_found += 1
                return roman_size,2
            roman_size,returendFlag=self.check_urdu_word_dictionary(urdu, urdu_size, roman, roman_size)
            if  returendFlag > 0:  
                self.word_found += 1
                roman[(roman_size)] = 0
                j = 0
                for i in range(0, roman_size):
                    if roman[i] == 0:
                        j += 1
                    if roman[i] == ord('-') and roman[i + 1] == 0:
                        j -= 1
                if j > 0:
                    j += 1
                    if j > 4:
                        j = 4
                    self.multi_count += j
                    self.merged_word_count += 1
                    self.total_merged_words[j] += 1
                return roman_size,1
        
        urdu_int_ptr = 0
        while urdu_ptr < urdu_size:
            ch = urdu[urdu_ptr]
            ch1 = urdu[urdu_ptr + 1]
            int1 = ch1
            int1 <<= 8
            int1 += ch
            urdu_ptr += 2
            urdu_int[urdu_int_ptr] = int1
            urdu_int_ptr += 1
    
        self.olda = 0
        self.corpus_flag = 1
        hindi_int_size=self.rule_based_urdu_word_to_hindi(urdu_int, int(urdu_size / 2), hindi_int, hindi_int_size)  
        hindi_int_size=self.improve_hindi_word(hindi_int, hindi_int_size)  
        if self.conversion_level < 1: self.corpus_flag = 0
        hindi_int_size,returendFlag=self.check_hindi_corpus(hindi_int, hindi_int_size, final_word)
        if self.corpus_flag > 0 and returendFlag > 0:  
    
            for i in range(0, self.strlen(final_word)):
                if final_word[i] == 113:
                    roman[(roman_size)] = ord('-')
                    roman_size += 1
                    roman[(roman_size)] = 0
                    roman_size += 1
                    continue
                roman[(roman_size)] = final_word[i]
                roman_size += 1
                roman[(roman_size)] = 9
                roman_size += 1
            self.corpus_found += 1
            roman[(roman_size)] = 0
            return roman_size,0
        words_found = 0
    
        if self.conversion_level < 3: self.corpus_flag = 0
        words_found,returendFlag=self.split_and_check_word_latest(urdu, urdu_size, roman2, roman_size2, words_found)
        if self.corpus_flag > 0 and returendFlag > 0:  
            j = 0
            for i in range(int(urdu_size / 2)):
                troman[j] = int(urdu_int[i] % 256)
                j += 1
                troman[j] = int(urdu_int[i] / 256)
                j += 1
    
    
            j = 0
            for i in range(hindi_int_size):
                troman[j] = int(hindi_int[i] % 256)
                j += 1
                troman[j] = int(hindi_int[i] / 256)
                j += 1
     
            for i in range(words_found):
                for j in range(roman_size2[i]):
                    roman[(roman_size)] = roman2[i][j]
                    roman_size += 1
                if i < words_found - 1:
                    roman[(roman_size)] = ord(' ')
                    roman_size += 1
                    roman[(roman_size)] = 0
                    roman_size += 1
            self.multi_count += words_found
            return roman_size,5
    
        self.add_frequency(urdu, urdu_size)
        urdu_int_ptr = 0
        while urdu_int_ptr < hindi_int_size:
            int1 = hindi_int[urdu_int_ptr]
            hindi8[urdu_int_ptr] = int(int1 % 256)
            urdu_int_ptr += 1
        hindi8[urdu_int_ptr] = 0
        urdu_int_ptr += 1
        self.new_refine_word(hindi8, refined)  
        self.strcpy(refined, hindi8)  
        urdu_int_ptr = 0
    
        while urdu_int_ptr < self.strlen(refined):  
            ch = refined[urdu_int_ptr]
            urdu_int_ptr += 1
            ch1 = 9
            urdu_ptr += 2
            if ch == 113:
                ch = ord('-')
                ch1 = 0
            roman[(roman_size)] = ch
            roman_size += 1
            roman[(roman_size)] = ch1
            roman_size += 1
    
        if urdu_size >= 2:
            self.word_not_found += 1
            j = 0
            for i in range(int(urdu_size / 2)):
                troman[j] = int(urdu_int[i] % 256)
                j += 1
                troman[j] = int(urdu_int[i] / 256)
                j += 1
            j = 0
            for i in range(hindi_int_size):
                troman[j] = int(hindi_int[i] % 256)
                j += 1
                troman[j] = int(hindi_int[i] / 256)
                j += 1
    
    
        return roman_size,0
    

    
    def improve_hindi_word(self, hindi_int, hindi_int_size):
        i = hindi_int_size - 1
        h = 9
        len = hindi_int_size
    
        if (i > 2) and (hindi_int[i - 2] == 2368) and (hindi_int[i - 1] == 2357) and (hindi_int[i] == 2306):
            hindi_int[i - 2] = 2351
            hindi_int[i - 1] = 2370
            hindi_int[i] = 2306
    
        if (i > 2) and (hindi_int[len - 2] == 2323) and (hindi_int[len - 1] == 2306):
            hindi_int[len - 2] = 2314
    
        if (i > 2) and (hindi_int[len - 2] == 2379) and (hindi_int[len - 1] == 2306):
            hindi_int[len - 2] = 2370
    
        if (i > 2) and (hindi_int[i - 1] == 2368) and (hindi_int[i] == 2357):
            hindi_int[i - 1] = 2351
            hindi_int[i] = 2379
    
        if (i > 2) and (hindi_int[i - 2] == 2368) and (hindi_int[i - 1] == 2357) and (
                hindi_int[i] == 2344):
            hindi_int[i - 2] = 2367
            hindi_int[i - 1] = 2351
            hindi_int[i] = 2370
            hindi_int[i + 1] = 2306
            hindi_int_size += 1
    
        if (i > 2) and (hindi_int[i - 2] == 2366) and (hindi_int[i - 1] == 2319) and (
                hindi_int[i] == 2357):
            hindi_int[i - 1] = 2351
            hindi_int[i] = 2379
    
        for i in range(2, hindi_int_size):
            if (hindi_int[i - 1] == 2344) and (
                    (hindi_int[i] >= 2340) and (hindi_int[i] <= 2343) or (hindi_int[i] == 2332)):
                hindi_int[i - 1] = 2306
    
    
        for i in range(1, hindi_int_size):
            if (self.check_hindi_matra(hindi_int[i - 1] % 256)) and (self.check_hindi_matra(hindi_int[i] % 256)):
                if not self.check_hindi_full_matra(hindi_int[i] % 256):
                    h <<= 8
                    hindi_int[i] = h + self.toggle_hindi_matra((hindi_int[i]))
    
        if (i > 2) and (hindi_int[len - 2] == 2323) and (hindi_int[len - 1] == 2306):
            hindi_int[len - 2] = 2314
        
        return hindi_int_size
    
    
    def check_hindi_full_matra(self, u):
        return (((u > 3) and (u < 11)) or ((u > 12) and (u < 21)))
    
    def convertToByte(self,u):
        u=u%256
        return u

    def toggle_hindi_matra(self, u):
        u = self.convertToByte(u)
        toggle_table = [0] * 256
        for i in range(0, 256):
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
        return (toggle_table[u])



    def UnicodeTo8(self, UnicodeString, UnicodePos, szOut):


            len = 0
            j = 0

            if  UnicodeString[1] == 6:
                self.normalise_urdu(UnicodeString, UnicodePos)
            for  i in range(0,UnicodePos,2):
                szOut[j] = UnicodeString[i]
                j+=1
            szOut[j] = 0
            j+=1
            return


    def UtoH(self, u, urdu_int, urdu_ptr, hindi_int, hindi_ptr):
        
        
        x = unicode
        hindi_chr = 0
        
        
        
        
        
        
        
        
        
        
        
        
        if urdu_ptr >= 2:
            oolda = urdu_int[urdu_ptr - 2]
        else:
            oolda = -1
        if u == 1570:  
            if self.olda > 0:
                return urdu_ptr,hindi_ptr, 2366
            else:
                return urdu_ptr,hindi_ptr, 2310  
        if hindi_ptr > 0:
            hindi_chr = hindi_int[hindi_ptr - 1]  
        else:
            hindi_ptr = 0
        
        if u == 1615:  
            urdu_ptr,hindi_ptr,returendFlag=(self.PESH_RULE(urdu_int, urdu_ptr, hindi_ptr))  
            return urdu_ptr,hindi_ptr, returendFlag
        if u == 1608:  
            urdu_ptr,hindi_ptr,returendFlag=self.VAO_RULE(urdu_int, urdu_ptr, hindi_int, hindi_ptr)  
            return urdu_ptr,hindi_ptr,returendFlag
        if u == 1746:  
            urdu_ptr,hindi_ptr,returendFlag=(self.BADI_YEH_RULE(urdu_int, urdu_ptr, hindi_ptr))  
            return urdu_ptr,hindi_ptr,returendFlag
        if u == 1740 or u == 1610:
            urdu_ptr,hindi_ptr,returendFlag=(self.CHOTI_YEH_RULE(urdu_int, urdu_ptr, hindi_int, hindi_ptr))  
            return urdu_ptr,hindi_ptr,returendFlag
        if u == 1729:  
            urdu_ptr,hindi_ptr,returendFlag=(self.CHOTI_HEH_RULE(urdu_int, urdu_ptr, hindi_int, hindi_ptr))  
            return urdu_ptr,hindi_ptr,returendFlag
        if u == 1593:
            urdu_ptr,hindi_ptr,returendFlag=(self.EIN_RULE(urdu_int, urdu_ptr, hindi_int, hindi_ptr))  
            return urdu_ptr,hindi_ptr,returendFlag
        if u == 1648:
            urdu_ptr,hindi_ptr,returendFlag=(self.KHARA_ZABAR_RULE(urdu_int, urdu_ptr, hindi_int, hindi_ptr))  
            return urdu_ptr,hindi_ptr,returendFlag
        if u == 1611:
            urdu_ptr,hindi_ptr,returendFlag= (self.DO_ZABAR_RULE(urdu_int, urdu_ptr, hindi_int, hindi_ptr))  
            return urdu_ptr,hindi_ptr,returendFlag
        if u == 1622:
            urdu_ptr,hindi_ptr,returendFlag=(self.KHARAZER_RULE(urdu_int, urdu_ptr, hindi_int, hindi_ptr))  
            return urdu_ptr,hindi_ptr,returendFlag
        
        if u == 1572 or u == 1574 or u == 1747 or u == 1730 or u == 1569:
            urdu_ptr,hindi_ptr,returendFlag=(self.HAMZA_RULE(u, urdu_int, urdu_ptr, hindi_int, hindi_ptr))  
            return urdu_ptr,hindi_ptr,returendFlag
        
        if u == 1606:  
            urdu_ptr,hindi_ptr,tmp = self.NUN_RULE(urdu_int, urdu_ptr, hindi_int, hindi_ptr)  
            if tmp != -1:
                return urdu_ptr,hindi_ptr,(tmp)
        if u == 1617:  
            urdu_ptr,hindi_ptr,returendFlag=(self.SHAAD_CONJUNCT_RULE(urdu_int, urdu_ptr, hindi_int, hindi_ptr))  
            return urdu_ptr,hindi_ptr,returendFlag
        
        if (u == 0x065b):
            return urdu_ptr,hindi_ptr, (self.JAZM_CONJUNCT_RULE())
        
        
        if self.checkMATRA(u):
            consonant_flag = ((hindi_chr == 2351) or (hindi_chr == 2357))
            if (not consonant_flag) and (((self.olda == 1722) and self.checkMATRA(oolda)) or (
                    self.olda == 32 or self.olda == 1748 or self.olda == 58 or self.olda == 8216 or self.olda == 8217 or self.olda == 46 or self.olda == 40 or self.olda == 34 or self.olda == 10 or self.olda == 45 or self.olda == 1548 or self.olda == 47 or self.olda == 92 or self.olda == 8216 or self.olda <= 0) or self.checkMATRA(self.olda)):  
                if u == 1570:
                    return urdu_ptr,hindi_ptr, 2310
                elif u == 1575:
                    return urdu_ptr,hindi_ptr, 2309
                elif u == 1616:
                    if self.olda == 1575:  
                        hindi_ptr -= 1
                    return urdu_ptr,hindi_ptr, 2311
                elif u == 1615:
                    return urdu_ptr,hindi_ptr, 2313
            else:  
                if u == 1570:
                    return urdu_ptr,hindi_ptr, 2366
                elif u == 1575:
                    return urdu_ptr,hindi_ptr, 2366
                elif u == 1616:
                    return urdu_ptr,hindi_ptr, 2367
                elif u == 1615:
                    return urdu_ptr,hindi_ptr, 2369
        
        
        
        
        return urdu_ptr,hindi_ptr, self.convert_urdu_hindi_char(u)
        
    def convert_urdu_hindi_char(self, u):
            c = int (u % 256)
            c1 = int (u / 256)
            table=[0]*256

            for  i in range(0,255): 
                table[i] = i

            if  (u < 10) or (u ==64):
                return 32
            table[14] = 0
            table[15] = 0
            table[20] = 0
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

            table[39] =5
            table[40] =44
            table[123] =127
            table[128] =45
            table[42] =36
            table[127] =37
            table[125] =31
            table[122] =32
            table[43] =56
            table[126] =42
            table[44] =28
            table[132] =124
            table[131] =30
            table[134] =26
            table[135] =27
            table[45] =57
            table[46] =89
            table[47] =38
            table[140] =39
            table[143] =126
            table[138] =33
            table[141] =34
            table[48] =91
            table[49] =48
            table[153] =92
            table[50] =91
            table[51] =56
            table[52] =54
            table[53] =56
            table[54] =91
            table[55] =36
            table[56] =91
            table[58] =90
            table[65] =94
            table[166] =43
            table[66] =88
            table[71] =57
            table[170] =21
            table[169] =22
            table[175] =23
            table[187] =123
            table[177] =25
            table[68] =50
            table[69] =46
            table[187] =35
            table[72] =53
            table[190] =57
            table[179] =123
            table[74] =47

            for  i in range(96,105+1):
                table[i] = (i + 6)
            for  i in range(240,249+1):
                table[i] = (i -138)
            table[133] =57
            if  c1 == 6:
                h = 9
            else:
                h = 0
            h <<= 8
            h += table[c]
            return h
    def checkMATRA(self, u):
            return (u ==1570 or u ==1575 or u ==1616 or u ==1615 or u ==1614 or u == 1740)  
    def PESH_RULE(self, urdu_int, urdu_ptr, hindi_ptr):    
        a = urdu_int[urdu_ptr + 1]
        if  a ==1608: 
            b = urdu_int[urdu_ptr + 2]
            if  b ==1614: 
                return urdu_ptr,hindi_ptr, 2357      
            if  self.olda ==1575: 
                hindi_ptr-=1 
                return urdu_ptr,hindi_ptr, 2314   
            else:
                return urdu_ptr,hindi_ptr, 2370   
        self.corpus_flag = 0
        if self.olda == 1575:
            hindi_ptr-=1 
            return urdu_ptr,hindi_ptr, 2313
        
        else:
            return urdu_ptr,hindi_ptr, 2369 

    def VAO_RULE(self, urdu_int, urdu_ptr, hindi_int, hindi_ptr):
            if  urdu_ptr >= 2:
                oolda = urdu_int[urdu_ptr - 2]
            else:
                oolda = -1

            if  self.olda ==1614: 

                if (oolda == 1575):
                    hindi_ptr-=1
                    return urdu_ptr,hindi_ptr, 2324   
                else:
                    return urdu_ptr,hindi_ptr, 2380  
        
            if  self.olda <= 0 or self.olda ==32 or self.olda ==1608 or self.olda ==1748 or self.olda ==58 or self.olda ==8216 or self.olda ==8217 or self.olda ==46 or self.olda ==40 or self.olda ==34 or self.olda ==10 or self.olda ==47 or self.olda ==92 or self.olda ==45 or self.olda ==8216:
                return urdu_ptr,hindi_ptr, 2357 
            elif  (self.checkMATRA(self.olda) and self.olda !=1615 and self.olda !=1614 and self.olda !=1575): 
                return urdu_ptr,hindi_ptr, 2357 
            elif  self.olda ==1740 or self.olda ==1610 or self.olda ==1746:  
                return urdu_ptr,hindi_ptr, 2357
            else:  
                b = urdu_int[urdu_ptr + 1]
            
                if (b ==1615):
                    self.olda = b
                    self.PROTECTOLDA = 1
                if  b ==1614:
                    return urdu_ptr,hindi_ptr, 2357
                elif  b ==1593 or b ==1746 or self.checkMATRA(b): 
                    self.olda = b
                    return urdu_ptr,hindi_ptr, 2357 

                elif  b ==1740 or b ==1610:

                    return urdu_ptr,hindi_ptr, 2357
                if ((hindi_ptr > 0 and hindi_int[hindi_ptr - 1] != 0x093e) and (self.olda == 0x0627 or self.olda == 0x0639)):
                
                    hindi_ptr -=1
                    return urdu_ptr,hindi_ptr, 2323
                else:
                    if ((hindi_ptr > 0 and hindi_int[hindi_ptr - 1] != 0x093e) and (self.olda == 0x064f)):
                        
                        hindi_ptr -= 1
                        return urdu_ptr,hindi_ptr, 2370
                    else:
                        if  (hindi_int[hindi_ptr - 1] ==2366):
                            return urdu_ptr,hindi_ptr, 2357
                        else:
                            return urdu_ptr,hindi_ptr, 2379 
        
    def BADI_YEH_RULE(self, urdu_int, urdu_ptr, hindi_ptr):

            if  urdu_ptr >= 2:
                oolda = urdu_int[urdu_ptr - 2]
            else:
                oolda = -1

            b = urdu_int[urdu_ptr + 1]
            if  self.olda ==1614:     
                if  b ==1569:  
                    urdu_ptr+=1 
                    return urdu_ptr,hindi_ptr, 2319
                if  b ==1614:  
                    urdu_ptr+=1
                    return urdu_ptr,hindi_ptr, 2351 


                if  oolda ==1575:  
                    hindi_ptr-=1
                    return urdu_ptr,hindi_ptr, 2320
                return urdu_ptr,hindi_ptr, 2376  
            elif  self.olda ==1575:  
                return urdu_ptr,hindi_ptr, 2319
            elif  self.olda ==32 or self.olda ==1593 or self.olda ==1740 or self.olda ==1610 or self.checkMATRA(self.olda):  
                return urdu_ptr,hindi_ptr, 2319

            if  self.checkMATRA(b):  
                return urdu_ptr,hindi_ptr, 2351
            elif  b ==1746: 
                return urdu_ptr,hindi_ptr, 2351 

            return urdu_ptr,hindi_ptr, 2375  
    def CHOTI_YEH_RULE(self, urdu_int, urdu_ptr, hindi_int, hindi_ptr):
            if  urdu_ptr >= 2:
                oolda = urdu_int[urdu_ptr - 2]
            else:
                oolda = -1
            b = urdu_int[urdu_ptr + 1]
            if  self.olda ==1575 and (b ==1575 or b ==1729):   
                return urdu_ptr,hindi_ptr, 2351
            if  b == 1620: 
                urdu_ptr+=1
                return urdu_ptr,hindi_ptr, 2319
            if  b ==1620:
                urdu_ptr+=1
                return urdu_ptr,hindi_ptr, 2312
            if  (self.olda ==1575 and (b !=1620)):   
                if  hindi_ptr < 2:
                    hindi_ptr-=1
                return urdu_ptr,hindi_ptr, 2319

            if  self.olda == 1616:    
                hindi_ptr-=1
                return urdu_ptr,hindi_ptr, 2368 
            if  self.olda <= 0 or self.olda ==32 or self.olda ==1748 or self.olda ==58 or self.olda ==8216 or self.olda ==8217 or self.checkMATRA(self.olda) or self.olda ==46 or self.olda ==40 or self.olda ==10 or self.olda ==34 or self.olda ==47 or self.olda ==92 or self.olda ==45 or self.olda ==8216:  
                return urdu_ptr,hindi_ptr, 2351
            if  self.olda ==1648:
                return urdu_ptr,hindi_ptr, 2312
            if  self.olda ==1729:
                return urdu_ptr,hindi_ptr, 2368

            if  self.checkMATRA(b) or b ==1648 or self.olda <= 0 or self.olda ==32 or self.olda ==1748 or self.olda ==58 or self.olda ==8216 or self.olda ==8217 or self.olda ==46 or self.olda ==40 or self.olda ==34 or self.olda ==1548 or self.olda ==10 or self.olda ==47 or self.olda ==92 or self.olda ==45 or self.olda ==8216:   
                if  b == 1575:
                    hindi_int[hindi_ptr] =2351
                    urdu_ptr+=1
                    hindi_ptr+=1
                    return urdu_ptr,hindi_ptr, 2366
                else:
                    return urdu_ptr,hindi_ptr, 2351

            if  self.olda ==1605 and (oolda <= 0 or oolda ==32 or oolda ==1748 or oolda ==58 or oolda ==8216 or oolda ==8217 or oolda ==46 or oolda ==40 or oolda ==34 or oolda ==10 or oolda ==47 or oolda ==92 or oolda ==45 or oolda ==8216 or oolda ==1548) and b ==1722: 
                return urdu_ptr,hindi_ptr, 2375
                return urdu_ptr,hindi_ptr, 2376
            if  b ==1620:
                urdu_ptr+=1
                return urdu_ptr,hindi_ptr, 2311
            return urdu_ptr,hindi_ptr, 2368  
    def CHOTI_HEH_RULE(self, urdu_int, urdu_ptr, hindi_int, hindi_ptr):

            b = urdu_int[urdu_ptr + 1]
            if  urdu_ptr >= 2:
                oolda = urdu_int[urdu_ptr - 2]
            else:
                oolda = -1

            if  self.checkMATRA(self.olda) or self.olda ==1608 or self.olda ==1593 or self.olda ==1740 or self.olda ==1610 or self.olda ==32 or self.olda ==1748 or self.olda ==58 or self.olda ==8216 or self.olda ==8217 or self.olda ==46 or self.olda ==40 or self.olda ==34 or self.olda ==10 or self.olda ==47 or self.olda ==92 or self.olda ==45 or self.olda ==8216 or (self.checkMATRA(b) and b != 0):  
                return urdu_ptr,hindi_ptr, 2361   

            if  b ==1615:  
                urdu_ptr+=1
                hindi_int[(hindi_ptr)] =2361
                hindi_ptr+=1
                return urdu_ptr,hindi_ptr, 2370  


            if  b ==1622:  
                urdu_ptr+=1
                hindi_int[(hindi_ptr)] =2361
                hindi_ptr+=1
                return urdu_ptr,hindi_ptr, 2368

            if (self.olda == 0x06a9 and oolda == 0x0020):
                return urdu_ptr,hindi_ptr, 2375
        
            if (not (b != 0) or b == 0x0020 or b == 0x06d4 or b == 0x003a or b == 0x2018 or b == 0x2019 or b == 0x002e or b == 0x0028 or b == 0x0022 or b == 0x000a or b == 0x002f or b == 0x005c or b == 0x002d or b == 0x2018 or b == 0x060c):
                return urdu_ptr,hindi_ptr, 2366

            return urdu_ptr,hindi_ptr, 2361    
    def EIN_RULE(self, urdu_int, urdu_ptr, hindi_int, hindi_ptr):

















            b = urdu_int[urdu_ptr + 1]
            bb = urdu_int[(urdu_ptr) + 2]
            if  urdu_ptr >= 2:
                oolda = urdu_int[urdu_ptr - 2]
            else:
                oolda = -1


            if  self.olda ==1575 and (b ==1740 or b ==1610): 
                urdu_ptr+=1
                return urdu_ptr,hindi_ptr, 2312
            if  self.olda ==1575 and b ==1575:    
                urdu_ptr+=1
                return urdu_ptr,hindi_ptr, 2310
                hindi_ptr-=1
                return urdu_ptr,hindi_ptr, 2310
            if  (self.checkMATRA(self.olda) or self.olda ==1740) and b ==1575: 
                urdu_ptr+=1
                return urdu_ptr,hindi_ptr, 2310

            if  (b ==1614 and (bb !=1608 and bb !=1746)) or (self.checkMATRA(self.olda) or self.olda == 1574): 

                return urdu_ptr,hindi_ptr, 2309

            if  b ==1740 or b ==1610:   
                urdu_ptr+=1
                return urdu_ptr,hindi_ptr, 2312
            if  (self.olda ==1740 or self.olda ==1610) and oolda ==32: 
                hindi_ptr-=1 
                return urdu_ptr,hindi_ptr, 2351   

            if  self.olda ==1740 or self.olda ==1610:   
                hindi_ptr-=1 
                return urdu_ptr,hindi_ptr, 2368
            if  b ==1616:     
                urdu_ptr+=1 
                return urdu_ptr,hindi_ptr, 2311
            if  b ==1746:      
                urdu_ptr+=1  
                return urdu_ptr,hindi_ptr, 2375
            if  b ==1614 and bb ==1746: 
                urdu_ptr+=2
                return urdu_ptr,hindi_ptr, 2320


            if  ((self.checkMATRA(oolda) or oolda <= 0 or oolda ==32 or oolda ==1748 or oolda ==58 or oolda ==8216 or oolda ==8217 or oolda ==46 or oolda ==40 or oolda ==34 or oolda ==10 or oolda ==47 or oolda ==92 or oolda ==45 or oolda ==8216) and self.olda ==1575) or ((self.olda <= 0 or self.olda ==32 or self.olda ==1748 or self.olda ==58 or (self.olda <= 0) or self.olda ==8216 or self.olda ==8217 or self.olda ==46 or self.olda ==40 or self.olda ==34 or self.olda ==10 or self.olda ==47 or self.olda ==92 or self.olda ==1575 or self.olda ==1740 or self.checkMATRA(self.olda)) and b ==1575):   
                if  self.olda ==1575: 
                    hindi_ptr-=1

                if  b ==1575 and (bb ==1740 or bb ==1610): 
                    urdu_ptr+=1
                    urdu_ptr+=1
                    hindi_int[(hindi_ptr)] =2310
                    hindi_ptr+=1
                    return urdu_ptr,hindi_ptr, 2351 

                if  b ==1575:      
                    urdu_ptr+=1
                    if  self.olda <= 0:
                        return urdu_ptr,hindi_ptr, 2310
                    hindi_int[(hindi_ptr)] =2366
                    hindi_ptr+=1
                    return urdu_ptr,hindi_ptr, 2309


                return urdu_ptr,hindi_ptr, 2310

            if  b ==1608 and bb ==1615: 
                urdu_ptr+=1
                urdu_ptr+=1
                return urdu_ptr,hindi_ptr, 2314  
            if  oolda ==1608 and self.olda ==1615: 
                hindi_ptr-=1
                return urdu_ptr,hindi_ptr, 2370 



            if  b ==1615:  
                urdu_ptr+=1 
                return urdu_ptr,hindi_ptr, 2313 
            if  b ==1614 and bb ==1608: 

                urdu_ptr+=1
                urdu_ptr+=1 
                return urdu_ptr,hindi_ptr, 2324
            if  (self.olda > 0) and (b ==1729 or b ==1575):   
                urdu_ptr+=1  
                return urdu_ptr,hindi_ptr, 2366
            if  self.olda ==1608:
                return urdu_ptr,hindi_ptr, 2366
            if  self.olda <= 0 or self.olda ==32 or self.olda ==1748 or self.olda ==58 or self.olda ==8216 or self.olda ==8217 or self.olda ==46 or self.olda ==40 or self.olda ==34 or self.olda ==10 or self.olda ==47 or self.olda ==92 or self.olda ==45 or self.olda ==8216:  
                return urdu_ptr,hindi_ptr, 2309


            return urdu_ptr,hindi_ptr, 2366 
    def KHARA_ZABAR_RULE(self, urdu_int, urdu_ptr, hindi_int, hindi_ptr):
            b = urdu_int[urdu_ptr + 1]
            if  urdu_ptr >= 2:
                oolda = urdu_int[urdu_ptr - 2]
            else:
                oolda = -1

            if  (self.olda ==1746 or self.olda ==1740 or self.olda ==1610) and (b ==32 or not b != 0): 
                hindi_ptr-=1
                return urdu_ptr,hindi_ptr, 2366

            if  not self.checkMATRA(self.olda) and self.olda !=1746: 
                return urdu_ptr,hindi_ptr, 2366
            return urdu_ptr,hindi_ptr, 2366  

    def NUN_RULE(self, urdu_int, urdu_ptr, hindi_int, hindi_ptr):
        a = 0
        b = 0
        b = urdu_int[urdu_ptr + 1]
        if  urdu_ptr > 0:
            a = urdu_int[urdu_ptr - 1]

        if  b ==1624:   
            urdu_ptr+=1
            return urdu_ptr,hindi_ptr, 2306

        if  (a ==1740) or (a ==1572) or (a ==1608):   
            if  (not ((b ==1740) or (b ==1572) or (b ==1575) or (b ==1608))):
                return urdu_ptr,hindi_ptr, 2306

        return urdu_ptr,hindi_ptr, -1

    def SHAAD_CONJUNCT_RULE(self, urdu_int, urdu_ptr, hindi_int, hindi_ptr):
            halant =2381



            hindi_int[(hindi_ptr)] = halant
            hindi_ptr+=1
            urdu_ptr,hindi_ptr,returendFlag=self.UtoH(self.olda,  urdu_int, urdu_ptr,  hindi_int, hindi_ptr)
            return urdu_ptr,hindi_ptr, (returendFlag) 
    def JAZM_CONJUNCT_RULE(self, ):
            return 2381  
    def DO_ZABAR_RULE(self, urdu_int, urdu_ptr, hindi_int, hindi_ptr):
            hindi_ptr-=1
            return urdu_ptr,hindi_ptr, 2344 
    def HAMZA_RULE(self, u, urdu_int, urdu_ptr, hindi_int, hindi_ptr):
        k = 0
        
        
        
        b = urdu_int[urdu_ptr + 1]
        if  urdu_ptr >= 2:
            oolda = urdu_int[urdu_ptr - 2]
        else:
            oolda = -1
        if  urdu_ptr >= 1:
            self.olda = urdu_int[urdu_ptr - 1]
        else:
            self.olda = -1
        
        if  (u ==1572) and (self.olda ==1608):
            return urdu_ptr,hindi_ptr, 2323
        if  u ==1572:
            return urdu_ptr,hindi_ptr, 2314
        if  (u == 1574) and (b == 1575):
            urdu_ptr+=1
            return urdu_ptr,hindi_ptr, 2310
        hindi_ptr-=1  
        
        if  self.olda ==1570 or self.olda ==1575 or self.olda ==1729:  
            if  (oolda ==32) or (oolda <= 0):
                if  self.olda ==1570:
                    k =2310
                elif  self.olda ==1575:
                    k =2309
                elif  self.olda ==1729:
                    k =2361
            else:
                k =2366
        
        
        elif  (self.olda ==1608) and (oolda > 0):     
            if  oolda ==1615:   
                k =2370
            elif  oolda ==1614:  
                k =2380
            elif  oolda ==1740: 
                k =2357
            else:
                k =2379
        
        elif  self.olda ==1740 or self.olda ==1610:    
            if  oolda ==1575:
                hindi_ptr-=1
                k =2312
            else:
                k =2368
        elif  self.olda ==1746:        
            if  oolda ==1614:   
                k =2376
            else:
                k =2375
        
        if  (k != 0) and (hindi_ptr >= 0):
            hindi_int[(hindi_ptr)] = k
            hindi_ptr+=1
        
        urdu_ptr+=1
        if  k == 0:
            hindi_ptr+=1
        if  (self.olda ==1740 or self.olda ==1610) and b ==1746:   
            return urdu_ptr,hindi_ptr, 2319
        
        bb = urdu_int[(urdu_ptr)]
        if  (b ==1740 or b ==1610) and bb ==1575: 
            return urdu_ptr,hindi_ptr, 2351      
        
        
        if  b ==1616:       
            return urdu_ptr,hindi_ptr, 2311
        
        if  b ==1740:       
            return urdu_ptr,hindi_ptr, 2312
        
        
        if  b ==1608:       
            return urdu_ptr,hindi_ptr, 2323
        
        if  b ==1746:       
            return urdu_ptr,hindi_ptr, 2319
        if  b ==1614:       
            return urdu_ptr,hindi_ptr, 2309
        if  b ==1616:       
            return urdu_ptr,hindi_ptr, 2311
        if  b ==1615:       
            return urdu_ptr,hindi_ptr, 2313
        
        if  b ==1610:       
            return urdu_ptr,hindi_ptr, 2312
        
        
        
        
        if  u ==1730:
            hindi_int[(hindi_ptr)] =2366
            hindi_ptr+=1
            hindi_int[(hindi_ptr)] =2417
            hindi_ptr+=1
            hindi_int[(hindi_ptr)] =2319
            hindi_ptr+=1
            return urdu_ptr,hindi_ptr, 2417
        
        if  k != 0:
            urdu_ptr-=1
            if  u ==1572:    
                return urdu_ptr,hindi_ptr, 2323  
            return urdu_ptr,hindi_ptr, 2311
        else:
            if  u ==1574:
                urdu_ptr-=1
                return urdu_ptr,hindi_ptr, 2309
            else:
                urdu_ptr,hindi_ptr,returendFlag=self.UtoH(b,  urdu_int, urdu_ptr,  hindi_int, hindi_ptr)
                return urdu_ptr,hindi_ptr, (returendFlag)

    def KHARAZER_RULE(self, urdu_int, urdu_ptr, hindi_int, hindi_ptr):

            if  urdu_ptr >= 2:
                oolda = urdu_int[urdu_ptr - 2]
            else:
                oolda = -1
            if  (self.olda ==1740 or self.olda ==1610) and oolda ==1575:
                hindi_ptr-=1
                hindi_ptr-=1
                return urdu_ptr,hindi_ptr, 2312
            else:
                return urdu_ptr,hindi_ptr, 2368
    def generate_normalized_corpus(self):
        pass





    def read_binary_corpus(self, corpus_words, corpus_word_count):
        FILE_NAME = self.appPath + "fcorpus.bin"
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return corpus_word_count
    
        r= open(FILE_NAME, 'rb')
        corpus_word_count = int.from_bytes(r.read(4), 'little')

        for  i in range(0,corpus_word_count):
            rawBytes = r.read(16)
            for j, byte in enumerate(rawBytes):
                self.corpus_words[i].original_word[j] = byte
             
            rawBytes = r.read(16)
            for j, byte in enumerate(rawBytes):
                self.corpus_words[i].normalised_word[j] = byte

            
            self.corpus_words[i].freq = int.from_bytes(r.read(4), 'little')
            
        r.close()
        
        self.isBinCorpus = True
        return corpus_word_count
    def read_bigram_corpus(self, bigrams, bigram_total, bigram_index1, bigram_index_count):
        FILE_NAME = self.appPath + "normal_bigrams.bin"
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return
        
        FILE_NAME1 = self.appPath + "bigrams.bin"
        if not os.path.exists(FILE_NAME1):
            self.printMSG("File not exists! " + FILE_NAME1)
            return
        
        r1 = open(FILE_NAME1, 'rb')
        bigram_total = int.from_bytes(r1.read(4), 'little')
        for i in range(0, bigram_total):
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
        for i in range(0, bigram_total):
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


    def read_ignore_words(self, ):
            


        FILE_NAME = self.appPath + "ignore.bin"
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return
        
        r = open(FILE_NAME, 'rb')
        self.ignore_word_count = int.from_bytes(r.read(4), 'little')
        for i in range(0, self.ignore_word_count):
            rawBytes = r.read(len(self.ignore[i]))
            for j, byte in enumerate(rawBytes):
                self.ignore[i][j] = byte
        r.close()
    def read_urdu_corpus(self, ):
    
        Buffer = ""
        str = ""
        FILE_NAME = self.appPath + "ucorpus.bin"


        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return	
            
        r = open(FILE_NAME, 'rb')
        self.urdu_corpus_word_count = int.from_bytes(r.read(4), 'little')
        for  i in range(0,self.urdu_corpus_word_count):
            rawBytes = r.read(len(self.urdu_corpus_words[i]))
            for j, byte in enumerate(rawBytes):
                self.urdu_corpus_words[i].original_word[j] = byte
            
            self.urdu_corpus_words[i].freq = int.from_bytes(r.read(4), 'little')
            if  i <= 50:
                f = self.urdu_corpus_words[i].freq
                str = ""
                for  n in range(0,len(self.urdu_corpus_words[i].original_word)):
                    if  self.urdu_corpus_words[i].original_word[n] == 0: break
                    str = str + self.urdu_corpus_words[i].original_word[n]
                Buffer = Buffer + str + "\n"
            r.close()
            

    def read_pre_bigram_corpus(self, pre_bigram, pre_bigram_total, pre_bigram_index, pre_bigram_index_count):
        pre_count = 0
        corpus_word=[0]*200
        freq=[0]*8
        word=[0]*20
        t_corpus=bigram_corpus()
        word[0] = 0
        FILE_NAME = self.appPath + "pre_bigram.bin"
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return pre_bigram_total, pre_bigram_index_count
        
        r = open(FILE_NAME, 'rb')
        pre_bigram_total = int.from_bytes(r.read(4), 'little')
        for i in range(0, pre_bigram_total):
            try:
                rawBytes = r.read(len(pre_bigram[i].first_word))
                for j, byte in enumerate(rawBytes):
                    pre_bigram[i].first_word[j] = byte
                
                rawBytes = r.read(len(pre_bigram[i].second_word))
                for j, byte in enumerate(rawBytes):
                    pre_bigram[i].second_word[j] = byte
                
                pre_bigram[i].freq = int.from_bytes(r.read(4), 'little')
                pre_bigram[i].unigram_freq = int.from_bytes(r.read(4), 'little')
            except:
                break
        r.close()
        
        
        FILE_NAME = self.appPath + "pre_normal_bigram.bin"
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return pre_bigram_total, pre_bigram_index_count
        
        r = open(FILE_NAME, 'rb')
        pre_bigram_index_count = int.from_bytes(r.read(4), 'little')
        pre_bigram_index_count = 0
        for i in range(0, pre_bigram_total):
            
            try:
                rawBytes = r.read(len(pre_bigram_index[i].normalised_word))
                for j, byte in enumerate(rawBytes):
                    pre_bigram_index[i].normalised_word[j] = byte
                readValue = r.read(4)
                pre_bigram_index[i].index = int.from_bytes(readValue, 'little')
                if readValue:
                    pre_bigram_index_count += 1
                else:
                    break
            except:
                break
        r.close()
        
        self.isPreBinCorpus = True
        return pre_bigram_total, pre_bigram_index_count




    def read_pre_trigram_corpus(self, pre_trigram, pre_trigram_total, pre_trigram_index, pre_trigram_index_count):
        
        FILE_NAME = self.appPath + "pre_trigram.bin"
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return pre_trigram_total,pre_trigram_index_count
        
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
        
        FILE_NAME = self.appPath + "pre_normal_trigram.bin"
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return pre_trigram_total,pre_trigram_index_count
        
        r = open(FILE_NAME, 'rb')
        pre_trigram_index_count = int.from_bytes(r.read(4), 'little')
        pre_trigram_index_count = 0
        for i in range(0, pre_trigram_total):
            try:
                rawBytes = r.read(len(pre_trigram_index[i].normalised_word))
                for j, byte in enumerate(rawBytes):
                    pre_trigram_index[i].normalised_word[j] = byte
                readValue = r.read(4)
                pre_trigram_index[i].index = int.from_bytes(readValue, 'little')
                if readValue:
                    pre_trigram_index_count += 1
                else:
                    break
            except:
                break
        
        r.close()
        return pre_trigram_total, pre_trigram_index_count





    def read_mid_trigram_corpus(self, mid_trigram, mid_trigram_total, mid_trigram_index, mid_trigram_index_count):
        pre_count = 0
        corpus_word=[0]*200
        freq=[0]*8
        word=[0]*20
        t_corpus=bigram_corpus
        word[0] = 0

        
        FILE_NAME = self.appPath + "mid_trigram.bin"
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return mid_trigram_total, mid_trigram_index_count
        
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
        
        FILE_NAME = self.appPath + "mid_normal_trigram.bin"
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return mid_trigram_total, mid_trigram_index_count
        
        r = open(FILE_NAME, 'rb')
        mid_trigram_index_count = int.from_bytes(r.read(4), 'little')
        mid_trigram_index_count = 0
        
        for i in range(0, mid_trigram_total):
            try:
                rawBytes = r.read(len(mid_trigram_index[i].normalised_word))
                for j, byte in enumerate(rawBytes):
                    mid_trigram_index[i].normalised_word[j] = byte
                readValue = r.read(4)
                mid_trigram_index[i].index = int.from_bytes(readValue, 'little')
                if readValue:
                    mid_trigram_index_count += 1
                else:
                    break
            
            except:
                break
        r.close()
        return mid_trigram_total, mid_trigram_index_count





    def read_post_bigram_corpus(self, post_bigram, post_bigram_total, post_bigram_index, post_bigram_index_count):
        post_count = 0
        corpus_word=[0]*200
        freq=[0]*8
        word=[0]*20
        t_corpus=bigram_corpus
        word[0] = 0
        
        FILE_NAME = self.appPath + "post_bigram.bin"
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return post_bigram_total,post_bigram_index_count
        
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
        
        FILE_NAME = self.appPath + "post_normal_bigram.bin"
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return post_bigram_total,post_bigram_index_count
        
        r = open(FILE_NAME, 'rb')
        post_bigram_index_count = int.from_bytes(r.read(4), 'little')
        post_bigram_index_count = 0
        
        for i in range(0, post_bigram_total):
            try:
                rawBytes = r.read(len(post_bigram_index[i].normalised_word))
                for j, byte in enumerate(rawBytes):
                    post_bigram_index[i].normalised_word[j] = byte
                readValue = r.read(4)
                post_bigram_index[i].index = int.from_bytes(readValue, 'little')
                if readValue:
                    post_bigram_index_count += 1
                else:
                    break
            except:
                break
        
        r.close()
        self.isPostBinCorpus = True
        return post_bigram_total, post_bigram_index_count
            




    def read_post_trigram_corpus(self, post_trigram, post_trigram_total, post_trigram_index, post_trigram_index_count):
        pre_count = 0
        corpus_word=[0]*200
        freq=[0]*8
        word=[0]*20
        t_corpus=bigram_corpus
        word[0] = 0


        FILE_NAME = self.appPath + "post_trigram.bin"
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return post_trigram_total, post_trigram_index_count
        
        r = open(FILE_NAME, 'rb')
        post_trigram_total = int.from_bytes(r.read(4), 'little')
        for i in range(0, post_trigram_total):
            rawBytes = r.read(len(post_trigram[i].first_word))
            for j, byte in enumerate(rawBytes):
                post_trigram[i].first_word[j] = byte
            
            rawBytes = r.read(len(post_trigram[i].second_word))
            for j, byte in enumerate(rawBytes):
                post_trigram[i].second_word[j] = byte
            
            rawBytes = r.read(len(post_trigram[i].third_word))
            for j, byte in enumerate(rawBytes):
                post_trigram[i].third_word[j] = byte
            
            post_trigram[i].freq = int.from_bytes(r.read(4), 'little')
        
        r.close()
        FILE_NAME = self.appPath + "post_normal_trigram.bin"
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return post_trigram_total, post_trigram_index_count
        
        r = open(FILE_NAME, 'rb')
        post_trigram_index_count = int.from_bytes(r.read(4), 'little')
        post_trigram_index_count = 0
        for i in range(0, post_trigram_total):
            try:
                rawBytes = r.read(len(post_trigram_index[i].normalised_word))
                for j, byte in enumerate(rawBytes):
                    post_trigram_index[i].normalised_word[j] = byte
                readValue = r.read(4)
                post_trigram_index[i].index = int.from_bytes(readValue, 'little')
                if readValue:
                    post_trigram_index_count += 1
                else:
                    break
            except:
                break
        return post_trigram_total, post_trigram_index_count





    def read_sindhi_hindi_dict(self, ):
        dic_word=[0]*40
        freq=[0]*8
    
        FILE_NAME = os.path.join(self.appPath + "dict.bin")
        
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return
        
        r = open(FILE_NAME, 'rb')
        self.dict_word_count = int.from_bytes(r.read(4), 'little')
        for i in range(0, self.dict_word_count):
            rawBytes = r.read(len(self.urdu_dict[i]))
            for j, byte in enumerate(rawBytes):
                self.urdu_dict[i][j] = byte
            
            rawBytes = r.read(len(self.roman_dict[i]))
            for j, byte in enumerate(rawBytes):
                self.roman_dict[i][j] = byte
            
            if i == 23502:
                self.strcpy(dic_word, self.urdu_dict[i])
            self.strcpy(dic_word, self.roman_dict[i])
        r.close()
        self.isDic = True
    
    def read_urdu_bigram(self, ):
        FILE_NAME = self.appPath + "BigramUrdu.bin"
        
        if not os.path.exists(FILE_NAME):
            self.printMSG("File not exists! " + FILE_NAME)
            return
        
        r = open(FILE_NAME, 'rb')
        self.urdu_bigram_total = int.from_bytes(r.read(4), 'little')
        
        for i in range(0, self.urdu_bigram_total):
            rawBytes = r.read(len(self.urdu_bigram[i].urdu1))
            for j, byte in enumerate(rawBytes):
                self.urdu_bigram[i].urdu1[j] = byte
            
            rawBytes = r.read(len(self.urdu_bigram[i].urdu2))
            for j, byte in enumerate(rawBytes):
                self.urdu_bigram[i].urdu2[j] = byte
            
            rawBytes = r.read(len(self.urdu_bigram[i].hindi))
            for j, byte in enumerate(rawBytes):
                self.urdu_bigram[i].hindi[j] = byte
        
        r.close()
        self.isUrduBigram = True
    def get_corpus_pos(self, corpus_words, count, hindi_word):
        for i in range(count - 1, -1, -1):
            if  self.strcmp(self.corpus_words[i].normalised_word, hindi_word) <= 0:
                return i
        return 0
    def search_corpus(self, corpus_words, total, hindi_word):

            high = total - 1
            low = 0
            mid = 0
            read_word=[0]*15

            while  low <= high:
                mid = int((low + high) / 2)
                self.strcpy(read_word, self.corpus_words[mid].normalised_word)
                if  self.strcmp(read_word, hindi_word) == 0:
                    return mid
                if  self.strcmp(read_word, hindi_word) < 0:
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
    def generate_words(self, hindi, size, hindi_words, word_count):
            ptr = 0
            hindi_ptr = 0
            flag = 0
            hindi_word_size = 0
            hindi_word=[0]*15
            word_count = 0
        
            if  not(hindi_word_size != 0):
                for  i in range(0,15): 
                    hindi_word[i] = 0
            while  hindi_ptr < size:
                ch = hindi[hindi_ptr]
                ch1 = hindi[hindi_ptr + 1]
                if  flag == 1 or self.check_hindi_punctuation(ch, ch1) > 0:
                    if  hindi_word_size > 0:
                        for  i in range(0,hindi_word_size+1): 
                            hindi_words[word_count][i] = hindi_word[i]
                        word_count+=1
                        hindi_word_size = 0
                        for  i in range(0,15): 
                            hindi_word[i] = 0
                        flag = 0
                else:
                    hindi_word[hindi_word_size] = ch
                    hindi_word_size+=1
                    if  hindi_word_size > 13: flag = 1
                hindi_ptr += 2
            return 0
    def get_freq_corpus(self, hindi_int, hindi_int_size, corpus_pos):
            multi = 0
            hindi_word=[0]*20
            first_hindi_word=[0]*16
            rest_hindi_word=[0]*16


            self.normalise_hindi_word(hindi_int, hindi_int_size, hindi_word)
            if  multi > 0:
                self.normalise_hindi_word(hindi_int, multi, first_hindi_word)
            pos = self.search_corpus(self.corpus_words, self.corpus_word_count, first_hindi_word)
            if  pos < 0: return 0
            corpus_pos = pos
            low = high = pos
            return self.corpus_words[pos].freq
    def get_word_corpus(self, hindi_int, hindi_int_size, final_word):
            multi = 0
            hindi_word=[0]*20
            first_hindi_word=[0]*16
            rest_hindi_word=[0]*16
            word_size = 0
            final_word[0] = 0
            self.normalise_hindi_word(hindi_int, hindi_int_size, hindi_word)
            if  multi > 0:
                self.normalise_hindi_word(hindi_int, multi, first_hindi_word)
            pos = self.search_corpus(self.corpus_words, self.corpus_word_count, first_hindi_word)
            if  pos < 0: return 0
            self.strcpy(final_word, self.corpus_words[pos].original_word)
            if  multi > 0:
                self.strcat(final_word, rest_hindi_word)
            return 1


    def check_hindi_corpus(self, hindi_int, hindi_int_size, final_word):
        multi = 0
        first_int = [0] * 20
        hindi_word = [0] * 50
        first_hindi_word = [0] * 50
        rest_hindi_word = [0] * 50
        hindi_word = [0] * 50
        first_hindi_word = [0] * 50
        rest_hindi_word = [0] * 50
        hindi_word = [0] * 50
        first_hindi_word = [0] * 50
        rest_hindi_word = [0] * 50
        
        self.normalise_hindi_word(hindi_int, hindi_int_size, hindi_word)
        multi = self.break_word_for_corpus(hindi_word, first_hindi_word, rest_hindi_word)
        if multi > 0:
            for i in range(0, multi):
                first_int[i] = hindi_int[i]
            if self.izafat_flag > 0:
                first_int[multi] = 2366
            self.normalise_hindi_word(first_int, multi + self.izafat_flag, first_hindi_word)
        pos = self.search_corpus(self.corpus_words, self.corpus_word_count, first_hindi_word)
        if pos < 0: return hindi_int_size, 0
        low = high = pos
        self.strcpy(final_word, self.corpus_words[pos].original_word)
        if multi > 0:
            self.strcat(final_word, rest_hindi_word)
        return hindi_int_size, self.corpus_words[pos].freq
        
    def check_urdu_corpus(self, urdu1, urdu_size):
            low = 0
            high = self.urdu_corpus_word_count - 1

            read_word=[0]*25
            urdu=[0]*30

            self.UnicodeTo8(urdu1, urdu_size, urdu)
            while  low <= high:
                mid = int((low + high) / 2)
                self.strcpy(read_word, self.urdu_corpus_words[mid].original_word)
                if  not(self.strcmp(read_word, urdu) != 0):
                    return self.urdu_corpus_words[mid].freq
                if  self.strcmp(read_word, urdu) < 0:
                    low = mid + 1
                else:
                    high = mid - 1
            return 0
    def break_word_for_corpus(self, hindi_word, first_hindi_word, rest_hindi_word):
        found =0
        for  i in range(0, self.strlen(hindi_word)+1):

                if  hindi_word[i] ==113:
                    first_hindi_word[i] = 0
                    found = i
                    break
                else:
                    first_hindi_word[i] = hindi_word[i]

        if  found > 0:
            for  j in range(i,self.strlen(hindi_word)+1):
                rest_hindi_word[i - j] = hindi_word[i]
        return found
    def normalise_hindi_word(self, hindi_int, hindi_int_size, hindi_word):
            extra = 0
            table =[0]*256
            t_hindi_word = [0]*50
            table = [0]*256
            t_hindi_word = [0]*50

            i = j = 0
            while  i < hindi_int_size:
                int1 = hindi_int[i]
                ch = (int1 % 256)
                if  (ch == 28) and (i < hindi_int_size - 1) and ((hindi_int[i + 1] % 256) == 60):
                    t_hindi_word[j] =91
                    j+=1
                    i+=1
                    extra+=1
                else:
                    if  (ch ==43) and (i < hindi_int_size - 1) and ((hindi_int[i + 1] % 256) == 60):
                        t_hindi_word[j] =94
                        j+=1
                        i+=1
                        extra+=1
                    else:
                        if  (ch ==21) and (i < hindi_int_size - 1) and ((hindi_int[i + 1] % 256) == 60):
                            t_hindi_word[j] =88
                            j+=1
                            i+=1
                            extra+=1
                        else:
                            if  (ch ==22) and (i < hindi_int_size - 1) and ((hindi_int[i + 1] % 256) == 60):
                                t_hindi_word[j] =89
                                j+=1
                                i+=1
                                extra+=1
                            else:
                                if  (ch ==23) and (i < hindi_int_size - 1) and ((hindi_int[i + 1] % 256) == 60):
                                    t_hindi_word[j] =90
                                    j+=1
                                    i+=1
                                    extra+=1
                                else:
                                    t_hindi_word[j] = ch
                                    j+=1
                i+=1
            hindi_int_size -= extra
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
            table[60] = 0
            table[63] = 0
            table[65] = 0
            table[75] = table[76] =66
            table[69] = table[77] = 0
            table[88] =21
            table[89] =22
            table[90] =23
            table[93] =92
            table[94] =43
            table[72] =71
            table[64] =71
            table[67] =48
            table[1] = table[2] =40

            table[47] =71
            table[73] =62  
            table[17] =62   
            table[13] =15   
            table[10] = table[19] = table[20] =20
            table[66] = table[75] = table[76] =53
            table[17] = 6

            j=0
            for  i in range(0,hindi_int_size):

                if  (i > 0) and ((t_hindi_word[i - 1] ==62) or (t_hindi_word[i - 1] ==6)) and (t_hindi_word[i] ==47) and (t_hindi_word[i + 1] ==71):
                    hindi_word[j] =15
                    j+=1
                    i+=1
                    continue

                if  (i > 0) and (i != hindi_int_size - 1) and ((t_hindi_word[i] == 5) or (t_hindi_word[i] == 7) or (t_hindi_word[i] == 8) or (t_hindi_word[i] == 15) or (t_hindi_word[i] == 16)):
                    hindi_word[j] = 15
                    j+=1
                    continue

                if  (i != hindi_int_size - 1) and ((t_hindi_word[i] == 8) or (t_hindi_word[i] == 15) or (t_hindi_word[i] == 16)):
                    hindi_word[j] = 15
                    j+=1
                    continue

                if  (i > 0) and (t_hindi_word[i] ==9) and (i != hindi_int_size - 1):
                    hindi_word[j] =20
                    j+=1
                    continue

                if  t_hindi_word[i] ==24:
                    hindi_word[j] =23
                    j+=1
                    hindi_word[j] =57
                    j+=1
                    continue

                if  t_hindi_word[i] ==29:
                    hindi_word[j] =28
                    j+=1
                    hindi_word[j] =57
                    j+=1
                    continue

                if  (i > 0) and (self.check_long_hindi_matra(t_hindi_word[i - 1])) and ((self.check_ye_matra(t_hindi_word[i])) or (t_hindi_word[i] == 15)):
                    hindi_word[j] = 15
                    j+=1
                    continue
                if  (i == 0) and ((t_hindi_word[i] ==47) or (t_hindi_word[i] ==53)):
                    hindi_word[j] = t_hindi_word[i]
                    j+=1
                    continue
                if  (i > 0) and (t_hindi_word[i - 1] ==113):
                    hindi_word[j] = t_hindi_word[i]
                    j+=1
                    continue
                if  i == 0:
                    if  (t_hindi_word[i] ==19) or (t_hindi_word[i] ==20) or (t_hindi_word[i] ==10):
                        hindi_word[j] =19
                        j+=1
                        continue
                    else:
                        if  (t_hindi_word[i] ==5) and (t_hindi_word[i + 1] ==53):
                            hindi_word[j] =19
                            j+=1
                            i+=1
                            continue
                        else:
                            if  (t_hindi_word[i] ==8) or (t_hindi_word[i] ==16):
                                hindi_word[j] =8
                                j+=1
                                continue
                            else:
                                if  (t_hindi_word[i] ==5) and (t_hindi_word[i + 1] ==47):
                                    hindi_word[j] =8
                                    j+=1
                                    i+=1
                                    continue
                                else:
                                    if  (t_hindi_word[i] ==7) or (t_hindi_word[i] ==9) or (t_hindi_word[i] ==5) or (t_hindi_word[i] ==15):
                                        hindi_word[j] =5
                                        j+=1
                                        continue

                if  (t_hindi_word[i] == 2) and ((t_hindi_word[i + 1] ==42) or (t_hindi_word[i + 1] ==44) or (t_hindi_word[i + 1] ==45)):
                    hindi_word[j] =46
                    j+=1
                    continue

                if  (t_hindi_word[i + 1] == 77) and (t_hindi_word[i + 2] == t_hindi_word[i] + 1) and (t_hindi_word[i] <47):
                    continue

                if  i > 0 and t_hindi_word[i - 1] == 77:
                    if  t_hindi_word[i - 2] == t_hindi_word[i]: continue
                if  i == hindi_int_size - 1:
                    if  (t_hindi_word[i] == 15) or (t_hindi_word[i] ==71) or (t_hindi_word[i] ==72) or (t_hindi_word[i] ==8):
                        hindi_word[j] = t_hindi_word[i]
                        j+=1
                        continue
                    if  (t_hindi_word[i] == 5) or (t_hindi_word[i] == 7) or (t_hindi_word[i] == 9):
                        hindi_word[j] = t_hindi_word[i]
                        j+=1
                        continue
                if  t_hindi_word[i] ==60:
                    if  (t_hindi_word[i - 1] ==33) or (t_hindi_word[i - 1] ==34):
                        hindi_word[j] = t_hindi_word[i]
                        j+=1
                        continue

                if  not (table[t_hindi_word[i]] != 0): continue
                hindi_word[j] = table[t_hindi_word[i]]
                j+=1
            hindi_word[j] = 0
    def check_hindi_matra(self, u1):
        u = u1
        return (((u > 3) and (u <11)) or ((u >12) and (u <21)) or ((u >61) and (u <67)) or ((u >69) and (u <77)))

    def check_hindi_matra(self, u):
        return (((u > 3) and (u <11)) or ((u >12) and (u <21)) or ((u >61) and (u <67)) or ((u >69) and (u <77)))

    def check_hindi_diactric(self, u1):
        u = u1
        return ((u >61) and (u <77))
    def split_and_check_word(self, urdu, urdu_size, roman, roman_size, tt):
        start = 0
        end = urdu_size - 1
        roman1 = [0] * 40
        p_urdu = [0] * 40
        roman_size1 = 0
        p_size = 0
        count = 0
        min = 0
        cflag = 0
        
        
        
        
        
        total = 0
        
        for i in range(0, urdu_size, 2):
            if (urdu[i] == 36) or (urdu[i] == 39) or (urdu[i] == 47) or (
                    urdu[i] == 48) or (urdu[i] == 49) or (urdu[i] == 50) or (
                    urdu[i] == 72) or (urdu[i] == 136) or (urdu[i] == 145) or (
                    urdu[i] == 210):
                end = i + 1
                if urdu[i + 2] == 80:
                    start = i + 4
                else:
                    start = i + 2
                p_size = 0
                for j in range(i + 2, urdu_size):
                    p_urdu[p_size] = urdu[j]  
                    p_size += 1
                roman_size1,returendFlag=self.check_urdu_word_bigram(p_urdu, urdu, p_size, start, roman1, roman_size1)
                if  returendFlag> 0:  
                    total = 1
                    roman_size[0] = roman_size1
                    for j in range(0, roman_size1):
                        roman[0][j] = roman1[j]
                    return tt, 1
        
        for k in range(0, 6):
            total = 0
            start = 0
            end = urdu_size - 1
            count = 0
            
            if k == 0:
                min = 2
                cflag = 0
            
            elif k == 1:
                min = 1
                cflag = 0
            
            elif k == 2:
                min = 0
                cflag = 0
            
            elif k == 3:
                min = 2
                cflag = 0
            
            elif k == 4:
                min = 2
                cflag = 1
            
            elif k == 5:
                min = 1
                cflag = 1
            
            elif k == 6:
                min = 0
                cflag = 1
                break
            
            for i in range(0, urdu_size, 2):
                if (urdu[i] == 80) or (urdu[i] == 36) or (urdu[i] == 39) or (
                        urdu[i] == 47) or (urdu[i] == 48) or (urdu[i] == 49) or (
                        urdu[i] == 50) or (urdu[i] == 72) or (urdu[i] == 136) or (
                        urdu[i] == 145) or (urdu[i] == 210):
                    count += 1
                    if count <= min: continue
                    end = i + 1
                    if urdu[i + 2] == 80: end += 2
                    if end - start < 3: continue
                    
                    start = end + 1
                    roman_size[total] = roman_size1
                    for j in range(0, roman_size1):
                        roman[total][j] = roman1[j]
                    total += 1
                    if end == urdu_size - 1:
                        return tt, 1
                    end = urdu_size - 1
                    roman_size[total] = roman_size1
                    for j in range(0, roman_size1):
                        roman[total][j] = roman1[j]
                    total += 1
                    return tt, 1
                    
                    if tt > 5: return tt, 0
        
        return tt, 0
        
    def check_valid_broken_words(self, total, word_size, words):
        cf = 0
        Urdu_UTF8=[0]*30
        Urdu1_UTF8=[0]*30
        t_size=[0]*6
        for  i in range(0,total):
            t_size[i] = word_size[i]
        for  i in range(0,total):
            for  j in range(0,word_size[i],2):
                if  words[i][j] == 77: t_size[i] -= 2

        for  i in range(0,total):
            if  t_size[i] > 7:
                return 1


        for  i in range(0,1):
            self.UnicodeTo8(words[i], word_size[i], Urdu_UTF8)
            self.UnicodeTo8(words[i + 1], word_size[i + 1], Urdu1_UTF8)
            if  self.get_bigram_freq(Urdu_UTF8, Urdu1_UTF8) > 0:
                return 1
        return 0
    def split_and_check_word_latest(self, urdu, urdu_size, roman, roman_size, total):








        start = 0
        end = urdu_size - 1
        pos = [0]*6
        f_pos = [0]*6
        t_roman_size = [0]*6
        t_urdu_size = [0]*6
        join_pt = [0]*20
        
        roman1 = [0]*40
        p_urdu = [0]*40
        t_roman = [0]*6
        t_urdu = [0]*6
        
        for  i in range(0,len(t_roman)):
            t_roman[i]=[0]*100
        for  i in range(0,len(t_urdu)):
            t_urdu[i]=[0]*100
        roman_size1 = 0
        p_size = 0
        count = 0
        flag = 0
        jcount = 0
        cflag = 0
        freq =[0]*6
        total_freq = 4250000.0
        sp = [0]*6
        ep = [0]*6
        max_bi_freq = 0
        extra = 0
        combination = 0
        self.swc = 0
        self.max_c = 0
        self.min_c = 0
        
        total = 0
        
        if  self.conversion_level < 3:
            return total, 0
        if  flag > 0:
            total_freq /= 7
        flag = -1



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
                roman_size1,returendFlag=self.check_urdu_word_bigram(p_urdu,  urdu,  p_size,  start,  roman1, roman_size1)
                if  returendFlag > 0:
                    total = 1
                    roman_size[0] = roman_size1
                    for  j in range(0,roman_size1):
                        roman[0][j] = roman1[j]
                    return total, 1
        jcount = 0
        for  i in range(0,20):
            join_pt[i] = -1
        join_pt[jcount] = -1
        jcount+=1

        if  self.check_freq_corpus(urdu,  0,  urdu_size - 1,  t_roman[0], t_roman_size[0],  flag) > 0: 
            total = 1

            for  i in range(0,1):
                roman_size[i] = t_roman_size[i]
                for  j in range(0,roman_size[i]):
                    roman[i][j] = t_roman[i][j]

            if  self.check_freq_corpus(urdu,  0,  urdu_size - 1,  t_roman[0], t_roman_size[0],  flag) > 0:
                for  i in range(0,1):
                    roman_size[i] = t_roman_size[i]
                    for  j in range(0,roman_size[i]):
                        roman[i][j] = t_roman[i][j]
                self.total_merged_words[1]+=1 
            return total, 1
        for i in range(0, urdu_size, 2):
            if (((urdu[i] == 34) or (urdu[i] == 36) or (urdu[i] == 39) or (urdu[i] == 47) or (urdu[i] == 48) or (
                    urdu[i] == 49) or (urdu[i] == 50) or (urdu[i] == 72) or (urdu[i] == 136) or (urdu[i] == 145) or (
                         urdu[i] == 210) or (urdu[i] == 186)
                 or (urdu[i] == 19) or (urdu[i] == 77) or (urdu[i] == 75) or (urdu[i] == 16)) and
                    ((urdu[i + 2] != 186) and (urdu[i + 2] != 190) and (urdu[i + 2] != 33) and (urdu[i + 2] != 35) and (
                            urdu[i + 2] != 36) and (urdu[i + 2] != 37) and (urdu[i + 2] != 38)
                     and (urdu[i + 2] != 41) and (urdu[i + 2] != 192) and (urdu[i + 2] != 81) and (
                             urdu[i + 2] != 17) and (urdu[i + 2] != 3) and (urdu[i + 2] != 213) and (
                             urdu[i + 2] != 117) and (urdu[i + 2] != 118) and (urdu[i + 2] != 190) and (
                             urdu[i + 2] != 210))):
                join_pt[jcount] = i + 1
                jcount += 1
                if urdu[i + 2] == 80:
                    join_pt[jcount - 1] += 2
                if jcount > 16: return total, 0
        if join_pt[jcount - 1] != urdu_size - 1:
            join_pt[jcount] = urdu_size - 1
            jcount += 1
        

        max_freq = max_cfreq = 0

        self.merged_words_searched+=1

        if  flag > 0:
            total_freq = urdu_size
        if  jcount == 12:
            max_freq = 0
            
        pos[0] = 0
        sp[0] = join_pt[pos[0]] + 1
        while pos[0] < jcount - 1:
            ep[0] = join_pt[pos[0] + 1]
            freq[0] = self.check_freq_corpus(urdu,  sp[0],  ep[0],  t_roman[0], t_roman_size[0],  flag)
            if  freq[0] == 0:
                pos[0] += 1
                continue
            if  flag > 0:
                freq[0] = ep[0] - sp[0] + 1
            if  flag == 2:
                freq[0] = freq[0] * freq[0]
            if  freq[0] == -1:
                freq[0] = 1
            else:
                freq[0] = freq[0] / (total_freq)
            if  ep[0] >= urdu_size - 1:
                if  flag == -1:
                    cfreq = (freq[0] / 100.0)
                else:
                    cfreq = freq[0]

                t_urdu_size[0] = ep[0] - sp[0] + 1
                for  j in range(0,t_urdu_size[0]):
                    t_urdu[0][j] = urdu[sp[0] + j]
                if  cfreq > max_freq:
                    total = 1
                    for  i in range(0,1):
                        roman_size[i] = t_roman_size[i]
                        for  j in range(0,roman_size[i]):
                            roman[i][j] = t_roman[i][j]
                    max_freq = cfreq
                    for  i in range(0,6):
                        f_pos[i] = pos[i]
            if  total >= 1:
                self.merged_word_count+=1
                self.total_joint = self.total_joint+jcount - 1

                if (max_joint < jcount - 1):
                    max_joint = jcount - 1
                    
                self.average_joint_count = (1.0 * self.total_joint) / self.merged_word_count
                if  total == 1:
                    self.single_words_found+=1
                else:
                    self.merged_words_found+=1

                self.swc += jcount
                if  self.max_c < urdu_size:
                    self.max_c = urdu_size
                if  self.min_c > urdu_size:
                    self.min_c = urdu_size
                self.average_c = (1.0 * self.swc) / self.merged_word_count

            self.total_merged_words[total]+=1

            return total, total
            
            pos[1] = pos[0] + 1
            sp[1] = join_pt[pos[1]] + 1
            freq[1] = 1
            while pos[1] < jcount - 1:
                ep[1] = join_pt[pos[1] + 1]
                freq[1] = self.check_freq_corpus(urdu,  sp[1],  ep[1],  t_roman[1], t_roman_size[1],  flag)
                if  freq[1] == 0:
                    pos[1]+=1
                    continue
                
                if  flag > 0:
                    freq[1] = ep[1] - sp[1] + 1
                if  flag == 2:
                    freq[1] = freq[1] * freq[1]
                if  freq[1] == -1:
                    freq[1] = 1
                else:
                    freq[1] = freq[1] / total_freq
                if  ep[1] >= urdu_size - 1:
                    combination+=1
                    cfreq = 1.0 * (freq[0] * freq[1])
                    if  cfreq > max_cfreq:
                        extra = 2
                        max_cfreq = cfreq
                    else: extra = 0
                    if  flag == 2:
                        cfreq = 1.0 * (freq[0] + freq[1])
                    if  flag == -1:
                        cfreq *= self.get_word_bigram_freq(2, t_roman_size, t_roman)

                    if  (cfreq > max_freq) and (self.check_valid_broken_words(2, t_roman_size, t_roman) > 0):
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
                    ep[2] = join_pt[pos[2] + 1]
                    freq[2] = self.check_freq_corpus(urdu,  sp[2],  ep[2],  t_roman[2], t_roman_size[2],  flag)
                    if  freq[2] == 0:
                        pos[2] += 1
                        continue
                    if  flag > 0:
                        freq[2] = ep[2] - sp[2] + 1
                    if  flag == 2:
                        freq[2] = freq[2] * freq[2]
                    if  freq[2] == -1:
                        freq[2] = 1
                    else:
                        freq[2] = freq[2] / total_freq
                    if  ep[2] >= urdu_size - 1:
                        combination+=1
                        cfreq = 1.0 * (freq[0] * freq[1] * freq[2])
                        if  cfreq > max_cfreq:
                            extra = 2
                            max_cfreq = cfreq
                        else: extra = 0
                        if  flag == 2:
                            cfreq = 1.0 * (freq[0] + freq[1] + freq[2])
                        if  flag == -1:
                            cfreq *= self.get_word_bigram_freq(3, t_roman_size, t_roman)

                        if  (cfreq > max_freq) and (self.check_valid_broken_words(3, t_roman_size, t_roman) > 0):
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
                        ep[3] = join_pt[pos[3] + 1]
                        freq[3] = self.check_freq_corpus(urdu,  sp[3],  ep[3],  t_roman[3], t_roman_size[3],  flag)
                        if  freq[3] == 0:
                            pos[3] += 1
                            continue
                        if  flag > 0:
                            freq[3] = ep[3] - sp[3] + 1
                        if  flag == 2:
                            freq[3] = freq[3] * freq[3]
                        if  freq[3] == -1:
                            freq[3] = 1
                        else:
                            freq[3] = freq[3] / total_freq
                        if  ep[3] >= urdu_size - 1:
                            combination+=1
                            cfreq = 1.0 * (freq[0] * freq[1] * freq[2] * freq[3])
                            if  cfreq > max_cfreq:
                                extra = 2
                                max_cfreq = cfreq
                            else: extra = 0
                            if  flag == 2:
                                cfreq = 1.0 * (freq[0] + freq[1] + freq[2] + freq[3])
                            if  flag == -1:
                                cfreq *= self.get_word_bigram_freq(4, t_roman_size, t_roman)

                            if  (cfreq > max_freq) and (self.check_valid_broken_words(4, t_roman_size, t_roman)) > 0:
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
                            ep[4] = join_pt[pos[4] + 1]
                            freq[4] = self.check_freq_corpus(urdu,  sp[4],  ep[4],  t_roman[4], t_roman_size[4],  flag)
                            if  freq[4] == 0:
                                pos[4] += 1
                                continue
                            if  flag > 0:
                                freq[4] = ep[4] - sp[4] + 1
                            if  flag == 2:
                                freq[4] = freq[4] * freq[4]
                            if  freq[4] == -1:
                                freq[4] = 1
                            else:
                                freq[4] = freq[4] / total_freq
                            if  ep[4] >= urdu_size - 1:
                                combination+=1
                                cfreq = 1.0 * (freq[0] * freq[1] * freq[2] * freq[3] * freq[4])
                                if  cfreq > max_cfreq:
                                    extra = 2
                                    max_cfreq = cfreq
                                else: extra = 0
                                if  flag == 2:
                                    cfreq = 1.0 * (freq[0] + freq[1] + freq[2] + freq[3] + freq[4])
                                if  flag == -1:
                                    cfreq *= self.get_word_bigram_freq(5, t_roman_size, t_roman)

                                if  (cfreq > max_freq) and (self.check_valid_broken_words(5, t_roman_size, t_roman) > 0):
                                    total = 5
                                    max_freq = cfreq
                                    roman_size[4] = roman_size1
                                    for  i in range(0,5):
                                        roman_size[i] = t_roman_size[i]
                                        for  j in range(0,roman_size[i]):
                                            roman[i][j] = t_roman[i][j]
                            pos[5] = pos[4] + 1
                            if  pos[5] >= jcount - 1:
                                freq[5] = 1
                                j = 0
                            else:
                                sp[5] = join_pt[pos[5]] + 1
                                ep[5] = join_pt[jcount - 1]
                                freq[5] = self.check_freq_corpus(urdu,  sp[5],  ep[5],  t_roman[5], t_roman_size[5],  flag)
                                if  flag > 0:
                                    freq[5] = ep[5] - sp[5] + 1
                                if  flag == 2:
                                    freq[5] = freq[5] * freq[5]
                                if  freq[5] == -1:
                                    freq[5] = 1
                                    j = 0
                                else:
                                    freq[5] = freq[5] / total_freq
                                    j = 1
                            cfreq = 1.0 * (freq[0] * freq[1] * freq[2] * freq[3] * freq[4] * freq[5])
                            if  cfreq > max_cfreq:
                                extra = 2
                                max_cfreq = cfreq
                            else: extra = 0
                            if  flag == 2:
                                cfreq = 1.0 * (freq[0] + freq[1] + freq[2] + freq[3] + freq[4] + freq[5])
                            if  flag == -1:
                                cfreq *= self.get_word_bigram_freq(6, t_roman_size, t_roman)

                            combination+=1
                            if  (cfreq > max_freq) and (self.check_valid_broken_words(6, t_roman_size, t_roman) > 0):
                                max_freq = cfreq
                                if  j > 1:
                                    j = 1
                                total = 5 + j
                                roman_size[5] = roman_size1
                                for  i in range(0,6):
                                    roman_size[i] = t_roman_size[i]
                                    for  j in range(0,roman_size[i]):
                                        roman[i][j] = t_roman[i][j]
                            pos[4] += 1
                        pos[3] += 1
                    pos[2] += 1
                pos[1] += 1
            pos[0] += 1
        

        
        if total >= 1:
            self.merged_word_count += 1
            self.total_joint += (jcount - 1)
            if (self.max_joint < (jcount - 1)):
                max_joint = jcount - 1
            self.average_joint_count = (1.0 * self.total_joint) / self.merged_word_count
    
            if  total == 1:
                self.single_words_found+=1
            else:
                self.merged_words_found+=1

            self.swc += jcount
            if  self.max_c < urdu_size:
                self.max_c = urdu_size
            if  self.min_c > urdu_size:
                self.min_c = urdu_size
            self.average_c = (1.0 * self.swc) / self.merged_word_count

        self.total_merged_words[total]+=1
        
        return total, total

    def get_word_bigram_freq(self, total, word_size, words):

            freq = 0
            Urdu_UTF8=[0]*30
            Urdu1_UTF8=[0]*30


            t_size =[0]*6
            cf = 1.0
            ratio = 100.0


            for  i in range(0,total): 
                t_size[i] = word_size[i]
            for  i in range(0,total): 
                for  j in range(0,word_size[i],2): 
                    if  words[i][j] == 77: t_size[i] -= 2


            for  i in range(0,1): 
                self.UnicodeTo8(words[i], word_size[i], Urdu_UTF8)
                self.UnicodeTo8(words[i + 1], word_size[i + 1], Urdu1_UTF8)
                freq = self.get_bigram_freq(Urdu_UTF8, Urdu1_UTF8)
                if  freq > 0: freq += 10
                else: freq+=1
                cf *= freq / ratio
        
            return cf
    def check_freq_corpus(self, urdu, start, end, hindi, hindi_size, flag):
            full = 0
            urdu_size = end - start + 1
            urdu1=[0]*80
            final_word=[0]*80
            normalise=[0]*80
            urdu_ptr = 0
            roman_ptr = 0
            urdu_int_ptr = 0
            hindi_int_size = 0
            urdu_int = [0]*128
            hindi_int = [0]*128
            urdu2=[0]*30



            if  start >= end: return -1
            if  (urdu_size <= 2) and (urdu[start] !=34):
                return 0
            j=k=0
            i = start
            while i<=end:
                urdu1[j] = urdu[i]
                j+=1
                if  int(i % 2) > 0:
                    i+=1
                    continue 
                urdu2[k] = urdu[i]
                k+=1
                i += 1
            urdu2[k] = 0
            k+=1

            if  flag >= 1:
                freq = self.check_urdu_corpus(urdu1, urdu_size)
                if  freq > 0:
                    hindi_size,returendFlag=self.check_urdu_word_dictionary(urdu1,  urdu_size,  hindi, hindi_size)
                    if  returendFlag > 0:
                        return freq
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
                    hindi_int_size=self.rule_based_urdu_word_to_hindi(urdu_int,  int(urdu_size / 2),  hindi_int, hindi_int_size)
                    hindi_int_size=self.improve_hindi_word(hindi_int, hindi_int_size)
                    hindi_int_size,j = self.check_hindi_corpus(hindi_int, hindi_int_size,  final_word)
                    if  not(j != 0):
                        hindi_size = 0
                        for  i in range(0,hindi_int_size): 
                            hindi[(hindi_size)] = hindi_int[i]
                            hindi_size+=1
                            hindi[(hindi_size)] = 9
                            hindi_size+=1
                        return freq
                    else:
                        hindi_size = 0
                        for  i in range(0,self.strlen(final_word)): 
                            if  final_word[i] ==113:
                                hindi[(hindi_size)] = ord('-')
                                hindi_size+=1
                                hindi[(hindi_size)] = 0
                                hindi_size+=1
                                continue
                            hindi[(hindi_size)] = final_word[i]
                            hindi_size+=1
                            hindi[(hindi_size)] = 9
                            hindi_size+=1
                        return freq
                else:
                    return 0

            if  self.search_ignore_word_list(urdu2) >= 0:
                return 0
            original_size = urdu_size
            for  k in range(0,urdu_size-2,2):
                if  urdu1[k] ==210:
                    urdu1[k] =204

            for  k in range(0,22):
                urdu_size = original_size
                full = 0
                if  k == 1:
                    if  (urdu_size > 9) and (urdu1[urdu_size - 2] ==70) and ((urdu1[urdu_size - 4] ==36) or (urdu1[urdu_size - 4] ==72)) and (urdu1[urdu_size - 6] ==204) and (urdu1[urdu_size - 8] !=38):
                        if  urdu1[urdu_size - 4] ==36:
                            full = 1
                            urdu_size -= 4
                    else:
                        continue
                if  k == 2:
                    if  (urdu_size > 9) and (urdu1[urdu_size - 2] ==70) and ((urdu1[urdu_size - 4] ==36) or (urdu1[urdu_size - 4] ==72)) and (urdu1[urdu_size - 6] ==204):
                        if  urdu1[urdu_size - 8] ==38:
                            full = 1
                            urdu_size += 2
                        urdu_size -= 6
                    else:
                        continue
                if  k == 3:
                    if  (urdu_size > 7) and (urdu1[urdu_size - 2] ==70) and ((urdu1[urdu_size - 4] ==36) or (urdu1[urdu_size - 4] ==72)):
                        if  urdu1[urdu_size - 4] ==36:
                            full = 1
                        if (urdu1[urdu_size - 6] ==38):
                            full = 1
                            urdu_size -= 2
                        urdu_size -= 4
                    else:
                        continue
                if  k == 4:
                    if  (urdu_size > 7) and (urdu1[urdu_size - 2] ==70) and (urdu1[urdu_size - 4] ==204):
                        if  urdu1[urdu_size - 6] ==38:
                            full = 1
                            urdu_size -= 2
                        urdu_size -= 4 
                    else:
                        continue
                if  k == 5:
                    if  (urdu_size > 9) and (urdu1[urdu_size - 2] ==70) and (urdu1[urdu_size - 4] ==39) and (urdu1[urdu_size - 6] ==204) and (urdu1[urdu_size - 8] !=38):
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
                    if  (urdu_size > 9) and (urdu1[urdu_size - 2] ==33): 
                        urdu_size -= 2
                    else:
                        continue
                if  k == 8:
                    if  (urdu_size > 7) and (urdu1[urdu_size - 2] ==39) and (urdu1[urdu_size - 4] ==42):  
                        urdu_size -= 4 
                    else:
                        continue
                if  k == 9:
                    if  (urdu_size > 7) and (urdu1[urdu_size - 2] ==39) and (urdu1[urdu_size - 4] ==70):  
                        urdu_size -= 4
                    else:
                        continue
                if  k == 10:
                    if  (urdu_size > 7) and (urdu1[urdu_size - 2] ==210) and (urdu1[urdu_size - 4] ==42):
                        urdu_size -= 4
                    else:
                        continue
                if  k == 11:
                    if  (urdu_size > 7) and (urdu1[urdu_size - 2] ==210) and (urdu1[urdu_size - 4] ==70):
                        urdu_size -= 4
                    else:
                        continue
                if  k == 12:
                    if  (urdu_size > 7) and (urdu1[urdu_size - 2] ==204) and (urdu1[urdu_size - 4] ==42):
                        urdu_size -= 4
                    else:
                        continue
                if  k == 13:
                    if  (urdu_size > 7) and (urdu1[urdu_size - 2] == 70) and (urdu1[urdu_size - 4] == 36):  
                        urdu_size -= 4
                    else:
                        continue
                if  k == 14:
                    if  (urdu_size > 7) and (urdu1[urdu_size - 2] ==78) and (urdu1[urdu_size - 4] ==33):  
                        urdu_size -= 4
                    else:
                        continue
                if  k == 15:
                    if  (urdu_size > 7) and (urdu1[urdu_size - 2] ==80) and (urdu1[urdu_size - 4] ==33):  
                        urdu_size -= 4
                    else:
                        continue
                if  k == 16:
                    if  (urdu_size > 9) and (urdu1[urdu_size - 2] ==49) and (urdu1[urdu_size - 4] ==39) and (urdu1[urdu_size - 6] ==47):  
                        urdu_size -= 6
                    else:
                        continue
                if  k == 17:
                    if  (urdu_size > 7) and (urdu1[urdu_size - 2] ==79) and (urdu1[urdu_size - 4] ==33):  
                        urdu_size -= 4
                    else:
                        continue

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
                    if  (urdu_size > 7) and (urdu1[urdu_size - 4] ==70) and (urdu1[urdu_size - 2] ==175):  
                        urdu_size -= 4 
                    else:
                        continue


                hindi_size,returendFlag=self.check_urdu_word_dictionary(urdu1,  urdu_size,  hindi, hindi_size)
                if  returendFlag > 0:
                    if  k == 1:
                        hindi_size -= 2
                        hindi[(hindi_size)] =63
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =47
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =66
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =2
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 2:
                        if  full > 0:
                            hindi_size -= 2
                            hindi[(hindi_size)] =7
                            hindi_size+=1
                            hindi[(hindi_size)] = 9
                            hindi_size+=1
                        hindi[(hindi_size)] =47
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =66
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =2
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 3:
                        if  full > 0:
                            hindi[(hindi_size)] =10
                            hindi_size+=1
                        else:
                            hindi[(hindi_size)] =66
                            hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =2
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 4:
                        if  full > 0:
                            hindi[(hindi_size)] =15
                            hindi_size+=1
                        else:
                            hindi[(hindi_size)] =71
                            hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =2
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 5:
                        hindi[(hindi_size)] =47
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =62
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =1
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 6:
                        hindi[(hindi_size)] =91
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 7:
                        hindi[(hindi_size)] =5
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 8:  
                        hindi[(hindi_size)] =36
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =62
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 9:  
                        hindi[(hindi_size)] =40
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =62
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 10:  
                        hindi[(hindi_size)] =36
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =71
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 11:  
                        hindi[(hindi_size)] =40
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =71
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 12:  
                        hindi[(hindi_size)] =36
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =64
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 13:  
                        hindi[(hindi_size)] =10
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =2
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 14:  
                        hindi[(hindi_size)] =5
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 15:  
                        hindi[(hindi_size)] =7
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1

                    if  k == 16:  
                        hindi[(hindi_size)] =38
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =62
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =48
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 17:  
                        hindi[(hindi_size)] =9
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 18:  
                        hindi[(hindi_size)] =23
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =62
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 19:  
                        hindi[(hindi_size)] =23
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =64
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 20:  
                        hindi[(hindi_size)] =23
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =71
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 21:  
                        hindi[(hindi_size)] =63
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =2
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =23
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    j=0
                    for  i in range(0,hindi_size,2):
                        hindi_int[j] = hindi[i]
                        j+=1
                    hindi_int_size = int((hindi_size) / 2)
                    hindi_int_size,freq = self.check_hindi_corpus(hindi_int, hindi_int_size,  final_word)
                    hindi_size=self.improve_hindi_word_matra(hindi, hindi_size)
                    if  freq < 1: freq = 1
                    return freq
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
                hindi_int_size=self.rule_based_urdu_word_to_hindi(urdu_int,  int(urdu_size / 2),  hindi_int, hindi_int_size)
                hindi_int_size=self.improve_hindi_word(hindi_int, hindi_int_size)
                final_word[0] = 0
                hindi_int_size,freq = self.check_hindi_corpus(hindi_int, hindi_int_size,  final_word)
                if  (k == 0) and (freq < 5) and (self.strlen(final_word) < 5) and (original_size < 10):
                    return 0
                if  (k == 0) and (original_size < 4):
                    return 0

                if  freq > 0:
                    hindi_size = 0
                    for  i in range(0,self.strlen(final_word)): 
                        if  final_word[i] ==113:
                            hindi[(hindi_size)] = ord('-')
                            hindi_size+=1
                            hindi[(hindi_size)] = 0
                            hindi_size+=1
                            continue
                        hindi[(hindi_size)] = final_word[i]
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 1:
                        hindi_size -= 2
                        hindi[(hindi_size)] =63
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =47
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =66
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =2
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        freq = 1
                    if  k == 2:
                        if  full > 0:
                            hindi_size -= 2
                            hindi[(hindi_size)] =7
                            hindi_size+=1
                            hindi[(hindi_size)] = 9
                            hindi_size+=1
                        hindi[(hindi_size)] =47
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =66
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =2
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        freq = 1
                    if  k == 3:
                        if  full > 0:
                            hindi[(hindi_size)] =10
                            hindi_size+=1
                        else:
                            hindi[(hindi_size)] =66
                            hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =2
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        freq = 1
                    if  k == 4:
                        if  full > 0:
                            hindi[(hindi_size)] =15
                            hindi_size+=1
                        else:
                            hindi[(hindi_size)] =64
                            hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =2
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        freq = 1
                    if  k == 5:
                        hindi[(hindi_size)] =47
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =62
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =1
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        freq = 1
                    if  k == 6:
                        hindi[(hindi_size)] =91
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        freq = 1
                    if  k == 7:
                        hindi[(hindi_size)] =5
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        freq = 1
                    if  k == 8:  
                        hindi[(hindi_size)] =36
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =62
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 9:  
                        hindi[(hindi_size)] =40
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =62
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 10:  
                        hindi[(hindi_size)] =36
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =71
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 11:  
                        hindi[(hindi_size)] =40
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =71
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 12:  
                        hindi[(hindi_size)] =36
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =64
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 13:  
                        hindi[(hindi_size)] =40
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =64
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 14:  
                        hindi[(hindi_size)] =53
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =62
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 15:  
                        hindi[(hindi_size)] =42
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =40
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 16:  
                        hindi[(hindi_size)] =38
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =62
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =48
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 17:  
                        hindi[(hindi_size)] =57
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =31
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 18:  
                        hindi[(hindi_size)] =23
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =62
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 19:  
                        hindi[(hindi_size)] =23
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =64
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 20:  
                        hindi[(hindi_size)] =23
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =71
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    if  k == 21:  
                        hindi[(hindi_size)] =63
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =2
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                        hindi[(hindi_size)] =23
                        hindi_size+=1
                        hindi[(hindi_size)] = 9
                        hindi_size+=1
                    hindi_size=self.improve_hindi_word_matra(hindi, hindi_size)
                    return freq
            return 0
    def improve_hindi_word_matra(self, hindi, hindi_size):


            for  i in range(2,hindi_size,2): 
                if  (self.check_hindi_matra(hindi[i - 2])) and (self.check_hindi_matra(hindi[i])):
                    if  not self.check_hindi_full_matra(hindi[i]):
                        hindi[i] = self.toggle_hindi_matra(hindi[i])
    def rule_based_urdu_word_to_hindi(self, urdu_int, urdu_size, hindi_int, hindi_int_size):
           
            cp = -1
            hindi_size = 0
            b=0
            self.olda = 0
            hindi_int_size = 0
            self.izafat_flag = 0
            cp+=1
            while  cp < urdu_size:            
                a = urdu_int[cp]
                if  (a ==1730) or (a ==1747) or (a ==1728) or (a ==1620) or (a ==1569):
                    if  cp == urdu_size - 1:
                        if not self.prev_number != 0:
                            hindi_int[hindi_size] =2309
                            hindi_size+=1
                            cp+=1
                            continue
                        else:
                            hindi_int[hindi_size] =2312
                            hindi_size+=1
                            b =2307
                            self.prev_number = 0
                            cp += 1
                            continue
                        if  a ==1730: self.izafat_flag = 1  
                    else:
                        if  urdu_int[cp + 1] ==1614:
                            hindi_int[hindi_size] =2309
                            hindi_size += 1
                            cp+=2
                            continue
                            
                        if  urdu_int[cp + 1] ==1616:
                            hindi_int[hindi_size] =2311
                            hindi_size += 1
                            cp+=2
                            continue

                if  a ==1614:
                    self.olda = a
                    cp += 1
                    continue    
                elif  a ==1648 and self.olda ==1608:  
                    self.olda =1648
                    cp+=1
                    continue
                if  a ==1726:
                    bb = urdu_int[cp + 1]

                    hindi_size-=1
                    
                    if self.olda==1580:
                        if  bb ==1617:
                            urdu_size,hindi_size,hindi_int[hindi_size] = self.UtoH(1580, urdu_int, urdu_size, hindi_int, hindi_size)
                            hindi_size+=1
                            hindi_int[hindi_size] =2381
                            hindi_size+=1
                        b =2333
                            
                    elif self.olda==1711:
                        if  bb ==1617:
                            hindi_int[hindi_size] =2328
                            hindi_size+=1
                            hindi_int[hindi_size] =2381
                            hindi_size+=1
                        b =2328
                    
                    elif self.olda==1681:
                        if  bb ==1617:
                            hindi_int[hindi_size] =2397
                            hindi_size+=1
                            hindi_int[hindi_size] =2381
                            hindi_size+=1
                        b =2397
                        
                    else:
                        b =2361
                        hindi_size+=1
                else:
                    if  a == 1790:
                        hindi_int[hindi_size] =2350
                        hindi_size+=1
                        hindi_int[hindi_size] =2375
                        hindi_size+=1
                        b =2306 

                    else:
                        cp,hindi_size,b = self.UtoH(a,  urdu_int, cp,  hindi_int, hindi_size)
                if  b == 0:
                    b = a
                if  hindi_size >= 0:
                    hindi_int[hindi_size] = b
                    hindi_size+=1
                if  a ==1688:   
                    b =2364
                    hindi_int[hindi_size] = b
                    hindi_size+=1
                if  self.PROTECTOLDA == 0:
                    self.olda = a
                else:
                    self.PROTECTOLDA = 0
                cp+=1
            hindi_int_size = hindi_size
            if  self.prev_number > 0: self.prev_number+=1 
            if  self.prev_number > 3: 
                self.prev_number = 0  
            return hindi_int_size

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
                    szOut[j] = 128 | ((uc1.ui)  & 63)
                    j+=1
                else:
                    szOut[j] = 224 | ((uc1.ui) >> 12)
                    j+=1
                    szOut[j] = 128 | (((uc1.ui) >> 6) & 63)
                    j+=1
                    szOut[j] = 128 | ((uc1.ui) &63)
                    j+=1
            szOut[j] = 0
            return
    def check_vao_matra(self, u):
            return ((u ==53) or (u ==66) or (u ==75) or (u ==76))
    def check_ye_matra(self, u):
            return ((u ==47) or (u ==64) or (u ==71) or (u ==72))
    def check_long_hindi_matra(self, u):
            return (((u > 3) and (u <11)) or ((u >12) and (u <21)) or (u ==62) or (u ==64) or (u ==66) or (u ==47) or (u ==53) or ((u >69) and (u <77)))
    def check_urdu_line_end(self, ch, ch1):
            q = ord('?')
            b = ord('?')
            if  q == ord('?'):
                q = ord('?')
            if  b == ord('?'):
                b = 0
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
                if  not(self.strcmp(read_word, word) != 0):
                    self.strcpy(selected_word, self.pre_bigram[mid].first_word)
                    return (1.0 * self.pre_bigram[mid].freq / (self.pre_bigram[mid].unigram_freq + 1))
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
                if  not (self.strcmp(read_word, word) != 0):
                    self.strcpy(selected_word, self.pre_bigram[mid].first_word)
                    return (self.pre_bigram[mid].freq)
                if  self.strcmp(read_word, word) < 0:
                    low = mid + 1
                else:
                    high = mid - 1

            return 0
    def search_word_pre_trigram_index(self, word, start, end):
            read_word=[0]*20

            high = self.pre_trigram_index_count - 1
            low = 0
            while  low <= high:
                mid = int((low + high) / 2)
                if  mid >= len(self.pre_trigram_index):
                    break
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

            return start, end, 0
    def search_word_post_bigram(self, word, low, high, selected_word):
            read_word=[0]*20

            while  low <= high:
                mid = int((low + high) / 2)
                if  mid >= len(self.post_bigram):
                    break
                self.strcpy(read_word, self.post_bigram[mid].first_word)
                if  not (self.strcmp(read_word, word) != 0):
                    self.strcpy(selected_word, self.post_bigram[mid].second_word)
                    return ((1.0 * self.post_bigram[mid].freq) / (self.post_bigram[mid].unigram_freq + 1))
                if  self.strcmp(read_word, word) < 0:
                    low = mid + 1
                else:
                    high = mid - 1

            return 0


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
    def search_word_mid_trigram_index(self, word, start, end):
            read_word=[0]*20

            high = self.mid_trigram_index_count - 1
            low = 0
            while  low <= high:
                mid = int((low + high) / 2)
                if  mid >= len(self.mid_trigram_index):
                    break
                self.strcpy(read_word, self.mid_trigram_index[mid].normalised_word)
                if  not(self.strcmp(read_word, word) != 0):
                    if  mid == 0:
                        start = 0
                    else:
                        start = self.mid_trigram_index[mid - 1].index + 1
                    end = self.mid_trigram_index[mid].index
                    return start, end, 1
                if  self.strcmp(read_word, word) < 0:
                    low = mid + 1
                else:
                    high = mid - 1

            return start, end,0
    def search_word_post_trigram(self, word1, word2, low, high, selected_word):
            first = low
            last = high
            read_word=[0]*20

            while  low <= high:
                mid = int((low + high) / 2)
                if  mid >= len(self.post_trigram):
                    break
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
    def search_word_pre_bigram_index(self, word, start, end):
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
                if  mid >= len(self.post_trigram_index):
                    break
                self.strcpy(read_word, self.post_trigram_index[mid].normalised_word)
                if  not(self.strcmp(read_word, word) != 0):
                    if  mid == 0:
                        start = 0
                    else:
                        start = self.post_trigram_index[mid - 1].index + 1
                    end = self.post_trigram_index[mid].index
                    return start, end,1
                if  self.strcmp(read_word, word) < 0:
                    low = mid + 1
                else:
                    high = mid - 1

            return start, end,0
    def get_freq(self, word):
            low = 0
            mid = 0
            high = self.corpus_word_count - 1
            hindi_int = [0]*20
            normalise=[0]*20
            read_word=[0]*20

            for  k in range(0,self.strlen(word)): 
                hindi_int[k] = word[k]
            self.normalise_hindi_word(hindi_int, self.strlen(word), normalise)

            while  low <= high:
                mid = int((low + high) / 2)
                if  mid >= len(self.corpus_words):
                    break
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
    def check_invalid_first_char(self, c):
            tej = ((c ==33) or (c ==36) or (c ==37) or (c ==38) or (c ==80) or (c ==81) or (c ==82) or (c ==84) or (c ==85) or (c ==88) or (c ==116) or (c ==194) or (c ==195) or (c ==210) or (c ==211))
            if  tej:
                return 1
            else:
                return 0
    def check_matra(self, c):
            tej = (c ==34 or c ==39 or c ==73 or c ==74 or c ==204 or c ==210)  
            if  tej:
                return 1
            else:
                return 0
    def check_definte_join_word(self, urdu2):
            post_dict=[0]*20
            for  i in range(0,len(post_dict)): 
                post_dict[i]=[0]*10
            Urdu_UTF8=[0]*40
            total = 8
            post_dict[2][0] = post_dict[1][0] = post_dict[0][0] =175
            post_dict[5][0] = post_dict[4][0] = post_dict[3][0] =42
            post_dict[0][1] =210
            post_dict[3][1] =210
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
    def check_invalid_combination(self, urdu1, urdu2):


            n = self.strlen(urdu1) - 1
            if  (urdu2[0] ==72) and (self.strlen(urdu2) < 2):
                return 1
            if  (urdu1[0] ==72) and (self.strlen(urdu1) < 2):
                return 1
            if  urdu1[n] ==194:
                return 1
            if  urdu1[0] == 33:
                return 1
            if  self.check_matra(urdu1[n]) > 0 and self.check_matra(urdu2[0]) > 0 and (urdu2[0] != 204):
                return 1
            if  (urdu1[n] ==186) and (urdu2[0] !=175):
                return 1
            if  (urdu2[0] ==34) and (urdu2[1] !=40):
                return 1
            if  (urdu2[0] ==70) and (urdu2[1] ==193) and (self.strlen(urdu2) == 2):
                return 1
            if  (urdu2[0] ==55) and (urdu2[1] ==210) and (self.strlen(urdu2) == 2):
                return 1
            return 0


    def check_joining_combination(self, urdu1, urdu2):
            if  self.check_invalid_first_char(urdu2[0]) > 0:
                return 1

            return 0

    def get_word_freq(self, urdu, urdu_size, hindi, hindi_size, dj):
        mid = 0
        last = 0
        found = 0
        high = self.urdu_bigram_total
        hindi_int_size = 0
        hindi_int = [0]*40
        urdu_int = [0]*30
        final_word=[0]*30
        Urdu_UTF8=[0]*30
        Urdu1_UTF8=[0]*30
        temp=[0]*50
        urdu1=[0]*40
        hindi_size,returendFlag=self.check_urdu_word_dictionary(urdu,  urdu_size,  hindi, hindi_size)
        if  returendFlag > 0:
            j=0
            for  i in range(0,hindi_size,2):
                hindi_int[j] = hindi[i]
                j+=1
            hindi_int_size = int((hindi_size) / 2)
            hindi_int_size,freq = self.check_hindi_corpus(hindi_int, hindi_int_size,  final_word)
            return hindi_size, freq
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
        hindi_int_size=self.rule_based_urdu_word_to_hindi(urdu_int, int((urdu_size) / 2), hindi_int, hindi_int_size)
        hindi_int_size=self.improve_hindi_word(hindi_int, hindi_int_size)
        hindi_int_size,freq = self.check_hindi_corpus(hindi_int, hindi_int_size, final_word)
        if  freq > 0 or dj > 0:
            hindi_size = 0
            for  i in range(0,self.strlen(final_word)):
                if  final_word[i] ==118:
                    hindi[(hindi_size)] = ord('-')
                    hindi_size+=1
                    hindi[(hindi_size)] = 0
                    hindi_size+=1
                    continue
                hindi[(hindi_size)] = final_word[i]
                hindi_size+=1
                hindi[(hindi_size)] = 9
                hindi_size+=1
            return hindi_size, freq
        else:
            return hindi_size, 0
        return hindi_size,0

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
                return start, end,1
            if  self.strcmp(read_word, word) < 0:
                low = mid + 1
            else:
                high = mid - 1

        return start, end,0
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
    def get_bigram_freq(self, word1, word2):
            hindi_int =[0]*20
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
                hindi_int[k] = word1[k]
            self.normalise_hindi_word(hindi_int, self.strlen(word1), norm1)

            for  k in range(0,self.strlen(word2)): 
                hindi_int[k] = word2[k]
            self.normalise_hindi_word(hindi_int, self.strlen(word2), norm2)

            start, end, returnedFlag=self.search_word_pre_bigram_index(norm1, start, end)
            if   returnedFlag > 0:
                pre_freq = self.search_word_pre_int_bigram(norm2, start, end, temp_word)
                if  pre_freq > 2: return pre_freq
            start, end, returnedFlag=self.search_word_post_bigram_index(norm2, start, end)
            if  returnedFlag > 0:
                pre_freq = self.search_word_post_int_bigram(norm1, start, end, temp_word)
                if  pre_freq > 2: return pre_freq
            start, end, returnedFlag = self.search_word_bigram_index(word1, start, end)
            if  returnedFlag > 0:
                freq = self.search_word_bigram(word2, start, end)
            return freq




    def check_urdu_broken_word(self, urdu, p_urdu, urdu_size, p_urdu_size, hindi, hindi_size):
        total = 100000
        min_limit = 10
        hindi_int = [0] * 40
        urdu_int = [0] * 30
        urdu_ptr = 0
        urdu_int_ptr = 0
        temp_size = 0
        temp_size1 = 0
        final_word = [0] * 30
        Urdu_UTF8 = [0] * 30
        Urdu1_UTF8 = [0] * 30
        temp = [0] * 50
        temp1 = [0] * 50
        urdu1 = [0] * 50
        c = 0
        definte_join = 0
        
        self.UnicodeTo8(urdu, urdu_size, Urdu_UTF8)
        self.UnicodeTo8(p_urdu, p_urdu_size, Urdu1_UTF8)
        
        
        if self.check_invalid_combination(Urdu1_UTF8, Urdu_UTF8) > 0:
            hindi_size = 0
            return 0
        
        
        for i in range(0, p_urdu_size):
            urdu1[i] = p_urdu[i]
        for i in range(0, urdu_size):
            urdu1[i + p_urdu_size] = urdu[i]  
        c += 1
        if c == 2438:
            c += 1
        hindi_size, freq = self.get_word_freq(urdu1, urdu_size + p_urdu_size, hindi, hindi_size, definte_join)
        if freq > 0 and self.check_joining_combination(Urdu1_UTF8, Urdu_UTF8) > 0:
            return freq
        definte_join = self.check_definte_join_word(Urdu_UTF8)
        if definte_join > 0:
            temp_size = temp_size1 = 0
            temp_size, freq2 = self.get_word_freq(p_urdu, p_urdu_size, temp, temp_size, 0)  
            temp_size, freq1 = self.get_word_freq(urdu, urdu_size, temp1, temp_size1, 0)  
            if not (temp_size != 0):
                hindi_size = 0
                return 0  
            
            r1 = (freq * 1.0) / total
            r2 = (1.0 * freq1) / (total)
            r3 = (1.0 * freq2) / (total)
            r4 = r2 * r3
            if (freq > 10) and (r4 < r1):
                return freq
            
            hindi_size = temp_size + temp_size1
            for i in range(0, temp_size):
                hindi[i] = temp[i]
            for i in range(0, temp_size1):
                hindi[i + temp_size] = temp1[i]
            return 1
        if freq < 4:
            hindi_size = 0
            return 0
        temp_size, freq2 = self.get_word_freq(p_urdu, p_urdu_size, temp, temp_size, 0)  
        
        temp_size, freq1 = self.get_word_freq(urdu, urdu_size, temp1, temp_size1, 0)  
        if freq1 == 0:
            temp_size1 = 0
        if freq2 == 0:
            temp_size = 0
        if (freq1 < 1) or (freq2 < 1):
            return freq
        r1 = (freq * 1.0) / total
        r2 = (1.0 * freq1) / (total)
        r3 = (1.0 * freq2) / (total)
        r4 = r2 * r3
        if r4 > r1:
            hindi_size = 0
            return 0  
        
        self.UnicodeTo8(temp, temp_size, Urdu_UTF8)
        self.UnicodeTo8(temp1, temp_size1, Urdu1_UTF8)
        if self.get_bigram_freq(Urdu_UTF8, Urdu1_UTF8) > 0:
            hindi_size = 0
            return 0  
        
        return freq
    
    
        
    def check_broken_punc(self, roman_word, roman_word_size):
        if  roman_word_size > 2: return  False
        if  roman_word[0] != 32: return  False
        if  roman_word[1] != 0: return  False
        return True
    def get_similar(self, s, similar, pos, len):
            j = 0
            similar[j] = s
            j+=1
            if  (s >= 11) and (s <= 205):
                if  s % 5 == 1:
                    if  s == 141 and pos == 0:
                        similar[j] = (s + 3)
                        j+=1
                        similar[j] = (s + 4)
                        j+=1
                    else:
                        for  i in range(1,5): 
                            similar[j] = (s + i)
                            j+=1
            if  s == 106:
                for  i in range(0,5): 
                    similar[j] = (81 + i)
                    j+=1
                if  (pos > 0) and (pos != len - 1):
                    similar[j] = 216
                    j+=1
                    similar[j] = 217
                    j+=1
            if  s >= 161 and s <= 165:
                for  i in range(0,5): 
                    similar[j] = (156 + i)
                    j+=1
            if  s >= 136 and s <= 140 and pos > 0:
                similar[j] = 208
                j+=1
                similar[j] = 212
                j+=1
                similar[j] = 213
                j+=1
            if  s >= 151 and s <= 155:
                similar[j] = 210
                j+=1
                similar[j] = 214
                j+=1
                similar[j] = 215
                j+=1
            if  s >= 141 and s <= 145:
                similar[j] = 211
                j+=1
            if  s == 210 or s == 214 or s == 215:
                for  i in range(0,5): 
                    similar[j] = (151 + i)
                    j+=1
            if  s == 1:
                similar[j] = 3
                j+=1
                similar[j] = 5
                j+=1
            if  s == 3:
                similar[j] = 136
                j+=1
            if  (s == 4) and (pos != len - 1):
                similar[j] = 7
                j+=1
                similar[j] = 8
                j+=1
            if  s == 6:
                similar[j] = 9
                j+=1
                similar[j] = 10
                j+=1
            if  (s == 7) and (pos != len - 1):
                similar[j] = 4
                j+=1
                similar[j] = 8
                j+=1
            if  s == 9:
                similar[j] = 6
                j+=1
                similar[j] = 10
                j+=1
            if  s == 10:
                similar[j] = 6
                j+=1
                similar[j] = 9
                j+=1
            if  (s == 208) and (pos != len - 1):
                similar[j] = 212
                j+=1
                similar[j] = 213
                j+=1
            if  s == 214:
                similar[j] = 210
                j+=1
                similar[j] = 215
                j+=1
            similar[j] = 0
            j+=1
            return
    def get_max_bigram(self, first, second, third, c1, c2, c3, freq):
            max = 0
            l1 = self.strlen(first)
            l2 = self.strlen(second)
            l3 = self.strlen(third)
            r1 = 0
            r2 = 0
            r3 = 0
            if  l1 == 0: l1 = 1
            if  l2 == 0: l2 = 1
            if  l3 == 0: l3 = 1
            for  i in range(0,l1): 
                for  j in range(0,l2): 
                    for  k in range(0,l3): 
                        if  self.cs[first[i], second[j], third[k]] > max:
                            max = self.cs[first[i], second[j], third[k]]
                            r1 = first[i]
                            r2 = second[j]
                            r3 = third[k]
            freq = max
            c1 = r1
            c2 = r2
            c3 = r3
            return c1, c2, c3, freq

    def get_reverse(self, c, s):
        j = 0
        if c == 1:
            s[j] = 5
            j += 1
        elif c == 2:
            s[j] = 6
            j += 1
        elif c == 3:
            s[j] = 7
            j += 1
        elif c == 4:
            s[j] = 8
            j += 1
        elif c == 5:
            s[j] = 9
            j += 1
        elif c == 6:
            s[j] = 10
            j += 1
        elif c == 7:
            s[j] = 15
            j += 1
        elif c == 8:
            s[j] = 16
            j += 1
        elif c == 9:
            s[j] = 19
            j += 1
        elif c == 10:
            s[j] = 20
            j += 1

        elif c == 15:
            s[j] = 21
            j += 1

        elif c == 20:
            s[j] = 22
            j += 1
 
        elif c == 25:
            s[j] = 23
            j += 1

        elif c == 30:
            s[j] = 24
            j += 1

        elif c == 35:
            s[j] = 25
            j += 1

        elif c == 40:
            s[j] = 26
            j += 1

        elif c == 45:
            s[j] = 27
            j += 1

        elif c == 50:
            s[j] = 28
            j += 1
        
        elif c == 55:
            s[j] = 29
            j += 1
        
        elif c == 60:
            s[j] = 30
            j += 1
        
        elif c == 65:
            s[j] = 31
            j += 1
        
        elif c == 70:
            s[j] = 32
            j += 1
        
        elif c == 75:
            s[j] = 33
            j += 1
        
        elif c == 80:
            s[j] = 34
            j += 1
        
        elif c == 85:
            s[j] = 35
            j += 1
        
        elif c == 90:
            s[j] = 36
            j += 1
        
        elif c == 95:
            s[j] = 37
            j += 1
        
        elif c == 100:
            s[j] = 38
            j += 1
        
        elif c == 105:
            s[j] = 39
            j += 1
        
        elif c == 110:
            s[j] = 40
            j += 1
        
        elif c == 115:
            s[j] = 42
            j += 1
        
        elif c == 120:
            s[j] = 43
            j += 1
        
        elif c == 125:
            s[j] = 44
            j += 1
        
        elif c == 130:
            s[j] = 45
            j += 1
        
        elif c == 135:
            s[j] = 46
            j += 1
        
        elif c == 140:
            s[j] = 47
            j += 1
        
        elif c == 145:
            s[j] = 48
            j += 1
        
        elif c == 150:
            s[j] = 50
            j += 1
        
        elif c == 155:
            s[j] = 53
            j += 1
        
        elif c == 160:
            s[j] = 54
            j += 1
        
        elif c == 165:
            s[j] = 55
            j += 1
        
        elif c == 170:
            s[j] = 56
            j += 1
        
        elif c == 175:
            s[j] = 57
            j += 1
        
        elif c == 180:
            s[j] = 89
            j += 1
        
        elif c == 185:
            s[j] = 90
            j += 1
        
        elif c == 190:
            s[j] = 91
            j += 1
        
        elif c == 195:
            s[j] = 92
            j += 1
        
        elif c == 200:
            s[j] = 93
            j += 1
        
        elif c == 205:
            s[j] = 94
            j += 1
        elif c == 206:
            s[j] = 62
            j += 1
        elif c == 207:
            s[j] = 63
            j += 1
        elif c == 208:
            s[j] = 64
            j += 1
        elif c == 209:
            s[j] = 65
            j += 1
        elif c == 210:
            s[j] = 66
            j += 1
        elif c == 211:
            s[j] = 67
            j += 1
        elif c == 212:
            s[j] = 71
            j += 1
        elif c == 213:
            s[j] = 72
            j += 1
        elif c == 214:
            s[j] = 75
            j += 1
        elif c == 215:
            s[j] = 76
            j += 1
        elif c == 216:
            s[j] = 1
            j += 1
        elif c == 217:
            s[j] = 2
            j += 1
        elif c == 218:
            s[j] = 3
            j += 1
        elif c == 219:
            s[j] = 113
            j += 1
        if (c >= 11) and (c <= 206):
            if c % 5 == 0:
                s[j] = 63
                j += 1
            elif c % 5 == 2:
                s[j] = 77
                j += 1
            elif c % 5 == 3:
                s[j] = 77
                j += 1
                if c == 18 or c == 43 or c == 93:
                    if c == 18:
                        s[j] = 22
                        j += 1
                    elif c == 43:
                        s[j] = 27
                        j += 1
                    elif c == 93:
                        s[j] = 37
                        j += 1
                
                else:
                    s[j] = s[j - 2]
                    j += 1
            
            elif c % 5 == 4:
                s[j] = 65
                j += 1
        s[j] = 0
        j += 1
        
    def refine_word(self, hs, refined):
        j = 0
        k = 0
        first = [0]*50
        second = [0]*50
        third = [0]*50
        s = [0]*50
        cstring=[0]*9
        c3 = 0
        c4 = 0
        c5 = 0
        c6 = 0
        c7 = 0
        c8 = 0
        c9 = 0
        c1 = 0
        c2 = 0

        self.strcpy(refined,  hs)
        for  i in range(0,self.strlen(hs)):
            if  hs[i] == 77:
                return 2
        if  self.strlen(hs) < 2:
            return 1
        len = self.strlen(s)
        if  len == 2:
            for  i in range(0,1):
                freq1 = freq2 = freq3 = 0
                self.get_similar(s[0], first, 0, len)
                self.get_similar(s[1], second, 1, len)
                self.get_similar(s[2], third, 2, len)
                c1, c2, c3, freq1=self.get_max_bigram(first,  second,  third, c1, c2, c3, freq1)
                self.get_reverse(c1, cstring)
                k = 0
                while  cstring[k] > 0:
                    refined[j] = cstring[k]
                    k+=1
                    j+=1
                self.get_reverse(c2, cstring)
                k = 0
                while  cstring[k] > 0:
                    refined[j] = cstring[k]
                    k+=1
                    j+=1
        else:
            len = self.strlen(s)
            for  i in range(0,len):
                freq1 = freq2 = freq3 = 0
                if  i <= 1:
                    self.get_similar(0, first, 0, len)
                else:
                    self.get_similar(s[i - 2], first, i - 2, len)
                if  i == 0:
                    self.get_similar(0, second, 0, len)
                else:
                    self.get_similar(s[i - 1], second, i - 1, len)
                self.get_similar(s[i], third, i, len)
                if  i > 1:
                    c1, c2, c3, freq1=self.get_max_bigram(first,  second,  third, c1, c2, c3, freq1)
                self.get_similar(s[i + 1], first, i + 1, len)
                if  (i > 0) and (i < self.strlen(s) - 1):
                    c4, c5, c6, freq2=self.get_max_bigram(second,  third,  first, c4, c5, c6, freq2)
                self.get_similar(s[i + 2], second, i + 2, len)
                if  i < self.strlen(s) - 2:
                    c7, c8, c9, freq3=self.get_max_bigram(third,  first,  second, c7, c8, c9, freq3)
                if  (freq1 >= freq2) and (freq1 >= freq3):
                    self.get_reverse(c3, cstring)
                if  (freq2 >= freq3) and (freq2 >= freq1):
                    self.get_reverse(c5, cstring)
                if  (freq3 >= freq1) and (freq3 >= freq2):
                    self.get_reverse(c7, cstring)
                if  freq1 + freq2 + freq3 == 0:
                    self.get_reverse(s[i], cstring)

                k = 0
                while  cstring[k] > 0:
                    refined[j] = cstring[k]
                    k+=1
                    j+=1
        refined[j] = 0
        j+=1
        return 1

    def all_form_code(self, s, allform):
        j = 0
        for  i in range(0,self.strlen(s)):
            c = 0
            if s[i]==5: c = 1
            elif s[i]==6: c = 2
            elif s[i]==7: c = 3
            elif s[i]==8: c = 4
            elif s[i]==9: c = 5
            elif s[i]==10: c = 6
            elif s[i]==15: c = 7
            elif s[i]==16: c = 8
            elif s[i]==19: c = 9
            elif s[i]==20: c = 10
            elif s[i]==21: c = 11
            elif s[i]==22: c = 16
            elif s[i]==23: c = 21
            elif s[i]==24: c = 26
            elif s[i]==25: c = 31
            elif s[i]==26: c = 36
            elif s[i]==27: c = 41
            elif s[i]==28: c = 46
            elif s[i]==29: c = 51
            elif s[i]==30: c = 56
            elif s[i]==31: c = 61
            elif s[i]==32: c = 66
            elif s[i]==33: c = 71
            elif s[i]==34: c = 76
            elif s[i]==35: c = 81
            elif s[i]==36: c = 86
            elif s[i]==37: c = 91
            elif s[i]==38: c = 96
            elif s[i]==39: c = 101
            elif s[i]==40: c = 106
            elif s[i]==42: c = 111
            elif s[i]==43: c = 116
            elif s[i]==44: c = 121
            elif s[i]==45: c = 126
            elif s[i]==46: c = 131
            elif s[i]==47: c = 136
            elif s[i]==48: c = 141
            elif s[i]==50: c = 146
            elif s[i]==53: c = 151
            elif s[i]==54: c = 156
            elif s[i]==55: c = 161
            elif s[i]==56: c = 166
            elif s[i]==57: c = 171
            elif s[i]==88: c = 11
            elif s[i]==89: c = 176
            elif s[i]==90: c = 181
            elif s[i]==91: c = 186
            elif s[i]==92: c = 191
            elif s[i]==93: c = 196
            elif s[i]==94: c = 201
            elif s[i]==62: c = 206
            elif s[i]==63: c = 207
            elif s[i]==64: c = 208
            elif s[i]==65: c = 209
            elif s[i]==66: c = 210
            elif s[i]==67: c = 211
            elif s[i]==71: c = 212
            elif s[i]==72: c = 213
            elif s[i]==75: c = 214
            elif s[i]==76: c = 215
            elif s[i]==1: c = 216
            elif s[i]==2: c = 217
            elif s[i]==3: c = 218
            elif s[i]==113: c = 219
            if  c == 0:
                allform[j] = 0
                j+=1
                return 0
            if  (c >= 11) and (c <= 201):				
                if s[i]+1==77:
                    if  s[i + 2] == s[i]:
                        c += 2
                        i += 2
                    elif  s[i + 2] == s[i] + 5:
                        c += 7
                        i += 2
                    else:
                        c+=1
                        i+=1
                elif s[i]+1==65:
                    c += 3
                    i+=1
                elif s[i]+1==63:
                    c += 4
                    i+=1
        return 1


    def new_refine_word(self, hs, refined):
        j = 0
        k = 0
        found = 0
        leaf_met = 0
        valid_c = 0
        s = [0] * 50
        c1 = [0] * 20
        cstring = [0] * 50
        alt = [0] * 20
        for i in range(0, 20):
            alt[i] = [0] * 20
        path = [0] * 20
        fpath = [0] * 20
        limit = [0] * 20
        cprob = [0] * 15
        denom = 10000
        prob = 1.0
        maxprob = 0
        tprob = 1.0
        self.strcpy(refined, hs)  
        for i in range(0, self.strlen(hs)):
            if hs[i] == 77: return 2
        if self.strlen(hs) < 2:
            return 1
        len = self.strlen(s)
        for i in range(0, len):
            self.get_similar(s[i], c1, i, len)
            self.strcpy(alt[i], c1)
            limit[i] = self.strlen(c1)
            if limit[i] < 1: limit[i] = 1
        
        i = 0
        j = 0
        tprob = prob = 1.0
        while True:
            if i == 0:
                if j >= limit[i]: break
            path[i] = j
            first = i - 2
            second = i - 1
            third = alt[i][j]
            if first < 0:
                first = 0
            else:
                first = alt[i - 2][path[i - 2]]
            if second < 0:
                second = 0
            else:
                second = alt[i - 1][path[i - 1]]
            
            prob = self.cs[first, second, third]
            if i == len - 1:
                leaf_met += 1
            if prob <= 0:
                i += 1
                while True:
                    i -= 1
                    if i < 0:
                        i = 0
                    j = path[i]
                    j += 1
                    path[i] = j
                    if j >= limit[i]:
                        if i == 0:
                            break
                        else:
                            continue
                    else:
                        if i == 0:
                            tprob = 1.0
                        else:
                            tprob = cprob[i - 1]
                        break
                continue
            else:
                prob /= denom
                tprob *= prob
                cprob[i] = tprob
            i += 1
            j = 0
            if i >= len:
                leaf_met += 1
                valid_c += 1
                
                if tprob > maxprob:
                    found = 1
                    maxprob = tprob
                    for i in range(0, len):
                        fpath[i] = alt[i][path[i]]
                while True:
                    i -= 1
                    if i < 0:
                        i = 0
                    j = path[i]
                    j += 1
                    path[i] = j
                    if j >= limit[i]:
                        if i == 0:
                            break
                        else:
                            continue
                    else:
                        if i == 0:
                            tprob = 1.0
                        else:
                            tprob = cprob[i - 1]
                        break
        
        j = 0
        for i in range(0, len):
            self.get_reverse(fpath[i], cstring)
            k = 0
            while cstring[k] > 0:
                refined[j] = cstring[k]
                k += 1
                j += 1
        refined[j] = 0
        j += 1
        return 0

    def convert_sindhi_urdu(self, sindhi, urdu):
            len = self.strlen(sindhi)
            j = 0

            for  i in range(0,len+1):
                if  sindhi[i] ==74:
                    urdu[j] =204
                    j+=1
            
                elif  sindhi[i] ==36:
                    urdu[j] =38
                    j+=1
                    urdu[j] =72
                    j+=1
                elif  sindhi[i] ==71:
                    urdu[j] =193
                    j+=1
                elif  sindhi[i] ==169:
                    urdu[j] =169
                    j+=1
                    urdu[j] =190
                    j+=1
                elif  sindhi[i] ==135:
                    urdu[j] =134
                    j+=1
                    urdu[j] =190
                    j+=1

                elif  sindhi[i] ==71:
                    urdu[j] =193
                    j+=1
                    urdu[j] =190
                    j+=1
                elif  sindhi[i] ==131:
                    urdu[j] =70 
                    j+=1
                    urdu[j] =190
                    j+=1
                elif  sindhi[i] ==122:
                    urdu[j] =121 
                    j+=1
                    urdu[j] =190
                    j+=1
                elif  sindhi[i] ==141:
                    urdu[j] =136 
                    j+=1
                    urdu[j] =190
                    j+=1
                elif  sindhi[i] ==127:
                    urdu[j] =42 
                    j+=1
                    urdu[j] =190
                    j+=1
                elif  sindhi[i] ==140:
                    urdu[j] =47
                    j+=1
                    urdu[j] =190
                    j+=1
                elif  sindhi[i] ==166:
                    urdu[j] =126 
                    j+=1
                    urdu[j] =190
                    j+=1
                elif  sindhi[i] ==128:
                    urdu[j] =40;
                    j+=1
                    urdu[j] =190
                    j+=1
                elif  sindhi[i] ==71:
                    urdu[j] =193
                    j+=1
                    urdu[j] =190
                    j+=1
                else:
                    urdu[j] = sindhi[i]
                    j+=1
    def post_process(self, hindi, line_size):
            i = 0
            hindi_ptr = 0
            hindi_word_size = 0
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
            hindi_word=[0]*20
            punc1=[0]*5000
            punc2=[0]*5000
            word1=[0]*20
            word2=[0]*20
            word3=[0]*20
            word4=[0]*20
            word5=[0]*20
            temp=[0]*20000


            if  self.conversion_level < 4: return line_size
            if  line_size == 0: return line_size
            if  self.get_line_word_count(hindi, line_size) < 3: 
                return line_size
            self.strcpy(word1, self.QTS)
            self.strcpy(word2, self.QTS)
            self.strcpy(word3, self.QTS)
            self.strcpy(word4, self.QTS)
            self.strcpy(word5, self.QTS)
            while  hindi_ptr < line_size:
                ch = hindi[hindi_ptr]
                ch1 = hindi[hindi_ptr + 1]
                if  (ch == 255) and (ch1 == 254):
                    hindi_ptr += 2
                    continue
                if  flag > 0 or self.check_hindi_punctuation(ch, ch1) > 0:
                    if  hindi_word_size > 0:
                        start1 = start2
                        end1 = end2
                        start2 = start3
                        end2 = end3
                        start3 = start4
                        end3 = end4
                        start4 = start5
                        end4 = end5
                        start5 = hindi_ptr

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

                        for  i in range(0,hindi_word_size): 
                            word5[i] = hindi_word[i]
                        word_size5 = hindi_word_size

                        while  self.check_hindi_punctuation(ch, ch1) > 0:
                            hindi_ptr += 2
                            ch = hindi[hindi_ptr]
                            ch1 = hindi[hindi_ptr + 1]
                            if  hindi_ptr >= line_size:
                                break
                        end5 = hindi_ptr - 1
                        if  not(flag != 0):
                            hindi_ptr -= 2
                        word1[word_size1] = 0
                        word2[word_size2] = 0
                        word3[word_size3] = 0
                        word4[word_size4] = 0
                        word5[word_size5] = 0
                        if  hindi_ptr == 624:
                            i = 0
                        if  self.check_hindi_trigram(word1, word2, word3, word4, word5) > 0:
                            for  i in range(0,self.strlen(word3)): 
                                temp[temp_size] = word3[i]
                                temp_size+=1
                                temp[temp_size] = 9
                                temp_size+=1
                            for  i in range(start3,end3+1): 
                                temp[temp_size] = hindi[i]
                                temp_size+=1
                            self.hindi_trigram_found+=1
                        else:
                            if  self.check_hindi_bigram(word2, word3, word4) > 0:
                                for  i in range(0,self.strlen(word3)): 
                                    temp[temp_size] = word3[i]
                                    temp_size+=1
                                    temp[temp_size] = 9
                                    temp_size+=1
                                for  i in range(start3,end3+1): 
                                    temp[temp_size] = hindi[i]
                                    temp_size+=1
                        flag = 0
                        hindi_word_size = 0
                else:
                    hindi_word[hindi_word_size] = ch
                    hindi_word_size+=1
                    if  hindi_word_size > 18: flag = 1
                hindi_ptr += 2
            if  hindi_word_size > 0:
                start1 = start2
                end1 = end2
                start2 = start3
                end2 = end3
                start3 = start4
                end3 = end4
                start4 = start5
                end4 = end5
                start5 = hindi_ptr

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

                for  i in range(0,hindi_word_size): 
                    word5[i] = hindi_word[i]
                word_size5 = hindi_word_size
                word4[word_size4] = 0
                word5[word_size5] = 0
            word2[word_size2] = 0
            word3[word_size3] = 0
            if  self.check_hindi_trigram(word2, word3, word4, word5, self.QTS) > 0:
                for  i in range(0,self.strlen(word4)): 
                    temp[temp_size] = word4[i]
                    temp_size+=1
                    temp[temp_size] = 9
                    temp_size+=1
                for  i in range(start4,end4+1): 
                    temp[temp_size] = hindi[i]
                    temp_size+=1
                self.hindi_trigram_found+=1
            else:
                self.check_hindi_bigram(word3, word4, word5)
                for  i in range(0,self.strlen(word4)): 
                    temp[temp_size] = word4[i]
                    temp_size+=1
                    temp[temp_size] = 9
                    temp_size+=1
                for  i in range(start4,end4+1): 
                    temp[temp_size] = hindi[i]
                    temp_size+=1


            if  self.check_hindi_trigram(word3, word4, word5, self.QTS, self.QTS) > 0:
                for  i in range(0,self.strlen(word5)): 
                    temp[temp_size] = word5[i]
                    temp_size+=1
                    temp[temp_size] = 9
                    temp_size+=1
                for  i in range(start5,end5+1): 
                    temp[temp_size] = hindi[i]
                    temp_size+=1
            else:
                self.check_hindi_bigram(word4, word5, self.QTS)
                for  i in range(0,self.strlen(word5)): 
                    temp[temp_size] = word5[i]
                    temp_size+=1
                    temp[temp_size] = 9
                    temp_size+=1
                for  i in range(start5,end5+1): 
                    temp[temp_size] = hindi[i]
                    temp_size+=1

            for  i in range(0,temp_size): 
                hindi[i] = temp[i]
            line_size = temp_size
            line_size=self.check_for_vao_in_line(hindi, line_size)
            return line_size
    def check_hindi_bigram(self, word1, word2, word3):
            normalise=[0]*20
            temp_word=[0]*20
            temp_word1=[0]*20
            norm1=[0]*20
            norm2=[0]*20
            hindi_int = [0]*20
            pre_freq = -0.1
            post_freq = -0.1
            start = 0
            end = 0


            pre_freq = -0.1
            post_freq = -0.1

            if  self.strlen(word2) == 0: return 0
            if  (self.strlen(word1) > 14) or (self.strlen(word2) > 14) or (self.strlen(word3) > 14):
                return 0
            for  k in range(0,self.strlen(word2)): 
                hindi_int[k] = word2[k]
            self.normalise_hindi_word(hindi_int, self.strlen(word2), normalise)
            temp_word[0] = temp_word1[0] = 0



            for  k in range(0,self.strlen(word1)): 
                hindi_int[k] = word1[k]
            self.normalise_hindi_word(hindi_int, self.strlen(word1), norm1)
            for  k in range(0,self.strlen(word3)): 
                hindi_int[k] = word3[k]
            self.normalise_hindi_word(hindi_int, self.strlen(word3), norm2)


            start,end,returendFlag = self.search_word_pre_bigram_index(normalise, start, end)
            if  returendFlag > 0:
                pre_freq = self.search_word_pre_bigram(norm2, start, end, temp_word)
            start, end, returendFlag = self.search_word_post_bigram_index(normalise, start, end)
            if  returendFlag > 0:
                post_freq = self.search_word_post_bigram(norm1, start, end, temp_word1)
            if  pre_freq + post_freq <= 0.0: return 3
            if  pre_freq > post_freq:
                self.strcpy(word2, temp_word)
                return 1
            if  post_freq >= pre_freq:
                self.strcpy(word2, temp_word1)
                return 2
            return 3
    def check_hindi_trigram(self, word1, word2, word3, word4, word5):
            normalise=[0]*20
            norm1=[0]*20
            norm2=[0]*20
            temp_word=[0]*20
            temp_word1=[0]*20
            temp_word2=[0]*20
            hindi_int =[0]*20
            start = 0
            end = 0
            pre_freq = 0
            mid_freq = 0
            post_freq = 0;
            if  self.offTriGram:
                return 0
            if  self.strlen(word2) == 0: return 0
            if  self.strlen(word3) == 0: return 0
            if  (self.strlen(word1) > 14) or (self.strlen(word2) > 14) or (self.strlen(word3) > 14) or (self.strlen(word4) > 14) or (self.strlen(word5) > 14):
                return 0

            for  k in range(0,self.strlen(word3)): 
                hindi_int[k] = word3[k]
            self.normalise_hindi_word(hindi_int, self.strlen(word3), normalise)
            temp_word[0] = temp_word1[0] = 0
            pre_freq = mid_freq = post_freq = 0


            start,end,returnedFlag = self.search_word_pre_trigram_index(normalise, start, end)
            if returnedFlag> 0:
                for  k in range(0,self.strlen(word4)): 
                    hindi_int[k] = word4[k]
                self.normalise_hindi_word(hindi_int, self.strlen(word4), norm1)
                for  k in range(0,self.strlen(word5)): 
                    hindi_int[k] = word5[k]
                self.normalise_hindi_word(hindi_int, self.strlen(word5), norm2)
                pre_freq = self.search_word_pre_trigram(norm1, norm2, start, end, temp_word)
            start, end, returnedFlag = self.search_word_mid_trigram_index(normalise, start, end)
            if  returnedFlag > 0:
                for  k in range(0,self.strlen(word2)): 
                    hindi_int[k] = word2[k]
                self.normalise_hindi_word(hindi_int, self.strlen(word2), norm1)
                for  k in range(0,self.strlen(word4)): 
                    hindi_int[k] = word4[k]
                self.normalise_hindi_word(hindi_int, self.strlen(word4), norm2)
                mid_freq = self.search_word_mid_trigram(norm1, norm2, start, end, temp_word1)
            start, end, returnedFlag = self.search_word_post_trigram_index(normalise, start, end)
            if  returnedFlag> 0:
                for  k in range(0,self.strlen(word1)): 
                    hindi_int[k] = word1[k]
                self.normalise_hindi_word(hindi_int, self.strlen(word1), norm1)
                for  k in range(0,self.strlen(word2)): 
                    hindi_int[k] = word2[k]
                self.normalise_hindi_word(hindi_int, self.strlen(word2), norm2)
                post_freq = self.search_word_post_trigram(norm1, norm2, start, end, temp_word2)
            if  mid_freq + pre_freq + post_freq == 0: return 0
            if  mid_freq > pre_freq:
                self.strcpy(word3, temp_word1)
                if  mid_freq < post_freq:
                    self.strcpy(word3, temp_word2)
    
            else:
                self.strcpy(word3, temp_word)
                if  pre_freq < post_freq:
                    self.strcpy(word3, temp_word2)

            return 1
    def search_word_pre_trigram(self, word1, word2, low, high, selected_word):
            first = low
            last = high
            read_word=[0]*20

            while  low <= high:
                mid = int((low + high) / 2)
                if  mid >= len(self.pre_trigram):
                    break
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
    def search_word_mid_trigram(self, word1, word2, low, high, selected_word):
            first = low
            last = high
            read_word=[0]*20

            while  low <= high:
                mid = int((low + high) / 2)
                if  mid >= len(self.mid_trigram):
                    break
                self.strcpy(read_word, self.mid_trigram[mid].first_word)
                if  not(self.strcmp(read_word, word1) != 0):
                    if  self.strcmp(self.mid_trigram[mid].third_word, word2) > 0:
                        dir = -1
                    else: dir = +1
                    while  not (self.strcmp(self.mid_trigram[mid].first_word, word1) != 0):
                        if  not (self.strcmp(self.mid_trigram[mid].third_word, word2) != 0):
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
        self.MSG = self.MSG + s
    
    
    def printMSG2(self, s, v):
        #self.MSG = self.MSG + self.separator + s + v
        self.MSG = self.MSG + s + v
    
    
    def convertToByte(self, u):
        u = u % 256
        return u


    def splitStr(self,txt, seps):
        default_sep = seps[0]
        
        for sep in seps[1:]:
            txt = txt.replace(sep, default_sep)
        return [i.strip() for i in txt.split(default_sep)]

    






