def fixedXOR(p, q):
	'''
	p : str representing hex
	q : str representing hex

	r: str representing hex
	'''
	if len(p) != len(q):
		return -1
	a = int(p,16)
	b = int(q,16)
	c = hex(a^b)[2:-1]
	return(c)


def testFixedXOR():
	print(fixedXOR('1c0111001f010100061a024b53535009181c','686974207468652062756c6c277320657965'))

testFixedXOR()
