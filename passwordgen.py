#!/usr/bin/env python2

import random
import requests

dictionary = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = requests.get(dictionary)
WORDS = response.content.splitlines()
no_words = 2
no_passwds = 10

for j in range(no_passwds):
    mypw = ""
    for i in range(no_words):
        next_index = random.randrange(len(WORDS))
        mypw = mypw + str(WORDS[next_index])

    print(mypw)
