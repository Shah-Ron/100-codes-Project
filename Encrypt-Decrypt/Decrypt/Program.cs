using System;
using System.IO;
using System.Security.Cryptography;
using Newtonsoft.Json;

public class EncryptionHelper
{
    private byte[] key;
    private byte[] iv;

    public EncryptionHelper(byte[] key, byte[] iv)
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

class Program
{
    static void Main(string[] args)
    {
        // Initialising Paths
        string keyIVPath = /*Provide the path*/;
        string encryptedInputPath = /*Provide the path*/;
        
        // Read key and IV from JSON file
        byte[] key = ReadKeyFromJson(keyIVPath, "Key");
        byte[] iv = ReadKeyFromJson(keyIVPath, "IV");

        // Initialize encryption helper
        EncryptionHelper encryptionHelper = new EncryptionHelper(key, iv);

        // Decrypt encrypted JSON file
        encryptionHelper.DecryptJsonFile(encryptedInputPath, "decrypted.json");
    }

    static byte[] ReadKeyFromJson(string jsonFilePath, string keyName)
    {
        string json = File.ReadAllText(jsonFilePath);
        dynamic jsonObj = JsonConvert.DeserializeObject(json);
        string base64EncodedKey = jsonObj[keyName];
        return Convert.FromBase64String(base64EncodedKey);
    }
}
