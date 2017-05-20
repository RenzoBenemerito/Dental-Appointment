(function ($) {
$(document).ready(function(){
  $('#embeddedCalendar').click(function(){
    var date = $('#embeddedDateField').text();
    $('.tableContainer').empty();
    $.ajax({
      url: '/tableRenderer',
      type: 'POST',
      data: {
        date: date
      },
      success: function(table){
        $('.tableContainer1').html(table);
      }
    });
  });
});
})(jQuery);
