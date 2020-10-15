def insertion_sort(array)
  array.length.times do |j|
    while j.positive?
      break unless array[j - 1] > array[j]

      array[j], array[j - 1] = array[j - 1], array[j]
      j -= 1
    end
  end
  array
end
