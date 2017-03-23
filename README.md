# mock-server
Mock API Server using flask


##How to Deploy ?

Use Docker	`> docker-compose -f example.yml up -d `


## Config


-  Edit `routes.cfg` 

 like
  
 ```
	[routes]
	/ping = ping.json
	/users/<user_id> = example_user.json

 ```
 
 The first param is the API path , and the target is mocked json .     

- Put your mock json data  in `json_files` directory.


- Enjoy it 



## Todo List

- Integrating with sphinx 
- Add logger


 
 
 
 