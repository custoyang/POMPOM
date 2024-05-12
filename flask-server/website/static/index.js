function deletePill(pillId) {
    fetch('/delete-pill', {
        method: 'POST',
        body: JSON.stringify({ pillId: pillId }),
    }).then((_res) => {
        window.location.href = "/";
    });
}