english_character_frequencies = {
		'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
		'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
		'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
		'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
		'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
		'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
		'y': .01974, 'z': .00074, ' ': .13000
	}

def english_score(input_bytes):
	return sum([english_character_frequencies.get(chr(byte),0) for byte in input_bytes.lower()])


def singleCharXOR(input_bytes, char_byte):
	output_bytes = b''

	for byte in input_bytes:
		output_bytes += bytes([byte ^ char_byte])

	return(output_bytes)

def bruteforceXOR(ciphertext):
	potential_messages = []
	
	for char in range(256):
		message = singleCharXOR(ciphertext, char)
		score = english_score(message)
		data = {
			'message': message,
			'score': score,
			'key': char
		}
		potential_messages.append(data)
	return sorted(potential_messages, key=lambda x: x['score'], reverse=True)[0]

def main():
	ciphers = open('60characterStrings.txt').read().splitlines()
	potential_plaintext = []

	for hexstring in ciphers:
		ciphertext = bytes.fromhex(hexstring)
		potential_plaintext.append(bruteforceXOR(ciphertext))

	best_score = sorted(potential_plaintext, key=lambda x: x['score'], reverse=True)[0]
	for item in best_score:
		print("{}: {}".format(item.title(), best_score[item]))

main()

