
# URL rules for adjust documents on Mongodb:

```
    <!-- get all words -->
    (GET) http://localhost:3000 

    <!-- get word by ID -->
    (GET) http://localhost:3000/:id

    <!-- get word -->
    (GET) http://localhost:3000/word/:wordfind
    
    <!-- create word -->
    (POST) http://localhost:3000/

    <!-- update word by ID -->
    (PUT) http://localhost:3000/:id

    <!-- delete word by ID -->
    (DELETE) http://localhost:3000/:id
```

## Deploy local server:

Create `.env` file on highest level folder:
```
<!-- Past this on your .env file -->
DATABASE_URL=<your url dababase>

```

Example:
```
DATABASE_URL=mongodb://127.0.0.1:9191/Datasys
```

Connect directly to dtb follow commands below: 
```
zrok enable utz8rO7v1kIw
zrok access private 47bmlngw8uuj
```

run server by

```
npm i <!-- install pacakages  -->
npm run api <!-- run server -->
```

`If u need support pls contact HUY`
`* need update .env and token for policy rule `
