from __future__ import unicode_literals
# import hazm
# import os
# import parsivar 
# import sentencepiece as spm
from googletrans import Translator
from scipy import stats
from time import sleep
import spacy


#---------------------------for google translation---------------------------
class GenRandDelayExpDist():

    def __init__(self,nsamples,lambda_param=0.2,scale=1):
        self.lambda_param = lambda_param
        self.scale = scale
        self.dist = None 
        self.samples = nsamples
        self.sample = None
        self.__exp()

    def __exp(self):
        
        self.dist = stats.expon(self.scale / self.lambda_param)
        self.sample = self.dist.rvs(self.samples)

    def get_sample(self):
        return(self.sample[0])

    def google_translation_func(word):
            
            # tool1: google translator"
            # zh_translation = ts.google(word, from_language='en', to_language='zh')
            # return zh_translation
            while True:
                try:
                    translator = Translator()
                    result = translator.translate(word)
                    return result.text

                    
                except:

                    print("----------server error-------------")
                    grded_obj = GenRandDelayExpDist(1)
                    print("time: ",grded_obj.get_sample())
                    sleep(grded_obj.get_sample())
                    continue



class tokenizer_tools:
# ------------------- persian tokenizers -----------------------------
    def hazm_tokenizer(script):
            # normalizer = hazm.Normalizer()
            # normalized_text = normalizer.normalize(script)
            tokens = hazm.word_tokenize(script)
            with open('out/hazm_tokenizer.txt', 'w+') as f:
                for tok in tokens:
                    en_trans = GenRandDelayExpDist.google_translation_func(tok)
                    f.write(tok)
                    f.write('\t\t\t')
                    f.write(en_trans)
                    f.write('\n')


    def farsi_verb_tokenizer(script):

            perl_file_path = 'Farsi-Verb-Tokenizer-master/script/farsi-verb-tokenizer.perl'
            input_file_path = 'in/processed_text.txt'
            output_file_path = 'out/farsi_verb_tokenizer.txt'
            my_cmd = f"perl {perl_file_path} {input_file_path} > {output_file_path}"
            my_cmd_output = os.popen(my_cmd)
            for line in my_cmd_output:
                print(line.rstrip())

    def parsivar_tokenizer(script):
        my_normalizer = parsivar.Normalizer()
        my_tokenizer = parsivar.Tokenizer()
        tokens = my_tokenizer.tokenize_words(my_normalizer.normalize(script))
        with open('out/parsivar_tokenizer.txt', 'w+') as f:
                for tok in tokens:
                    en_trans = GenRandDelayExpDist.google_translation_func(tok)
                    f.write(tok)
                    f.write('\t\t\t')
                    f.write(en_trans)
                    f.write('\n')

    #----------------------------------urdu tokenizer-----------------------------------

    def sentencepiece_tokenizer(script):

        s = spm.SentencePieceProcessor(model_file='urdu_lm.model')
        for n in range(5):
            pieces=s.encode(script, out_type=str, enable_sampling=True, alpha=0.1, nbest_size=-1)
        detokenized = ''.join(pieces).replace('▁', '\t')
        tokens = detokenized.split('\t')
        with open('out/sentencepiece_tokenizer.txt','w+') as f:
            for tok in tokens:
                en_trans = GenRandDelayExpDist.google_translation_func(tok)
                f.write(tok)
                f.write('\t\t\t')
                f.write(en_trans)
                f.write('\n')

    

    def spacy_tokenizer(script):

        nlp = spacy.blank('ur')
        tokens = nlp(script)
        token_list = []
        for tok in tokens:
            token_list.append(tok.text)
        return token_list
        # with open('out/spacy_tokenizer.txt','w+') as f:
        #     for tok in tokens:
        #         print(tok)
        #         en_trans = GenRandDelayExpDist.google_translation_func(tok)
        #         print(en_trans)
        #         f.write(tok.text)
        #         f.write('\t\t\t')
        #         f.write(en_trans)
        #         f.write('\n')