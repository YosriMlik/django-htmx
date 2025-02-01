

document.addEventListener("htmx:configRequest", function(evt) {
    var progressBar = document.getElementById("progress-bar");
    progressBar.style.width = "0%";
    progressBar.style.opacity = "1";
    progressBar.style.display = "block";

    var width = 0;
    var interval = setInterval(function() {
        if (width >= 90) {
            clearInterval(interval);
        } else {
            width += 10;
            progressBar.style.width = width + "%";
        }
    }, 100); // Adjust the interval time for speed

    evt.detail.target.addEventListener("htmx:beforeSwap", function() {
        clearInterval(interval);
        progressBar.style.width = "100%";
        setTimeout(function() {
            progressBar.style.opacity = "0";
            setTimeout(function() {
                progressBar.style.display = "none";
            }, 500); // Adjust this timeout for fade out
        }, 500); // Adjust this timeout for pause at 100%
    });
});
if (!sessionStorage.getItem('users')){
    //let myArray = ['apple', 'banana', 'cherry'];
    let myArray = [];
    sessionStorage.setItem('users', JSON.stringify(myArray));

    // Retrieve the JSON string from sessionStorage
    const storedArray = JSON.parse(sessionStorage.getItem('users'));
    console.log("create again");
} else{
    console.log("already created");
}
//console.log(JSON.parse(JSON.stringify(sessionStorage.getItem('users'))) + " is like " + JSON.stringify(myArray));
//console.log(JSON.parse(sessionStorage.getItem('users')));


