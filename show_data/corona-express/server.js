const express = require('express');
const fs = require('fs');
const http = require('http');
const https = require('https');

// Credentials for HTTPS
const privateKey = fs.readFileSync('/etc/letsencrypt/live/infocovid19.de/privkey.pem', 'utf8');
const certificate = fs.readFileSync('/etc/letsencrypt/live/infocovid19.de/cert.pem', 'utf8');
const ca = fs.readFileSync('/etc/letsencrypt/live/infocovid19.de/chain.pem', 'utf8');
const credentials = {
	key: privateKey,
	cert: certificate,
	ca: ca
};


let app = express();
http.createServer(function (req, res) {
    res.writeHead(301, { "Location": "https://" + req.headers['host'] + req.url });
    res.end();
}).listen(80);

const httpsServer = https.createServer(credentials, app);
app.use('/', express.static('../corona-app/build/'));

httpsServer.listen(443, () => {
	console.log('HTTPS Server running on port 443');
});
