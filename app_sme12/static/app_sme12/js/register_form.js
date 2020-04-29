$(document).ready(function () {

  $("div.bus_model_etc1").hide()
  $("div.bus_model_etc2").hide()
  $("div.juristic_id").hide()
  $("div.card_id").hide()
  $("div.regis_number").hide()
  $("div.commercial_regis_number").hide()
  

  // smart wizard
  $("#smartwizard").smartWizard({
    theme: "",
    transitionEffect: "slide",
    transitionSpeed: "400",

    lang: { next: "ถัดไป", previous: "ย้อนหลัง" },
  });

  $("#smartwizard").on("leaveStep", function(e, anchorObject, stepNumber, stepDirection) {
    // return confirm("Do you want to leave the step "+stepNumber+"?");
    if ($('form').valid()) {
      return true;
    } else {
      return false; 
    }
  });

  //// ------------ Select2
  $('.select2bs4').select2({
    theme: 'bootstrap4'
  })

  //// ------------ Input Mask 
  //Datemask dd/mm/yyyy
  $('#id_ent_establish_date').inputmask('9999-99-99', { 'placeholder': 'ปปปป-ดด-วว' })
  $('#id_ent_postcode').inputmask("99999", { 'placeholder': ' ' });
  $('#id_ent_tel').inputmask('9 9999 9999', { 'placeholder': ' ' });
  $('#id_ent_fax').inputmask('9 9999 9999', { 'placeholder': ' ' });
  $('#id_owner_card_id').inputmask('9 9999 99999 99 9', { 'placeholder': ' ' });
  $('#id_owner_postcode').inputmask("99999", { 'placeholder': ' ' });
  $('#id_owner_tel').inputmask('9 9999 9999', { 'placeholder': ' ' });
  $('#id_owner_fax').inputmask('9 9999 9999', { 'placeholder': ' ' });
  $('#id_owner_mobile').inputmask('99 9999 9999', { 'placeholder': ' ' });
  $('#id_contact_tel').inputmask('99 9999 9999', { 'placeholder': ' ' });

  
//////////////  Dependent/Chained Dropdown List Provice, Amphur, BusinessGroup
//////////////  Provice
  $("#id_ent_province").change(function () {
    var url = $("#registerSme").attr("data-amphur-url");  // get the url of the `load_amphur` view
    var provinceId = $(this).val();  // get the selected province ID from the HTML input

    $.ajax({                       // initialize an AJAX request
      url: url,                    // set the url of the request (= localhost:8000/sme12/ajax/load-amphur/)
      data: {
        'province': provinceId       // add the province id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the `load_amphur` view function
        $("#id_ent_amphur").html(data);  // replace the contents of the amphur input with the data that came from the server
      }
    });
  });
//////////////  Amphur
  $("#id_ent_amphur").change(function () {
    var url = $("#registerSme").attr("data-tumbol-url");  // get the url of the `load_tumbol` view
    var amphurId = $(this).val();  // get the selected amphur ID from the HTML input

    $.ajax({                       // initialize an AJAX request
      url: url,                    // set the url of the request (= localhost:8000/sme12/ajax/load-tumbol/)
      data: {
        'amphur': amphurId       // add the amphur id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the `load_tumbol` view function
        $("#id_ent_tumbol").html(data);  // replace the contents of the tumbol input with the data that came from the server
      }
    });

    var postcode = $("#id_ent_amphur option:selected").data("postcode");
    // alert(postcode)
    $("#id_ent_postcode").val(postcode)
  });
//////////////  Provice
  $("#id_owner_province").change(function () {
    var url = $("#registerSme").attr("data-amphur-url");  // get the url of the `load_amphur` view
    var provinceId = $(this).val();  // get the selected province ID from the HTML input

    $.ajax({                       // initialize an AJAX request
      url: url,                    // set the url of the request (= localhost:8000/sme12/ajax/load-amphur/)
      data: {
        'province': provinceId       // add the province id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the `load_amphur` view function
        $("#id_owner_amphur").html(data);  // replace the contents of the amphur input with the data that came from the server
      }
    });
  });
//////////////  Amphur
  $("#id_owner_amphur").change(function () {
    var url = $("#registerSme").attr("data-tumbol-url");  // get the url of the `load_tumbol` view
    var amphurId = $(this).val();  // get the selected amphur ID from the HTML input

    $.ajax({                       // initialize an AJAX request
      url: url,                    // set the url of the request (= localhost:8000/sme12/ajax/load-tumbol/)
      data: {
        'amphur': amphurId       // add the amphur id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the `load_tumbol` view function
        $("#id_owner_tumbol").html(data);  // replace the contents of the tumbol input with the data that came from the server
      }
    });

    var postcode = $("#id_owner_amphur option:selected").data("postcode");
    // alert(postcode)
    $("#id_owner_postcode").val(postcode)

  });
//////////////  BusinessGroup
  $("#id_business_type").change(function () {
    var url = $("#registerSme").attr("data-busgroup-url");  // get the url of the `load_businessgroup` view
    var bustypeId = $(this).val();  // get the selected business_type ID from the HTML input

    $.ajax({                       // initialize an AJAX request
      url: url,                    // set the url of the request (= localhost:8000/sme12/ajax/load-busgroup/)
      data: {
        'business_type': bustypeId       // add the business id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the `load_businessgroup` view function
        $("#id_business_group").html(data);  // replace the contents of the businessgroup input with the data that came from the server
      }
    });
  });
///////////////////////////////////////////////////////////////////////////////

  ////// 1.3 รูปแบบการจัดตั้งกิจการ 
  $("#id_business_model").change(function () {  
    var businessmodelGroup = $("#id_business_model option:selected").data("model-group");
    var businesscode = $("#id_business_model option:selected").data("model-code"); // get the selected business_model code from the HTML input
    // alert(businessmodelGroup);

    if (businesscode == '104') {
      $(".bus_model_etc1").show();
      $(".bus_model_etc2").hide();
      return true;
    } else if (businesscode == '304') {
      $(".bus_model_etc1").hide();
      $(".bus_model_etc2").show();
      return true; 
    } else {
      $(".bus_model_etc1").hide();
      $(".bus_model_etc2").hide();
    }

    if (businessmodelGroup == '1') {
      $("div.juristic_id").show()
      $("div.card_id").hide()
      $("div.regis_number").hide()
      $("div.commercial_regis_number").hide()
      return true;
    } else if (businessmodelGroup == '2') {
      $("div.juristic_id").hide()
      $("div.card_id").show()
      $("div.regis_number").hide()
      $("div.commercial_regis_number").show()
      return true; 
    } else {
      $("div.juristic_id").hide()
      $("div.card_id").hide()
      $("div.regis_number").show()
      $("div.commercial_regis_number").hide()
    }


    
  });


});
