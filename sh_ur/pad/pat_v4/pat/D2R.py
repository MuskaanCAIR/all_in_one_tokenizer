class HindiToRoman():    #{
    mapper = dict()
    romanWord=''
    devConsonants=[]
    SindhiDevWord=''
    def __init__(self):
                if  not self.mapper:
                    self.initMapper()
                if  not self.devConsonants:
                    self.initDevConsonants()

    def isDevFullVowels(self,ch):
                start = '\u0907'
                end = '\u0910'
                flag = (ch >= start and ch <= end)
                return flag

    def initDevConsonants(self): 
                self.devConsonants.append('\u0915')
                self.devConsonants.append('\u0916')
                self.devConsonants.append('\u0917')
                self.devConsonants.append('\u0918')
                self.devConsonants.append('\u0919')
                self.devConsonants.append('\u091A')
                self.devConsonants.append('\u091B')
                self.devConsonants.append('\u091C')
                self.devConsonants.append('\u091D')
                self.devConsonants.append('\u091E')
                self.devConsonants.append('\u091F')
                self.devConsonants.append('\u0920')
                self.devConsonants.append('\u0921')
                self.devConsonants.append('\u0922')
                self.devConsonants.append('\u0923')
                self.devConsonants.append('\u0924')
                self.devConsonants.append('\u0925')
                self.devConsonants.append('\u0926')
                self.devConsonants.append('\u0927')
                self.devConsonants.append('\u0928')
                self.devConsonants.append('\u0929')
                self.devConsonants.append('\u092A')
                self.devConsonants.append('\u092B')
                self.devConsonants.append('\u092C')
                self.devConsonants.append('\u092D')
                self.devConsonants.append('\u092E')
                self.devConsonants.append('\u092F')
                self.devConsonants.append('\u0930')
                self.devConsonants.append('\u0931')
                self.devConsonants.append('\u0932')
                self.devConsonants.append('\u0933')
                self.devConsonants.append('\u0934')
                self.devConsonants.append('\u0935')
                self.devConsonants.append('\u0936')
                self.devConsonants.append('\u0937')
                self.devConsonants.append('\u0938')
                self.devConsonants.append('\u0939')
                #h
                self.devConsonants.append('\u0958')
                self.devConsonants.append('\u0959')
                self.devConsonants.append('\u095A')
                self.devConsonants.append('\u095B')
                self.devConsonants.append('\u095C')
                self.devConsonants.append('\u095D')
                self.devConsonants.append('\u095E')
                self.devConsonants.append('\u095F')
                self.devConsonants.append('\u095A')
                self.devConsonants.append('\u095B')
                self.devConsonants.append('\u095C')
                self.devConsonants.append('\u095D')
                self.devConsonants.append('\u095E')
                self.devConsonants.append('\u095F')
                self.devConsonants.append('\u097A')
                self.devConsonants.append('\u097B')
                self.devConsonants.append('\u097C')
                self.devConsonants.append('\u097E')
                self.devConsonants.append('\u097F')

    def initMapper(self):
            self.mapper["\u0901"]="'n"
            self.mapper["\u0902"]="'n"
            self.mapper["\u0905"]="a"
            self.mapper["\u0906"]="aa"
            self.mapper["\u0907"]="i"
            self.mapper["\u0908"]="ee"
            self.mapper["\u0909"]="u"
            self.mapper["\u090A"]="oo"
            self.mapper["\u090F"]="e"
            self.mapper["\u0910"]="ai"
            self.mapper["\u0911"]="aa"
            self.mapper["\u0913"]="o"
            self.mapper["\u0914"]="au"
            self.mapper["\u0915"]="k"
            self.mapper["\u0916"]="kh"
            self.mapper["\u0917"]="g"
            self.mapper["\u0918"]="gh"
            self.mapper["\u0919"]="g~"
            self.mapper["\u091A"]="ch"
            self.mapper["\u091B"]="chh"
            self.mapper["\u091C"]="j"
            self.mapper["\u091D"]="jh"
            self.mapper["\u091E"]="j~"
            self.mapper["\u091F"]="t"
            self.mapper["\u0920"]="th"
            self.mapper["\u0921"]="d"
            self.mapper["\u0922"]="dh"
            self.mapper["\u0923"]="n~"
            self.mapper["\u0924"]="t~"
            self.mapper["\u0925"]="th~"
            self.mapper["\u0926"]="d~"
            self.mapper["\u0927"]="dh~"
            self.mapper["\u0928"]="n"
            self.mapper["\u0929"]="n"
            self.mapper["\u092A"]="p"
            self.mapper["\u092B"]="ph"
            self.mapper["\u092C"]="b"
            self.mapper["\u092D"]="bh"
            self.mapper["\u092E"]="m"
            self.mapper["\u092F"]="y"
            self.mapper["\u0930"]="r"
            self.mapper["\u0931"]="r"
            self.mapper["\u0932"]="l"
            self.mapper["\u0933"]="l"
            self.mapper["\u0934"]="l"
            self.mapper["\u0935"]="v"
            self.mapper["\u0936"]="sh"
            self.mapper["\u0937"]="sh"
            self.mapper["\u0938"]="s"
            self.mapper["\u0939"]="h"
            #093C
            self.mapper["\u093C"]= ""
            # Bindi
            self.mapper["\u093E"]="aa"
            self.mapper["\u093F"]="i"
            self.mapper["\u0940"]="ee"
            self.mapper["\u0941"]="u"
            self.mapper["\u0942"]="oo"
            self.mapper["\u0947"]="e"
            self.mapper["\u0948"]="ai"
            self.mapper["\u0949"]="aa"
            self.mapper["\u094B"]="o"
            self.mapper["\u094C"]="au"
            self.mapper["\u094D"]=""
            self.mapper["\u0950"]="OM"
            self.mapper["\u0953"]= ""
            self.mapper["\u0958"]="q"
            self.mapper["\u0959"]="khh"
            self.mapper["\u095A"]="ghh"
            self.mapper["\u095B"]="z"
            self.mapper["\u095C"]="r^"
            self.mapper["\u095D"]="rh"
            self.mapper["\u095E"]="f"
            self.mapper["\u095F"]="y"
            self.mapper["\u0960"]="ri"
            self.mapper["\u0964"]="."
            self.mapper["\u0965"]=".."
            self.mapper["\u0966"]="0"
            self.mapper["\u0967"]="1"
            self.mapper["\u0968"]="2"
            self.mapper["\u0969"]="3"
            self.mapper["\u096A"]="4"
            self.mapper["\u096B"]="5"
            self.mapper["\u096C"]="6"
            self.mapper["\u096D"]="7"
            self.mapper["\u096E"]="8"
            self.mapper["\u096F"]="9"
            self.mapper["\u0970"]="."
            self.mapper["\u0971"]="."
            self.mapper["\u097B"]="g^"
            self.mapper["\u097C"]="j^"
            self.mapper["\u097E"]="d^"
            self.mapper["\u097F"]="b^"

    def normaizeDevanagari(self,devText):
                s = devText
                s = s.replace("\u094D\u093C", "\u093C\u094D")
                s = s.replace("\u0938\u093C", "\u0936")
                s = s.replace("\u0932\u093C", "\u0933")
                s = s.replace("\u0917\u093C", "\u095A")
                s = s.replace("\u091C\u093C", "\u095B")
                s = s.replace("\u0921\u093C", "\u095C")
                s = s.replace("\u092B\u093C", "\u095E")
                s = s.replace("\u0916\u093C", "\u0959")
                s = s.replace("\u0915\u093C", "\u0915")
                s = s.replace("\u0917\u0952", "\u097B")
                s = s.replace("\u091C\u0952", "\u097C")
                s = s.replace("\u0921\u0952", "\u097E")
                s = s.replace("\u092C\u0952", "\u097F")
                if  s.IndexOf("\u0952") != -1:
                        i = 0
                        returnWord = ""
                        skipCount = 0
                        found =  False
                        for ch in s:
                            if  skipCount > 0:
                                skipCount-=1
                                i+=1
                                continue

                            isbarChar = ch == ('\u0917') or ch == '\u091C' or ch=='\u0921' or ch=='\u092C'
                            if  isbarChar:
                                subword = ""
                                j = i+1
                                while j<len(s) and (s[j]!='\u0952'):
                                    t=s[j]
                                    t1=[s-1]
                                    t2=[s+1]
                                    if s[j] in self.devConsonants:
                                        subword = ""
                                        break

                                    subword += s[j]
                                    j+=1

                                if len(subword)> 0 or (s[j] == '\u0952'):

                                    skipCount = len(subword)+ 1

                                    if  ch == ('\u0917'):
                                        returnWord += "\u097B" + subword
                                        found = True

                                    elif  ch == '\u091C':
                                        returnWord += "\u097C" + subword
                                        found = True

                                    elif  ch == '\u0921':
                                        returnWord += "\u097E" + subword
                                        found = True

                                    elif  ch == '\u092C':
                                        returnWord += "\u097F" + subword
                                        found = True

                                    else:
                                        returnWord += ch + subword

                                else:
                                    returnWord += ch

                            else:

                                returnWord += ch

                            i+=1


                        if  found:
                            s = returnWord

                return s

    def isTerminationChar(self,nxtChar):

                flag = (nxtChar == '\u0964' or nxtChar == '\u0965' or ord(nxtChar) < 127)
                return flag

    def isVowelToForceShawa_off(self,vowel):
                return (vowel == '\u093E'
                    or vowel == '\u0940'
                    or vowel == '\u0941')

    def isVowelToForceShawa(self,vowel):
                return  False

    def getRomanForm(self,SindhiDevText):

                skipNext = 0
                romanText=""
                nxtChar='\0'
                nxtnxtChar = '\0'
                preChar = '\0'
                prepreChar = '\0'
                if  not SindhiDevText or SindhiDevText.isspace():
                    return ""
                else:

                    for  i in range(0,len(SindhiDevText)):

                        if  skipNext > 0:

                            skipNext-=1
                            continue

                        if  i - 2>=0:
                            prepreChar = SindhiDevText[i - 2]
                        if  i - 1 >= 0:
                            preChar = SindhiDevText[i - 1]
                        ch=SindhiDevText[i]

                        
                        if  (i + 1) < len(SindhiDevText):
                            nxtChar = SindhiDevText[i + 1]
                        if  (i + 2) < len(SindhiDevText):
                            nxtnxtChar = SindhiDevText[i + 2]

                        if  len(self.mapper) > 0 and ch in self.mapper:

                            self.romanWord=self.mapper[ch]

                            if  ch== '\u091C' and nxtChar == '\u094D' and nxtnxtChar== '\u091E':
                                romanText += "gy"
                                skipNext = 2
                            elif  ch in self.devConsonants and nxtChar == '\u094D':

                                romanText += self.romanWord

                            elif  self.isTerminationChar(preChar) and ch in self.devConsonants and self.isDevFullVowels(nxtChar):
                                romanText += self.romanWord + 'a'

                            elif  preChar == '\u094D' and ch in self.devConsonants and (nxtChar in self.devConsonants or self.isTerminationChar(nxtChar)):

                                if  self.isTerminationChar(nxtChar):
                                    romanText += self.romanWord
                                else:
                                    romanText += self.romanWord + 'a'

                            elif  ch in self.devConsonants and (nxtChar in self.devConsonants or nxtChar=='\u0902'):

                                if  nxtChar == '\u0902' and nxtnxtChar not in self.devConsonants:
                                    romanText += self.romanWord
                                else:
                                    romanText += self.romanWord + 'a'

                            elif  preChar in self.devConsonants and ch in self.devConsonants and self.isTerminationChar(nxtChar):

                                if  prepreChar in self.devConsonants or prepreChar == '\u094D':
                                    romanText += self.romanWord
                                else:
                                    romanText += self.romanWord

                            elif  prepreChar in self.devConsonants and self.isVowelToForceShawa(preChar) and ch in self.devConsonants and (nxtChar in self.devConsonants or self.isTerminationChar(nxtChar)):

                                romanText += self.romanWord + 'a'

                            else:
                                romanText += self.romanWord

                        else:

                            if  ord(ch) < 127:
                                romanText += ch

                    return romanText