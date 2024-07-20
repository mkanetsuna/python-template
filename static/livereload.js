setInterval(() => {
    fetch('/reload')
        .then(response => response.json())
        .then(data => {
            if (data.reload) {
                window.location.reload();
            }
        });
}, 1000);
