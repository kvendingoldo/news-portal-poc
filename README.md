# news-portal-poc


    docker run -d \
               --name portal-db \
               --restart=always \
               -e MYSQL_DATABASE=website \
               -e MYSQL_USER=kvendingoldo \
               -e MYSQL_PASSWORD="q7W#t&d)CYxt8dK$" \
               -e MYSQL_ROOT_PASSWORD="q7W#t&d)CYxt8dK$" \
               -p 3306:3306 \
               mysql:latest \
               --character-set-server=utf8mb4 \
               --collation-server=utf8mb4_unicode_ci
