  
$(document).ready(function(){


  $('input').keyup(function (e) {
    e.preventDefault();
    
    // Remove previous list
    $('.result-list').empty();

    // In case of long wait time, add loading status to list, if prefix entered
    if ($('input').val().length > 0)
      var $elem = $('<li></li>').html("Loading...");
      $('.result-list').append($elem);

    // Fetch path names from server, append results to list
    $.get('/fetch', {'prefix': $('input').val()}, function (data) {

      $('.result-list').empty();

      if (typeof data === 'object')
        $.each(data, function (idx){
          var $li = $('<li></li>').html(data[idx]);
          $('.result-list').append($li);
        })
    })
  });



})