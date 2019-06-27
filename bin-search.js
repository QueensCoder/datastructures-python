const arr = [1, 2, 3, 4, 5];

const targ = 1;

const binSearch = (arr, targ) => {
  const idx = Math.floor(arr.length / 2);
  const mid = arr[idx];
  console.log(mid);
  if (mid === targ) return true;
  else if (!arr[0] || arr.length === 1) return false;
  else if (mid > targ) return binSearch(arr.slice(0, idx), targ);
  else if (mid < targ) return binSearch(arr.slice(idx), targ);
};

console.log('hi');
const x = binSearch(arr, targ);

console.log(x);
