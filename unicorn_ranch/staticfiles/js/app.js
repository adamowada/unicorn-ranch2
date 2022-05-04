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
  $(this).parent().parent().hide();
  $(this).parent().parent().prev().show();
}

function editLocation(event) {
  event.preventDefault();
  const serializedData = $(this).serialize();
  const regex1 = /[^\r\n.]+=[^\r\n.]+=(\d+)/;
  const regex2 = /[^\r\n.]+=[^\r\n.]+=[^\r\n.]+=([a-zA-Z]+)/;
  const id = serializedData.match(regex1)[1];
  const location = serializedData.match(regex2)[1];
  console.log(id, location); // flag to remove
  $.ajax({
    url: `unicorn-update/${id}`,
    type: "POST",
    data: serializedData,
    dataType: "json",
    success: function (data) {
      console.log("it posted");
      window.location.reload();
    },
  });
}
