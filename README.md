# Tennis Court API Server

Tennis kort rezervatsiya tizimi uchun API server. Vercel serverless platform'ida ishlaydi.

## API Endpoints

### Health Check
- **GET** `/` - Asosiy health check
- **GET** `/health` - Health check
- **GET** `/api/health` - API health check

### Ticket Operations
- **POST** `/api/check-ticket` - Ticket ni tekshirish
- **POST** `/api/consume-ticket` - Ticket ni ishlatish

## Deployment

### Vercel ga deploy qilish: sdwsqawdqd

1. Vercel CLI o'rnatish:
```bash
npm i -g vercel
```

2. Login qilish:
```bash
vercel login
```

3. Deploy qilish:
```bash
vercel --prod
```

### Environment Variables

Vercel dashboard'da quyidagi environment variable'larni sozlang:

- `DATABASE_URL` - PostgreSQL database connection string

## Local Development

1. Dependencies o'rnatish:
```bash
pip install -r requirements.txt
```

2. Environment variables sozlash:
```bash
export DATABASE_URL="postgresql://username:password@host:port/database"
```

3. Local server ishga tushirish:
```bash
vercel dev
```

## API Usage

### Ticket tekshirish:
```bash
curl -X POST https://your-domain.vercel.app/api/check-ticket \
  -H "Content-Type: application/json" \
  -d '{"ticket_id": "your-ticket-id"}'
```

### Ticket ishlatish:
```bash
curl -X POST https://your-domain.vercel.app/api/consume-ticket \
  -H "Content-Type: application/json" \
  -d '{"ticket_id": "your-ticket-id"}'
```

## Features

- ✅ Serverless architecture
- ✅ PostgreSQL database integration  
- ✅ CORS support
- ✅ Uzbekistan timezone support
- ✅ Error handling
- ✅ Health monitoring

## Tech Stack

- **Runtime**: Python 3.9
- **Platform**: Vercel Serverless Functions
- **Database**: PostgreSQL
- **Libraries**: psycopg2, pytz

## Project Structure

```
api-server-vercel/
├── api/
│   ├── check-ticket.py   # Ticket validation endpoint
│   ├── consume-ticket.py # Ticket consumption endpoint
│   └── health.py         # Health check endpoint
├── vercel.json           # Vercel configuration
├── requirements.txt      # Python dependencies
├── package.json          # Node.js configuration
└── README.md            # This file
```