"use strict";

console.log("proof of life");

// remove before deployment
$("#testButton").on("click", showLife);
function showLife(event) {
  console.log("jquery is working");
}

$(".dropDownButton").on("click", dropDownList);
$(".cancel").on("click", cancelEdit);
$(".dropDownList").submit(editLocation);

function dropDownList(event) {
  $(this).hide();
  $(this).next().show();
}

function cancelEdit(event) {
  $(this).parent().hide();
  $(this).parent().prev().show();
}

function editLocation(event) {
  event.preventDefault();
  const serializedData = $(this).serialize();
  $.ajax({
    url: `unicorn-update/`,
    type: "POST",
    data: serializedData,
    dataType: "json",
    success: function (data) {
      console.log("it posted");
      location.reload();
    },
  });
}
