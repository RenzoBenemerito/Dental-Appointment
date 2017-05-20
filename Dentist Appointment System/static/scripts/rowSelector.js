$(document).ready(function(){
  $("table tr").click(function(){
     $(this).addClass('selected').siblings().removeClass('selected');
     var value=$(this).find('td:first').html();


     $('#delete').click(function(event){
       event.preventDefault();
       $.ajax({
         data: {
          id: value
        },
         url: '/cancelAppt',
         type: 'POST',
         success: function(){
           window.location = '/home';
         }
       });
     });

  $('#resched').click(function(){
    $('#resched').css('display','none');
    $('#delete').css('display','none');
    $('.updateContainer').css('display','block');
    $("#updateAppt").submit( function(eventObj) {
        $('<input />').attr('type', 'hidden')
            .attr('name', "id")
            .attr('value', value)
            .appendTo('#updateAppt');
    });
    });
  });
});
