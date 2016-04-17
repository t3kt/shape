# starify ...
#   for 5 pointed ring, stepping by 2
#   0	2	4	6%5	8%5
#   0	2	4	1	3
#
#   for 6 pointed ring, stepping by 2
#   0	2	4	6%6
#   0	2	4	0**
#   and then offset by 1:
#   1	3	5	7%6
#   1	3	5	1**
#
#   for 7 pointed ring, stepping by 2:
#   0%7	2%7	4%7	6&7	8%7	10%7	12%7	14%7
#   0	2	4	6	1	3		5		0**
#
#   for 7 pointed ring, stepping by 3:
#   0%7	3%7	6%7	9&7	12%7	15%7	18%7	21%7
#   0	3	6	2	5		1		4		0**
#
#

def _CopyPoints(inprim, outprim, sourcepoints):
	count = len(outprim) - 1
	sourcepoints = list(sourcepoints)
	print('_CopyPoints count: %r, len(inprim): %r, sourcepoints: %r' % (count, len(inprim), sourcepoints))
	for to, src in enumerate(sourcepoints):
		if to != count:
			src %= count
			to %= count
		print('trying to map to point', to, 'from point', src, '... count: ', count)
		outprim[to].point.P = inprim[src].point.P

def StarifyFivePointBy2(inprim, outsop):
	count = 5
	outprim = outsop.appendPoly(count + 1, closed=False, addPoints=True)
	_CopyPoints(
		inprim,
		outprim,
		[0, 2, 4, 6, 8, 5])

def StarifySevenPointBy2(inprim, outsop):
	count = 7
	outprim = outsop.appendPoly(count + 1, closed=False, addPoints=True)
	_CopyPoints(
		inprim=inprim,
		outprim=outprim,
		sourcepoints=[0, 2, 4, 6, 8, 10, 7])
