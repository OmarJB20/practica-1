from flask import Flask, render_template_string

app = Flask(__name__)


pagina_html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Página </title>
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);
            height: 100vh;
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .card {
            background-color: white;
            border-radius: 20px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
            padding: 40px;
            text-align: center;
            max-width: 400px;
            width: 90%;
        }
        h1 {
            color: #333;
            margin-bottom: 10px;
        }
        p {
            color: #666;
            font-size: 16px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 10px;
            cursor: pointer;
            margin-top: 15px;
            transition: background 0.3s ease;
        }
        button:hover {
            background-color: #45a049;
        }
        .mensaje {
            margin-top: 20px;
            font-weight: bold;
            color: #2c3e50;
            transition: opacity 0.5s;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>✨ Bienvenido a mi página Flask ✨</h1>
        <p>Esta página está corriendo en <strong>Python Flask</strong> en el puerto 80.</p>
        <button onclick="mostrarMensaje()">Haz clic aquí</button>
        <div id="mensaje" class="mensaje" style="opacity:0;">¡Gracias por visitar mi web! 💚</div>
    </div>

    <script>
        function mostrarMensaje() {
            const msg = document.getElementById("mensaje");
            msg.style.opacity = 1;
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(pagina_html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
