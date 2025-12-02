using System;
using System.IO;

namespace Day02;

class Program
{
    static void Main(string[] args)
    {
        string[] ranges = File.ReadAllText("input.txt").Split(",");

        long result = 0;

        foreach (string segment in ranges)
        {
            string[] parts = segment.Split("-");
            long first = long.Parse(parts[0]);
            long last = long.Parse(parts[1]);

            for (long i = first; i <= last; i++)
            {
                if (IsRepeatedPattern(i.ToString()))
                {
                    result += i;
                }
            }
        }

        System.Console.WriteLine(result);
    }
    static bool IsInvalid(long n)
    {
        string s = n.ToString();
        return s.Length % 2 == 0 &&
            s.Substring(0, s.Length / 2) == s.Substring(s.Length / 2);
    }
    static bool IsRepeatedPattern(string s)
    {
        int n = s.Length;
        for (int size = 1; size <= n / 2; size++)
        {
            if (n % size == 0)
            {
                string substr = s.Substring(0, size);
                int repeatCount = n / size;

                System.Text.StringBuilder sb = new System.Text.StringBuilder(n);
                for (int r = 0; r < repeatCount; r++)
                {
                    sb.Append(substr);
                }
                if (sb.ToString() == s)
                {
                    return true;
                }
            }
        }
        return false;
    }
}
