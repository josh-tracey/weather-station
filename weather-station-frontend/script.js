setInterval(() => {
	fetch('/weather')
		.then(res => res.json())
		.then(data => {
			document.getElementById('weather-data').innerHTML = `
                <p>Temperature: ${parseFloat(data.temperature).toFixed(2)}&#176;C</p>
                <p>Humidity: ${data.humidity}%</p>
                <p>Wind Speed: ${parseFloat(data.wind_speed).toFixed(2)} m/s</p>
            `;
		})
}, 1000);
