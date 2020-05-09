$(function () {
  // Setup - add a text input to each footer cell
  $("#sme-list tfoot th.filter").each(function (i) {
    var title = $("#sme-list thead th.reffilter").eq($(this).index() - 1).text();
    $(this).html(
      '<input type="text" class="form-control" placeholder="ค้นหา ' +
        title +
        '" data-index="' +
        (i + 1) +
        '" />'
    );
  });

  // DataTable
  var table = $("#sme-list").DataTable({
    paging: true,
    searching: true,
    ordering: true,
  });

  // Filter event handler
  $(table.table().container()).on("keyup", "tfoot input", function () {
    table.column($(this).data("index")).search(this.value).draw();
  });
  
  //Cancle Modal 
  $(document).on('click', '.confirm-delete', function () {
    $("#confirmDeleteModal").attr("caller-id", $(this).attr("id"));
  });
  
  $(document).on('click', '#confirmDeleteButtonModal', function () {
    var caller = $("#confirmDeleteButtonModal").closest(".modal").attr("caller-id");
    window.location = $("#".concat(caller)).attr("href");
  });

  //Not approve Modal
  


  ////////////////

});
 