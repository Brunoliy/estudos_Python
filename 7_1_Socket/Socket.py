import socket

resp = "S"
while(resp=="S"):
    url=input("Digite um URL: ")
    ip = socket.gethostbyname(url)
    print("O IP referente á url informada é: ", ip)
    resp=input("Digite <S> para continuar: ").upper()

