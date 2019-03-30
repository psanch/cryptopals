import base64

def getHexCiphers():
	ciphers = open('6.txt').read().splitlines()

	hex_ciphers = []
	for cipher in ciphers:
		tmp = base64.b64decode(cipher)
		print(tmp.hex())
		hex_ciphers.append(tmp)

	return hex_ciphers

def getHammingDistance():
	a = bytes("this is a test".encode('ascii'))
	b = bytes("wokka wokka!!!".encode('ascii'))
	output = b""

	for index in range(len(a)):
		output += bytes([a[index] ^ b[index]])


	print(output.hex())

getHammingDistance()
