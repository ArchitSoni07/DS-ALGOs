#Hill Cipher
import numpy as np
keyMatrix = [[0] * 3 for i in range(3)]
messageVector = [[0] for i in range(3)]
cipherMatrix = [[0] for i in range(3)]

def getKeyMatrix(key):
	k = 0
	for i in range(3):
		for j in range(3):
			keyMatrix[i][j] = ord(key[k]) % 65
			k += 1

def getInvertedKeyMatrix(key):
    k = 0
	for i in range(3):
		for j in range(3):
			keyMatrix[i][j] = ord(key[k]) % 65
			k += 1
    invertedKeyMatrix = np.linalg.inv(keyMatrix)

def encrypt(messageVector):
	for i in range(3):
		for j in range(1):
			cipherMatrix[i][j] = 0
			for x in range(3):
				cipherMatrix[i][j] += (keyMatrix[i][x] *
									messageVector[x][j])
			cipherMatrix[i][j] = cipherMatrix[i][j] % 26
			
def decrypt(invertedKeyMatrix):
    text = []
    for i in invertedKeyMatrix:
        text.append(chr(chr(i)-65))
    return text

def HillCipher(message, key):

	getInvertedKeyMatrix(key)
	getKeyMatrix(key)
	
	for i in range(3):
		messageVector[i][0] = ord(message[i]) % 65

	encrypt(messageVector)
	CipherText = []
	for i in range(3):
		CipherText.append(chr(cipherMatrix[i][0] + 65))

	print("Ciphertext: ", "".join(CipherText))
    print(decrypt(invertedKeyMatrix))


def main():

	message = "ACT"
	key = "GYBNQKURP"

	HillCipher(message, key)

if __name__ == "__main__":
	main()

