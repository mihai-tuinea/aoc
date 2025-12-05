using System.IO;
class Program
{
    static void Main(string[] args)
    {
        string[] lines = File.ReadAllLines("input.txt");
        List<(long Low, long High)> ranges = [];
        long count = 0;

        foreach (var line in lines)
        {
            string tLine = line.Trim();

            if (string.IsNullOrEmpty(tLine))
                continue;

            string[] parts = tLine.Split("-");

            if (parts.Length == 2)
            {
                long low = long.Parse(parts[0]);
                long high = long.Parse(parts[1]);

                ranges.Add((low, high));
            }
        }

        ranges.Sort((a, b) => a.Low.CompareTo(b.Low));

        long currentL = ranges[0].Low;
        long currentH = ranges[0].High;

        for (int i = 1; i < ranges.Count; i++)
        {
            long nextL = ranges[i].Low;
            long nextH = ranges[i].High;

            if (currentH + 1 >= nextL)
                currentH = Math.Max(currentH, nextH);
            else
            {
                count += currentH - currentL + 1;
                currentL = nextL;
                currentH = nextH;
            }
        }
        count += currentH - currentL + 1;

        System.Console.WriteLine(count);
    }
}