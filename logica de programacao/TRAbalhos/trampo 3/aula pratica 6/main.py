palavras = ('mario','luigi','yoshi','peach','bowser')

for palavra in palavras:
    print('\npalavra: {}, vogais: ' .format(palavra.upper()), end= ' ')
    for letra in palavra:
        if letra.lower() in "aeiou":
            print(letra.upper(), end= " ")
