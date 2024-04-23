# FTP Client
A simple File Transfer client that uses the FTP (File Transfer Protocol). As a bonus challenge, add support for secure file transfer. It can be a web, desktop, or CLI app.
You can try to first implement TFTP (Trivial File Transfer Protocol) as it's easier.

<b>Suggested Language</b>: C/C++  
<b>Suggested Frameworks/Tools</b>: Use Wireshark to observe packets and debug them  
<b>Example Implementation</b>: Filezilla is extremely complete, here is a simple Go implementation

---------------------------------------------------------------------------------------------------------------------------------

## Explaination of the code

I have done a wide variety of stuff just for this code, even though this was supposed to be a simple File Transfer Client Program. I wanted to add several more features into it so that the program will eventually be good for multiple tasks.

Here you can see three different cs files. Each of it representing one function. Upload, View and Download. You can also see a cs file named Decrypt.cs; The intention was to make the data a bit more secure as we need to provide the server address, username and password in a JSON format which is pretty exposed and easily acquirable. So I made an encrypted JSON file which contains all the details regarding the server in an encrypted format. The program is set up in such a way that it will decrypt the JSON file in the beginning of the program and then deleted at the end of the program. 

I still don't think this is a secure method, But I do know how to make it way more secure by decrypting just before and deleting just after the process of uploading, viewing or downloading. I also think I can add more feautres into the Program like deleting the file from the server. 

For the process of making a encryption and decryption, I first created programs just for that which are provided in the Folder Encrypt-Decrypt along with the code for generating a Key-IV. and then created a unique Key-IV for myself and then encrypted the data, which was transfered to the directory.

<b>I will be deleting the filepaths, JSON files which contains my details for the server and Key-IV which I creatd myself for the program. So if you want to try out this program, make sure you have your encrypted JSON file containing the server name, username and password. Also make sure you provide the respective paths you want to provide as well.</b>

Note:- If you are unsure how to encrypt or create a Key-IV pair, just go to the folder "Encrypt-Decrypt" in the directory "100-codes-Project"