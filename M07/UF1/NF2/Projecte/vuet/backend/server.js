const express = require("express");
const mongoose = require("mongoose");
const bcrypt = require("bcryptjs");
const cors = require("cors");

// Configuración del servidor
const app = express();
const port = 3001;

// Middlewares
app.use(cors({ origin: "*" })); // Permitir todas las solicitudes de origen cruzado
app.use(express.json()); // Para procesar JSON en el cuerpo de las solicitudes

// Conexión a MongoDB
const uri = "mongodb://127.0.0.1:27017/HeavenTaste"; // Uso de 127.0.0.1 en lugar de localhost
mongoose
  .connect(uri)
  .then(() => console.log("Conexión a MongoDB exitosa"))
  .catch((err) => console.error("Error al conectar a MongoDB:", err));

// Definición del esquema y modelo de usuario
const userSchema = new mongoose.Schema({
  username: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
});

const User = mongoose.model("User", userSchema);

// Rutas
app.post("/register", async (req, res) => {
  const { username, email, password } = req.body;

  // Validación de entrada
  if (!username || !email || !password) {
    return res
      .status(400)
      .json({ message: "Todos los campos son obligatorios" });
  }

  try {
    // Verifica si el usuario ya existe
    const existingUser = await User.findOne({ email });
    if (existingUser) {
      return res.status(400).json({ message: "El correo ya está registrado" });
    }

    // Hashea la contraseña
    const hashedPassword = await bcrypt.hash(password, 10);

    // Crea y guarda el nuevo usuario
    const newUser = new User({ username, email, password: hashedPassword });
    await newUser.save();

    res.status(201).json({ username, id: newUser._id });
  } catch (error) {
    console.error("Error en el servidor:", error.message);
    res.status(500).json({ message: "Error interno del servidor" });
  }
});

// Ruta de prueba
app.get("/", (req, res) => {
  res.send("Servidor funcionando correctamente");
});

// Middleware para manejar rutas no encontradas
app.use((req, res) => {
  res.status(404).json({ message: "Ruta no encontrada" });
});
app.post('/login', async (req, res) => {
  const { email, password } = req.body;

  if (!email || !password) {
    return res.status(400).json({ message: 'Todos los campos son obligatorios' });
  }

  const user = await User.findOne({ email });
  if (!user) {
    return res.status(404).json({ message: 'Usuario no encontrado' });
  }

  const isPasswordValid = await bcrypt.compare(password, user.password);
  if (!isPasswordValid) {
    return res.status(401).json({ message: 'Contraseña incorrecta' });
  }

  res.status(200).json({ message: 'Inicio de sesión exitoso', username: user.username });
});


// Inicia el servidor
app.listen(port, () => {
  console.log(`Servidor escuchando en http://localhost:${port}`);
});
