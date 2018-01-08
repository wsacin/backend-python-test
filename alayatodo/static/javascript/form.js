$("form[action='/todo']").submit(function() {
  if ($.trim($("input[name=description]").val()) === '') {
    $('#form-alert').prop('hidden', false);
    setTimeout(function() {
      $('#form-alert').prop('hidden', true);
    }, 5000);
    return false;
  }
});

$('a[id*="mark-done"]').click(event, function() {
  var todoId = $(event.target).attr('value');
  var todoClass = $(event.target).attr('class');
  $.ajax({
    url: '/todo/' + todoId,
    type: 'PUT',
    data: 'done=true',
    success: function(data) {
      var doneClass = "btn btn-xs btn-success glyphicon glyphicon-ok"
      var undoneClass = "btn btn-xs btn-info glyphicon glyphicon-minus"
      if (todoClass === undoneClass) {
        $("#mark-done-" + todoId).attr('class', doneClass);
      } else {
        $("#mark-done-" + todoId).attr('class', undoneClass);
      }
    }
  });
})
