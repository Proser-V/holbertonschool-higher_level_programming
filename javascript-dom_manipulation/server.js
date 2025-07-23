const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 3000;

http.createServer((req, res) => {
  let filePath = '.' + req.url;
  if (filePath === './') filePath = './101-main.html';

  const ext = path.extname(filePath);
  let contentType = 'text/html';

  if (ext === '.js') contentType = 'text/javascript';
  if (ext === '.css') contentType = 'text/css';

  fs.readFile(filePath, (err, content) => {
    if (err) {
      res.writeHead(404);
      res.end('404 Not Found');
    } else {
      res.writeHead(200, { 'Content-Type': contentType });
      res.end(content, 'utf-8');
    }
  });
}).listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}/`);
});
