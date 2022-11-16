function* generatorFunc() {
  yield 1;
  yield 2;
}
var g = generatorFunc();
console.log(g.next(), g.next(), g.next());
