namespace ConsoleAppDemo.Array;
public class ArrayDemo
{
    public ArrayDemo()
    {
        Console.WriteLine("Array Demo");
    }

    public int IndexOf(int[] array, int value)
    {
        for (int i = 0; i < array.Length; i++)
        {
            if (array[i] == value)
            {
                return i;
            }
        }
        return -1;
    }

    public  List<int> GetEvens(int[] array)
    {
        List<int> events = new List<int>();
        for (int i = 0; i < array.Length; i++)
        {
            if (array[i] % 2 == 0)
            {
                events.Add(array[i]);
            }
        }
        return events;
    }

    List<int> RemoveDuplicete(int[] arr)
    {
        List<int> result = new List<int>();
        for (int i = 0; i < arr.Length; i++)
        {
            if (!result.Contains(arr[i]))
            {
                result.Add(arr[i]);
            }
        }
        return result;

    }
}