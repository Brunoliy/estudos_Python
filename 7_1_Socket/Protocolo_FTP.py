from ftplib import *

ftp_ativo=False
ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())
usuario=input("Digite o usuário: ")
senha=input("Digite a senha: ")
ftp.login(usuario, senha)
print("Dirtório atual de trabalho: ", ftp.pwd())
ftp.cwd("pub")
print("Diretório corrente: ", ftp.pwd())
print(ftp.retrlines('LIST'))

ftp.quit()