document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('searchInput').addEventListener('input', function() {
        let filter = this.value.toLowerCase();
        let rows = document.querySelectorAll('.maincontent table tr');

        rows.forEach(function(row, index) {
            if (index === 0) {
                return;
            }

            let cells = row.getElementsByTagName('td');
            let found = false;

            row.style.display = '';

            if (filter === '') {
                return;
            }

            for (let i = 0; i < cells.length; i++) {
                let cell = cells[i];
                if (cell.textContent.toLowerCase().includes(filter)) {
                    found = true;
                    break;
                }
            }
            
            if (!found) {
                row.style.display = 'none';
            }
        });
    });
});
