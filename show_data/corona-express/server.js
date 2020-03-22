const express = require('express');
const secure = require('express-force-https');
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
const httpServer = http.createServer(app);
const httpsServer = https.createServer(credentials, app);
app.use(secure);
app.use(express.static('../corona-app/build/'));
