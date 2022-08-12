export default function getStudentIdsSum(arr) {
  return arr.reduce((x, y) => x + y.id, 0);
}
