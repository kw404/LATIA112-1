let myGraph1 = document.getElementById('Bar_chart');
let trace1 = {};
trace1.type = "bar";
trace1.title = "現大專院校分布";
trace1.x = [];
trace1.y = [];
trace1.domain = {
    row:0,
    column:0
};

for (let i=0; i<school_part.length; i++){
    trace1.x[i] = school_part[i]['name'];
    trace1.y[i] = school_part[i]['count'];
}


let myGraph2 = document.getElementById('pie_chart');
let trace2 = {};
trace2.type ="pie";
trace2.title = "大專院校公私立比";
trace2.labels = [];
trace2.values = [];
trace2.domain = {
    row:0,
    column:1
};
trace2.hole = 0.65;

for (let x=0; x<school_count.length; x++) {
    trace2.values[x] = school_count[x]['count'];
    trace2.labels[x] = school_count[x]['name'];
}

let myGraph3 = document.getElementById('Line_chart');
let trace3 = {};
trace3.mode = 'lines+markers';
trace3.type ="scatter";
trace3.title = "歷屆大專院校數";
trace3.x = [];
trace3.y = [];
trace3.domain = {
    row:1,
    column:0
};

for (let j=0; j<school_amount.length; j++) {
    trace3.x[j] = school_amount[j]['name'];
    trace3.y[j] = school_amount[j]['count'];
}



let data1 = [];
data1.push(trace1);
let data2 = [];
data2.push(trace2);
let data3 = [];
data3.push(trace3);

let layout1 = {
    xaxis: {
        title: '區域'
    },
    yaxis: {
        title: '間數'
    },
    margin: {
        t: 70,
        l: 90
    }
};

let layout2 = {
    margin: {
        t: 70,
        l: 90
    }
};

let layout3 = {
    xaxis: {
        title: '大專院校數量'
    },
    yaxis: {
        title: '時間（年度）'
    },
    margin: {
        t: 70,
        l: 90
    }
};

Plotly.newPlot(myGraph1, data1, layout1);
Plotly.newPlot(myGraph2, data2, layout2);
Plotly.newPlot(myGraph3, data3, layout3);