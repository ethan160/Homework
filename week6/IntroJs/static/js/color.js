function Car(year, make, model, color) {
    this.year = year
    this.make = make
    this.model = model
    this.color = color
    const paintArrow = (color) => {
        this.color = color
    }
    const paintFunc = function (color) {
        this.color = color
    }
    this.letsPaint = () => {
        console.log(this.color)
        paintArrow('Blue')
        console.log(this.color)
        // paintArrow('Green')  //  --> return to green
        paintFunc('Green')  // --> return blue
        console.log(this.color)
    }
}
let ourCar = new Car(2021, 'Honda', 'CRV', 'Red')
ourCar.letsPaint()