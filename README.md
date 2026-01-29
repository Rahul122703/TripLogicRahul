"# TripLogicRahul" 

BACKEND
fastapi-backend/
│
├── app/
│   ├── main.py                # Entry point
│
│   ├── core/                   # App-level config
│   │   ├── config.py           # env, settings
│   │   └── security.py         # JWT, hashing, auth logic
│
│   ├── db/
│   │   ├── database.py         # DB connection
│   │   └── models.py           # SQLAlchemy models
│
│   ├── schemas/                # Pydantic schemas
│   │   └── user.py
│
│   ├── routers/                # All routes
│   │   └── user.py
│
│   ├── services/               # Business logic
│   │   └── user_service.py
│
│   └── utils/                  # Helpers
│       └── response.py
│
├── .env
├── requirements.txt
└── run.py
