import base64

def hex2Base64(h):

	hx = bytearray(h)
	b64 = base64.b64encode(hx)
	return b64

def testHex2Base64():
	hex2Base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'.decode('hex'))

