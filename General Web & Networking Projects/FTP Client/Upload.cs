using System;
using System.IO;
using System.Net;
using FluentFTP;

namespace UploadToServer
{
    public class Upload
    {
        private string server;
        private string username;
        private string password;

        public Upload(string server, string username, string password)
        {
            this.server = server;
            this.username = username;
            this.password = password;
        }

        public void UploadTheFile(string localFilePath, string remoteFilePath)
        {
            using (FtpClient client = new FtpClient(server, new NetworkCredential(username, password)))
            {
                client.Connect();

                FtpStatus status = client.UploadFile(localFilePath, remoteFilePath, FtpRemoteExists.Overwrite);

                if (status == FtpStatus.Success)
                {
                    Console.WriteLine("The file was uploaded successfully.");
                }
                else
                {
                    Console.WriteLine("The file could not be uploaded. Status: " + status);
                }

                client.Disconnect();
            }
        }
    }
}
