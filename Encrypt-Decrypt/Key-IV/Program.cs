using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Generating Key and IV...");
        KeyIVGenerator.GenerateKeyAndIV();
        Console.WriteLine("Key and IV generation complete.");
    }
}
