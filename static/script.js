function mohit() {
    clearInterval(id);
    let re = confirm("would you want to read in Hindi?");
    if (re) {
        alert("Oooo we're working on this feature----> You might get it soon...");
    } else {
        alert("Ok That's smart choice to continue with English....");
    }
    id = setInterval(mohit, 300000);
    // calls after 300 sec 


    // Function to be use if we add support to hindi language.

}

id = setInterval(satija, 100);

function replaceAll(string, search, replace) {
    return string.split(search).join(replace);
}

function satija() {
    clearInterval(id);
    ans = document.querySelector("p").innerHTML;
    ans = replaceAll(ans, '&lt;', '<');
    ans = replaceAll(ans, '&gt;', '>');
    document.querySelector("p").innerHTML = ans;
    ans = document.getElementById("2").innerHTML;
    ans = replaceAll(ans, '&lt;', '<');
    ans = replaceAll(ans, '&gt;', '>');
    document.getElementById("2").innerHTML = ans;
    ans = document.getElementById("3").innerHTML;
    ans = replaceAll(ans, '&lt;', '<');
    ans = replaceAll(ans, '&gt;', '>');
    document.getElementById("3").innerHTML = ans;
}