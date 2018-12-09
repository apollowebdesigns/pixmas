const {LEDBoard} = require('gpiozero');
const {random_values} = require('gpiozero/tools');
let numbers = [];
for(let i = 2; i < 28; i++) {
    numbers.push(i);    
}
const tree = LEDBoard(numbers, True);
