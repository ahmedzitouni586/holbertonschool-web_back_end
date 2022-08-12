export default function cleanSet(set, startString) {
  if (startString.length === 0 || typeof startString !== 'string' || typeof set !== 'object') {
    return '';
  }
  const myArr = [];
  for (const idx of set) {
    if (idx && idx.startsWith(startString)) {
      myArr.push(idx.replace(startString, ''));
    }
  }
  return myArr.join('-');
}
