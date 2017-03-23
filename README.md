# mock-server
Mock API Server using flask



## How to Deploy ?

Of course use Docker  `> docker-compose -f example.yml up -d `


## Config


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


 
 
 
 
