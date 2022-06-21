sentence = "Prezentarea si introducerea in lumea automatizării"

# sentence.upper()
print(sentence.upper())


def putere_n(x, n,add=101):

    print("Variabilele sunt: ", x, n, add)
    return x ** n + add


result = putere_n(4, 5, add=101)
print(putere_n(4.55, 5, add=101))
print(result)
