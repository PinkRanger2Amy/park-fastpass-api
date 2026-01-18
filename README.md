# 🎢 Park FastPass API

A modern FastPass management system for theme parks that lets you skip the lines! Built with FastAPI and featuring 21 Disney World attractions.

## ✨ Features

- **🎫 FastPass Management** - Purchase, manage, and check in with digital FastPasses
- **🎢 Ride Database** - 21 authentic Disney World attractions pre-loaded
- **📱 Beautiful Frontend** - Responsive UI with blue and pink rainbow design
- **⚡ Fast API** - Built with FastAPI for high performance
- **💾 SQLAlchemy ORM** - Robust database management
- **🔐 Email Validation** - Visitor authentication via email

## 🏗️ Project Structure

```
park-fastpass-api/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI application
│   │   ├── database.py          # SQLAlchemy setup
│   │   ├── models/              # Database models (Ride, FastPass)
│   │   ├── routes/              # API endpoints
│   │   └── schemas/             # Pydantic schemas
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   └── index.html               # React-like single page app
├── scripts/
│   └── seed_rides.py           # Disney rides seeding script
├── docker-compose.yml
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Virtual Environment

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/park-fastpass-api.git
cd park-fastpass-api
```

2. **Set up virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
cd backend
pip install -r requirements.txt
```

4. **Start the API server**
```bash
python app/main.py
```

The API will be running at `http://localhost:8765`

### 🎨 Access the Frontend

Open `frontend/index.html` in your browser to use the FastPass system.

Or serve it with Python:
```bash
cd frontend
python -m http.server 8080
```

Then visit `http://localhost:8080`

## 📚 API Endpoints

### Rides
- `GET /api/rides` - List all rides
- `GET /api/rides/{ride_id}` - Get ride details
- `POST /api/rides` - Create new ride

### FastPass
- `GET /api/fastpasses` - List all FastPasses
- `POST /api/fastpasses` - Purchase a FastPass
- `GET /api/fastpasses/{fastpass_id}` - Get FastPass details
- `POST /api/fastpasses/{fastpass_id}/checkin` - Check in to ride
- `GET /api/fastpasses/visitor/{email}` - Get visitor's FastPasses
- `PUT /api/fastpasses/{fastpass_id}` - Update FastPass
- `DELETE /api/fastpasses/{fastpass_id}` - Cancel FastPass

## 🎪 Pre-loaded Disney Rides

### Magic Kingdom
- Jungle Cruise, Pirates of the Caribbean
- Big Thunder Mountain Railroad, Splash Mountain
- Space Mountain, Buzz Lightyear Astro Blasters
- Cinderella's Royal Table, It's a Small World
- Haunted Mansion

### EPCOT
- Test Track, Soarin' Around the World
- The Seas with Nemo & Friends, Frozen Ever After

### Hollywood Studios
- Star Wars: Millennium Falcon Smugglers Run
- Tower of Terror, Rock 'n' Roller Coaster
- Toy Story Land - Slinky Dog Dash

### Animal Kingdom
- Expedition Everest, Kilimanjaro Safaris
- Avatar Flight of Passage, Kali River Rapids

## 🗄️ Database

The system uses SQLite by default (easily switchable to PostgreSQL, MySQL, etc.)

### Models
- **Ride** - Park attractions with queue times and details
- **FastPass** - Digital passes for skip-the-line access

## 🌈 Frontend Features

- **Browse Rides** - View all attractions with queue times
- **Purchase FastPass** - Buy passes with tier selection (Standard/Express/Premium)
- **My FastPass** - Manage your purchased passes
- **Check In** - Use FastPass to skip lines

## 🛠️ Tech Stack

- **Backend**: FastAPI, SQLAlchemy, Uvicorn, Pydantic
- **Database**: SQLite (configurable)
- **Frontend**: Vanilla JavaScript, CSS3
- **Deployment Ready**: Docker & Docker Compose included

## 📦 Requirements

See `backend/requirements.txt`:
- fastapi==0.115.12
- uvicorn==0.34.0
- sqlalchemy==2.0.23
- pydantic==2.11.1
- email-validator
- python-dotenv

## 🐳 Docker

Build and run with Docker:
```bash
docker-compose up --build
```

## 🔧 Configuration

Create a `.env` file for environment variables:
```
DATABASE_URL=sqlite:///./tickets.db
API_HOST=0.0.0.0
API_PORT=8765
```

## 📝 Seed Database

Populate with Disney rides:
```bash
python scripts/seed_rides.py
```

## 🤝 Contributing

Feel free to fork, modify, and submit pull requests!

## 📄 License

MIT License - See LICENSE file for details

## 👨‍💻 Author

Park FastPass Developer - 2026

## 🎉 Enjoy!

Skip the lines and experience more rides with Park FastPass! 🎢✨

---

**Questions?** Check the API docs at `http://localhost:8765/docs`
