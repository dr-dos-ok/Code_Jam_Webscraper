#!/usr/bin/env python
"""
Problem B. Dancing With the Googlers
Qualification Round 2012, Google Code Jam

14 April 2012

"""
import logging
import sys


def setup_parser():
    from optparse import OptionParser
    usage = 'usage: %prog [options] <input file>'
    parser = OptionParser(usage=usage)
    parser.add_option('-v', '--verbose', dest='verbose', action='count',
                      help='increase verbosity')
    return parser


def setup_logging(options):
    log_level = logging.WARNING
    if options.verbose == 1:
        log_level = logging.INFO
    elif options.verbose >= 2:
        log_level = logging.DEBUG
    logging.basicConfig(level=log_level)


def compute(line):
    maxnum = 0;
    scores = [int(s) for s in line.split()]
    n = scores.pop(0)  # the number of Googlers
    s = scores.pop(0)  # the number of surprising triplets of scores
    p = scores.pop(0)  #

    for score in scores:
        if score >= max(3 * p - 2, 0):
            maxnum += 1
        elif score >= max(3 * p - 4, 1) and s > 0:
            maxnum += 1
            s -= 1

    return maxnum

def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser = setup_parser()
    options, args = parser.parse_args()
    setup_logging(options)

    if len(args) < 1:
        parser.print_help()
        return 2

    try:
        with open(args[0], 'r') as f:
            lines = [line.strip() for line in f.readlines()]
    except IOError, err:
        print >>sys.stderr, err
        return 1

    t = int(lines.pop(0))
    for i in range(t):
        print 'Case #%d: %s' % (i + 1, compute(lines[i]))

    return 0


if __name__ == '__main__':
    sys.exit(main())
