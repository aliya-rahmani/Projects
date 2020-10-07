//Example declaration in the main function should be let mut v = [..,..,..]; 
//and then function call --> selection_sort(&mut v);

fn selection_sort(array: &mut [i32]) {
    let mut min;
    for i in 0..array.len() {
        min = i;
        for j in (i+1)..array.len() {
            if array[j] < array[min] {
                min = j;
            }
        }
        let tmp = array[i];
        array[i] = array[min];
        array[min] = tmp;
    }
}

