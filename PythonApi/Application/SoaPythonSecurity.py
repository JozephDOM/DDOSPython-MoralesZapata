#Soa python security

#########################################################################

from fastapi import FastAPI

app:FastAPI = FastAPI(title="Soa python security", description="IUE 2023-2")

#########################################################################

@app.get("/autenticarUsuario", 
         summary="Autenticar usuario",
         description="Api para autenticar usuario",
         tags=["Autenticar usuario"])

async def autenticar_usuario(usuario:str| None = None, clave:str| None = None):
    salida: str = usuario + " " + clave
    return salida

#########################################################################
