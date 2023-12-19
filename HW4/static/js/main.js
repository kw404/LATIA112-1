let school_kind = document.getElementById('school_SorI');
let school_data = JSON.parse(document.getElementById('exchangeData').innerHTML);

console.log(school_data);

let trace1 = {};
trace1.type = "pie";
trace1.labels = [];
trace1.values = [];

trace1.x = [];
trace1.y = [];

for (let i = 0; i < school_data[0].length; i++) {
    trace1.x[i] = school_data[i].date;
    trace1.y[i] = school_data[i]['twd-jpy'];
}

console.log("trace1.x: ", trace1.x);
console.log("trace1.y: ", trace1.y);

let data = [];
data.push(trace1);


Plotly.newPlot(school_kind, data, layout);