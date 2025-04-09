document.addEventListener('DOMContentLoaded', function() {
    // Menambahkan event listener setelah DOM dimuat
    document.getElementById('sidebarToggle').addEventListener('click', function() {
        var sidebar = document.getElementById('accordionSidebar');
        sidebar.classList.toggle('toggled'); // Menambah/menghapus kelas 'toggled'
    });
});
