"""Writing a Web Server with at least one GET endpont which returns a JSON response"""
#1st pip3 install Flask

#using simple API

#use the from
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

import logging  # Import the logging module

# Configure logging (optional but recommended)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')  # Set logging level

#class call
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/data':
            data = {
                'message': 'Hello from the API!',
                'status': 200,
                'items': [
                    {'id': 1, 'name': 'Item 1'},
                    {'id': 2, 'name': 'Item 2'}
                ]
            }
            self.send_response(200)  # HTTP status code 200 (OK)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_response(404)  # HTTP status code 404 (Not Found)
            self.send_header('Content-type', 'application/json')  # Indicate JSON even for error
            self.end_headers()
            error_data = {"error": "Not Found"}
            self.wfile.write(json.dumps(error_data).encode())

            
if __name__ == '__main__':
    server_address = ('', 8000)  # Listen on all interfaces, port 8000
    httpd = HTTPServer(server_address, MyHandler)
    print('Starting server...')
    httpd.serve_forever()
    # localhost: 8000/api/data