const express = require('express');
const path = require('path');
const app = express();


app.set('views', path.join(__dirname, './'));

app.use(express.static(path.join(__dirname, './')));


app.get('/', function (req, res) {
    res.render('index');
});

app.listen(3003, function () {
    console.log('app started on port 3000');
});