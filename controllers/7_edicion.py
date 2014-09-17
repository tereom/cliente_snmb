# coding: utf8

def manage_users():
    grid = SQLFORM.grid(db.Huella_excreta.hay_nombre_comun==False,user_signature=False)
    return locals()