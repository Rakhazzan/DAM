
const API_KEY = 'e2c1359d753244bd7d97732c06120c02';

const cities = [
  { name: 'Barcelona', lat: 41.3851, lon: 2.1734 },
  { name: 'Madrid', lat: 40.4168, lon: -3.7038 },
  { name: 'Paris', lat: 48.8566, lon: 2.3522 },
  { name: 'Rome', lat: 41.9028, lon: 12.4964 }
];

const map = L.map('map').setView([50, 10], 4);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '© OpenStreetMap'
}).addTo(map);

async function getWeather(lat, lon) {
  const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric&lang=ca`;
  const response = await fetch(url);
  const data = await response.json();
  return data.main.temp; 
}

async function addCityMarkers() {
  map.eachLayer((layer) => {
    if (layer instanceof L.Marker) {
      map.removeLayer(layer);
    }
  });

  for (const city of cities) {
    const temp = await getWeather(city.lat, city.lon);
    

    const marker = L.marker([city.lat, city.lon]).addTo(map);
    
    marker.bindPopup(`
      <div class="weather-popup">
        <strong>${city.name}</strong><br>
        Temperatura: ${temp} °C
      </div>
    `).openPopup();
  }
}

addCityMarkers();

setInterval(addCityMarkers, 60000);
