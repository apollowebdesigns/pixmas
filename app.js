// const boards = require('js-gpiozero/gpiozero/boards');
const {LEDBoard} = require('js-gpiozero/gpiozero/boards/LEDBoard');
console.log(JSON.stringify(LEDBoard));
const {random_values} = require('gpiozero/tools');
let numbers = [];
for(let i = 2; i < 28; i++) {
    numbers.push(i);    
}
const tree = LEDBoard(numbers, True);
for (led of tree){
    led.source_delay = 0.1
    led.source = random_values()
    if(this.on == False) {
        break
    }
}
            