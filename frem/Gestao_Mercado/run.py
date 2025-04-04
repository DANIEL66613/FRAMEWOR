from flask import Flask
from app.adapters.api.routes import api
from app.adapters.database.database import criar_app
from app.adapters.auth.auth import configurar_auth

app = criar_app()  # Configura app e o banco de dados
configurar_auth(app)  # Configura a autenticação do JWT


app.register_blueprint(api)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
