var showWishes = function(){
    $( window ).load(function(){
        $("#show-wishes").slideDown(2000);
    });
}

$(document).ready(showWishes)

var registerForm = function(){
    $("#show").click(function(){
        $("#register-form").slideToggle(1000);
    });
}

$(document).ready(registerForm)


$(document).ready(function() {
    $(".task-box").one('mouseover', function () {
        $(".task-box").animate({
            width: '+=400px',
        });
    });
});

//
// window.onload = function () {
//   document.getElementById("register-form").onclick = function () { showWishes() (); };