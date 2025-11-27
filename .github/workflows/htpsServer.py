import http.server
import socketserver
import ssl

PORT = 8000
HANDLER = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), HANDLER) as httpd:
    httpd.socket = ssl.wrap_socket(
        httpd.socket,
        keyfile="key.pem",
        certfile="cert.pem",
        server_side=True
    )
    print(f"Serving securely on https://localhost:{PORT}")
    httpd.serve_forever()   
