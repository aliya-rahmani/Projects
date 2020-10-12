function mergesort(list){
    if(list.length < 2){
        return list;
    }else if(list.length > 1){
        let n = list.length;
        let middle = n/2;
        return merge(mergesort(list.slice(0, middle)), mergesort(list.slice(middle, n)));
    }
}

function merge(listA, listB){
    let list = [];

    listA.push(Infinity);
    listB.push(Infinity);

    let i = 0;
    let j = 0;

    while(i < listA.length-1 || j < listB.length-1){
        if(listA[i] < listB[j]){
            list.push(listA[i]);
            i++;
        }else{
            list.push(listB[j]);
            j++;
        }
    }

    return list;

}
