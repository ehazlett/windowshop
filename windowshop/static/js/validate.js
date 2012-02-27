function validateForm(form, errorClass){
  var valid = true;
  var cssClass = errorClass ? errorClass : 'error';
  if (form) {
    $(form).find(':input').each(function(index, el){
      if ($(el).hasClass('required')) {
        if ($(el).val() == "") {
          valid = false;
          //debug.log($(el) + ' invalid');
          $(el).parent().parent().addClass(cssClass);
        }
      }
    });
  }
  return valid;
}
