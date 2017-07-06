#!/usr/bin/python
#
# numerics are converted to num-class
#
# usage:
#       $ python num_class5.py < $inputfile$ > $outputfile
# inputfile: <ENG-sentence><TAB><JPN-sentence>
# outputfile: <ENG-sentence_tokenized><TAB><JPN-sentence_tokenized>
#

import fileinput
import re
import random

#Numeric Class
class AdjustmentInfoClass:
    norm_date = ''
    norm_val  = ''
    orig_txt  = ''
    index     = -1

class Dict:
    key = ''
    val = ''

#Global Variable
adjustments = []
words = []

#Playground
x = AdjustmentInfoClass()
adjustments.append(x);
print(adjustments[0].index)
