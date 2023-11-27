let  Bar_chart = document.getElementById("Bar_chart")

let layout ={
    margin:{
        t:0
        },
    barmode:'stack'
}

let trace1 = {};
trace1.type ="bar";
trace1.x =[];
trace1.y = [];
trace1.text =[];
trace1.name = 'lion';
trace1.textposition = "top center";
trace1.textfont = {
    family:"Fantasy",
    size: 30 ,
    color: 'white'
}
trace1.marker = {
    color: 'black'
}

// for(let i=0; i<animals_Taipei_Zoo.length;i++){
//     trace1.x[i] = animals_Taipei_Zoo[i]['name'];
//     trace1.y[i] = animals_Taipei_Zoo[i]['count'];
// }
trace1.x[0] = "animals_Taipei_Zoo";
trace1.y[0] = animals_Taipei_Zoo[0]['count'];
trace1.x[1] = "animals_Kaoshiung_Zoo";
trace1.y[1] = animals_Kaoshiung_Zoo[0]['count'];

trace1.text = trace1.y;

let trace2 ={};
trace2.type = "bar";
trace2.name = 'monkey';
trace2.x = [];
trace2.y = [];
trace2.textfont = {
    family:"Fantasy",
    size: 30 
}

// for (let i =0; i<animals_Kaoshiung_Zoo.length;i++){
//     trace2.x[i] = animals_Kaoshiung_Zoo[i]['name'];
//     trace2.y[i] = animals_Kaoshiung_Zoo[i]['count'];
// }
trace2.x[0] = "animals_Taipei_Zoo";
trace2.y[0] = animals_Taipei_Zoo[1]['count'];
trace2.x[1] = "animals_Kaoshiung_Zoo";
trace2.y[1] = animals_Kaoshiung_Zoo[1]['count'];

trace2.text = trace2.y;

let trace3 ={};
trace3.type = "bar";
trace3.name = 'tiger';
trace3.x = [];
trace3.y = [];
trace3.textfont = {
    family:"Fantasy",
    size: 30 
}

// for (let i =0; i<animals_Kaoshiung_Zoo.length;i++){
//     trace3.x[i] = animals_Kaoshiung_Zoo[i]['name'];
//     trace3.y[i] = animals_Kaoshiung_Zoo[i]['count'];
// }
trace3.x[0] = "animals_Taipei_Zoo";
trace3.y[0] = animals_Taipei_Zoo[2]['count'];
trace3.x[1] = "animals_Kaoshiung_Zoo";
trace3.y[1] = animals_Kaoshiung_Zoo[2]['count'];

trace3.text = trace3.y;

let data = [];
data.push(trace1);
data.push(trace2);
data.push(trace3);

Plotly.newPlot(Bar_chart,data,layout);