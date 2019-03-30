
def repeatCharXOR(input_bytes, char_bytes):
	output_bytes = b''

	count = 0
	l = len(char_bytes)

	for byte in input_bytes:
		char_byte = char_bytes[count % l]
		output_bytes += bytes([byte ^ char_byte])
		count += 1

	return(output_bytes)


def main(input_msg, keystream):
	message = bytes(input_msg.encode('ascii'))

	key = bytes(keystream.encode('ascii'))

	enc = repeatCharXOR(message, key)

	print(enc.hex())

main("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal","ICE")
