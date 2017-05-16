$('document').ready(function(){
  var date = new Date();
  var year = date.getFullYear();
  var month = date.getMonth();
  var day = date.getDate();
  var dateView = document.getElementById('infoTop');
  var monthNames = ["January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"
  ];
  month = monthNames[month];
  dateView.innerHTML = "Date today: "+ month + " " + day + ", " +year;
  var html = ""
  $('#searchButton').clicked(function(){
    var namesArray = {{names}}
    for (var i = 0; i < namesArray.length; i++) {
      html += "<div class='searchPane'>"+namesArray[i]+"</div>"
      $('.searchPane').html(html);
  });
});
