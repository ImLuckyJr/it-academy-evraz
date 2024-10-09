const listDOM = document.querySelector('.movies')

async function getMovies(page = 1, keyword = '', yearFrom = null) {
    const request = {};
    
    if (page) {
        request.page = page;
    }
    
    if (keyword) {
        request.keyword = keyword;
    }
    
    if (yearFrom) {
        request.yearFrom = yearFrom;
    }
    
    const url = `https://kinopoiskapiunofficial.tech/api/v2.2/films?${ new URLSearchParams(request).toString() }`
    const response= await fetch(url, {
        headers: {
            'X-API-KEY': 'ebbee2c0-522d-4470-bf57-74f8983ecc72',
            "Content-Type":"application/json"
        }
    })

    const movies = await response.json();
    
    // const movieSearch = document.getElementById("input")
    // // movieSearch.oninput()
    // console.log(movieSearch)
    for (const movie of movies.items) {
        const newDivHTML = `<img class="movie__cover" src=${movie.posterUrlPreview} alt="">
                            <div class="movie__average">${movie.ratingKinopoisk}</div>`
        const newDiv = document.createElement('div') //1
        newDiv.classList.add('movie')
        newDiv.innerHTML = newDivHTML
        listDOM.appendChild(newDiv)
    }
}

getMovies(1, 'Холодное сердце')
