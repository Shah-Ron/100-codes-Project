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

    public void EncryptJsonFile(string inputFilePath, string outputFilePath)
    {
        // Read JSON data from input file
        string jsonData = File.ReadAllText(inputFilePath);

        // Encrypt JSON data
        byte[] encryptedData = EncryptStringToBytes(jsonData);

        // Write encrypted data to output file
        File.WriteAllBytes(outputFilePath, encryptedData);

        Console.WriteLine($"JSON file encrypted and saved to {outputFilePath}");
    }

    private byte[] EncryptStringToBytes(string plainText)
    {
        using (Aes aesAlg = Aes.Create())
        {
            aesAlg.Key = key;
            aesAlg.IV = iv;

            ICryptoTransform encryptor = aesAlg.CreateEncryptor(aesAlg.Key, aesAlg.IV);

            using (MemoryStream msEncrypt = new MemoryStream())
            {
                using (CryptoStream csEncrypt = new CryptoStream(msEncrypt, encryptor, CryptoStreamMode.Write))
                {
                    using (StreamWriter swEncrypt = new StreamWriter(csEncrypt))
                    {
                        swEncrypt.Write(plainText);
                    }
                    return msEncrypt.ToArray();
                }
            }
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        // Read key and IV from JSON file
        string path = @"C:\Users\shahr\OneDrive\Desktop\Self Study\100 codes project\100-codes-Project\Encrypt-Decrypt\Key-IV\key_and_iv.json";
        byte[] key = ReadKeyFromJson(path, "Key");
        byte[] iv = ReadKeyFromJson(path, "IV");

        // Initialize encryption helper
        EncryptionHelper encryptionHelper = new EncryptionHelper(key, iv);

        // Encrypt JSON file
        encryptionHelper.EncryptJsonFile("inputs.json", "encryptedinputs.json");
    }

    static byte[] ReadKeyFromJson(string jsonFilePath, string keyName)
    {
        string json = File.ReadAllText(jsonFilePath);
        dynamic jsonObj = JsonConvert.DeserializeObject(json);
        string base64EncodedKey = jsonObj[keyName];
        return Convert.FromBase64String(base64EncodedKey);
    }
}
