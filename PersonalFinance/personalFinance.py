import http.server
import socketserver
import urllib.parse
import json

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/submit':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = urllib.parse.parse_qs(post_data.decode('utf-8'))
            
            income = data.get('income', [''])[0]
            expenses = data.get('expenses', [''])[0]
            
            finance_data = {
                "income": income,
                "expenses": expenses
            }
            
            with open('finance_data.json', 'w') as f:
                json.dump(finance_data, f)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Submission successful! <a href="/">Go back</a>')
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()