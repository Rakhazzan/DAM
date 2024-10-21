document.getElementById('generateButton').addEventListener('click', generateDates);
document.getElementById('language').addEventListener('change', generateDates);

const monthsCa = ["gener", "febrer", "març", "abril", "maig", "juny", "juliol", "agost", "setembre", "octubre", "novembre", "desembre"];
const monthsEn = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
const daysCa = ["diumenge", "dilluns", "dimarts", "dimecres", "dijous", "divendres", "dissabte"];
const daysEn = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

function generateDates() {
    const currentYear = new Date().getFullYear();
    let randomDates = [];

    for (let i = 0; i < 5; i++) {
        randomDates.push(randomDateInYear(currentYear));
    }

    // Ordenar les dates cronològicament
    randomDates.sort((a, b) => a - b);

    displayDates(randomDates);
}

function randomDateInYear(year) {
    const start = new Date(year, 0, 1);
    const end = new Date(year, 11, 31);
    return new Date(start.getTime() + Math.random() * (end.getTime() - start.getTime()));
}

function displayDates(dates) {
    const language = document.getElementById('language').value;
    const months = language === "ca" ? monthsCa : monthsEn;
    const days = language === "ca" ? daysCa : daysEn;

    const dateContainer = document.getElementById('dates');
    dateContainer.innerHTML = '';

    dates.forEach((date, index) => {
        const day = date.getDate();
        const month = months[date.getMonth()];
        const year = date.getFullYear();
        const dayOfWeek = days[date.getDay()];

        let formattedDate = `${dayOfWeek}, ${day} de ${month} de ${year}`;

        if (language === "en") {
            formattedDate = `${dayOfWeek}, ${day} ${month} ${year}`;
        }

        const dateElement = document.createElement('p');
        dateElement.textContent = `Data ${index + 1}: ${formattedDate}`;
        dateContainer.appendChild(dateElement);
    });
}
