"use strict";

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
  const id = serializedData.match(regex1)[1];
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
