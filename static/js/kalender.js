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
    calendar.innerHTML += `<div class="header" style"background-color: slategray;">Minggu</div>
    <div class="header" style"background-color: slategray;">Senin</div>
    <div class="header" style"background-color: #ffcf50;">Selasa</div>
    <div class="header" style"background-color: #ffcf50;">Rabu</div>
    <div class="header" style"background-color: #ffcf50;">Kamis</div>
    <div class="header" style"background-color: #ffcf50;">Jumat</div>
    <div class="header" style"background-color: #ffcf50;">Sabtu</div>`;

    for (let x = firstDayIndex; x > 0; x--) {
        calendar.innerHTML += `<div class="day prev-date" style= "background-color: #f3f3f3;">${prevLastDay - x + 1}</div>`;
    }

    for (let i = 1; i <= lastDay; i++) {
        if (i === today.getDate() && date.getMonth() === today.getMonth() && date.getFullYear() === today.getFullYear()) {
            calendar.innerHTML += `<div style=" background-color: #ffcf50; border-color: white;" class="day today">${i}</div>`;
        } else {
            calendar.innerHTML += `<div class="day" >${i}</div>`;
        }
    }

    for (let j = 1; j <= nextDays; j++) {
        calendar.innerHTML += `<div class="day next-date">${j}</div>`;
    }
}
generateCalendar();