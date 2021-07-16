// fetch('./static/data.json')
//     .then(res => res.json())
//     .then(data => console.log(data))


var xhr = new XMLHttpRequest();

xhr.onreadystatechange = () => {
    if (xhr.readyState == 4 && xhr.status == 200) {
        // console.log(JSON.parse(this.responseText));
        console.log(typeof this.responseText);
    }
}

xhr.open('GET', './static/data.json')
xhr.send()