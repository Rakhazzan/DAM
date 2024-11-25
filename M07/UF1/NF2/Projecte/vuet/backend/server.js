const express = require('express');
const cors = require('cors');
const mysql = require('mysql2');

const app = express();
const PORT = 3000;

// Configuración de CORS
app.use(cors());

// Middleware para manejar JSON
app.use(express.json());

// Conexión a la base de datos MariaDB
const db = mysql.createConnection({
  host: 'localhost',
  user: 'root', // Usuario de tu base de datos MariaDB
  password: '', // Contraseña de tu base de datos MariaDB
  database: 'heaven_taste'
});

// Conexión exitosa a MariaDB
db.connect((err) => {
  if (err) {
    console.error('Error de conexión a MariaDB:', err);
    return;
  }
  console.log('Conexión a MariaDB exitosa');
});

// Ruta para obtener todos los usuarios
app.get('/users', (req, res) => {
  db.query('SELECT * FROM users', (err, results) => {
    if (err) {
      res.status(500).json({ message: 'Error al obtener usuarios' });
    } else {
      res.status(200).json(results);
    }
  });
});

// Ruta para crear un nuevo usuario
app.post('/users', (req, res) => {
  const { name, email, password } = req.body;
  db.query('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', [name, email, password], (err, results) => {
    if (err) {
      res.status(500).json({ message: 'Error al agregar usuario' });
    } else {
      res.status(201).json({ message: 'Usuario creado exitosamente' });
    }
  });
});

// Iniciar el servidor
app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
