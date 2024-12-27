function generateCalendar() {
    const calendar = document.querySelector('.calendar');
    const date = new Date();
    const today = new Date();
    const monthYear = document.getElementById('monthYear');
    
    const months = [
        "Januari", "Februari", "Maret", "April", "Mei", "Juni",
        "Juli", "Agustus", "September", "Oktober", "November", "Desember"
    ];

    monthYear.innerText = `${months[date.getMonth()]} ${date.getFullYear()}`;

    date.setDate(1);
    const firstDayIndex = date.getDay();
    const lastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDate();
    const prevLastDay = new Date(date.getFullYear(), date.getMonth(), 0).getDate();
    const nextDays = 7 - new Date(date.getFullYear(), date.getMonth() + 1, 0).getDay() - 1;

    calendar.innerHTML = '';
    calendar.innerHTML += `<div class="header">Minggu</div>
    <div class="header">Senin</div>
    <div class="header">Selasa</div>
    <div class="header">Rabu</div>
    <div class="header">Kamis</div>
    <div class="header">Jumat</div>
    <div class="header">Sabtu</div>`;

    for (let x = firstDayIndex; x > 0; x--) {
        calendar.innerHTML += `<div class="day prev-date">${prevLastDay - x + 1}</div>`;
    }

    for (let i = 1; i <= lastDay; i++) {
        if (i === today.getDate() && date.getMonth() === today.getMonth() && date.getFullYear() === today.getFullYear()) {
            calendar.innerHTML += `<div class="day today">${i}</div>`;
        } else {
            calendar.innerHTML += `<div class="day">${i}</div>`;
        }
    }

    for (let j = 1; j <= nextDays; j++) {
        calendar.innerHTML += `<div class="day next-date">${j}</div>`;
    }
}
generateCalendar();