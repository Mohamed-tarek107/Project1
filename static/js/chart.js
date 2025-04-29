document.addEventListener('DOMContentLoaded', function () {
    
    const labels = JSON.parse(document.getElementById('chart-data').dataset.labels);
    const values = JSON.parse(document.getElementById('chart-data').dataset.values);
    const orderlabels = JSON.parse(document.getElementById('chart-data').dataset.orderlabels);
    const ordervalues = JSON.parse(document.getElementById('chart-data').dataset.ordervalues);
    const revenuelabels = JSON.parse(document.getElementById('chart-data').dataset.revenuelabels);
    const revenuevalues = JSON.parse(document.getElementById('chart-data').dataset.revenuevalues);

    console.log("Labels:", labels); 
    console.log("Values:", values); 

    const ctx1 = document.getElementById('chart1').getContext('2d')
    new Chart(ctx1, {
        type: 'pie',
        data: {
            labels: orderlabels,
            datasets: [{
                label: 'Product Sales',
                data: ordervalues,
                backgroundColor: ['#ff6384', '#36a2eb', '#cc65fe', '#ffce56'],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true
        }
    });

    const ctx2 = document.getElementById('chart2').getContext('2d');
    new Chart(ctx2, {
        type: 'line',
        data: {
            labels: revenuelabels,
            datasets: [{
                label: 'Revenue Over Time',
                data: revenuevalues,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 2,
                tension: 0.4,
                fill: true
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Time',
                        color: '#FFFFFF',
                        font: {
                            size: 14
                        }
                    }
                },
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Revenue',
                        color: '#FFFFFF',
                        font: {
                            size: 14
                        }
                    }
                }
            },
            plugins: {
                legend: {
                    display: true,
                    position: 'top'
                }
            }
        }
    });
    

    const ctx3 = document.getElementById('chart3').getContext('2d');

    new Chart(ctx3, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Stock',
                data: values,
                backgroundColor: 'lightblue',
                borderColor: 'blue',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});