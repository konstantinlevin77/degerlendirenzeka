window.onload = function() {

    screen.orientation.addEventListener('change', function() {
        if (screen.orientation.type === "portrait-primary" || screen.orientation.type == "portrait-secondary") {
            document.getElementById("portrait-content").style.visibility = 'visible';

        }
        else if (screen.orientation.type === "landscape-primary" || screen.orientation.type === "landscape-secondary") {
            document.getElementById("portrait-content").style.visibility = 'hidden';

        }
        
    });
}