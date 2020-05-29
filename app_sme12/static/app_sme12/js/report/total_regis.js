$(document).ready(function() {
    $('#myTable').DataTable( {
        searching: false,
        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'excel',
                title: 'สรุปจำนวนผู้สมัคร(SME Award12) ขั้นตอนสมัครประกวด'
            },
            {
                extend: 'print',
                title: 'สรุปจำนวนผู้สมัคร(SME Award12) ขั้นตอนสมัครประกวด'
            }
        ]
    } );
} );