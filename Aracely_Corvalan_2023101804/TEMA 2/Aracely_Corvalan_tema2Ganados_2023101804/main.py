from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configuración base de datos MySQL
db_config = {
    'host': 'localhost',
    'user': 'tu_usuario',
    'password': 'tu_contraseña',
    'database': 'ganados_db'
}

# Lotes de animales con datos y descripciones
lot_data = [
    {'tipo': 'Ternero/a', 'descripcion': 'Bovino joven, generalmente al pie de la madre.',
     'imagen': 'ternero.jpg', 'cantidad': 10, 'precio': 1500},
    {'tipo': 'Novillito', 'descripcion': 'Macho castrado de destete hasta aprox. 2 años.',
     'imagen': 'novillito.jpg', 'cantidad': 8, 'precio': 2000},
    {'tipo': 'Novillo', 'descripcion': 'Macho castrado de más de dos años.',
     'imagen': 'novillo.jpg', 'cantidad': 6, 'precio': 2500},
    {'tipo': 'Vaquillona', 'descripcion': 'Hembra desde el destete hasta su primera parición.',
     'imagen': 'vaquillona.jpg', 'cantidad': 5, 'precio': 3000},
    {'tipo': 'Vaca', 'descripcion': 'Hembra adulta.',
     'imagen': 'vaca.jpg', 'cantidad': 7, 'precio': 3500},
    {'tipo': 'Toro', 'descripcion': 'Macho entero (no castrado).',
     'imagen': 'toro.jpg', 'cantidad': 3, 'precio': 4000},
]

@app.route('/')
def dashboard():
    return render_template('dashboard.html', lotes=lot_data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        celular = request.form['celular']
        horario = request.form['horario']

        # Guardar en MySQL
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        sql = "INSERT INTO contactos (nombre, apellido, correo, celular, horario) VALUES (%s, %s, %s, %s, %s)"
        values = (nombre, apellido, correo, celular, horario)
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('dashboard'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
