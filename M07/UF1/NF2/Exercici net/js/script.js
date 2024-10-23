// Esperar a que el DOM esté completamente cargado antes de ejecutar el script
document.addEventListener("DOMContentLoaded", function () {
    const newsForm = document.getElementById('news-form');
    const createNewsForm = document.getElementById('create-news-form');
    const articlesSection = document.getElementById('articles-section'); // Sección de artículos principales
    const asideSection = document.getElementById('aside-section'); // Sección de noticias secundarias (aside)

    // Función para alternar la visibilidad del formulario
    window.toggleForm = function () {
        if (newsForm.style.display === 'none' || newsForm.style.display === '') {
            newsForm.style.display = 'block';
        } else {
            newsForm.style.display = 'none';
        }
    };

    // Función para crear un nuevo artículo
    function createArticle(title, content, section) {
        // Crear un nuevo elemento de artículo
        const article = document.createElement('article');
        
        // Crear y agregar la imagen de eliminación
        const deleteIcon = document.createElement('img');
        deleteIcon.src = 'img/drop.png'; // Aquí es donde puedes colocar la URL de la imagen
        deleteIcon.alt = 'Eliminar noticia';
        deleteIcon.classList.add('delete-icon');
        deleteIcon.style.cursor = 'pointer';
        deleteIcon.style.width = '20px'; // Ajusta el tamaño según necesites
        article.appendChild(deleteIcon);

        // Crear y agregar el título
        const h2 = document.createElement('h2');
        h2.textContent = title;
        article.appendChild(h2);

        // Crear y agregar el contenido
        const p = document.createElement('p');
        p.textContent = content;
        article.appendChild(p);

        // Seleccionar la sección correcta (Principal o Secundari)
        if (section === 'Secundari') {
            asideSection.appendChild(article); // Agregar el artículo al aside
        } else {
            articlesSection.appendChild(article); // Agregar el artículo a la sección principal
        }

        // Agregar evento de clic para eliminar el artículo
        deleteIcon.addEventListener('click', function() {
            article.parentElement.removeChild(article);
        });
    }

    // Escuchar el evento submit del formulario
    createNewsForm.addEventListener('submit', function (event) {
        // Evitar que la página se recargue
        event.preventDefault();

        // Obtener los valores del formulario
        const newsTitle = document.getElementById('news-title').value;
        const newsContent = document.getElementById('news-content').value;
        const newsSection = document.getElementById('news-section').value;

        // Crear un nuevo artículo
        createArticle(newsTitle, newsContent, newsSection);

        // Limpiar el formulario
        createNewsForm.reset();

        // Ocultar el formulario después de crear la noticia
        newsForm.style.display = 'none';
    });

    // Agregar eventos de clic a las imágenes de eliminación de los artículos preexistentes
    document.querySelectorAll('.delete-icon').forEach(function(deleteIcon) {
        deleteIcon.addEventListener('click', function() {
            const article = deleteIcon.parentElement;
            article.parentElement.removeChild(article);
        });
    });
});
