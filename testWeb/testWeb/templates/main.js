$(document).ready(function(){
  $("#apireq").click(function(){
  $('#email').text( "hola");


$.ajax({
  method: 'GET',
  url: 'http://localhost:8000/API/',
  dataType: 'json',
  success: function (data) {
    for (var i=0;i<data.length;i++){
      $("#jsonresp").append("<div id='iter"+i+"' class='center'>");
      $("#iter"+i).append("<p align='center'>Nombre: "+data[i].nombre+ "</p>");
      $("#iter"+i).append("<p>Direccion: "+data[i].direccion+ "</p>");
      $("#iter"+i).append("<p>Superficie: "+data[i].superficie+ "</p>");
      $("#iter"+i).append("<p>Email: "+data[i].email+ "</p>");
      $("#jsonresp").append("<hr>");

    }
  }
});

  });
});