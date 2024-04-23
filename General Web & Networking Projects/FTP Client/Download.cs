using System;
using System.IO;
using System.Net;
using FluentFTP;

namespace DownloadFromServer
{
    public class Download
    {
        private string server;
        private string username;
        private string password;

        public Download(string server, string username, string password)
        {
            this.server = server;
            this.username = username;
            this.password = password;
        }

        public void DownloadTheFile(string localFilePath, string remoteFilePath)
        {
            using (FtpClient client = new FtpClient(server, new NetworkCredential(username, password)))
            {
                client.Connect();

                FtpStatus status = client.DownloadFile(localFilePath, remoteFilePath);

                if (status == FtpStatus.Success)
                {
                    Console.WriteLine("The file was downloaded successfully.");
                }
                else
                {
                    Console.WriteLine("The file could not be downloaded. Status: " + status);
                }

                client.Disconnect();
            }
        }
    }
}
