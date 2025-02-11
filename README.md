# Project


### 1. Run MongoDB Container
Start a MongoDB container using Podman:
```bash
podman run -d --name mongodb -p 27017:27017 docker.io/library/mongo:4.4
```

### 2. Interact mongodb
directly access db 
```bash
podman exec -it mongodb /bin/bash
# mongo
       > use file_logs
       > db.deleted_files.find().pretty()
```

### 3. venv
activate virtual enviroment ( in Linux )

```bash
source venv/bin/activate
```

### 4. Install python modules

```bash
pip3 install -r requirements.txt
```


### 5. Run FastAPI
```bash
uvicorn main:app --reload
```

### 6. Swagger UI

```bash
http://127.0.0.1:8000/docs
```

---