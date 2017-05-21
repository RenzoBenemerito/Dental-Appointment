$(document).ready(function(){
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
      function upperCaseF(a){
        setTimeout(function(){
            a.value = a.value.toUpperCase();
        }, 1);
    }
    $('#messageAlert').click(function(){
      $.ajax({
        url: '/messageAlert',
        type: 'GET',
        success: function(){
          alert('All Patients have been alerted');
        }
      });
    });
});
