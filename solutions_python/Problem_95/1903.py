# Speaking in Tongues

string = [30,
'ejp mysljylc kd kxveddknmc re jsicpdrysi',
'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
'de kr kd eoya kw aej tysr re ujdr lkgc jv',
'hello i am the google code jam test data',
'how are you',
'aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny ieeeeeeeee',
'y n f i c w l b k u o m x s e v z p d r j g a t h a q set k oset xa ynfd',
'schr rkxc tesr aej dksl tkrb xc',
'set kd rbc djxxcp ew ejp myfo ew ikdfesrcsr',
'mcr mkvd ie tbyr bysid ie',
'cyfb ew jd byd bkd ets dvcfkym lkwr ysi aej oset rbkd tyd xcysr re nc rpjc',
'ysi kw aej iesr jsicpcdrkxyrc xc k tesr jsicpcdrkxyrc aej',
'aej vkddci eww rbc fbkfocs myia',
'w ew rte czjymd w ew esc czjymd esc',
'wep k ncrtccs rbpcc ysi s w ew k czjymd w ew k xksjd esc vmjd w ew k xksjd rte',
'rbkd bcpc kd ljsveticp yfrkgyrci rtcsra dcgcs fymkncp wjmm yjre se okfonyfo sykmrbpetksl xyabcx',
'k bygc ncdrci wpjkr dvkoc ysi xees set k dbymm ncdr aej rbc lja',
'bet ypc aej bemiksl jv ncfyjdc kx y veryre',
'wpkcsid iesr mcr wpkcsid mcr dfkcsrkwkf vpelpcdd le nekso',
'eb byk kx ks jp fexvjrcp cyrksl aejp fbccqnjplcpd ysi leelmcpcdksl aejp rchrq',
'ejp feic uyx kd mkoc rbc varbylepcys rbcepcx',
'rbcpc kd se ysdtcp',
'kr tyd rbc ncdr ew rkxcd kr tyd rbc nmjpdr ew rkxcd',
'tbeeeeeeeeeeeeeeeeeeeyyyyyyyyy k oset f vmjd vmjd',
'njww rpasiyxcpc ysi yxjxj',
'aej oset aej tysr re',
'na rbc vpkfoksl ew xa rbjxnd dexcrbksl tkfoci rbkd tya fexcd',
'lpccrksld fbccdc vevdkfmc rbc sjxncp aej bygc ikymci kd fjppcsrma ejr ew vepofbevd',
'kx fexxysicp dbcvypi ysi rbkd kd xa wygepkrc vpenmcx es rbc leelmc feic uyx',
'dtkwr yd rbc tksi zjkcr yd rbc wepcdr drcyia yd rbc xejsryks']


def translate(char):    
    english = 'abcdefghijklmnopqrstuvwxyz'
    google =  'ynficwlbkuomxsevzpdrjgthaq'
    return english[google.index(char)]


def toenglish(T, string):
    translated = ''
    if 1 <= T and T <= 30:
        for i in range(T):
            if len(string[i]) <= 100:
                for a in string[i]:
                    if ' ' not in a:                        
                        translated += translate(a)
                    else:
                        translated += ' '                    
                print 'Case #'+str(i+1)+': '+translated
                translated = ''            
            
toenglish(string[0], string[1:])

