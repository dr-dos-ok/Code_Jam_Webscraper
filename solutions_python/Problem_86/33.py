#!/usr/bin/python2

"""
  Google Code Jam 2011
  Philfifi  --  http://www.pluc.fr
  All rigths reserved
"""

from math import sqrt
from decimal import *
getcontext().prec = 100

#import psyco
#psyco.full()

_debug = 0



def solve_case(case_no, L, H, f_others_l    ):
    print "-------------- New case", case_no

    print "L", L, "H", H,
    print f_others_l


    for f in range(L, H+1):
        all_other_ok = True
        for o in f_others_l:
            M = max(o, f)
            m = min(o, f)

            _, remainder = divmod(M,m)
            if remainder:
                all_other_ok = False
                break

        if all_other_ok:
            return f


    return "NO"


def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        N, L, H = [int(item) for item in fd.readline().split()]
        f_others_l = [int(item) for item in fd.readline().split()]


        # Have read all stuff for this case:
        f_out.write( "Case #%d: %s\n" % (case_no,
                                         solve_case(case_no, L, H, f_others_l)
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
