// var myObj = {
//     'name': 'Ethan Ji',
//     "age": 88,
//     location: 'San Francisco',
//     latops:['Apple', 'Dell', 'Samsung']
// }

// console.log(myObj)

// Object literal notation
// console.log(myObj['name'])

// Object dot notation
// console.log(myObj.name)

// console.log(myObj.latops)
// for (let i = 0; i < myObj.latops.length; i++) {
//     const laptop = myObj.latops[i];
//     console.log(laptop)
// }

// below code will cause a error
// for (const o of myObj) {
//     console.log(o)
// }


// for (const o of myObj.latops) {
//     console.log(o)
// }

// for (const key in myObj) {
//     if (Object.hasOwnProperty.call(myObj, key)) {
//         const element = myObj[key];
//         console.log(element)
//     }
// }

// create a 2 arguments call back function
// myObj.latops.forEach(function(laptop, index) {
//     console.log(`${index}: ${laptop}`)
// });

var myObj = {
    'name': 'Ethan Ji',
    "age": 88,
    location: 'San Francisco',
    latops: ['Apple', 'Dell', 'Samsung']
}

function Car(year, make, model) {
    this.year = year;
    this.make = make;
    this.model = model;

    this.drive = () => {
        console.log('Vroom!');
        console.log('Hello');
    }
    // this.drive = function() {
    //     console.log("Vroom!");
    // }
}

var carOne = new Car(2015, 'Chevrolet', 'Corvette');
// console.log(carOne['year']);
// console.log(carOne.make);
// console.log(carOne.model);

// change the 
carOne['year'] = 2018;
carOne.model = 'Tahoe';
console.log(carOne['year']);
console.log(carOne.make);
console.log(carOne.model);

carOne.drive();

// Below is equavlent in python

// class Car:
//     def __init__(self, year, make, model):
//         self.year = year
//         self.make = make
//         self.model = model 

// car1 = Car(2015, 'Chevrolet', 'Corvette')
