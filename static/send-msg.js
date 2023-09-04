$(document).ready(function(){
  $("#msgForm").submit(function(event){
    event.preventDefault();
    var formData = $(this).serialize();
    $.ajax({
      type: "POST",
      url: "/save/",
      data: formData,
      success: function(responseData) { 
        console.log('Success:', responseData);
        document.getElementById('msg-box').value = ''
      },
      error: function(xhr, status, error) {
        console.error('Error:', error);
        alert('Error in Sending Msg: Server might be down')
      }
    });
  });
});

function ResetBox(){
 document.getElementById('msg-box').value = '';
}
  