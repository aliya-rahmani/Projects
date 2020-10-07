//Example declaration in the main function should be let mut v = vec!(..,..,..); 
//and then function call --> insertion_sort(&mut v);

pub fn insertion_sort(arr: &mut Vec<isize>) {
    for i in 1..arr.len() {
        let mut j = i;
        while j > 0 && arr[j - 1] > arr[j] {
            arr.swap(j - 1, j);
            j -= 1;
        }
    }
}