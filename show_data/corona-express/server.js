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
const httpServer = express.createServer();

httpServer.get('*', function(req, res) {
    res.redirect('https://' + req.headers.host + req.url);
})

const httpsServer = https.createServer(credentials, app);
app.use('/', express.static('../corona-app/build/'));
httpServer.listen(80, () => {
  console.log('HTTP redirector running on port 80')
});

httpsServer.listen(443, () => {
	console.log('HTTPS Server running on port 443');
});
