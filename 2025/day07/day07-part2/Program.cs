using System;
using System.IO;
using System.Linq;

class Program
{
    static void Main()
    {
        using StreamReader reader = new("input.txt");
        string? firstLine = reader.ReadLine();

        firstLine = firstLine!.Trim();
        int width = firstLine.Length;

        long[] beams = new long[width];
        long[] nextBeams = new long[width];

        for (int i = 0; i < width; i++)
        {
            if (firstLine[i] == 'S')
            {
                beams[i] = 1;
                break;
            }
        }

        string? line;
        while ((line = reader.ReadLine()) != null)
        {
            line = line.Trim();
            Array.Clear(nextBeams, 0, width);

            for (int i = 0; i < width; i++)
            {
                long count = beams[i];

                if (line[i] == '^')
                {
                    if (i > 0)
                        nextBeams[i - 1] += count;
                    if (i < width - 1)
                        nextBeams[i + 1] += count;
                }
                else
                    nextBeams[i] += count;
            }
            (nextBeams, beams) = (beams, nextBeams);
        }

        long result = 0;
        foreach (var count in beams)
            result += count;

        Console.WriteLine(result);
    }
}