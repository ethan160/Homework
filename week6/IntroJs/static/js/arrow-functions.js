function Car(year, make, model) {
    this.year = year;
    this.make = make;
    this.model = model;

    // this.drive = function() {
    //     console.log("Vroom!");
    // }

    // this.drive = (m) => {
    //     console.log('Vroom!');
    //     console.log(`Hey, your ${m} is going too fast`);
    // }

    // this.drive = (m=this.model) => {
    //     console.log('Vroom!');
    //     console.log(`Hey, your ${m} is going too fast`);
    // }

    this.drive = (m, l) => {
        console.log(`Your ${l} said Zroom!`);
        console.log(`Hey, your ${m} is going too fast`);
    }
    
}

carTwo = new Car('2021', 'Tesla', 'Model3');
carTwo.drive(carTwo.model);