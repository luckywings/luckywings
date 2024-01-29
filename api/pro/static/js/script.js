const api_key = '360e4bc3865e745ec844bd7ec054ca11';
const form = document.getElementById('weather-form');
const cityInput = document.getElementById('city-input');
const cityElement = document.querySelector('.city');
const tempElement = document.querySelector('.temp');
const descriptionElement = document.querySelector('.description');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const cityName = cityInput.value.trim();
    if (cityName) {
        const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${cityName}&appid=${api_key}&units=metric`);
        const data = await response.json();

        if (data.cod === 200) {
            cityElement.innerText = data.name;
            tempElement.innerText = `${data.main.temp}°C`;
            descriptionElement.innerText = data.weather[0].description;

            // Change UI based on weather conditions
            if (data.weather[0].main === 'Clear') {
                document.body.style.backgroundColor = '#bde0c8';
            } else if (data.weather[0].main === 'Clouds') {
                document.body.style.backgroundColor = '#d3d3d3';
            } else if (data.weather[0].main === 'Rain' || data.weather[0].main === 'Drizzle' || data.weather[0].main === 'Mist') {
                document.body.style.backgroundColor = '#95a5a6';
            }
        } else {
            alert('City not found. Please try again.');
            cityInput.value = '';
        }
    } else {
        alert('Please enter a city name.');
    }
});