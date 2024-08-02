
# URL rules for adjust documents on Mongodb:

```
    <!-- get all words -->
    (GET) http://localhost:3000 

    <!-- get word by ID -->
    (GET) http://localhost:3000/:id
    
    <!-- create word -->
    (POST) http://localhost:3000/

    <!-- update word by ID -->
    (PUT) http://localhost:3000/:id

    <!-- delete word by ID -->
    (DELETE) http://localhost:3000/:id
```

## Deploy local server:

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
