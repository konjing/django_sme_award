$(function () {
    // Setup - add a text input to each footer cell
    $("#sme-list tfoot th.filter").each(function (i) {
      var title = $("#sme-list thead th.reffilter").eq($(this).index()).text();
      $(this).html(
        '<input type="text" class="form-control" placeholder="ค้นหา ' +
          title +
          '" data-index="' +
          (i) +
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
    
  
  });
   