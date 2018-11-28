import socketserver
import http.server
import ssl
import os


httpd = socketserver.TCPServer(('0.0.0.0', 443), http.server.SimpleHTTPRequestHandler)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('cert.pem', 'key.pem')
httpd.socket = context.wrap_socket(httpd.socket)
share_path = r"C:\Users\Public"
os.chdir(share_path)
httpd.serve_forever()
