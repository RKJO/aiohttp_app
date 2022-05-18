# aiohttp_app

## Usage:

1. Clone repository
2. run comand:

```bash
docker compose up --build
```

3. to create table in database run this command in aiohttp_server container
```bash
python init_db.py
```

## API endpoints

### GET
`get user` http://localhost:8080/get_user/{id}

### POST
`create user` http://localhost:8080/create_user?user_name={username}

