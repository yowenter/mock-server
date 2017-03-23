# mock-server
Mock API Server using flask



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



## Let's Mock Data 


-  Edit `routes.cfg` 

 	like
  
 	```
		[routes]
		/ping = ping.json
		/users/<user_id> = example_user.json

 	```
 
 	the first param is the API path , and the second  is mocked json file path  .     

- Put your mock json data  in `json_files` directory.


- Enjoy it 




## Todo List

- Integrating with sphinx 
- Add logger


 
 
 
 
