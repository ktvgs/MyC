const express = require('express');
const fs = require('fs');
const app = express();
const port = 3000;

app.set('view engine', 'ejs');
app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));

app.get('/', (req, res) => {
    res.render('index');
});

app.post('/submit', (req, res) => {
    try {
        const { date, wakeUp, breakfast, study, lunch, exercise, shower, dinner, sleep } = req.body;
        const data = `${date},${wakeUp},${breakfast},${study},${lunch},${exercise},${shower},${dinner},${sleep}\n`;

        // Append data to a text file
        fs.appendFileSync('formData.txt', data);

        res.send('Data stored in the text file successfully');
    } catch (err) {
        console.error('Error processing form submission', err);
        res.send('Error processing form submission');
    }
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
