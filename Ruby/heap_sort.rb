def heap_sort(array)
  n = array.length - 1
  a = array

  (n / 2).downto(0) do |i|
    create_max_heap(a, i, n)
  end

  while n.positive?
    a[0], a[n] = a[n], a[0]
    n -= 1
    create_max_heap(a, 0, n)
  end
  a
end

def create_max_heap(array, parent, limit)
  root = array[parent]
  while (child = 2 * parent) <= limit
    child += 1 if child < limit && array[child] < array[child + 1]
    break if root >= array[child]

    array[parent] = array[child]
    parent = child
  end
  array[parent] = root
end
