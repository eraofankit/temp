const tableBody = document.querySelector('#sensor-table tbody');
const trendCanvas = document.getElementById('trend');
const ctx = trendCanvas.getContext('2d');
const history = [];

function updateTable(data) {
    tableBody.innerHTML = '';
    for (const [key, value] of Object.entries(data)) {
        const row = document.createElement('tr');
        const nameCell = document.createElement('td');
        nameCell.textContent = key;
        const valCell = document.createElement('td');
        valCell.textContent = value.toFixed(2);
        row.appendChild(nameCell);
        row.appendChild(valCell);
        tableBody.appendChild(row);
    }
}

function drawTrend(value) {
    history.push(value);
    if (history.length > trendCanvas.width) {
        history.shift();
    }
    ctx.clearRect(0, 0, trendCanvas.width, trendCanvas.height);
    ctx.beginPath();
    ctx.moveTo(0, trendCanvas.height - history[0]);
    for (let i = 1; i < history.length; i++) {
        ctx.lineTo(i, trendCanvas.height - history[i]);
    }
    ctx.stroke();
}

const evtSource = new EventSource('/events');
evtsource = evtSource; // for debugging

evtSource.onmessage = function(event) {
    const data = JSON.parse(event.data);
    updateTable(data);
    if ('temperature' in data) {
        drawTrend(data.temperature + 50); // scale for canvas
    }
};
