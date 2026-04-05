# Dosya adı: api/index.py
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # URL'deki parametreleri ayrıştırıyoruz
        query_components = parse_qs(urlparse(self.path).query)
        
        # 'api' ve 'cikarilacak' parametrelerini alıyoruz
        # Eğer parametre yoksa boş string döner
        mesaj = query_components.get("api", [""])[0]
        cikarilacak = query_components.get("cikarilacak", [""])[0]
        
        # Temizleme işlemi: mesajın içinden cikarilacak kısmını siliyoruz
        sonuc = mesaj.replace(cikarilacak, "").strip()
        
        # JSON Yanıtı hazırlama
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        yanit = {
            "orijinal": mesaj,
            "cikarilan_kisim": cikarilacak,
            "sonuc": sonuc
        }
        
        self.wfile.write(json.dumps(yanit).encode('utf-8'))
        return
        