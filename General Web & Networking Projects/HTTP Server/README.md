# HTTP Server

To understand HTTP better, you need to build an HTTP server. It's not much difficult now a days (with the wealth of information around us).

<b>Suggested Language</b>: Python (or any other language you want to master)  
<b>Suggested Frameworks/Tools</b>>: socket (Python Library)  
<b>Example Implementation</b>: Blog Post by Ruslan  

 --------------------------------------------------------------------------------------------------------------------------------

## Explaination of the code

I've created a simple web server that is hosted on localhost which is 127.0.0.1 and on port number of 8888 ( which can be changed according to the need of the user). The server accepts requests from clients and then sends a response.

You can run the file in a normal python IDE or using linux (which I prefer). If you want to run using linux, do use the command 'python3 HTTPserver.py' (without the quotes) which will keep ther server up and running. If you want to see your server, you can either just open a webbrowser and type in the url "http://127.0.0.1:8888/hell0" or "http://localhost:8888/hello" or you can use linux (again, which I prefer). If you want to use linux, use the command "curl -v http://localhost:8888/hello".

PS: When running the python file through linux, make sure you are in the right directory as the python file.