$(document).ready(function () {
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

  // แสดงข้อความหลังกดปุ่มบันทึกแล้วผ่านการตรวจสอบ
  $.validator.setDefaults({
    submitHandler: function () {
      alert("ลงข้อมูลเสร็จสิ้น");
    },
  });



  //// ------------ Select2
  $('.select2bs4').select2({
    theme: 'bootstrap4'
  })

  //// ------------ Input Mask 
  //Datemask dd/mm/yyyy
  $('#id_ent_establish_date').inputmask('99-99-9999', { 'placeholder': 'วว-ดด-ปปปป' })
  $('#id_ent_postcode').inputmask("99999", { 'placeholder': ' ' });
  $('#id_ent_tel').inputmask('9 9999 9999', { 'placeholder': ' ' });
  $('#id_owner_card_id').inputmask('9 9999 99999 99 9', { 'placeholder': ' ' });
  $('#id_owner_postcode').inputmask("99999", { 'placeholder': ' ' });
  $('#id_owner_tel').inputmask('9 9999 9999', { 'placeholder': ' ' });
  $('#id_owner_mobile').inputmask('99 9999 9999', { 'placeholder': ' ' });

  //// ------------ Validation 
  // ตรวจสอบการลงข้อมูล
  $("#registerSme").validate({
    rules: {
      ent_name: {
        required: true,
        // minlength: 5,
      },    
      ent_establish_date: {
        required: true,
      },      
      ent_address_no: {
        required: true,
      },
      ent_amphur: {
        required: true,
      },
      ent_province: {
        required: true,
      },
      ent_postcode: {
        required: true,
      },
      ent_tel: {
        required: true,
      },
      ent_email: {
        required: true,
        email: true,
      },      
      owner_name: {
        required: true,
      },
      owner_card_id: {
        required: true,
      },
      owner_address_no: {
        required: true,
      },
      owner_tumbol: {
        required: true,
      },
      owner_amphur: {
        required: true,
      },
      owner_province: {
        required: true,
      },
      owner_postcode: {
        required: true,
      },
      owner_tel: {
        required: true,
      },
      owner_mobile: {
        required: true,
      },
      owner_email: {
        required: true,
        email: true,
      },
      business_model: {
        required: true,
      },
      contact_name: {
        required: true,
      },
      contact_position: {
        required: true,
      },
      contact_tel: {
        required: true,
      },
      contact_email: {
        required: true,
        email:true
      },  

    },
    messages: {
      ent_name: {
        required: "ต้องระบุชื่อสถานประกอบการ",
        // minlength: "Please enter name more tahn 5 ",
      },         
      ent_establish_date: {
        required: "ต้องระบุวันที่จัดตั้งกิจการ",
      },  
      ent_address_no: {
        required: "ต้องระบุเลขที่",
      },
      ent_amphur: {
        required: "ต้องระบุอำเภอ",
      },
      ent_province: {
        required: "ต้องระบุจังหวัด",
      },
      ent_postcode: {
        required: "ต้องระบุรหัสไปรษณีย์",
      },  
      ent_tel: {
        required: "ต้องระบุหมายเลขโทรศัพท์",
      },
      ent_email: {
        required: "ต้องระบุอีเมล",
        email: "รูปแบบอีเมลไม่ถูกต้อง",
      },
      owner_name: {
        required: "ต้องระบุชื่อ",
      },
      owner_card_id: {
        required: "ต้องระบุเลขบัตรประชาชน",
      },
      owner_address_no: {
        required: "ต้องระบุเลขที่",
      },
      owner_tumbol: {
        required: "ต้องระบุตำบล",
      },
      owner_amphur: {
        required: "ต้องระบุอำเภอ",
      },
      owner_province: {
        required: "ต้องระบุจังหวัด",
      },
      owner_postcode: {
        required: "ต้องระบุรหัสไปรษณีย์",
      },
      owner_tel: {
        required: "ต้องระบุเบอร์โทรศัพท์",
      },
      owner_mobile: {
        required: "ต้องระบุเบอร์มือถือ",
      },
      owner_email: {
        required: "ต้องระบุอีเมล",
        email: "รูปแบบอีเมลไม่ถูกต้อง",
      },
      business_model: {
        required: "ต้องเลือกรูปแบบการจัดตั้งกิจการ",
      },
      contact_name: {
        required: "ต้องระบุชื่อ นามสกุล",
      },
      contact_position: {
        required: "ต้องระบุตำแหน่ง",
      },
      contact_tel: {
        required: "ต้องระบุหมายเลขโทรศัพท์",
      },
      contact_email: {
        required: "ต้องระบุอีเมล",
        email: "รูปแบบอีเมลไม่ถูกต้อง"
      },
      // terms: "Please accept our terms",
    },

    // Show validation fail messages
    errorElement: "span",
    errorPlacement: function (error, element) {
      error.addClass("invalid-feedback");
      element.closest(".form-group").append(error);
    },
    highlight: function (element, errorClass, validClass) {
      $(element).addClass("is-invalid");
    },
    unhighlight: function (element, errorClass, validClass) {
      $(element).removeClass("is-invalid");
    },
  });
});
