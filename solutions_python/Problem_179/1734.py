{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Populating the interactive namespace from numpy and matplotlib\n"
     ]
    }
   ],
   "source": [
    "%pylab inline"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Task 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "with open(\"input.txt\", \"r\") as fin:\n",
    "    numbers = map(int, fin.readlines())\n",
    "    numbers = numbers[1:]\n",
    "\n",
    "def steps_to_sleep(n):\n",
    "    cur_set = set()\n",
    "    for i in range(1, 10 * n + 1000):\n",
    "        k = list(str(i * n))\n",
    "        cur_set.update(k)\n",
    "        if len(cur_set) == 10:\n",
    "            return i * n\n",
    "    return 'INSOMNIA'\n",
    "\n",
    "ans = []\n",
    "for i in range(1, len(numbers) + 1):\n",
    "    ans.append('Case #%d: ' % i + str(steps_to_sleep(numbers[i-1])))\n",
    "\n",
    "with open(\"output.txt\", \"w\") as ouf:\n",
    "    ouf.write('\\n'.join(ans))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Task 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-\n",
      "Case #1: 1\n",
      "\n",
      "-+\n",
      "Case #2: 1\n",
      "\n",
      "+-\n",
      "Case #3: 2\n",
      "\n",
      "+++\n",
      "Case #4: 0\n",
      "\n",
      "--+-\n",
      "Case #5: 3\n",
      "\n",
      "+---+++--+-+----+++----++-+---+-+-++++-++-+-+++++---+++++---+--+-----++-+-++-++++-+-+-+-+++---+--+-+\n",
      "Case #6: 52\n",
      "\n",
      "--------------------------------------------------\n",
      "Case #7: 1\n",
      "\n",
      "--+\n",
      "Case #8: 1\n",
      "\n",
      "-+---++--+-----+---++--++--++-+-+++--++-+++-+--++-++++++++-++++++++++--+-+--++-+--++---+++++-++---+-\n",
      "Case #9: 47\n",
      "\n",
      "++---+++-+++---+-+-++-+----+-+++-+---\n",
      "Case #10: 20\n",
      "\n",
      "-+-+--+++++--+-+-+-+--+-+-+++--++---+-++---++---+++++----+-+++++++--++--+---+++--++-+-++++-+-++-----\n",
      "Case #11: 51\n",
      "\n",
      "-++\n",
      "Case #12: 1\n",
      "\n",
      "-++--+-++-+-++-+++-++-+++-+++-+-+--++--+----+-+-+-+---+-+++++---+----+-+++--+---+--++++-++-++--++-++\n",
      "Case #13: 57\n",
      "\n",
      "+-+-++---++-----++-++---++++++----++-+-----++--+---+------+--++--++-++\n",
      "Case #14: 30\n",
      "\n",
      "-+--++-+-+-+--+--+--++----------++--+---+-++-+-+++---++-+----+-+----+++-+--+---+----+----+------+--+\n",
      "Case #15: 51\n",
      "\n",
      "+-+++----+++++-++-+++++----+-++-++-+----+\n",
      "Case #16: 18\n",
      "\n",
      "--+-----------+-++--+-+--++--+-++-+-++-+--++++++++----+-++-+-+----+-+--+++++-++-+-+++-+++-----+-+-++\n",
      "Case #17: 51\n",
      "\n",
      "-+-++--++-++-+--+--++-+-------+++---++++++++++--+--++++++---++-++-++--+---+++-+++++-+++++-+--+++-+++\n",
      "Case #18: 43\n",
      "\n",
      "++++-----+--++++--++-----+-+++-+-++-+++++++----+++-++---+++++----+---+---++++++-++--+-+---++++------\n",
      "Case #19: 38\n",
      "\n",
      "-+++--+++++++-++-+-+------+++++-+++--++--+-++----++-++-+-+-----+---\n",
      "Case #20: 31\n",
      "\n",
      "---+--+++---+-++-++-+-+--+++--+-+-+-----++---+++--+--+----+++-++-++++-++-----++---+--+-++-+--+--+--+\n",
      "Case #21: 53\n",
      "\n",
      "---++---+------++++---+---++++-++-+--++-++-+-+-+++---+-+++-+++++-+---+++++-+--+-++-+-+----+-+-++++++\n",
      "Case #22: 49\n",
      "\n",
      "+-+----+-+++++-++++-++----+-+-+++---++--++++--+-++---++++--+-+-----+-++++---+-++--------+-+---\n",
      "Case #23: 44\n",
      "\n",
      "--+-+-----+++-+-+-+++--++---++---+-++++++-+--++-+++-+-+--+++--+-+-+-++-+---+++++++++-++++---+-++-+-+\n",
      "Case #24: 53\n",
      "\n",
      "--+++--+-+-+---+-+++----+--+++-++----+--++-++-+-+-+++++-++++-++---+-+-----++-+----+-+---+++--+---+--\n",
      "Case #25: 53\n",
      "\n",
      "+--\n",
      "Case #26: 2\n",
      "\n",
      "++-+++--++++-++--+------++++---+---+++++--+-+--++++-++-+-++--++++-+-++-+---+---+--+--+--+++++-------\n",
      "Case #27: 46\n",
      "\n",
      "--++--+++-+-----+++-+--+++-+---++-----++--+---++++----+--------+-+++++-+++++++++-+-+-++--+-+++----++\n",
      "Case #28: 41\n",
      "\n",
      "+--+---++-++----+-++-++--+++-+++-+++------+---++-----+\n",
      "Case #29: 24\n",
      "\n",
      "-+-++-+-+++-++-++--+--++-+-++-+-+-+--++--+-++++--+++---++-+--+-----++-++-++++++--+---+-+-+--+----+-+\n",
      "Case #30: 59\n",
      "\n",
      "++++--+-+++-+-+---++---+-+--++++++++\n",
      "Case #31: 16\n",
      "\n",
      "+--------------------------------------------------------------------------------------------------+\n",
      "Case #32: 2\n",
      "\n",
      "+--------+\n",
      "Case #33: 2\n",
      "\n",
      "++--+-------++--+--++--+++----------+--+-+-++-----+++++++---+-------+-+++++-+++--+-+-+----++++--++--\n",
      "Case #34: 40\n",
      "\n",
      "--+-+---++-+-+-+--+--++++--+-++-+-+-+-++++++-----+-++--+--+--++-+-----+------+++-----+++++++++++-+-+\n",
      "Case #35: 49\n",
      "\n",
      "+-++---+-+-+++++--+-----+---+++--++++-+---+-+-----+++---+-+++-+-+--++++-+-++-\n",
      "Case #36: 40\n",
      "\n",
      "++-+++--++-++--+----++-+---++--++-++--+++---+--+++-+----+-++--+-+--++---+-------++++-+-++-++++-++-+-\n",
      "Case #37: 52\n",
      "\n",
      "+-++---+-+-++-+++-+-+----+--+++-++--+--------+-+--++--+-+-+-+++--+--+++-+---++++++--+-++--+++-+---+-\n",
      "Case #38: 56\n",
      "\n",
      "+++++-+-+-++--+---+-+--+-++-+-++--++-+++-+--++++++--+---++--++--+--+-++-++--+-+--+---++-++-+++-++++-\n",
      "Case #39: 58\n",
      "\n",
      "++-+++-+---++----+++-+---++-+--+++++++--+++----+----+---+-+-+-+--+---++++----+----+-+----+-+--+++++-\n",
      "Case #40: 48\n",
      "\n",
      "-----\n",
      "Case #41: 1\n",
      "\n",
      "---+++-----+++-+++++--+-+-+----+-++--------+-+-++++---++-++++++++---++-+--+++---+-++++++-----+++++--\n",
      "Case #42: 39\n",
      "\n",
      "++++++++++++++++++++++++++++++++++++++++++++++++++\n",
      "Case #43: 0\n",
      "\n",
      "+---+----+--+-+++--+--++-+----+-+--+-++-+-+--+--++-+++----++-++--+++---+-++-++-+--+-+++--++++-+\n",
      "Case #44: 54\n",
      "\n",
      "-++--+--++++--++-+-++++--+-+--+-+-+----+-+-+---+++--++-+++-+-+-+++--------+++---------+-+-++++++++--\n",
      "Case #45: 49\n",
      "\n",
      "+++----++-+---+--+-++++-++-----++-++-++++++-+-+-+++-+-++-+----+++++++++++---++--+---+-+-+-+--++-+++-\n",
      "Case #46: 50\n",
      "\n",
      "+++--++-+------++++---+---+-+----++------+-------+--++---+++-+--+-+-+-+--+---+-+++++++-+----+-------\n",
      "Case #47: 44\n",
      "\n",
      "+++++\n",
      "Case #48: 0\n",
      "\n",
      "++-++++++-++++-++--+++------++-+--++-+-+++-++------+-\n",
      "Case #49: 24\n",
      "\n",
      "-+-+++-+-+++-+-++++++-+-+-+-+--+--++--+-++--++----++--+++-++--+--++--+++--++-++--+-----+----+-++----\n",
      "Case #50: 55\n",
      "\n",
      "--\n",
      "Case #51: 1\n",
      "\n",
      "-++---++++-++++-+++-++-+----+++-+++-+-+----+---+---+++---+------+-+------+-++++++--+-+-++--+-+-+++-+\n",
      "Case #52: 49\n",
      "\n",
      "+--++-+++-+----+-+--+++---++-+-----+++++--+++-+-+-++-------++---+-+----+-+--++-++-+++++--++-++++-+-+\n",
      "Case #53: 50\n",
      "\n",
      "--+-+++-+-++-+++----+-++-++-+----++--+--+-+---++-+--+++++--+-+++++-+++++-+-++--+--++--++--+++++---++\n",
      "Case #54: 51\n",
      "\n",
      "+-+-+--++-+--+--++---+--+--++++++-++-+--+-++++++---+++--++-+---+--+---+-++-++-----++--++---+-+++-+-+\n",
      "Case #55: 54\n",
      "\n",
      "----+-------++++-+--++++++-+--\n",
      "Case #56: 11\n",
      "\n",
      "++-++-+--+++-++-+++-+-++++---------+------++-+-+++--++-++-++-+++++-+++++-+-++-+--+---++----+++-+-+++\n",
      "Case #57: 48\n",
      "\n",
      "---+---+-+-+-++++--+++--++------+--++-+\n",
      "Case #58: 19\n",
      "\n",
      "-+-+-+++-++-------++-+--++----++--+-+++--------+-++++++----+-+-+-+-+--+++++++-+----++++++++-+-+-++-+\n",
      "Case #59: 47\n",
      "\n",
      "--+----++-+-+-+-+-+++---+++----+--+-++-++--+--+-+-+---+++--+++---+++---+++----+---+--++--+-++++++-+-\n",
      "Case #60: 53\n",
      "\n",
      "--++------++-++-+---++++---+-+++-----++++---+--+++++-+-+-++-+-+++-++-+++-+----+---+-+-+---+--++++-++\n",
      "Case #61: 49\n",
      "\n",
      "-+-+++++++-++--+---++-++--+-++++-+---+----+----+-++---+----++++-++-+--++--+++++--++++-------++--+++-\n",
      "Case #62: 45\n",
      "\n",
      "+-++---+-++-+-+---++++-+++++-+++--+++-++-++------++----++------+-++---++-+--+++++++++-+--+-+--++----\n",
      "Case #63: 46\n",
      "\n",
      "+---+--+-++----+++\n",
      "Case #64: 8\n",
      "\n",
      "---\n",
      "Case #65: 1\n",
      "\n",
      "-++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-\n",
      "Case #66: 3\n",
      "\n",
      "++---+--+------+++-----+-+++--+++++--++-++-----+++++++--++-+--+--+++---+--+-+++----++--+-++--++-+-+-\n",
      "Case #67: 46\n",
      "\n",
      "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n",
      "Case #68: 100\n",
      "\n",
      "++-+-++-+-+---+-+++--+-+---+++----+-++++++++++-++++---++\n",
      "Case #69: 26\n",
      "\n",
      "+-+++----+-+++---\n",
      "Case #70: 8\n",
      "\n",
      "+-----+-++--+--++++++--++-++-+++++-++-+---+----------++-----+++-+-+-+---+-+-+--+---++-+--\n",
      "Case #71: 44\n",
      "\n",
      "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n",
      "Case #72: 99\n",
      "\n",
      "++-++----+-+----+-+--+-++--+-----+-++++--+--++-----+---+++-+-+-++++++-+-+-++++++++-++---++--++--++--\n",
      "Case #73: 50\n",
      "\n",
      "+-+\n",
      "Case #74: 2\n",
      "\n",
      "---+-+------+-----+--+-+----+-----++--+++-+-+++-+-+-++-+++--++-+---+-----++-++-++++++-++++++-+-+-+-+\n",
      "Case #75: 51\n",
      "\n",
      "+-+-+-+-+-\n",
      "Case #76: 10\n",
      "\n",
      "-++------++---+---++-+-++-++--+-++-+---+++++++--++-+--+--+++--+----+--+++---++-+++++++-+-+-+--++----\n",
      "Case #77: 49\n",
      "\n",
      "++++--++-+--++---+-++--+---++-+-++++-++++--+-++--+++--+-+++--+-+--++-++--+----+--++-+-+++--+++++-+-+\n",
      "Case #78: 54\n",
      "\n",
      "-+--++-+---+++----++-+------+-+----+---+-+++-+++++-+-+-+-+++---+--++--+--++-+-++-++---++-+++---+-+--\n",
      "Case #79: 55\n",
      "\n",
      "-++++++++-\n",
      "Case #80: 3\n",
      "\n",
      "++-+++-++-+---+--+-+++++-+-++++++++--+--+-+--++-+---+++--+++--++-+++-+-+-+-+-+-++-\n",
      "Case #81: 48\n",
      "\n",
      "--++++++-----+-----+++------+--+++--+---++------+--+++-++-++++++--+++++-++-+-+-++++-+++-+-----+++++-\n",
      "Case #82: 39\n",
      "\n",
      "---+++++-+---+-+-+++++---+---+--+---\n",
      "Case #83: 17\n",
      "\n",
      "-+--+-\n",
      "Case #84: 5\n",
      "\n",
      "++\n",
      "Case #85: 0\n",
      "\n",
      "+-++++--+++--+--++---++--+-----++-+-+-+----+-++--+-++--++--+--++--++++-+++---+---+--+-+--+++--++-+--\n",
      "Case #86: 54\n",
      "\n",
      "+---+--+-++--++--+++--+----+---+-+++-+++-+---+--+++-+-+++++-++++-++--+++++-+++++--+--+-+++-+----+-+-\n",
      "Case #87: 52\n",
      "\n",
      "++-\n",
      "Case #88: 2\n",
      "\n",
      "-+-+-+-+-+\n",
      "Case #89: 9\n",
      "\n",
      "--+++++-++-+-+-+-+-+-+++++-++++------+--+-+--+++-+++--++++---+++-+--+--+-++--+------+--+--+-+-+--+--\n",
      "Case #90: 55\n",
      "\n",
      "-++++--++++--+-+-+-+-------+++----++-+-+---+-------+-----++---+-+++-+-+--+-+++++--++-+-+-+---++-+++-\n",
      "Case #91: 51\n",
      "\n",
      "+++-+-+-+--+-+++---++-++++-+-+-+++++---++-+++-+---++-++-+++-------+-++--+-+---+--+-+--+++--+--+-++--\n",
      "Case #92: 56\n",
      "\n",
      "+---+--+++--+++-+++++--++-+-+-++-+-++++-+++-++----+-++--+-+-----+-+++--+--+-++++--+--+++++++-------+\n",
      "Case #93: 48\n",
      "\n",
      "-+++--+-----++-++-+++++---+--+-++-+-++++---+-----++++++--+-+---+++--++-++--+-+-++--+--++-----+----+-\n",
      "Case #94: 49\n",
      "\n",
      "-+-\n",
      "Case #95: 3\n",
      "\n",
      "-----+-+-+-++++--+-+---++--++++++-++++-++++++++--++--+-+---++---+---++-+++-++-+----+----+--++---+---\n",
      "Case #96: 47\n",
      "\n",
      "+++----+--+--+---+++--+-++++++-++-----++-+++--+---+-+++-++--+++----------++++++-+---++--+-+-++--+++-\n",
      "Case #97: 44\n",
      "\n",
      "+-+-+----+-+---+-++++---+-+-++-+-+-+---++--+-+++-+++----+-+--++-+-++-++-++-++-+--\n",
      "Case #98: 52\n",
      "\n",
      "+\n",
      "Case #99: 0\n",
      "\n",
      "--++----+--+-++-+++-++-+-+-++-+-++-+--+-+++---+++--++++-++--+--++-++++-++--+++++-+--+-++---+++-+--+-\n",
      "Case #100: 57\n",
      "\n"
     ]
    }
   ],
   "source": [
    "with open(\"input.txt\", \"r\") as fin:\n",
    "    inputs = map(lambda s: s.strip(), fin.readlines())\n",
    "    inputs = inputs[1:]\n",
    "\n",
    "    \n",
    "def solve2(s):\n",
    "    cnt = 1;\n",
    "    for i in range(len(s) - 1):\n",
    "        if s[i] != s[i+1]:\n",
    "            cnt += 1\n",
    "    if s[-1] == '+':\n",
    "        cnt -= 1\n",
    "    return cnt\n",
    "    \n",
    "ans = map(solve2, inputs)\n",
    "    \n",
    "with open(\"output.txt\", \"w\") as ouf:\n",
    "    for i in range(len(ans)):\n",
    "        line = 'Case #%d: %s\\n' % (i + 1, str(ans[i]))\n",
    "        print inputs[i]\n",
    "        print line\n",
    "        ouf.write(line)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Task 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "from itertools import count, islice\n",
    "\n",
    "def isPrime(n):\n",
    "    if n < 2: return False\n",
    "    for number in range(2, int(sqrt(n)+1)):\n",
    "        if not n % number:\n",
    "            return False\n",
    "    return True\n",
    "\n",
    "prime_numbers = filter(isPrime, range(100000))\n",
    "\n",
    "def findPrimeDivisor(x):\n",
    "    for d in prime_numbers:\n",
    "        if d < x and x % d == 0:\n",
    "            return d\n",
    "    return 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 1100010001101001\n",
      "2 1100011010011111\n",
      "3 1110000101110101\n",
      "4 1100011110101001\n",
      "5 1001010101010001\n",
      "6 1101000010000011\n",
      "7 1000110101101111\n",
      "8 1011010111000011\n",
      "9 1010111011010011\n",
      "10 1110000000111111\n",
      "11 1011010001000111\n",
      "12 1110001001000111\n",
      "13 1011000111000011\n",
      "14 1100001110101111\n",
      "15 1110110001110011\n",
      "16 1011111011000111\n",
      "17 1100101111111001\n",
      "18 1100011101111001\n",
      "19 1100000110000101\n",
      "20 1100110011001001\n",
      "21 1101111100010001\n",
      "22 1110100000011111\n",
      "23 1100010100101011\n",
      "24 1010110110110011\n",
      "25 1100110110111001\n",
      "26 1101001011110111\n",
      "27 1111111011111101\n",
      "28 1110000010001101\n",
      "29 1010011000100011\n",
      "30 1001110100001001\n",
      "31 1000100100100101\n",
      "32 1000111100100111\n",
      "33 1001000011110011\n",
      "34 1101111000000011\n",
      "35 1000001001000001\n",
      "36 1110100101100001\n",
      "37 1011100000001101\n",
      "38 1000101101011111\n",
      "39 1111010111111111\n",
      "40 1110110111001001\n",
      "41 1010101110000111\n",
      "42 1011111111011111\n",
      "43 1110011010011101\n",
      "44 1010111111111111\n",
      "45 1100100001111101\n",
      "46 1101111111011111\n",
      "47 1010011110100011\n",
      "48 1010100101010101\n",
      "49 1000100110010111\n",
      "50 1010111101000111\n"
     ]
    }
   ],
   "source": [
    "def solve3(N, J):\n",
    "    ans = set()\n",
    "    with open(\"output.txt\", \"w\") as ouf:\n",
    "        ouf.write('Case #1:\\n')\n",
    "        while len(ans) < J:\n",
    "            cur_x = [1] + list(np.random.randint(0,2, N-2)) + [1]\n",
    "            cur_x = ''.join(map(str, cur_x))\n",
    "            is_prime = False\n",
    "            for d in range(2, 11):\n",
    "                xd = int(cur_x, d)\n",
    "                if findPrimeDivisor(xd) == 0:\n",
    "                    is_prime = True\n",
    "                    break\n",
    "            if not is_prime and not cur_x in ans:\n",
    "                print len(ans) + 1, cur_x\n",
    "                sys.stdout.flush()\n",
    "                ouf.write(cur_x)\n",
    "                for d in range(2, 11):\n",
    "                    xd = int(cur_x, d)\n",
    "                    ouf.write(' %d' % findPrimeDivisor(xd))\n",
    "                ouf.write('\\n')\n",
    "                ans.add(cur_x)\n",
    "    return ans\n",
    " \n",
    "    \n",
    "#ans = solve3(32, 500)\n",
    "ans = solve3(32, 500)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "2\n",
      "5\n",
      "2\n",
      "7\n",
      "2\n",
      "3\n",
      "2\n",
      "7\n"
     ]
    }
   ],
   "source": [
    "cur_x = '1001'\n",
    "for d in range(2, 11):\n",
    "    xd = int(cur_x, d)\n",
    "    print findPrimeDivisor(xd)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "28"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "int('1001', 3) % 367"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4113"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "int('1000101', 4)"
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
   "version": "2.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
