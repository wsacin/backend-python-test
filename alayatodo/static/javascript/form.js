$("form[action='/todo/']").submit(function() {
  if ($.trim($("input[name=description]").val()) === '') {
    $('#form-alert').prop('hidden', false);
    setTimeout(function() {
      $('#form-alert').prop('hidden', true);
    }, 5000);
    return false;
  }
});
