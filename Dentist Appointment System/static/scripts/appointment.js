$('document').ready(function(){
  var name = $('.todaySched').text();
  var input = $("<input>")
               .attr("type", "hidden")
               .attr("name", "name").val(name);
$('#appointment').append($(input));
});
