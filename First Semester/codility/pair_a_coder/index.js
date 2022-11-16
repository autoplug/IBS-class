function solution(S) {
  // write your code in JavaScript (Node.js 8.9.4)
  var rS = S.split("").reverse().join("");
  function count(str) {
    var index = 0;
    while (true) {
      console.log(str);
      var end = str.indexOf(str[index], index + 1);
      if (end != -1) {
        str = str.replace(str.slice(index, end + 1), "");
      }
      index++;
      if (index >= str.length) break;
    }
    return str.length;
  }

  return Math.min(count(S), count(rS));
}

console.log(solution("axaabyab"));
