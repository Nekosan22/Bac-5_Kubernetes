import os
from flask import Flask, jsonify

app = Flask(__name__)

# Route principale de l'application (billetterie)
@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "Bienvenue sur l'API de la billetterie résiliente !"
    }), 200

# Liveness probe : vérifie simplement que le processus tourne
@app.route('/healthz')
def liveness():
    return jsonify({"status": "healthy"}), 200

# Readiness probe : vérifie si l'application est prête à recevoir du trafic 
# (vous pouvez y ajouter ici une vérification de la connexion à PostgreSQL si besoin)
@app.route('/ready')
def readiness():
    # Exemple basique : l'application est prête
    # En production, vous pouvez tester un ping vers la base de données ici
    return jsonify({"status": "ready"}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)