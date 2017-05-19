$(document).ready(function(){
  $("table tr").click(function(){
     $(this).addClass('selected').siblings().removeClass('selected');
     var value=$(this).find('td:first').html();
     $('#delete').click(function(event){
       event.preventDefault();
       console.log('you clicked me');
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
  });
  $('#resched').click(function(){
    $('#resched').css('display','none');
    $('#delete').css('display','none');
    $('.updateContainer').css('display','block');
  });
});
