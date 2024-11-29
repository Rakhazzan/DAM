const express = require("express");
const mongoose = require("mongoose");
const bcrypt = require("bcryptjs");
const cors = require("cors");

// Configuración del servidor
const app = express();
const port = 3000;

// Middlewares
app.use(cors({ origin: "*" })); // Permitir todas las solicitudes de origen cruzado
app.use(express.json()); // Para procesar JSON en el cuerpo de las solicitudes

// Conexión a MongoDB
const uri = "mongodb://127.0.0.1:27017/HeavenTaste";
mongoose
  .connect(uri)
  .then(() => console.log("Conexión a MongoDB exitosa"))
  .catch((err) => console.error("Error al conectar a MongoDB:", err));

// Esquema y modelo del usuario
const userSchema = new mongoose.Schema({
  username: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
});

const User = mongoose.model("User", userSchema);

// Rutas
// Registro de usuario
app.post("/register", async (req, res) => {
  const { username, email, password } = req.body;

  if (!username || !email || !password) {
    return res
      .status(400)
      .json({ message: "Todos los campos son obligatorios" });
  }

  try {
    const existingUser = await User.findOne({ email });
    if (existingUser) {
      return res.status(400).json({ message: "El correo ya está registrado" });
    }

    const hashedPassword = await bcrypt.hash(password, 10);
    const newUser = new User({ username, email, password: hashedPassword });
    await newUser.save();

    res.status(201).json({ username, id: newUser._id });
  } catch (error) {
    console.error("Error al registrar el usuario:", error.message);
    res.status(500).json({ message: "Error interno del servidor" });
  }
});

// Inicio de sesión
app.post('/login', async (req, res) => {
  const { email, password } = req.body;

  try {
    // Verificar si los campos están presentes
    if (!email || !password) {
      return res.status(400).json({ message: 'Todos los campos son obligatorios' });
    }

    // Buscar al usuario por correo
    const user = await User.findOne({ email });
    if (!user) {
      return res.status(404).json({ message: 'Usuario no encontrado' });
    }

    // Comparar contraseñas
    const isPasswordValid = await bcrypt.compare(password, user.password);
    if (!isPasswordValid) {
      return res.status(401).json({ message: 'Contraseña incorrecta' });
    }

    // Responder con el éxito y el nombre de usuario
    res.status(200).json({ message: 'Inicio de sesión exitoso', username: user.username });
  } catch (error) {
    console.error('Error en el login:', error);  // Detalles del error en la consola
    res.status(500).json({ message: 'Error desconocido en el servidor', error: error.message });
  }
});
// Middleware para rutas no encontradas
app.use((req, res) => {
  res.status(404).json({ message: "Ruta no encontrada" });
});

// Iniciar el servidor
app.listen(port, () => {
  console.log(`Servidor escuchando en http://localhost:${port}`);
});
