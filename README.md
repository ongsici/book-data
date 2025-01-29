## Book Data Server

FastAPI was used to serve this book server. Data on books is stored in `books.json`. This server interacts with a [client service](https://github.com/ongsici/book-client) that allows users to search for books by genre or title.

### Deploy
The Docker image for this client service is [here](https://github.com/users/ongsici/packages/container/package/book-data).

### Local Installation
```
conda create -n book-data python=3.10 -y
conda activate book-data

chmod +x docker_build.sh
./docker_build.sh

docker run -it -p 8000:8000 book-data
```
