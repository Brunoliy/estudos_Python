with open ("pagina.html", "w") as pagina:
    pagina.write("<body> <h1> Este é um teste para página web </h1>")
    pagina.write(("<b2> <h2> Abaixo seguem alguns nomes importantrs para o projeto: </h2>"))
    pagina.write("<h3>")
    nome = ""

    while nome != "SAIR":
        nome = input("Digite um nome ou SAIR: ").upper()
        if nome != "SAIR":
            pagina.write("<br>"+nome)
    pagina.write("</h3></body>")
