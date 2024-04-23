using System;
using System.IO;
using System.Security.Cryptography;
using Newtonsoft.Json;

public class KeyIVGenerator
{
    public static void GenerateKeyAndIV()
    {
        // Generate a 256-bit (32-byte) key
        byte[] key = GenerateRandomBytes(32);

        // Generate a 128-bit (16-byte) IV
        byte[] iv = GenerateRandomBytes(16);

        // Create a data structure to hold key and IV
        KeyAndIV data = new KeyAndIV
        {
            Key = key,
            IV = iv
        };

        // Serialize the data to JSON
        string json = JsonConvert.SerializeObject(data);

        // Write JSON to file
        File.WriteAllText("key_and_iv.json", json);

        Console.WriteLine("Generated Key and IV written to key_and_iv.json");
    }

    static byte[] GenerateRandomBytes(int length)
    {
        byte[] randomBytes = new byte[length];
        using (RandomNumberGenerator rng = RandomNumberGenerator.Create())
        {
            rng.GetBytes(randomBytes);
        }
        return randomBytes;
    }
}

public class KeyAndIV
{
    public byte[] Key {get; set; }
    public byte[] IV {get; set; }
}
