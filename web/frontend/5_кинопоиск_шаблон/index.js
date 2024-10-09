const API_KEY = "4d5b1014-2ce3-49d6-b2ac-e47e01ed4533";
const listDOM = document.querySelector('.movies');

async function getMovies(page = 1, yearFrom = null, keyword = '') {
    const request = {
        page: page,
        yearFrom: yearFrom,
        keyword: keyword
    };
    
    for (const i in request) {
        if (!request[i]) {
            delete request[i];
        }
    }
    
    const url = 'https://kinopoiskapiunofficial.tech/api/v2.2/films?' + new URLSearchParams(request).toString();
    const response = await axios.get(url, {
        headers: {
            "Content-Type": 'application/json',
            "X-API-KEY": API_KEY,
        },
    });
    const movies = response.data;
    
    for (let movie of movies.items) {
        const newDivHTML = `
              <div class="movie__cover">
                  <div class="movie__cover-inner" style="background-image: url(${ movie.posterUrlPreview })"></div>
                  <div class="movie__title">${ movie.nameRu || movie.nameOriginal } (${ movie.year })</div>
                  <div class="movie__info"></div>
                  <div class="movie__average">${ movie.ratingKinopoisk }</div>
              </div>`;
        const newDiv = document.createElement('div');
        newDiv.classList.add('movie');
        newDiv.innerHTML = newDivHTML;
        listDOM.appendChild(newDiv);
    }
}

getMovies(2);
