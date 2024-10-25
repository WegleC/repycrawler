// 間單的查詢篩選功能
document.getElementById('search-school').addEventListener('input', function() {
    let filter = this.value.toLowerCase();
    let rows = document.querySelectorAll('#school-table tbody tr');

    rows.forEach(row => {
        let schoolName = row.cells[1].textContent.toLowerCase();
        if (schoolName.includes(filter)) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
});