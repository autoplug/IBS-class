function solution(S) {
  // write your code in JavaScript (Node.js 8.9.4)
  replaceAt = function (str, index, replacement = "a") {
    return str.substring(0, index) + replacement + str.substring(index + 1);
  };
  var index = S.length / 2;
  index = Math.floor(index) - 1;
  for (var i = 0; i <= index; i++) {
    i2 = S.length - i - 1;
    if (S[i] == "?" && S[i2] != "?") S = replaceAt(S, i, S[i2]);
    if (S[i] != "?" && S[i2] == "?") S = replaceAt(S, i2, S[i]);
    if (S[i] == "?" && S[i2] == "?") {
      S = replaceAt(S, i);
      S = replaceAt(S, i2);
    }
  }
  for (var i = 0; i <= index; i++) {
    if (S[i] != S[S.length - i - 1]) return "NO";
  }
  return S.replace("?", "a");
}

console.log(solution("?ab??a"));
console.log(solution("bab??a"));
console.log(solution("?ki"));
console.log(solution("??d"));
