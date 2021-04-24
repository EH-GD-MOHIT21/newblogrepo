// Typing Animation ends here
function readyfunc() {
    clearInterval(id);
    var typed = new Typed(".typing", {
        strings: ["Youtuber", "Programmer", "Blogger", "Designer", "DataHandler"],
        typeSpeed: 100,
        backSpeed: 60,
        loop: true
    });

    var typed = new Typed(".typing1", {
        strings: ["Programmer", "Blogger", "Designer", "DataHandler", "Youtuber"],
        typeSpeed: 100,
        backSpeed: 60,
        loop: true
    });

    var typed = new Typed(".typing2", {
        strings: ["DataHandler", "Youtuber", "Programmer", "Blogger", "Designer"],
        typeSpeed: 100,
        backSpeed: 60,
        loop: true
    });
};
id = setInterval(readyfunc, 100);

//Typing Animation ends here