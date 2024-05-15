function Search() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("reservation_date");
    filter = input.value.toUpperCase();
    table = document.querySelector("table");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

$(".menuToggle").click("on", function () {
    $(".navigation").toggleClass("open");
});
$(".list").click("on", function () {
    $(".list").removeClass("active");
    $(this).addClass("active");
});


$("#HomePage").click("on", function () {
    $("#pg1").addClass("show");
    $("#pg2").removeClass("show");
    $("#pg3").removeClass("show");
    $("#pg4").removeClass("show");
    $("#pg5").removeClass("show");
});

$("#GoR").click("on", function () {
    $("#pg1").removeClass("show");
    $("#pg2").removeClass("show");
    $("#pg3").addClass("show");
    $("#pg4").removeClass("show");
    $("#pg5").removeClass("show");
});

$("#DeleteR").click("on", function () {
    $("#pg1").removeClass("show");
    $("#pg2").removeClass("show");
    $("#pg3").removeClass("show");
    $("#pg4").addClass("show");
    $("#pg5").removeClass("show");
});

$("#DATA").click("on", function () {
    $("#pg1").removeClass("show");
    $("#pg2").addClass("show");
    $("#pg3").removeClass("show");
    $("#pg4").removeClass("show");
    $("#pg5").removeClass("show");
});

$("#Logout").click("on", function () {
    $("#pg1").removeClass("show");
    $("#pg2").removeClass("show");
    $("#pg3").removeClass("show");
    $("#pg4").removeClass("show");
    $("#pg5").addClass("show");
});