"use strict";

console.log("proof of life");

// remove before deployment
$("#testButton").on("click", showLife);
function showLife(event) {
  console.log("jquery is working");
}


$(".dropDownButton").on("click", dropDownList);
$(".cancel").on("click", cancelEdit);

function dropDownList(event) {
    $(this).hide();
    $(this).next().show();
}

function cancelEdit(event) {
    $(this).parent().hide();
    $(this).parent().prev().show();
}