$('document').ready(function(){
var html = "";
var names = [];
var address = [];
$('#searchForm').on('submit' , function(event){
  event.preventDefault();
  html = "";
    $.ajax({
      data : {
        search : $('#searchPatients').val()
      },
      url : '/_search',
      type : 'POST',
      success : function(json){
        for (var i = 0; i < json.names.length; i++) {
          html += "<div class='searchItemsPane'> <h3 class='headerNames'>" + json.names[i] + "</h3>" + json.addresses[i] + "</div><br>";
        }
        $('#searchPane').html(html);
        $('.headerNames').click(function(){
          var name = $(this).text();
          $.ajax({
            data : {
                name : name
            },
            url : '/renzo',
            type: 'POST',
            success: function(data) {
              window.location.href = '/renzo'
            }
          });
        });
      }
    });

});

});
