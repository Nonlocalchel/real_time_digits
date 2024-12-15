let ctx = document.querySelector('#myChart')

let graphData = {
    type: 'line',
    data: {
        labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        datasets: [{
            label: 'My First Dataset',
            data: [65, 59, 80, 81, 56, 55, 40],
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
        }]
    },
}

let myChart = new Chart(ctx, graphData)

var socket = new WebSocket('ws://localhost:8000/ws/some-url')

socket.onmessage = function(event){
    var socketData = JSON.parse(event.data)

    let newGraphData = graphData.data.datasets[0].data
    newGraphData.shift()
    newGraphData.push(socketData.number)

    graphData.data.datasets[0].data = newGraphData
    myChart.update()
}