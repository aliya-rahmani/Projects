//intermediate
//The function call would be --> binary_search(&"element to search",&vec![..,array to search the element in,..]);
//index of the searched element would be returned

pub fn binary_search<T: PartialEq + PartialOrd>(item: &T, array: &[T]) -> i32 {
    let mut pos = -1; // value for not found

    if array.is_empty() {
        return pos;
    }

    let mut left = 0;
    let mut right = array.len() - 1;

    while left < right {
        let mid = left + (right - left) / 2;

        if &array[mid] > item {
            right = mid - 1;
        } else if &array[mid] < item {
            left = mid + 1;
        } else {
            left = mid;
            break;
        }
    }

    if &array[left] == item {
        	pos = left as i32;
        return pos;
    } else {
        return pos;
    }
}
