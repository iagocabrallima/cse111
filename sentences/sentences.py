import random

def main():
    
    determiners=['a','a few', 'a little', 'all', 'an', 'another', 'any', 'anybody', 'anyone', 'anything' ,'anywhere', 'both', 'certain', 'each', 'either', 'enough', 'every', 'everybody', 'everyone'
'ever', 'thing', 'everywhere', 'few', 'fewer', 'fewest', 'last' ,'least', 'less', 'little', 'many', 'many a', 'more', 'most' , 'much', 'neither', 'next' , 'no' , 'no one', 'nobody', 'none', 'nothing'
'no', 'where', 'once', 'one' , 'said' , 'several' , 'some', 'somebody', 'something', 'somewhere', 'sufficient' , 'that', 'thethese', 'this', 'those', 'three', 'thrice', 'twice', 'two', 'us', 'various', 'we', 'what', 'hatever', 'which', "whichever", "you", "zero"]
    nouns=[ 'people','history','way', 'art','world','information', 'map', 'two', 'family','government','health','system','computer','meat','year','thanks','music','person','reading','method','data','food','understanding', 'theory','law','bird','literature','problem','software','control']
    verbs = ['abandon', 'abase', 'abate', 'abbreviate', 'abdicate', 'abduct', 'abet', 'abhor', 'abide', 'abjure', 'abnegate', 'abolish', 'abominate', 'abort', 'abound', 'abrade', 'abridge', 'abrogate', 'abscond', 'abseil', 'absent', 'absolve', 'absorb', 'abstain', 'abstract', 'abuse', 'abut', 'accede', 'accelerate', 'accent', 'accentuate', 'accept', 'access', 'accessorise', 'accessorize', 'acclaim', 'acclimate', 'acclimatise', 'acclimatize', 'accommodate', 'accompany', 'accomplish', 'accord', 'accost', 'account', 'accouter', 'accoutre', 'accredit', 'accrue', 'acculturate', 'accumulate', 'accuse', 'accustom', 'ace', 'ache', 'achieve']
    
    get_determiner(determiners)
    get_noun(nouns)
    get_verb(verbs)
    
    print(get_determiner(determiners),get_noun(nouns),get_verb(verbs))

def get_determiner(determiners):
    determiner=random.choice(determiners)
    return determiner

def get_noun(nouns):
    noun=random.choice(nouns)
    return noun

def get_verb(verbs):
    verb=random.choice(verbs)
    return verb

main()