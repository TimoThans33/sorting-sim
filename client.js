// Clients can communicate with servers by adding query parameters to the URL

const http = require('http');
const url = require('url');

http.createServer((req, res) => {

    let q = url.parse(req.url, true).query;

    let msg = '${q.name} is ${'
})