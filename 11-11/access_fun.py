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

