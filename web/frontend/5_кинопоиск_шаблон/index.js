const API_KEY = "8c8e1a50-6322-4135-8875-5d40a5420d86";

async function getMovies() {
    const url = 'https://kinopoiskapiunofficial.tech/api/v2.2/films/top';
    const response = await fetch(url, {
        headers: {
            "Content-Type": 'application/json',
            "X-API-KEY": API_KEY,
        },
    });
    const movies = await response.json();
    console.log(movies);
}

getMovies();