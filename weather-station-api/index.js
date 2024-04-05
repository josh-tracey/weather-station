const express = require('express');
const fs = require('fs');

const app = express();
const port = 3000;

app.get('/weather', (_, res) => {
	fs.readFile('weather_data.json', 'utf-8', (err, data) => {
		if (err) {
			res.status(500).send("Error reading weather data");
		} else {
			res.json(JSON.parse(data));
		}
	});
});

app.listen(port, () => {
	console.log(`Weather API listening on port ${port}`);
});
