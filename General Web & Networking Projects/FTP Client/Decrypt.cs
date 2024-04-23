using System;
using System.IO;
using System.Security.Cryptography;
using Newtonsoft.Json;

namespace DecryptJSON{
    public class DecryptionHelper
    {
        private byte[] key;
        private byte[] iv;

        public DecryptionHelper(byte[] key, byte[] iv)
        {
            this.key = key;
            this.iv = iv;
        }

        public void DecryptJsonFile(string inputFilePath, string outputFilePath)
        {
            // Read encrypted data from input file
            byte[] encryptedData = File.ReadAllBytes(inputFilePath);

            // Decrypt data
            string decryptedData = DecryptBytesToString(encryptedData);

            // Write decrypted data to output file
            File.WriteAllText(outputFilePath, decryptedData);

            Console.WriteLine($"Encrypted JSON file decrypted and saved to {outputFilePath}");
        }

        private string DecryptBytesToString(byte[] cipherText)
        {
            using (Aes aesAlg = Aes.Create())
            {
                aesAlg.Key = key;
                aesAlg.IV = iv;

                ICryptoTransform decryptor = aesAlg.CreateDecryptor(aesAlg.Key, aesAlg.IV);

                using (MemoryStream msDecrypt = new MemoryStream(cipherText))
                {
                    using (CryptoStream csDecrypt = new CryptoStream(msDecrypt, decryptor, CryptoStreamMode.Read))
                    {
                        using (StreamReader srDecrypt = new StreamReader(csDecrypt))
                        {
                            return srDecrypt.ReadToEnd();
                        }
                    }
                }
            }
        }
    }
}
