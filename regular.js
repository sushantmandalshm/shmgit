var re = new RegExp('^[a-zA-Z]{2}[0-9]{8}$'); //first done AC12345678
//console.log(re.test('AC12345678'));

var re = new RegExp('^[a-zA-Z][0-9]{9}$'); //second done A123456789
//console.log(re.test('A123456789'));


var re = new RegExp('(^[a-zA-Z]{2}[0-9]{8}$)|(^[a-zA-Z][0-9]{9}$)'); //combined first and second
//console.log(re.test('AC12345678'));

// var re = new RegExp('^\\s+and+\\s$'); 
// console.log(re.test(' and '))
// console.log(re.test('and'))
// console.log(re.test(' and'))
// console.log(re.test('and '))
// console.log(re.test('Sushant and Sanket'))

// var re = new RegExp('^and$'); 
// console.log(re.test('and'));

// var re = new RegExp('^\\s+and+\\s$'); 
// console.log(re.match(' and '))

var re = new RegExp('$&:  and'); 
console.log(re.match(' and '))
