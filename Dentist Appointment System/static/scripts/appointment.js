$(document).ready(function(){
  $("#addAppt").submit( function(eventObj) {
      var name = $('#nameOf').text();
      alert('Appointment Added');
      $('<input />').attr('type', 'hidden')
          .attr('name', "Fullname")
          .attr('value', name)
          .appendTo('#addAppt');
  });
});
