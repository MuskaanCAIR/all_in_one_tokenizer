class Gur2Dev():
    gurUnicodeBytes = []
    devUnicodeBytes = []
    devAspiratedFormsMapping = dict()
    gurmukhiNullMapping = dict()
    isGurmukhiBindi = dict()

    def __init__(self):
        self.loadNullMapping()
        self.load_devAspiratedFormsMapping()
        self.load_isGurmukhiBindi()

    def load_isGurmukhiBindi(self):
        if not self.isGurmukhiBindi:
            self.isGurmukhiBindi['\u0A06'] = True
            self.isGurmukhiBindi['\u0A08'] = True
            self.isGurmukhiBindi['\u0A09'] = True
            self.isGurmukhiBindi['\u0A0A'] = True
            self.isGurmukhiBindi['\u0A0F'] = True
            self.isGurmukhiBindi['\u0A10'] = True
            self.isGurmukhiBindi['\u0A13'] = True
            self.isGurmukhiBindi['\u0A14'] = True
            self.isGurmukhiBindi['\u0A3E'] = True
            self.isGurmukhiBindi['\u0A40'] = True
            self.isGurmukhiBindi['\u0A47'] = True
            self.isGurmukhiBindi['\u0A48'] = True
            self.isGurmukhiBindi['\u0A4B'] = True
            self.isGurmukhiBindi['\u0A4C'] = True
            self.isGurmukhiBindi['\u0A73'] = True

    def load_devAspiratedFormsMapping(self):
        if not self.devAspiratedFormsMapping:
            self.devAspiratedFormsMapping[22] = 21
            self.devAspiratedFormsMapping[24] = 23
            self.devAspiratedFormsMapping[27] = 26
            self.devAspiratedFormsMapping[29] = 28
            self.devAspiratedFormsMapping[32] = 31
            self.devAspiratedFormsMapping[37] = 36
            self.devAspiratedFormsMapping[39] = 38
            self.devAspiratedFormsMapping[43] = 42
            self.devAspiratedFormsMapping[45] = 44

    def loadNullMapping(self):
        if not self.gurmukhiNullMapping:
            self.gurmukhiNullMapping[0] = 0
            self.gurmukhiNullMapping[4] = 0
            self.gurmukhiNullMapping[11] = 0
            self.gurmukhiNullMapping[12] = 0
            self.gurmukhiNullMapping[13] = 0
            self.gurmukhiNullMapping[14] = 0
            self.gurmukhiNullMapping[17] = 0
            self.gurmukhiNullMapping[18] = 0
            # self.gurmukhiNullMapping[19] = 0
            self.gurmukhiNullMapping[41] = 40
            self.gurmukhiNullMapping[49] = 48
            self.gurmukhiNullMapping[52] = 0
            self.gurmukhiNullMapping[55] = 54
            self.gurmukhiNullMapping[58] = 0
            self.gurmukhiNullMapping[61] = 0
            self.gurmukhiNullMapping[67] = 48
            self.gurmukhiNullMapping[68] = 0
            self.gurmukhiNullMapping[69] = 0
            self.gurmukhiNullMapping[70] = 0
            self.gurmukhiNullMapping[73] = 0
            self.gurmukhiNullMapping[74] = 0
            self.gurmukhiNullMapping[78] = 0
            self.gurmukhiNullMapping[79] = 0
            self.gurmukhiNullMapping[80] = 0
            self.gurmukhiNullMapping[82] = 0
            self.gurmukhiNullMapping[83] = 0
            self.gurmukhiNullMapping[84] = 0
            self.gurmukhiNullMapping[85] = 0
            self.gurmukhiNullMapping[86] = 0
            self.gurmukhiNullMapping[87] = 0
            self.gurmukhiNullMapping[88] = 21
            self.gurmukhiNullMapping[93] = 0
            self.gurmukhiNullMapping[95] = 0
            self.gurmukhiNullMapping[96] = 0
            self.gurmukhiNullMapping[97] = 0
            self.gurmukhiNullMapping[98] = 0
            self.gurmukhiNullMapping[99] = 0
            self.gurmukhiNullMapping[100] = 0
            self.gurmukhiNullMapping[101] = 0
            self.gurmukhiNullMapping[119] = 0
            self.gurmukhiNullMapping[120] = 0
            self.gurmukhiNullMapping[121] = 0
            self.gurmukhiNullMapping[122] = 0
            self.gurmukhiNullMapping[123] = 0
            self.gurmukhiNullMapping[124] = 0
            self.gurmukhiNullMapping[125] = 0
            self.gurmukhiNullMapping[126] = 0
            self.gurmukhiNullMapping[127] = 0

    def convertGurmukhiToDevanagariText(self, gurmukhiText):
        # print(f'text before normalization:\n {gurmukhiText}')
       
        dev = 9
        gur = 10
        halant = 77
        roman = 0
        nxt=0
        if gurmukhiText[0]:
            self.gurUnicodeBytes = self.str2Byte(self.normaizeGurmukhi(gurmukhiText))
            # print(f'step1: string to byte\n {self.gurUnicodeBytes}')
            self.devUnicodeBytes = [0] * (len(self.gurUnicodeBytes) * 2)
            devptr = 0
            skipCount=0
            for i in range(0, len(self.gurUnicodeBytes)):
                if skipCount > 0:
                    skipCount -= 1
                    continue
                b1 = self.gurUnicodeBytes[i]
                b2 = 0 
                if i < len(self.gurUnicodeBytes) - 2:
                    b2 = self.gurUnicodeBytes[i + 2]
                if i + 1 < len(self.gurUnicodeBytes):
                    nxt = self.gurUnicodeBytes[i + 1]
                else:
                    nxt = 0
                # print(f'{i}     {b1}---->{b2}   devptr: {devptr}')
                #255 is white space 254=small letter thorn
                if b1 == 255 or b1 == 254: continue
                if ((i % 2 != 0) and self.gurUnicodeBytes[i] != gur):
                    # print("from 1st if")
                    self.devUnicodeBytes[devptr] = self.gurUnicodeBytes[i]
                    devptr+=1
                    if i + 1 < len(self.gurUnicodeBytes):
                        self.devUnicodeBytes[devptr] = self.gurUnicodeBytes[i + 1]
                        devptr+=1
                        skipCount = 1
                        continue

                if (i % 2 != 0) and self.gurUnicodeBytes[i] == gur:
                    # print("from 2nd if")
                    self.devUnicodeBytes[devptr] = dev
                    devptr += 1
                elif (i+5 < len(self.gurUnicodeBytes)) and self.gurUnicodeBytes[i] == 92 and self.gurUnicodeBytes[i+1] == 10 and self.gurUnicodeBytes[i+2] == 77 and self.gurUnicodeBytes[i + 3] == 10 and self.gurUnicodeBytes[i + 4] == 57 and self.gurUnicodeBytes[i + 5] == 10:
                    # print("from 2nf if 1st elif")
                    self.devUnicodeBytes[devptr] = 93
                    devptr += 1
                    skipCount = 4
                elif self.gurUnicodeBytes[i] == 112:
                    # print("from 2nf if 2nd elif")
                    self.devUnicodeBytes[devptr] = 2
                    devptr += 1
                elif self.gurUnicodeBytes[i] == 113:
                    # print("from 2nf if 3rd elif")
                    if b2 in self.devAspiratedFormsMapping:
                        # print('aspirated mapping')
                        self.devUnicodeBytes[devptr] = self.devAspiratedFormsMapping[b2]
                        devptr += 1
                    else:
                        # print('not aspirated')
                        self.devUnicodeBytes[devptr] = b2
                        devptr += 1
                    self.devUnicodeBytes[devptr] = dev
                    devptr += 1
                    self.devUnicodeBytes[devptr] = halant
                    devptr += 1
                else:
                    # print('from 2nd if ka else')
                    self.devUnicodeBytes[devptr] = self.gurUnicodeBytes[i]
                    devptr += 1
                # print(f'devUnicode status: \n{self.devUnicodeBytes[:50]}')
        # print(f'devUnicode status: \n{self.devUnicodeBytes}')
        return self.byte2Str(self.devUnicodeBytes, len(self.devUnicodeBytes), True)

    def normalizeDevText(self, devanagariText):
        rstring = ""
        skipCount = 0
        if devanagariText:
            for i in range(0, len(devanagariText)):
                if skipCount > 0:
                    skipCount -= 1
                    continue
                ch = ord(devanagariText[i])
                if i - 1 >= 0:
                    pre = ord(devanagariText[i - 1])
                else:
                    pre = 0
                if i + 1 < len(devanagariText):
                    nxt = ord(devanagariText[i + 1])
                else:
                    nxt = 0
                if i + 2 < len(devanagariText):
                    nxtnxt = ord(devanagariText[i + 2])
                else:
                    nxtnxt = 0
                if nxtnxt > 0:
                    b1 = int(nxtnxt % 256)
                    b2 = int(nxtnxt / 256)
                    b3 = int(ch % 256)
                else:
                    b1 = 0
                    b2 = 0
                    b3 = 0
                if ch == nxtnxt and nxt == 2381:
                    rstring += '\u0971'
                    skipCount = 1
                elif b1 in self.devAspiratedFormsMapping and nxt == 2381 and self.devAspiratedFormsMapping[b1] == b3:
                    rstring += '\u0971'
                    skipCount = 1
                elif ch == 2326 and nxt == 2381 and nxtnxt == 2351:
                    rstring += '\u0971'
                    rstring += chr(ch)
                    skipCount = 2
                elif ch == 2397: #//Rh Apirated
                    rstring += '\u095C' # //ADD D
                    rstring += '\u094D' # //ADD \u094D Perin
                    rstring += '\u0939' # //ADD Ha:
                elif ch == 2337 and ch == 2364: #//Rh Apirated
                    rstring += '\u095C' # //ADD D
                    skipCount = 1
                else:
                    rstring += chr(ch)

        return rstring

    def postProcessingGurText(self, gText):
        rstring = ""
        skipCount = 0
        if gText:
            for i in range(0, len(gText)):
                if skipCount > 0:
                    skipCount -= 1
                    continue
                ch = gText[i]
                if i - 1 >= 0:
                    pre = gText[i - 1]
                else:
                    pre = '\0'
                if i + 1 < len(gText):
                    nxt = gText[i + 1]
                else:
                    nxt = '\0'
                if i + 2 < len(gText):
                    nxtnxt = gText[i + 2]
                else:
                    nxtnxt = '\0'
                if pre in self.isGurmukhiBindi and ch == '\u0A02':
                    rstring += ch
                elif pre not in self.isGurmukhiBindi and ch == '\u0A02':
                    rstring += '\u0A70'
                else:
                    rstring += ch
            if len(rstring) > 0:
                rstring = rstring.replace("\u0A4D\u0A39", "<Perin!h>");
                rstring = rstring.replace("\u0A4D\u0A30", "<Perin!r>");
                rstring = rstring.replace("\u0A4D\u0A35", "<Perin!v>");
                rstring = rstring.replace("\u0A4D", "");
                rstring = rstring.replace("<Perin!h>", "\u0A4D\u0A39");
                rstring = rstring.replace("<Perin!r>", "\u0A4D\u0A30");
                rstring = rstring.replace("<Perin!v>", "\u0A4D" + "\u0A35");
        print(rstring)
        return rstring

    def convertDevanagariToGurmukhiText(self, devanagariText):
        dev = 9
        devByte = False
        gur = 10
        roman = 0
        halant = 77
        gurptr = 0
        text = ""
        if devanagariText:
            self.devUnicodeBytes = self.str2Byte(self.normalizeDevText(devanagariText))
            self.gurUnicodeBytes = [0] * (len(self.devUnicodeBytes) * 2)

            skipCount = 0
            for i in range(0, len(self.devUnicodeBytes)):
                if skipCount > 0:
                    skipCount -= 1
                    continue
                b1 = self.devUnicodeBytes[i]
                b2 = 0
                if i < len(self.devUnicodeBytes) - 2:
                    b2 = self.devUnicodeBytes[i + 2]
                if b1 == 255 or b1 == 254: continue
                if (i % 2 != 0) and self.devUnicodeBytes[i] == dev:
                    self.gurUnicodeBytes[gurptr] = gur
                    gurptr += 1
                    devByte = True
                elif (i % 2 != 0) and self.devUnicodeBytes[i] == roman:
                    self.gurUnicodeBytes[gurptr] = roman
                    gurptr += 1
                    devByte = False
                else:
                    if ((i + 1) < len(self.devUnicodeBytes) and self.devUnicodeBytes[i + 1] == dev and (self.devUnicodeBytes[i] == 100 or self.devUnicodeBytes[i] == 100)):
                        self.gurUnicodeBytes[gurptr] = self.devUnicodeBytes[i]
                        gurptr += 1
                        self.gurUnicodeBytes[gurptr] = self.devUnicodeBytes[i + 1]
                        gurptr += 1
                        skipCount += 1
                    elif (i+1 < len(self.devUnicodeBytes) and self.devUnicodeBytes[i+1] == dev and self.devUnicodeBytes[i] in self.gurmukhiNullMapping):
                        self.gurUnicodeBytes[gurptr] = self.gurmukhiNullMapping[self.devUnicodeBytes[i]]
                        gurptr+=1
                    else:
                        self.gurUnicodeBytes[gurptr] = self.devUnicodeBytes[i]
                        gurptr += 1

        if self.gurUnicodeBytes:
            text = self.byte2Str(self.gurUnicodeBytes, len(self.gurUnicodeBytes), True)
            text1 = text[0: int(gurptr / 2)]
            text = self.postProcessingGurText(text1)
            print(text)
        return text

    def normaizeGurmukhi(self, GurText):
        s = GurText
        s = s.replace("\u0A38\u0A3C", "\u0A36")
        s = s.replace("\u0A32\u0A3C", "\u0A33")
        s = s.replace("\u0A17\u0A3C", "\u0A5A")
        s = s.replace("\u0A1C\u0A3C", "\u0A5B")
        s = s.replace("\u0A21\u0A3C", "\u0A5C")
        s = s.replace("\u0A2B\u0A3C", "\u0A5E")
        s = s.replace("\u0A16\u0A3C", "\u0A59")
        # print(f'after normalization:\n{s}')
        return s

    def byte2Str(self, data, length, SKIPFIRST2BYTES):
        s = ""
        b1 = 10
        b2 = 111
        # c1 = b1 * 256 + b2
        # c = (c1)
        # print('\n',c)
        if SKIPFIRST2BYTES:
            for t in range(0, length, 2):
                b1 = data[t]
                b2 = data[t + 1]
                if b1 == 255 and b2 == 254:
                    continue
                elif b1 == 11111:
                    b1 = 10
                c1 = b1 + (b2 * 256)
                if c1 != 0:
                    c = chr(c1)
                    s = s + c
        else:
            for t in range(0, length, 2):
                b1 = data[t]
                b2 = data[t + 1]
                if b1 == 255 and b2 == 254:
                    continue
                #signify end of line or something
                elif b1 == 11111:
                    b1 = 10
                c1 = b1 + (b2 * 256)
                if c1 != 0:
                    c = c1
                    s = s + c
               
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
            firstByte = int(code % 256)
            secondByte = int(code / 256)
            # print(f'{str1[t]} ---->{ch} --->{firstByte} --->{secondByte}')
            #signify end of line or something
            if firstByte == 10 and secondByte == 0:
                data[length] = 11111
            else:
                data[length] = firstByte
            length += 1
            data[length] = secondByte
            length += 1
        # print(data)
        return data