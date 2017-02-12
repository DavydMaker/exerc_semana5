def maior_primo(n):
	i = n
	while True:
		if i % 2 != 0 and i % 3 != 0:
			return i
		i -= 1