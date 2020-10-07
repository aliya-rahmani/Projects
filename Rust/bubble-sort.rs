fn bubble_sort(mut vec: Vec<i32>) -> Vec<i32> {
    loop {
        let mut swapped = false;
        let mut i = 0;
        while i < vec.len() {
            if i >= vec.len()-1 { break; }
            if vec[i] > vec[i+1] {
                swapped = true;
                let value = vec[i];
                vec.remove(i);
                vec.insert(i+1, value);
                break;
            }
            i += 1;
        }
        if !swapped { break; }
    }
    vec
}
