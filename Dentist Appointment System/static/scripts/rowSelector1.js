$(document).ready(function(){
  $("table tr").click(function(){
     $(this).addClass('selected').siblings().removeClass('selected');
     var value = $(this).find('td:first').html();
     var row1 = $(this);
     $("#updateAppt").submit( function(eventObj) {
         $('<input />').attr('type', 'hidden')
             .attr('name', "id")
             .attr('value', value)
             .appendTo('#updateAppt');
     });

     $('#delete').click(function(event){
       event.preventDefault();
       var name = $('#nameOf').text();
       $.ajax({
         data: {
          id: value
        },
         url: '/cancelAppt',
         type: 'POST',
         success: function(){
           alert('Delete Success!');
         }
       });
     });

  $('#resched').click(function(){
    $('#resched').css('display','none');
    $('#delete').css('display','none');
    $('.updateContainer').css('display','block');

    });
  });
  $('#updateProcess').submit(function(eventObj){
    var idPt = $('#id').text();
    alert(idPt);
    $('<input />').attr('type', 'hidden')
        .attr('name', "id")
        .attr('value', idPt)
        .appendTo('#updateProcess');
  });

});
$('#today').on('click','#deletePat',function(){
    console.log('hello world');
    var idPt = $('#id').text();
    $.ajax({
      url: '/deleteProcess',
      data: {
        id: idPt
      },
      type: 'POST',
      success: function(){
        alert("Patient Deleted");
        window.location = '/home';
    }
});
});
