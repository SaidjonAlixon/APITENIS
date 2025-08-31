from http.server import BaseHTTPRequestHandler
import json
import os
import psycopg2
from datetime import datetime
import pytz

# Timezone
UZBEKISTAN_TZ = pytz.timezone('Asia/Tashkent')

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # CORS headers
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            
            # Database connection test
            database_url = os.environ.get('DATABASE_URL')
            db_status = 'disconnected'
            
            if database_url:
                try:
                    conn = psycopg2.connect(database_url)
                    cursor = conn.cursor()
                    cursor.execute('SELECT 1')
                    cursor.fetchone()
                    cursor.close()
                    conn.close()
                    db_status = 'connected'
                except:
                    db_status = 'error'
            
            current_time = datetime.now(UZBEKISTAN_TZ)
            
            response = {
                'status': 'healthy',
                'timestamp': current_time.isoformat(),
                'service': 'tennis-api-server',
                'database': db_status,
                'timezone': 'Asia/Tashkent',
                'version': '1.0.0'
            }
            
            self.wfile.write(json.dumps(response).encode('utf-8'))
            
        except Exception as e:
            self.send_response(503)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {
                'status': 'unhealthy',
                'error': str(e),
                'timestamp': datetime.now(UZBEKISTAN_TZ).isoformat(),
                'service': 'tennis-api-server'
            }
            self.wfile.write(json.dumps(response).encode('utf-8'))
    
    def do_OPTIONS(self):
        # CORS preflight
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
