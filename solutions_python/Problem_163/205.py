{
 "metadata": {
  "name": "",
  "signature": "sha256:f2fc9016e060efd5553d077f4b408c90ac1a18ba38da30acfb1a6b2a24d63c5b"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "import numpy as np\n",
      "import itertools"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 3
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "def case():\n",
      "    global f\n",
      "\n",
      "    line = (f.readline()).split()\n",
      "    R = int(line[0])\n",
      "    C = int(line[1])\n",
      "    N = int(line[2])\n",
      "    \n",
      "    indices = list(range(R*C))\n",
      "    arr = [0]*(R*C)\n",
      "    combs = itertools.combinations(indices, N)\n",
      "\n",
      "    min_ = R*C*4\n",
      "    for l in combs:\n",
      "        arr = [0]*(R*C)\n",
      "        for i in l:\n",
      "            arr[i] = 1\n",
      "        arr = np.reshape(np.array(arr), (R, C))\n",
      "\n",
      "        count = 0\n",
      "        print(\"arr\", arr.shape)\n",
      "        for i in range(arr.shape[0]):\n",
      "            for j in range(arr.shape[1]-1):\n",
      "                if (arr[i, j] == 1 and arr[i, j+1] == 1):\n",
      "                    count += 1\n",
      "        print(count)\n",
      "        for j in range(arr.shape[1]):\n",
      "            for i in range(arr.shape[0]-1):\n",
      "                if (arr[i, j] == 1 and arr[i+1, j] == 1):\n",
      "                    count += 1\n",
      "        print(count)\n",
      "        min_ = count if count < min_ else min_\n",
      "    \n",
      "    return min_"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 39
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "task = \"T2\"\n",
      "f = open('input'+task+'.txt', 'r')\n",
      "n_tests = int(f.readline())\n",
      "result = []\n",
      "for i in range(n_tests):\n",
      "    res = case()\n",
      "    result.append(\"Case #\"+str(i+1)+\": \"+str(res))\n",
      "f.close()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "arr (2, 3)\n",
        "4\n",
        "7\n",
        "7\n",
        "arr (4, 1)\n",
        "0\n",
        "1\n",
        "1\n",
        "arr (4, 1)\n",
        "0\n",
        "0\n",
        "0\n",
        "arr (4, 1)\n",
        "0\n",
        "0\n",
        "0\n",
        "arr (4, 1)\n",
        "0\n",
        "1\n",
        "0\n",
        "arr (4, 1)\n",
        "0\n",
        "0\n",
        "0\n",
        "arr (4, 1)\n",
        "0\n",
        "1\n",
        "0\n",
        "arr (3, 3)\n",
        "5\n",
        "10\n",
        "10\n",
        "arr (3, 3)\n",
        "4\n",
        "9\n",
        "9\n",
        "arr (3, 3)\n",
        "5\n",
        "10\n",
        "9\n",
        "arr (3, 3)\n",
        "5\n",
        "9\n",
        "9\n",
        "arr (3, 3)\n",
        "4\n",
        "8\n",
        "8\n",
        "arr (3, 3)\n",
        "5\n",
        "9\n",
        "8\n",
        "arr (3, 3)\n",
        "5\n",
        "10\n",
        "8\n",
        "arr (3, 3)\n",
        "4\n",
        "9\n",
        "8\n",
        "arr (3, 3)\n",
        "5\n",
        "10\n",
        "8\n",
        "arr (5, 2)\n",
        "0\n",
        "0\n",
        "0\n"
       ]
      }
     ],
     "prompt_number": 40
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "result"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 34,
       "text": [
        "['Case #1: 8', 'Case #2: 1', 'Case #3: 9', 'Case #4: 1']"
       ]
      }
     ],
     "prompt_number": 34
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "# write to file\n",
      "fout = open('output'+task+'.txt', 'w')\n",
      "for line in result:\n",
      "    print(line)\n",
      "    fout.write(line+'\\n')\n",
      "fout.close()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "Case #1: 1\n",
        "Case #2: 3\n",
        "Case #3: 2\n",
        "Case #4: 5\n",
        "Case #5: 2\n",
        "Case #6: 5\n",
        "Case #7: 1\n",
        "Case #8: 4\n",
        "Case #9: 3\n",
        "Case #10: 3\n",
        "Case #11: 2\n",
        "Case #12: 1\n",
        "Case #13: 5\n",
        "Case #14: 2\n",
        "Case #15: 2\n",
        "Case #16: 2\n",
        "Case #17: 2\n",
        "Case #18: 4\n",
        "Case #19: 4\n",
        "Case #20: 5\n",
        "Case #21: 5\n",
        "Case #22: 4\n",
        "Case #23: 2\n",
        "Case #24: 3\n",
        "Case #25: 4\n",
        "Case #26: 2\n",
        "Case #27: 5\n",
        "Case #28: 1\n",
        "Case #29: 4\n",
        "Case #30: 5\n",
        "Case #31: 1\n",
        "Case #32: 5\n",
        "Case #33: 1\n",
        "Case #34: 2\n",
        "Case #35: 5\n",
        "Case #36: 1\n",
        "Case #37: 1\n",
        "Case #38: 1\n",
        "Case #39: 5\n",
        "Case #40: 4\n",
        "Case #41: 5\n",
        "Case #42: 2\n",
        "Case #43: 1\n",
        "Case #44: 1\n",
        "Case #45: 1\n",
        "Case #46: 3\n",
        "Case #47: 2\n",
        "Case #48: 1\n",
        "Case #49: 1\n",
        "Case #50: 1\n",
        "Case #51: 5\n",
        "Case #52: 1\n",
        "Case #53: 1\n",
        "Case #54: 1\n",
        "Case #55: 4\n",
        "Case #56: 2\n",
        "Case #57: 1\n",
        "Case #58: 3\n",
        "Case #59: 5\n",
        "Case #60: 3\n",
        "Case #61: 5\n",
        "Case #62: 5\n",
        "Case #63: 4\n",
        "Case #64: 2\n",
        "Case #65: 3\n",
        "Case #66: 4\n",
        "Case #67: 1\n",
        "Case #68: 2\n",
        "Case #69: 2\n",
        "Case #70: 4\n",
        "Case #71: 2\n",
        "Case #72: 3\n",
        "Case #73: 5\n",
        "Case #74: 5\n",
        "Case #75: 5\n",
        "Case #76: 3\n",
        "Case #77: 1\n",
        "Case #78: 5\n",
        "Case #79: 1\n",
        "Case #80: 2\n",
        "Case #81: 5\n",
        "Case #82: 5\n",
        "Case #83: 2\n",
        "Case #84: 3\n",
        "Case #85: 3\n",
        "Case #86: 2\n",
        "Case #87: 4\n",
        "Case #88: 5\n",
        "Case #89: 4\n",
        "Case #90: 2\n",
        "Case #91: 4\n",
        "Case #92: 1\n",
        "Case #93: 5\n",
        "Case #94: 1\n",
        "Case #95: 4\n",
        "Case #96: 5\n",
        "Case #97: 2\n",
        "Case #98: 2\n",
        "Case #99: 2\n",
        "Case #100: 3\n"
       ]
      }
     ],
     "prompt_number": 173
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "print( list(itertools.permutations([1,2,3])))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]\n"
       ]
      }
     ],
     "prompt_number": 4
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "R = 2\n",
      "C = 3\n",
      "N = 4\n",
      "\n",
      "indices = list(range(R*C))\n",
      "arr = [0]*(R*C)\n",
      "combs = itertools.combinations(indices, N)\n",
      "\n",
      "min_ = R*C*4\n",
      "for l in combs:\n",
      "    arr = [0]*(R*C)\n",
      "    for i in l:\n",
      "        arr[i] = 1\n",
      "    arr = np.reshape(np.array(arr), (C, R))\n",
      "    \n",
      "    count = 0\n",
      "    for i in range(arr.shape[0]):\n",
      "        for j in range(arr.shape[1]-1):\n",
      "            if (arr[i, j] == 1 and arr[i, j+1] == 1):\n",
      "                count += 1\n",
      "    for j in range(arr.shape[1]):\n",
      "        for i in range(arr.shape[0]-1):\n",
      "            if (arr[i, j] == 1 and arr[i+1, j] == 1):\n",
      "                count += 1\n",
      "    min_ = count if count < min_ else min_\n",
      "min_"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 17,
       "text": [
        "2"
       ]
      }
     ],
     "prompt_number": 17
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [],
     "language": "python",
     "metadata": {},
     "outputs": []
    }
   ],
   "metadata": {}
  }
 ]
}