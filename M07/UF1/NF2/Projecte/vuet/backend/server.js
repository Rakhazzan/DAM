const express = require("express");
const mongoose = require("mongoose");
const bcrypt = require("bcryptjs");
const cors = require("cors");


const app = express();
const port = 3001;

// Middlewares
app.use(cors({ origin: "http://localhost:3000" })); 
app.use(express.json()); 


const uri = "mongodb://127.0.0.1:27017/HeavenTaste"; 
mongoose
  .connect(uri, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log("Conexión a MongoDB exitosa"))
  .catch((err) => console.error("Error al conectar a MongoDB:", err));


const userSchema = new mongoose.Schema({
  username: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
});

const User = mongoose.model("User", userSchema);

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
    console.error("Error en el servidor:", error.message);
    res.status(500).json({ message: "Error interno del servidor" });
  }
});

app.post("/login", async (req, res) => {
  const { email, password } = req.body;


  if (!email || !password) {
    return res.status(400).json({ message: "Todos los campos son obligatorios" });
  }

  try {
 
    const user = await User.findOne({ email });
    if (!user) {
      return res.status(404).json({ message: "Usuario no encontrado" });
    }

  
    const isPasswordValid = await bcrypt.compare(password, user.password);
    if (!isPasswordValid) {
      return res.status(401).json({ message: "Contraseña incorrecta" });
    }


    res.status(200).json({ message: "Inicio de sesión exitoso", username: user.username });
  } catch (error) {
    console.error("Error en el servidor:", error);
    res.status(500).json({ message: "Error interno del servidor" });
  }
});

app.get('/profile', (req, res) => {

  const email = req.query.email;

 
  const user = users.find(u => u.email === email);

  if (user) {
    res.json({ username: user.username, email: user.email });
  } else {
    res.status(404).json({ message: "Usuario no encontrado" });
  }
});

app.get("/", (req, res) => {
  res.send("Servidor funcionando correctamente");
});


app.listen(port, () => {
  console.log(`Servidor escuchando en http://localhost:${port}`);
});
