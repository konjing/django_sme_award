$(function () {
  // Setup - add a text input to each footer cell
  $("#example tfoot th.filter").each(function (i) {
    var title = $("#example thead th.filter").eq($(this).index()).text();
    $(this).html(
      '<input type="text" class="form-control" placeholder="ค้นหา ' +
        title +
        '" data-index="' +
        i +
        '" />'
    );
  });

  // DataTable
  var table = $("#example").DataTable({
    paging: true,
    searching: true,
    ordering: true,
  });

  // Filter event handler
  $(table.table().container()).on("keyup", "tfoot input", function () {
    table.column($(this).data("index")).search(this.value).draw();
  });
  
});
 