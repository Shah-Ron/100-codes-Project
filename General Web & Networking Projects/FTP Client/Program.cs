using System;
using System.IO;
using UploadToServer;
using ViewInServer;
using DownloadFromServer;
using DecryptJSON;
using Newtonsoft.Json;

class Program
{
    static void Main(string[] args)
    {
        // Decryption path of encrypted JSON File
        string keyIVPath = /*Provide the path*/;
        string encryptedInputPath = /*Provide the path*/;

        // Read key and IV from JSON file
        byte[] key = ReadKeyFromJson(keyIVPath, "Key");
        byte[] iv = ReadKeyFromJson(keyIVPath, "IV");

        // Initialise and call decryption code
        DecryptionHelper decrypt = new DecryptionHelper(key, iv);
        decrypt.DecryptJsonFile(encryptedInputPath, "decrypted.json");


        // Read FTP server details from JSON file
        string jsonFilePath = "decrypted.json";
        string server = ReadFromJson(jsonFilePath, "ftpServer");
        string username = ReadFromJson(jsonFilePath, "userName");
        string password = ReadFromJson(jsonFilePath, "password");

        // Initialize all the classes
        Upload upload = new Upload(server, username, password);
        View view = new View(server, username, password);
        Download download = new Download(server, username, password);

        // Upload Filepaths
        string uploadLocalFilePath = /*Provide the path*/;
        string uploadRemoteFilePath = /*Provide the path*/;

        // Download Filepaths
        string downloadLocalFilePath = /*Provide the path*/; 

        // Create a small interface
        Console.WriteLine($"Hey there {username}");
        Console.WriteLine("Let's begin the File Transfer Program");

        
        string answer = "N";

        do{
            Console.WriteLine("\n\n-------------------------------------------------------------------------------------\n\n");
            Console.WriteLine("1. Upload File to the Server");
            Console.WriteLine("2. View the files in the Server");
            Console.WriteLine("3. Download File from the Server");
            Console.WriteLine("4. Exit");

            int option = int.Parse(Console.ReadLine());

            if(option == 1){
            upload.UploadTheFile(uploadLocalFilePath, uploadRemoteFilePath);
            }
            else if(option == 2){
                Console.WriteLine("\nEnter Directory\n(Press enter for home directory)");
                string viewRemoteFilePath = Console.ReadLine();
                view.ViewTheDirectory(viewRemoteFilePath);
            }
            else if(option == 3){
                Console.WriteLine("\nEnter File Path with the file name");
                string downloadRemoteFilePath = Console.ReadLine();
                download.DownloadTheFile(downloadLocalFilePath,downloadRemoteFilePath);
            }
            else if(option == 4){
                break;
            }
            while(true){
                Console.WriteLine("\nDo you wish to exit (Y/N)");
                answer = Console.ReadLine();

                if(answer.ToUpper() == "Y")
                {
                    break;
                }
                else if(answer.ToUpper() == "N")
                {
                    break;
                }
                else{
                    Console.WriteLine("Please provide a proper response as given in the options");
                    continue;
                }
            }
        } while(answer.ToUpper() != "Y");

        File.Delete("decrypted.json");

        
    }

    static string ReadFromJson(string jsonFilePath, string propertyName)
    {
        string json = File.ReadAllText(jsonFilePath);
        dynamic jsonObj = Newtonsoft.Json.JsonConvert.DeserializeObject(json);
        return jsonObj[propertyName];
    }
    static byte[] ReadKeyFromJson(string jsonFilePath, string keyName)
    {
        string json = File.ReadAllText(jsonFilePath);
        dynamic jsonObj = JsonConvert.DeserializeObject(json);
        string base64EncodedKey = jsonObj[keyName];
        return Convert.FromBase64String(base64EncodedKey);
    }
}
