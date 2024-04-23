using System;
using System.IO;
using System.Net;
using FluentFTP;

namespace ViewInServer
{
    public class View
    {
        private string server;
        private string username;
        private string password;

        public View(string server, string username, string password)
        {
            this.server = server;
            this.username = username;
            this.password = password;
        }

        public void ViewTheDirectory(string remoteDirectoryPath)
        {
            using (FtpClient client = new FtpClient(server, new NetworkCredential(username, password)))
            {
                client.Connect();

                foreach (FtpListItem item in client.GetListing(remoteDirectoryPath))
                {
                    Console. WriteLine("=====================================");
                    Console.WriteLine("Name: {0}, \nSize: {1}, \nModified: {2}, \nType: {3}", 
                        item.Name, 
                        item.Size, 
                        item.Modified, 
                        item.Type);
                }

                client.Disconnect();
            }
        }
    }
}