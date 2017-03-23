# Mock Server for poor man 

Mock API Server Using Flask



## How to Deploy ?

Of course use Docker  `> docker-compose -f example.yml up -d `



## Integrate with Nginx


To integrate with nginx, you can add an upstream in nginx.conf . 
The client can add  header  `X-Server-Select`, the nginx will map to mock_server .
 

```

upstream mock_api {

    server 192.168.1.11:5001;
    
}


upstream api {

    server 192.168.1.11:5000;
    
}



map $http_x_server_select $api_pool {

     default "api";
     mock "mock_api";
}



server {

    listen 80 ;
    server_name _;
    location / {
        proxy_pass http://api_pool;
    }
}


```  



## Let's Mock Data !


-  Edit `_static/routes.cfg` 

 	like
  
 	```
		[routes]
		/ping = json_files/ping.json
		/users/<user_id> = json_files/example_user.json

 	```
 	
 	the first param is the API path , and the second  is mocked json file path  .     

- Put your mock json data  in `_static` directory.


- Enjoy it 




## Todo List

- Integrating with sphinx 
- Add logger


 
 
 
 
