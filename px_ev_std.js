const pairs = process.argv[2]
  .split(',')
  .map(x => x.split(':').map(y => parseFloat(eval(y))))
console.log(pairs)

const add = arr => arr.reduce((a, b) => a + b, 0)
const ev = add(pairs.map(x => x[0] * x[1]))
const toSum = pairs.map(x => (x[0] - ev) ** 2 * x[1])

const sum = add(toSum)

console.log('EV:', ev)
console.log('STDDev:', Math.sqrt(sum))
