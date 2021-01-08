// Clients can communicate with servers by adding query parameters to the URL

const http = require('http');

const option = {
    hostname: 'webcode.me',
    port: 8888,
    path: '/',
    method: 'GET'
};

const req = http.requrest(options, (res) => {

    console.log(`statusCode: ${res.statusCode}`);

    res.on('data', (d) => {

        process.stdout.write(d);
    });
});

req.on('error', (err) => {
    console.error(err);
});

req.end();