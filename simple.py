from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloWorldHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Envia o status HTTP 200 (OK)
        self.send_response(200)
        # Define o tipo de conteúdo como texto simples
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        # Responde com "Hello, World!"
        self.wfile.write(b"Hello, World!")

# Porta 80 exige privilégios de administrador em muitos sistemas
def run(server_class=HTTPServer, handler_class=HelloWorldHandler, port=80):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()