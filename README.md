# mock-server
Mock API Server using flask



## How to Deploy ?

Of course use Docker   
` >> docker-compose -f example.yml up -d `


## Integrate with Nginx
  
The client can add  header  `X-Server-Select`, the nginx will map to mock_server .
You can find an example  `nginx.conf`  in the project root directory.
 

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



## How to  mock data ?


-  Edit `routes.cfg` 
  
 	```
		[api]
		prefix = /api
		
		
		[routes]
		/ping = json_files/ping.json
		/users/<user_id> = json_files/example_user.json
 	```
 
 	the first param is the API path , and the second  is mocked json file path  .     

- Put your mock json data  in `_static` directory.  
	
You'd better add  a volume like `example.yml` if you're using docker .






## Todo List

- Integrating with sphinx.http.domain
- 

## Demands

 - Mock API Forward to Real API server 
 - Import config  from sphinx docs
 - GUI
 - API Test workflow


 
 
 
 
