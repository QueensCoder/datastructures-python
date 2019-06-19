const numArr = [2, 5, 1, 3, 7, 4, 2, 3, 9, 8, 6, 3];

const mergeSort = arr => {
  console.log(arr);
  if (arr.length === 1) return arr;

  const middle = Math.floor(arr.length / 2);
  const left = arr.slice(0, middle);
  const right = arr.slice(middle);

  return merge(mergeSort(left), mergeSort(right));
};

const merge = (left, right) => {
  let result = [];
  let idxL = 0;
  let idxR = 0;
  while (idxL < left.length && idxR < right.length) {
    if (left[idxL] < right[idxR]) {
      result.push(left[idxL]);
      idxL++;
    } else {
      result.push(right[idxR]);
      idxR++;
    }
    return result.concat(left.slice(idxL)).concat(right.slice(idxR));
  }
};

const sortedArr = mergeSort(numArr);
console.log(sortedArr);
