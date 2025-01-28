import http.server
import socketserver
import urllib.parse
import json

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    """
    Custom request handler for handling POST and GET requests related to personal finance data submission.

    Inherits from http.server.SimpleHTTPRequestHandler.
    """

    def do_POST(self):
        """
        Handles POST requests.

        If the path is '/submit', it reads the post data, parses it, and saves the finance data to a JSON file.
        Sends a response with a success message and a link to go back to the homepage.
        If the path is not '/submit', sends a 404 response.
        """
        if self.path == '/submit':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = urllib.parse.parse_qs(post_data.decode('utf-8'))
            
            finance_data = {
                "income": {
                    "agri_business": {
                        "ll": data.get('agri_business_ll', [''])[0],
                        "usd": data.get('agri_business_usd', [''])[0]
                    },
                    "pet_food": {
                        "ll": data.get('pet_food_ll', [''])[0],
                        "usd": data.get('pet_food_usd', [''])[0]
                    },
                    "offshore_consultancy": {
                        "ll": data.get('offshore_consultancy_ll', [''])[0],
                        "usd": data.get('offshore_consultancy_usd', [''])[0]
                    }
                },
                "expenses": {
                    "secret": {
                        "ll": data.get('secret_expenses_ll', [''])[0],
                        "usd": data.get('secret_expenses_usd', [''])[0]
                    },
                    "regular": {
                        "ll": data.get('regular_expenses_ll', [''])[0],
                        "usd": data.get('regular_expenses_usd', [''])[0]
                    },
                    "cost_of_sales": {
                        "ll": data.get('cost_of_sales_ll', [''])[0],
                        "usd": data.get('cost_of_sales_usd', [''])[0]
                    },
                    "cost_of_living": {
                        "ll": data.get('cost_of_living_ll', [''])[0],
                        "usd": data.get('cost_of_living_usd', [''])[0]
                    }
                }
            }
            
            with open('finance_data.json', 'w') as f:
                json.dump(finance_data, f, indent=2)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Submission successful! <a href="/">Go back</a>')
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_GET(self):
        """
        Handles GET requests.

        If the path is '/', sets the path to 'index.html' and calls the base class's do_GET method.
        """
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
