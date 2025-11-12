from database import db_users as db

#Função para realizar o login
def login(user: str, password: str) -> bool:
    '''
    Função para verificar se um login é válido.

    Parâmetros: 
        - user (str): nome do usuário
        - password (str): senha do usuário
    
    Retorno: retornará um valor true ou false
    '''
    for k, v in db.items():
        if k == user and v == password:
            return True
    
    return False

#Função para redefinir a senha
def resetPassword(user: str, password: str, new_password: str) -> str:
    '''
    Função para redefinir a senha do usuário.

    Parâmetros:
        - user (str): nome do usuário
        - password (str): senha do usuário
        - new_password (str): senha atualizada para registrar
    
    Retorno: Uma String confirmando ou recusando a modificação da senha
    '''
    if login(user, password):
        db[user] = new_password
        return 'Senha Alterada!'
    
    return 'Error: Credenciais Inválidas!'

#Função para modificar o nome do usuário
def updateUser(user: str, password: str) -> object:


