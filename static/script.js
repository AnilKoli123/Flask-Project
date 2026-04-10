const ctx = document.getElementById('attendanceChart');

if (ctx) {
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Present', 'Absent'],
            datasets: [{
                label: 'Attendance',
                data: [70, 30], // You can connect real data later
                borderWidth: 1
            }]
        }
    });
}

function toggleMode() {
    document.body.classList.toggle('dark');
}