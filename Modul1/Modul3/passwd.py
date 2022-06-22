def office():
    credentials = {}
    for i in range(1, 4):
        PCs_user = input(f"Introduceti utilizatorul PC-ului {i}: ")
        PCs_pasw = input(f"Introduceti parola PC-ului {i}: ")
        credentials[PCs_user] = PCs_pasw
    print(f"{credentials}")


office()