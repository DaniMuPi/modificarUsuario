from cargarUsuarios import cargarUsuarios

def modificarUsuario(nombreUsuario, contraseñaUsuarioAntigua, contraseñaUsuarioNueva, archivoUsuarios):
    usuarios_dict = cargarUsuarios(archivoUsuarios)
    if (nombreUsuario in usuarios_dict):
        if (usuarios_dict[nombreUsuario] == contraseñaUsuarioAntigua):
            usuarios_dict[nombreUsuario] = contraseñaUsuarioNueva
            mensaje = "La contraseña se ha modificado correctamente."
        else:
            mensaje = "La contraseña anterior interoducida es incorrecta."
    else:
        mensaje = "Este usuario no esta registrado."
    return mensaje

