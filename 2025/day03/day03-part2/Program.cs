using System;
using System.IO;
using System.Collections.Generic;

namespace Day03;

class Program
{
    static long Highest(string line, int k = 12)
    {
        int toDelete = line.Length - k;
        LinkedList<char> resultDigits = new();

        foreach (char digit in line)
        {
            while (resultDigits.Count > 0 && resultDigits.Last!.Value < digit && toDelete > 0)
            {
                resultDigits.RemoveLast();
                toDelete--;
            }
            resultDigits.AddLast(digit);
        }

        while (toDelete > 0)
        {
            resultDigits.RemoveLast();
            toDelete--;
        }

        string highest = string.Concat(resultDigits);
        return long.Parse(highest);
    }

    static void Main(string[] args)
    {
        long result = 0;

        foreach (string line in File.ReadLines("input.txt"))
        {
            result += Highest(line, 12);
        }

        System.Console.WriteLine(result);
    }
}