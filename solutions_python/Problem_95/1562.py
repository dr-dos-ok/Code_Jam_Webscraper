googlerese = {'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d',
				'j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z',
				'r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}

test1 = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
hello i am the google code jam test data
how are you
aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny ieeeeeeeee
y n f i c w l b k u o m x s e v z p d r j g a t h a q set k oset xa ynfd
schr rkxc tesr aej dksl tkrb xc
aej ncrrcp fjr rbc vkqqy ks wejp vkcfcd ncfyjdc kx ser bjslpa csejlb re cyr dkh
lpccrksld fbccdc vevdkfmc rbc sjxncp aej bygc ikymci kd fjppcsrma ejr ew vepofbevd
kx fexxysicp dbcvypi ysi rbkd kd xa wygepkrc vpenmcx es rbc leelmc feic uyx
na rbc vpkfoksl ew xa rbjxnd dexcrbksl tkfoci rbkd tya fexcd
set kd rbc djxxcp ew ejp myfo ew ikdfesrcsr
eb seeeee lellymep kd bcyici wep rbc epvbysylc
eb xa lei mcrd xyoc ejr
wpkcsid iesr mcr wpkcsid mcr dfkcsrkwkf vpelpcdd le nekso
ymm aejp nydc ypc ncmesl re cppep rbc dveesa nypi
njww rpasiyxcpc ysi yxjxj
aej oset aej tysr re
ks y tepmi ew ikpctemgcd ysi mkesd dexcrkxcd rbc pypcdr fpcyrjpc kd y wpkcsi
k bygc ncdrci wpjkr dvkoc ysi xees set k dbymm ncdr aej rbc lja
tbeeeeeeeeeeeeeeeeeeeyyyyyyyyy k oset f vmjd vmjd
xa syxc kd ijl k bygc ujdr xcr aej ysi k meeegc aej
pklbr k wepler bcpc ks rbc dryrcd aej fymm kr y dyjdylc ks rbc xejrb
eb byk kx ks jp fexvjrcp cyrksl aejp fbccqnjplcpd ysi leelmcpcdksl aejp rchrq
mcr mkvd ie tbyr bysid ie
rbkd kd de chfkrksl k bygc re le rbc nyrbpeex
wep rbedc tbe dvcyo ks y resljc ie ser dvcyo re erbcp vcevmc
seneia jsicpdrysid rbcx dksfc rbca ypc dvcyoksl xadrcpkcd ks rbc dvkpkr
ip qykjd ip qykjd ip qykjd ip qykjd eeeeeeeeeeeeb ip qykjd"""
test2 = ["ejp mysljylc kd kxveddknmc re jsicpdrysi","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","de kr kd eoya kw aej tysr re ujdr lkgc jv","hello i am the google code jam test data","how are you","aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny ieeeeeeeee","y n f i c w l b k u o m x s e v z p d r j g a t h a q set k oset xa ynfd","schr rkxc tesr aej dksl tkrb xc","ymm aejp nydc ypc ncmesl re cppep rbc dveesa nypi","wpkcsid iesr mcr wpkcsid mcr dfkcsrkwkf vpelpcdd le nekso","wep rbedc tbe dvcyo ks y resljc ie ser dvcyo re erbcp vcevmc","seneia jsicpdrysid rbcx dksfc rbca ypc dvcyoksl xadrcpkcd ks rbc dvkpkr","kx fexxysicp dbcvypi ysi rbkd kd xa wygepkrc vpenmcx es rbc leelmc feic uyx","ys cac wep ys cac ysi y vklces wep y vklces","njww rpasiyxcpc ysi yxjxj","aej oset aej tysr re","set rbyr aej oset leelmcpcdc vmcydc ie ser jdc kr re byfo ksre ejp dadrcxd","eb byk kx ks jp fexvjrcp cyrksl aejp fbccqnjplcpd ysi leelmcpcdksl aejp rchrq","k bygc ncdrci wpjkr dvkoc ysi xees set k dbymm ncdr aej rbc lja","cyfb ew jd byd bkd ets dvcfkym lkwr ysi aej oset rbkd tyd xcysr re nc rpjc","ysi kw aej iesr jsicpcdrkxyrc xc k tesr jsicpcdrkxyrc aej","pklbr k wepler bcpc ks rbc dryrcd aej fymm kr y dyjdylc ks rbc xejrb","na rbc vpkfoksl ew xa rbjxnd dexcrbksl tkfoci rbkd tya fexcd","set kd rbc djxxcp ew ejp myfo ew ikdfesrcsr","aej ncrrcp fjr rbc vkqqy ks wejp vkcfcd ncfyjdc kx ser bjslpa csejlb re cyr dkh","bet ypc aej bemiksl jv ncfyjdc kx y veryre","rbkd bcpc kd ljsveticp yfrkgyrci rtcsra dcgcs fymkncp wjmm yjre se okfonyfo sykmrbpetksl xyabcx","vscjxesejmrpyxkfpedfevkfdkmkfegemfysefeskedkd","ks y tepmi ew ikpctemgcd ysi mkesd dexcrkxcd rbc pypcdr fpcyrjpc kd y wpkcsi","lpccrksld fbccdc vevdkfmc rbc sjxncp aej bygc ikymci kd fjppcsrma ejr ew vepofbevd"]

def translate(strings1):
	"""
	Strings is a list of strings.
	Prints some statements.  Returns None.
	"""
	strings = strings1.split('\n')
	case_num = 1
	for stringy in strings:
		outstr = "Case #"+str(case_num)+": "
		for letter in stringy:
			if letter in googlerese:
				outstr += googlerese[letter]
			else:
				outstr += letter
		case_num += 1
		print outstr
		
