$(document).ready(function () {
  // Setup - add a text input to each footer cell
  $("#sme-list tfoot th").each(function () {
    var title = $(this).text();
    $(this).html(
      '<input type="text" class="form-control" placeholder="ค้นหา ' +
        title +
        '" />'
    );
  });

  // DataTable
  var table = $("#sme-list").DataTable({
    // Button Excel+Print
    searching: false,
    dom: "Bfrtip",
    buttons: [
      {
        extend: "excel",
        title: "สรุปจำนวนผู้สมัคร(SME Award12) ขั้นตอนสมัครประกวด",
      },
      {
        extend: "print",
        title: "สรุปจำนวนผู้สมัคร(SME Award12) ขั้นตอนสมัครประกวด",
      },
    ],

    initComplete: function () {
      // Apply the search
      this.api()
        .columns()
        .every(function () {
          var that = this;

          $("input", this.footer()).on("keyup change clear", function () {
            if (that.search() !== this.value) {
              that.search(this.value).draw();
            }
          });
        });
    },
  });
});
