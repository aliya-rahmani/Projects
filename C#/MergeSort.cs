using System;
using System.Collections.Generic;
using System.Linq;

class MergeSort
{
    static void Main(string[] args)
    {
        // Based on the algorithm found here
        // https://www.tutorialspoint.com/data_structures_algorithms/merge_sort_algorithm.htm
        IList<int> elements = new List<int>();
        Console.WriteLine($"Enter array members:");
        int i = 1;
        while (true)
        {
            Console.Write($"Enter integer element {i}, anything else to sort:");
            string unparsedElement = Console.ReadLine();
            bool parsePass = int.TryParse(unparsedElement, out int element);
            if (parsePass)
            {
                elements.Add(element);
                i++;
            }
            else
            {
                break;
            }
        }

        Console.WriteLine("elements in array ");
        Printarray(elements);
        IList<int> sortedElements = Sort(elements);
        Console.WriteLine("elements after sorting");
        Printarray(sortedElements);

    }

    private static IList<int> Sort(IList<int> elements)
    {
        if (elements.Count == 1)
        {
            return elements;
        }

        IList<int> elementsLeftHalf = elements.Take(elements.Count / 2).ToList();
        IList<int> elementsRightHalf = elements.Skip(elements.Count / 2).ToList();
        IList<int> sortedLeftHalf = Sort(elementsLeftHalf);
        IList<int> sortedRightHalf = Sort(elementsRightHalf);
        return Merge(sortedLeftHalf, sortedRightHalf);
    }

    private static IList<int> Merge(IList<int> sortedLeftHalf, IList<int> sortedRightHalf)
    {
        IList<int> mergedSortedElements = new List<int>();
        while (sortedLeftHalf.Any() && sortedRightHalf.Any())
        {
            if (sortedLeftHalf[0] > sortedRightHalf[0])
            {
                mergedSortedElements.Add(sortedRightHalf[0]);
                sortedRightHalf.RemoveAt(0);
            }
            else
            {
                mergedSortedElements.Add(sortedLeftHalf[0]);
                sortedLeftHalf.RemoveAt(0);
            }
        }

        while (sortedLeftHalf.Any())
        {
            mergedSortedElements.Add(sortedLeftHalf[0]);
            sortedLeftHalf.RemoveAt(0);
        }

        while (sortedRightHalf.Any())
        {
            mergedSortedElements.Add(sortedRightHalf[0]);
            sortedRightHalf.RemoveAt(0);
        }

        return mergedSortedElements;

    }

    private static void Printarray(IList<int> elements)
    {
        foreach (var element in elements)
        {
            Console.Write($"{element},");
        }
        Console.WriteLine();
    }
}
