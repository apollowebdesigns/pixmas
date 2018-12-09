// const boards = require('js-gpiozero/gpiozero/boards');
const LEDBoard = require('js-gpiozero').LEDBoard;
console.log(JSON.stringify(LEDBoard));
const leds = new LEDBoard([2, 3, 4, 5, 6]);
leds.on();
            