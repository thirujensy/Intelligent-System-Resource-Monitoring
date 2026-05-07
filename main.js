async function loadMetrics() {
    const response = await fetch('http://127.0.0.1:5000/api/metrics');

    const data = await response.json();

    document.getElementById('cpu').innerText = data.cpu + '%';
    document.getElementById('memory').innerText = data.memory + '%';
    document.getElementById('disk').innerText = data.disk + '%';
    document.getElementById('prediction').innerText = data.prediction;
}

loadMetrics();
setInterval(loadMetrics, 3000);
