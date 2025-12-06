using System.Text;

class Program
{
    static long Calculate(List<string> nums, char op)
    {
        List<long> numbers = nums.Select(long.Parse).ToList();

        long value = numbers[0];
        for (int i = 1; i < numbers.Count; i++)
        {
            switch (op)
            {
                case '+':
                    value += numbers[i];
                    break;
                case '*':
                    value *= numbers[i];
                    break;
            }
        }

        return value;
    }
    static void Main(string[] args)
    {
        string[] lines = File.ReadAllLines("input.txt");

        int rows = lines.Length;
        int cols = lines[0].Length;
        long result = 0;

        List<string> currentNumbers = [];
        char currentOperator = ' ';

        for (int col = cols - 1; col >= 0; col--)
        {
            StringBuilder sb = new();
            for (int row = 0; row < rows - 1; row++)
                sb.Append(lines[row][col]);

            string number = sb.ToString();
            char op = lines[rows - 1][col];

            if (string.IsNullOrWhiteSpace(number) && op == ' ')
            {
                if (currentNumbers.Count > 0)
                {
                    result += Calculate(currentNumbers, currentOperator);
                    currentNumbers.Clear();
                }
            }
            else
            {
                if (!string.IsNullOrWhiteSpace(number))
                    if (long.TryParse(number.Trim(), out long parsedNum))
                        currentNumbers.Add(parsedNum.ToString());

                if (op == '+' || op == '*')
                    currentOperator = op;
            }
        }

        if (currentNumbers.Count > 0)
            result += Calculate(currentNumbers, currentOperator);

        System.Console.WriteLine(result);
    }
}