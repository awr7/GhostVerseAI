document.addEventListener('DOMContentLoaded', function() {
    function animateLoadingText() {
        let loadingText = document.getElementById('loadingText');
        let dotCount = 0;
        setInterval(() => {
            dotCount = (dotCount + 1) % 4;
            loadingText.innerHTML = 'Hang tight' + '.'.repeat(dotCount);
        }, 500);
    }

    document.getElementById('uploadForm').onsubmit = function() {
        document.getElementById('spinner').style.display = 'block';
        document.getElementById('mainContent').style.display = 'none';
        document.getElementById('generate-lyrics').style.display = 'none';
        animateLoadingText();
    };
});