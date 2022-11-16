var fs = require("fs");

var file = fs.readFileSync("example_big.in", "utf8");
file = file.split("\n");

var T = parseInt(file[0]);
var N1_N2 = 1;
var result = [];

for (var i = 0; i < T; i++) {
  var N1 = parseInt(file[N1_N2]);
  var dic = [];
  file.slice(N1_N2 + 1, N1_N2 + N1 + 1).map((line) => {
    line = line.toLowerCase();
    var s = line.split(" ");
    var available = -1;
    var value = "";
    dic.map((_dic, index) => {
      if (_dic.indexOf(s[0]) >= 0) {
        available = index;
        value = s[1];
      }
      if (_dic.indexOf(s[1]) >= 0) {
        available = index;
        value = s[0];
      }
    });
    if (available == -1) dic.push(s);
    else dic[available].push(value);
  });

  var N2 = parseInt(file[N1_N2 + 1 + N1]);
  var q = file.slice(N1_N2 + N1 + 2, N1_N2 + N1 + N2 + 2);
  q.map((line) => {
    line = line.toLowerCase();
    var q = line.split(" ");
    if (q[0] == q[1]) return result.push("synonyms");

    success = false;
    dic.map((_dic) => {
      if (_dic.indexOf(q[0]) >= 0 && _dic.indexOf(q[1]) >= 0) success = true;
    });
    if (success) return result.push("synonyms");
    return result.push("different");
  });
  N1_N2 += N1 + N2 + 2;
}

console.log(result);
fs.writeFileSync("result.out", result.join("\n"));
