import os
from definitions import ROOT_DIR
from .dict import Dict

#Dictionary file
NUM_ALPHABET_EN = os.path.join(ROOT_DIR,'conf/num_alphabet_en');
NUM_KANJI_JA = os.path.join(ROOT_DIR,'conf/num_kanji_ja');

#Lexer
class Lexer:
    def __init__(self):
        self.num_map_en = self._loadDictCsv(NUM_ALPHABET_EN,'en')
        self.num_map_ja = self._loadDictCsv(NUM_KANJI_JA,'ja')

    def _loadDictCsv(self,txtfile,lang):
        #result = []
        result = {}
        for line in open(txtfile,"r").readlines():
            line = line.replace("\r\n", "")
            line = line.split(',')
            if self._isComment(line):
                continue
            #word = Dict(line[0],line[1],lang)
            #result.append(word)
            result[line[0]] = line[1]
        return result

    def _isComment(self,text):
        x = text[:1]
        return x == '//'

    def _isEn(self,lang):
        return lang == 'en'

    def GetToken(word,lang):
        if self._isEn(lang):
            map_list = self.num_map_en
        else:
            map_list = self.num_map_ja

        if word in map_list:
            return map_list[word]
        else:
            return None
