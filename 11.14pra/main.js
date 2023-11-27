let myGraph  = document.getElementById("myGraph")

let layout ={
    margin:{
        t:40
        },
    xaxis:{
        range:[0,8]
    },
    yaxis:{
        range:[0,15]
    }
}

let trace1 = {};
trace1.mode = "markers+text";
trace1.type ="scatter";
trace1.name = "TeamA";
trace1.marker ={
    size:[10,3,7,8]
};
trace1.x =[];
trace1.y = [];
trace1.text =[];
trace1.textposition = "top center";
trace1.textfont = {
    family:"Fantasy",
    size: 60 
}

for(let i=0; i<set1.length;i++){
    trace1.x[i] = set1[i][0];
    trace1.y[i] = set1[i][1];
    trace1.text[i] =set1[i][2];
}

let trace2 = {};
trace2.mode = "lines";
trace2.type ="scatter";
trace2.name = "TeamB";
trace2.x =[];
trace2.y = [];

for(let i=0; i<set2.length;i++){
    trace2.x[i] = set2[i][0];
    trace2.y[i] = set2[i][1];
}

let trace3 = {};
trace3.mode = "lines+markers";
trace3.type ="scatter";
trace3.name = "TeamC";
trace3.x =[];
trace3.y = [];

for(let i=0; i<set3.length;i++){
    trace3.x[i] = set3[i][0];
    trace3.y[i] = set3[i][1];
}

let data = [];
data.push(trace1);
data.push(trace2);
data.push(trace3);

Plotly.newPlot(myGraph,data,layout);