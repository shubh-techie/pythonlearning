// See https://aka.ms/new-console-template for more information
using ConsoleAppDemo.Array;
Console.WriteLine("Hello, World!");
var arrayDemo = new ArrayDemo();
var indexValude =arrayDemo.IndexOf(new int[] { 1, 2, 3, 4, 5 }, 3);
Console.WriteLine($"Index of 3 is {indexValude}");
Console.ReadLine();
