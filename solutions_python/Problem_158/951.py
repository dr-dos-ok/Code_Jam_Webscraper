fname = 'D-small-attempt1'
inf = open('%s.in' % fname, 'r')
outf = open('%s.out' % fname, 'w')
getl = lambda: inf.readline().strip()
puts = lambda t, s: outf.write('Case #%s: %s\n' % (t, s))
precal = {
	(1, 1, 1): 0,
	(1, 1, 2): 0,
	(1, 1, 3): 0,
	(1, 1, 4): 0,
	(1, 2, 1): 0,
	(1, 2, 2): 0,
	(1, 2, 3): 0,
	(1, 2, 4): 0,
	(1, 3, 1): 0,
	(1, 3, 2): 0,
	(1, 3, 3): 0,
	(1, 3, 4): 0,
	(1, 4, 1): 0,
	(1, 4, 2): 0,
	(1, 4, 3): 0,
	(1, 4, 4): 0,
	(2, 1, 1): 1,
	(2, 1, 2): 0,
	(2, 1, 3): 1,
	(2, 1, 4): 0,
	(2, 2, 1): 0,
	(2, 2, 2): 0,
	(2, 2, 3): 0,
	(2, 2, 4): 0,
	(2, 3, 1): 1,
	(2, 3, 2): 0,
	(2, 3, 3): 1,
	(2, 3, 4): 0,
	(2, 4, 1): 0,
	(2, 4, 2): 0,
	(2, 4, 3): 0,
	(2, 4, 4): 0,
	(3, 1, 1): 1,
	(3, 1, 2): 1,
	(3, 1, 3): 1,
	(3, 1, 4): 1,
	(3, 2, 1): 1,
	(3, 2, 2): 1,
	(3, 2, 3): 0,
	(3, 2, 4): 1,
	(3, 3, 1): 1,
	(3, 3, 2): 0,
	(3, 3, 3): 0,
	(3, 3, 4): 0,
	(3, 4, 1): 1,
	(3, 4, 2): 1,
	(3, 4, 3): 0,
	(3, 4, 4): 1,
	(4, 1, 1): 1,
	(4, 1, 2): 1,
	(4, 1, 3): 1,
	(4, 1, 4): 1,
	(4, 2, 1): 1,
	(4, 2, 2): 1,
	(4, 2, 3): 1,
	(4, 2, 4): 1,
	(4, 3, 1): 1,
	(4, 3, 2): 1,
	(4, 3, 3): 1,
	(4, 3, 4): 0,
	(4, 4, 1): 1,
	(4, 4, 2): 1,
	(4, 4, 3): 0,
	(4, 4, 4): 0
}
players = ['GABRIEL', 'RICHARD']
for t in xrange(1, int(getl()) + 1):
	x, r, c = map(int, getl().split())
	if x <= 4 and r <= 4 and c <= 4:
		puts(t, players[precal[(x, r, c)]])
