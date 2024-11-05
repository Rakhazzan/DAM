document.addEventListener("DOMContentLoaded", function () {
    const newsForm = document.getElementById('news-form');
    const createNewsForm = document.getElementById('create-news-form');
    const articlesSection = document.getElementById('articles-section');
    const asideSection = document.getElementById('aside-section');
    const noNewsMessage = document.getElementById('no-news-message');
    const noAsideNewsMessage = document.getElementById('no-aside-news-message');
    const visitCounter = document.getElementById('counter-value');
    let visitCount = localStorage.getItem("visitCount") || 0;

    visitCount++;
    localStorage.setItem("visitCount", visitCount);
    visitCounter.textContent = visitCount;

    function toggleForm() {
        newsForm.style.display = (newsForm.style.display === 'none' || newsForm.style.display === '') ? 'block' : 'none';
    }
    window.toggleForm = toggleForm;

    function loadNews() {
        const newsList = JSON.parse(localStorage.getItem("newsList")) || [];
        newsList.forEach(news => createArticle(news.title, news.content, news.section, news.id, false));
        updateEmptyMessages();
    }

    function createArticle(title, content, section, id = Date.now(), save = true) {
        const article = document.createElement('article');
        article.dataset.id = id;

        const deleteIcon = document.createElement('img');
        deleteIcon.src = 'img/drop.png';
        deleteIcon.alt = 'Eliminar noticia';
        deleteIcon.classList.add('delete-icon');
        deleteIcon.style.cursor = 'pointer';
        deleteIcon.style.width = '20px';
        deleteIcon.addEventListener('click', () => deleteArticle(id, article, section));

        article.appendChild(deleteIcon);

        const h2 = document.createElement('h2');
        h2.textContent = title;
        article.appendChild(h2);

        const p = document.createElement('p');
        p.textContent = content;
        article.appendChild(p);

        const targetSection = (section === 'Secundari') ? asideSection : articlesSection;
        targetSection.appendChild(article);
        updateEmptyMessages();

        if (save) {
            const newsList = JSON.parse(localStorage.getItem("newsList")) || [];
            newsList.push({ title, content, section, id, date: new Date().toISOString() });
            localStorage.setItem("newsList", JSON.stringify(newsList));
        }
    }

    function updateEmptyMessages() {
        noNewsMessage.style.display = articlesSection.childElementCount === 0 ? 'block' : 'none';
        noAsideNewsMessage.style.display = asideSection.childElementCount === 0 ? 'block' : 'none';
    }

    function deleteArticle(id, article, section) {
        article.remove();
        updateEmptyMessages();
        const newsList = JSON.parse(localStorage.getItem("newsList")) || [];
        const updatedNewsList = newsList.filter(news => news.id !== id);
        localStorage.setItem("newsList", JSON.stringify(updatedNewsList));
    }

    createNewsForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const newsTitle = document.getElementById('news-title').value;
        const newsContent = document.getElementById('news-content').value;
        const newsSection = document.getElementById('news-section').value;

        createArticle(newsTitle, newsContent, newsSection);
        createNewsForm.reset();
        newsForm.style.display = 'none';
    });

    loadNews();
});
