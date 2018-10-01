{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 2, 11, 1692, 163444, 206929, 459923, 691520, 40, 999993, 612112, 908502, 241453, 926904, 567583, 718525, 994798, 999992, 930033, 25, 1250, 9, 91633, 200917, 5, 7, 4, 999999, 591085, 769864, 71189, 166, 476216, 933652, 609465, 859561, 151411, 58908, 842361, 12500, 323139, 999991, 125, 936133, 51830, 482657, 20, 116539, 34, 864874, 832128, 999995, 369944, 999996, 984828, 8, 316091, 125000, 963821, 3, 900468, 124, 938493, 479210, 594362, 943739, 109175, 210398, 558587, 61739, 1000000, 442303, 838365, 404663, 139873, 999994, 622115, 6665, 200, 434677, 794175, 959320, 446431, 270963, 249267, 328146, 438600, 685319, 790765, 999997, 382063, 521535, 570226, 555254, 365801, 406629, 10, 999998, 6]\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "os.chdir(\"D:/Code Jam/Qual_round_task1\")\n",
    "\n",
    "def readFile(f):\n",
    "    List=[]\n",
    "    with open(f) as handle:\n",
    "        N=int(handle.readline())\n",
    "        for n in range(N):\n",
    "            element=int(handle.readline())\n",
    "            List.append(element)\n",
    "    return List\n",
    "data=readFile(\"A-large.in\")\n",
    "print data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "x=1\n",
    "#len(set(str(x)))\n",
    "def Solve(x):\n",
    "    i=1\n",
    "    digits=set()\n",
    "    while True:\n",
    "        if x==0:\n",
    "            result=\"INSOMNIA\"\n",
    "            break\n",
    "        if i>1e6:     #our \"stop condition\" for insomnia is simply 1million tries. I checked that for numbers 1-1e6 it never happens\n",
    "            result=\"INSOMNIA\"\n",
    "            break\n",
    "        y=x*i\n",
    "        digits=digits.union(set(str(y)))\n",
    "        if len(digits)==10:\n",
    "            result=y\n",
    "            break\n",
    "        i+=1\n",
    "    return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: INSOMNIA\n",
      "\n",
      "Case #2: 10\n",
      "\n",
      "Case #3: 90\n",
      "\n",
      "Case #4: 110\n",
      "\n",
      "Case #5: 5076\n",
      "\n",
      "Case #6: 653776\n",
      "\n",
      "Case #7: 620787\n",
      "\n",
      "Case #8: 4139307\n",
      "\n",
      "Case #9: 2074560\n",
      "\n",
      "Case #10: 920\n",
      "\n",
      "Case #11: 9999930\n",
      "\n",
      "Case #12: 4896896\n",
      "\n",
      "Case #13: 3634008\n",
      "\n",
      "Case #14: 724359\n",
      "\n",
      "Case #15: 2780712\n",
      "\n",
      "Case #16: 1702749\n",
      "\n",
      "Case #17: 3592625\n",
      "\n",
      "Case #18: 4973990\n",
      "\n",
      "Case #19: 5999952\n",
      "\n",
      "Case #20: 4650165\n",
      "\n",
      "Case #21: 900\n",
      "\n",
      "Case #22: 90000\n",
      "\n",
      "Case #23: 90\n",
      "\n",
      "Case #24: 733064\n",
      "\n",
      "Case #25: 602751\n",
      "\n",
      "Case #26: 90\n",
      "\n",
      "Case #27: 70\n",
      "\n",
      "Case #28: 92\n",
      "\n",
      "Case #29: 9999990\n",
      "\n",
      "Case #30: 2364340\n",
      "\n",
      "Case #31: 2309592\n",
      "\n",
      "Case #32: 640701\n",
      "\n",
      "Case #33: 5478\n",
      "\n",
      "Case #34: 1904864\n",
      "\n",
      "Case #35: 1867304\n",
      "\n",
      "Case #36: 2437860\n",
      "\n",
      "Case #37: 4297805\n",
      "\n",
      "Case #38: 908466\n",
      "\n",
      "Case #39: 235632\n",
      "\n",
      "Case #40: 3369444\n",
      "\n",
      "Case #41: 900000\n",
      "\n",
      "Case #42: 2908251\n",
      "\n",
      "Case #43: 9999910\n",
      "\n",
      "Case #44: 9000\n",
      "\n",
      "Case #45: 3744532\n",
      "\n",
      "Case #46: 207320\n",
      "\n",
      "Case #47: 1930628\n",
      "\n",
      "Case #48: 900\n",
      "\n",
      "Case #49: 349617\n",
      "\n",
      "Case #50: 918\n",
      "\n",
      "Case #51: 4324370\n",
      "\n",
      "Case #52: 4992768\n",
      "\n",
      "Case #53: 6999965\n",
      "\n",
      "Case #54: 2589608\n",
      "\n",
      "Case #55: 5999976\n",
      "\n",
      "Case #56: 6893796\n",
      "\n",
      "Case #57: 96\n",
      "\n",
      "Case #58: 1580455\n",
      "\n",
      "Case #59: 9000000\n",
      "\n",
      "Case #60: 4819105\n",
      "\n",
      "Case #61: 30\n",
      "\n",
      "Case #62: 4502340\n",
      "\n",
      "Case #63: 2356\n",
      "\n",
      "Case #64: 5630958\n",
      "\n",
      "Case #65: 1437630\n",
      "\n",
      "Case #66: 1783086\n",
      "\n",
      "Case #67: 6606173\n",
      "\n",
      "Case #68: 436700\n",
      "\n",
      "Case #69: 841592\n",
      "\n",
      "Case #70: 3910109\n",
      "\n",
      "Case #71: 308695\n",
      "\n",
      "Case #72: 9000000\n",
      "\n",
      "Case #73: 2211515\n",
      "\n",
      "Case #74: 3353460\n",
      "\n",
      "Case #75: 2427978\n",
      "\n",
      "Case #76: 1398730\n",
      "\n",
      "Case #77: 5999964\n",
      "\n",
      "Case #78: 3732690\n",
      "\n",
      "Case #79: 73315\n",
      "\n",
      "Case #80: 9000\n",
      "\n",
      "Case #81: 2173385\n",
      "\n",
      "Case #82: 3176700\n",
      "\n",
      "Case #83: 2877960\n",
      "\n",
      "Case #84: 3125017\n",
      "\n",
      "Case #85: 812889\n",
      "\n",
      "Case #86: 747801\n",
      "\n",
      "Case #87: 1640730\n",
      "\n",
      "Case #88: 2193000\n",
      "\n",
      "Case #89: 2741276\n",
      "\n",
      "Case #90: 4744590\n",
      "\n",
      "Case #91: 9999970\n",
      "\n",
      "Case #92: 1528252\n",
      "\n",
      "Case #93: 3129210\n",
      "\n",
      "Case #94: 2851130\n",
      "\n",
      "Case #95: 4997286\n",
      "\n",
      "Case #96: 1097403\n",
      "\n",
      "Case #97: 1219887\n",
      "\n",
      "Case #98: 90\n",
      "\n",
      "Case #99: 7999984\n",
      "\n",
      "Case #100: 90\n",
      "\n"
     ]
    }
   ],
   "source": [
    "n=1\n",
    "with open(\"output.txt\",'w') as handle:\n",
    "    for x in data:\n",
    "        res=Solve(x)\n",
    "        string=\"Case #%s: %s\\n\"%(n,res)\n",
    "        n+=1\n",
    "        print string\n",
    "        handle.write(string)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4, 5, 6, 7, 8, 9]"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "range(1,10)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}