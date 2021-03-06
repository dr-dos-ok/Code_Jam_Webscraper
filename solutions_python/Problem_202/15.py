{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": true,
    "editable": true
   },
   "source": [
    "# Google Code Jam 2017 — Qualification Round — problem D\n",
    "## User: jdemeyer\n",
    "\n",
    "This is a Jupyter notebook to be run with SageMath version 8.0.beta1 on a 64-bit GNU/Linux system. Although the precise version of SageMath probably does not matter that much."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [],
   "source": [
    "%%cython\n",
    "\n",
    "import os, sys, datetime, time, collections\n",
    "from copy import copy\n",
    "from sage.rings.integer cimport Integer\n",
    "\n",
    "\n",
    "def log(msg):\n",
    "    sys.stderr.write(msg + \"\\n\")\n",
    "    sys.stderr.flush()\n",
    "\n",
    "\n",
    "class CodejamProblem(object):\n",
    "    def __init__(self, input):\n",
    "        self.inputlines = iter(input.splitlines())\n",
    "        self.cases = []\n",
    "    \n",
    "    def readline(self):\n",
    "        return next(self.inputlines)\n",
    "        \n",
    "    def readint(self):\n",
    "        return Integer(self.readline())\n",
    "\n",
    "    def readints(self):\n",
    "        return [Integer(x) for x in self.readline().split()]\n",
    "        \n",
    "    def solve(self, f=sys.stdout, raw=False):\n",
    "        for i, case in enumerate(self.cases, 1):\n",
    "            sig_check()\n",
    "            ans = self.solvecase(case)\n",
    "            if raw:\n",
    "                ans = repr(ans)\n",
    "            else:\n",
    "                ans = self.formatanswer(ans)\n",
    "            f.write(\"Case #{0}: {1}\\n\".format(i, ans.strip()))\n",
    "        f.flush()\n",
    "        \n",
    "    def solvecheck(self, output):\n",
    "        from StringIO import StringIO\n",
    "        out = StringIO()\n",
    "        self.solve(out)\n",
    "        assert out.getvalue() == output\n",
    "            \n",
    "    def formatanswer(self, ans):\n",
    "        if isinstance(ans, (tuple, list)):\n",
    "            return \" \".join(str(x) for x in ans)\n",
    "        else:\n",
    "            return str(ans)\n",
    "\n",
    "    @classmethod\n",
    "    def precompute(cls):\n",
    "        pass\n",
    "    \n",
    "    @classmethod\n",
    "    def autosolve(cls, filein, fileout, *args, **kwds):\n",
    "        log(\"precomputing...\")\n",
    "        cls.precompute()\n",
    "\n",
    "        log(\"autosolving...\")\n",
    "\n",
    "        nexc = 0\n",
    "        while nexc < 10:\n",
    "            sig_check()\n",
    "            t0 = datetime.datetime.now()\n",
    "            try:\n",
    "                input = open(filein).read()\n",
    "            except IOError:\n",
    "                time.sleep(0.2)\n",
    "                continue\n",
    "            d = datetime.datetime.now() - t0\n",
    "            log(\"Read input in %.2fs\" % d.total_seconds())\n",
    "            \n",
    "            t0 = datetime.datetime.now()\n",
    "            try:\n",
    "                problem = cls(input, *args, **kwds)\n",
    "            except Exception:\n",
    "                from traceback import print_exc\n",
    "                print_exc(file=sys.stderr)\n",
    "                nexc += 1\n",
    "                time.sleep(0.5)\n",
    "                continue\n",
    "            d = datetime.datetime.now() - t0\n",
    "            ncases = len(problem.cases)\n",
    "            log(\"Parsed input in %.2fs, got %s cases\" % (d.total_seconds(), ncases))\n",
    "            \n",
    "            t0 = datetime.datetime.now()\n",
    "            with open(fileout, 'w') as out:\n",
    "                problem.solve(out)\n",
    "            d = datetime.datetime.now() - t0\n",
    "            log(\"Solved problem in %.2fs\" % d.total_seconds())\n",
    "\n",
    "            problem.notify()\n",
    "            return\n",
    "        \n",
    "    @staticmethod\n",
    "    def notify():\n",
    "        os.system(\"mplayer /usr/share/apps/kgoldrunner/themes/default/victory.ogg >/dev/null\")\n",
    "\n",
    "        \n",
    "from sage.all import Matrix, ZZ\n",
    "\n",
    "class Problem(CodejamProblem):\n",
    "    def __init__(self, input):\n",
    "        CodejamProblem.__init__(self, input)\n",
    "        \n",
    "        T = self.readint()\n",
    "        for i in range(T):\n",
    "            N, M = self.readints()\n",
    "            case = [[\".\" for _ in range(N)] for _ in range(N)]\n",
    "            for k in range(M):\n",
    "                model, R, C = self.readline().split()\n",
    "                case[int(R)-1][int(C)-1] = model\n",
    "            self.cases.append(case)\n",
    "\n",
    "    def solvecase(self, case):\n",
    "        n = len(case)\n",
    "        \n",
    "        orthomat = self.solve_ortho(case)\n",
    "        diagmat = self.solve_diag(case, 0)\n",
    "        diagmat += self.solve_diag(case, 1)\n",
    "        \n",
    "        points = 0\n",
    "        changes = []\n",
    "        for i in range(n):\n",
    "            for j in range(n):\n",
    "                if orthomat[i,j]:\n",
    "                    if diagmat[i,j]:\n",
    "                        c = \"o\"\n",
    "                        points += 2\n",
    "                    else:\n",
    "                        c = \"x\"\n",
    "                        points += 1\n",
    "                else:\n",
    "                    if diagmat[i,j]:\n",
    "                        c = \"+\"\n",
    "                        points += 1\n",
    "                    else:\n",
    "                        c = \".\"\n",
    "                        points += 0\n",
    "                if c != case[i][j]:\n",
    "                    changes.append((c,i+1,j+1))\n",
    "        return points, changes\n",
    "\n",
    "    def formatanswer(self, ans):\n",
    "        points, changes = ans\n",
    "        ret = \"%i %i\\n\" % (points, len(changes))\n",
    "        for ch in changes:\n",
    "            ret += \"%s %i %i\\n\" % ch\n",
    "        return ret\n",
    "        \n",
    "    def solve_ortho(self, case):\n",
    "        n = len(case)\n",
    "        M = Matrix(ZZ, n, n)\n",
    "        freerows = set(range(n))\n",
    "        freecols = set(range(n))\n",
    "        \n",
    "        for i in range(n):\n",
    "            for j in range(n):\n",
    "                if case[i][j] in \"xo\":\n",
    "                    M[i,j] = 1\n",
    "                    freerows.remove(i)\n",
    "                    freecols.remove(j)\n",
    "                    \n",
    "        freerows = sorted(freerows)\n",
    "        freecols = sorted(freecols)\n",
    "                    \n",
    "        while freerows:\n",
    "            i = freerows.pop()\n",
    "            j = freecols.pop()\n",
    "            M[i,j] = 1\n",
    "            \n",
    "        return M\n",
    "    \n",
    "    def solve_diag(self, case, parity):\n",
    "        n = len(case)\n",
    "        M = Matrix(ZZ, n, n)\n",
    "        freeplus = set(k for k in range(2*n-1) if k%2 == parity)\n",
    "        freemin = set(k for k in range(n) if k%2 == parity)\n",
    "        freemin |= set(-k for k in range(n) if k%2 == parity)\n",
    "        \n",
    "        for i in range(n):\n",
    "            for j in range(n):\n",
    "                if (i+j) % 2 == parity and case[i][j] in \"+o\":\n",
    "                    M[i,j] = 1\n",
    "                    freeplus.remove(i+j)\n",
    "                    freemin.remove(i-j)\n",
    "                    \n",
    "        freeplus = sorted(freeplus, key=lambda x: abs(x-(n-1)))\n",
    "        freemin = sorted(freemin, key=lambda x: abs(x))\n",
    "\n",
    "        while freeplus:\n",
    "            p = freeplus.pop()\n",
    "            minbound = min(p, 2*(n-1)-p)\n",
    "            i = len(freemin) - 1\n",
    "            while i >= 0 and not abs(freemin[i]) <= minbound:\n",
    "                i -= 1\n",
    "            if i < 0:\n",
    "                continue\n",
    "            m = freemin.pop(i)\n",
    "            i = (p + m) // 2\n",
    "            j = (p - m) // 2\n",
    "            M[i,j] = 1\n",
    "            \n",
    "        return M"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {
    "collapsed": true,
    "deletable": true,
    "editable": true
   },
   "outputs": [],
   "source": [
    "input=\"\"\"\n",
    "3\n",
    "2 0\n",
    "1 1\n",
    "o 1 1\n",
    "3 4\n",
    "+ 2 3\n",
    "+ 2 1\n",
    "x 3 1\n",
    "+ 2 2\n",
    "\"\"\"\n",
    "\n",
    "output=\"\"\"\n",
    "Case #1: 4 3\n",
    "o 2 2\n",
    "+ 2 1\n",
    "x 1 1\n",
    "Case #2: 2 0\n",
    "Case #3: 6 2\n",
    "o 2 3\n",
    "x 1 2\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [],
   "source": [
    "input = \"\".join(line+\"\\n\" for line in input.splitlines() if line)\n",
    "output = \"\".join(line+\"\\n\" for line in output.splitlines() if line)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [],
   "source": [
    "P = Problem(input)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Case #1: (4, [('x', 1, 1), ('+', 1, 2), ('o', 2, 2)])\n",
      "Case #2: (2, [])\n",
      "Case #3: (6, [('x', 1, 2), ('o', 2, 3)])\n",
      "Case #1: 4 3\n",
      "x 1 1\n",
      "+ 1 2\n",
      "o 2 2\n",
      "Case #2: 2 0\n",
      "Case #3: 6 2\n",
      "x 1 2\n",
      "o 2 3\n"
     ]
    }
   ],
   "source": [
    "P.solve(raw=True)\n",
    "P.solve()\n",
    "#P.solvecheck(output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "precomputing...\n",
      "autosolving...\n"
     ]
    }
   ],
   "source": [
    "P.autosolve(\"in/D-small-attempt0.in\", \"out\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "SageMath 8.0.beta1",
   "language": "",
   "name": "sagemath"
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
   "version": "2.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
