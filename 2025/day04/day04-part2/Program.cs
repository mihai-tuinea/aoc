using System;
using System.Collections.Generic;
using System.IO;

class Program
{
    static void Main()
    {
        string[] matrix = File.ReadAllLines("input.txt"); // string 1d array can act as 2d matrix
        int rows = matrix.Length;
        int cols = matrix[0].Length;

        HashSet<(int, int)> rolls = [];
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                if (matrix[i][j] == '@')
                {
                    rolls.Add((i, j));
                }
            }
        }

        // array of ValueTuple
        (int, int)[] directions =
        [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1)
        ];

        long result = 0;

        while (true)
        {
            List<(int, int)> occupied = [];

            foreach (var (i, j) in rolls)
            {
                int count = 0;

                foreach (var (x, y) in directions)
                {
                    int temp_i = i + x;
                    int temp_j = j + y;

                    if ((temp_i >= 0 && temp_i < rows) && (temp_j >= 0 && temp_j < cols))
                    {
                        if (rolls.Contains((temp_i, temp_j)))
                        {
                            count++;
                        }
                    }

                    if (count >= 4)
                    {
                        break;
                    }
                }

                if (count < 4)
                {
                    result++;
                    occupied.Add((i, j));
                }
            }

            if (occupied.Count == 0)
            {
                break;
            }

            foreach (var item in occupied)
            {
                rolls.Remove(item);
            }
        }

        Console.WriteLine(result);
    }
}