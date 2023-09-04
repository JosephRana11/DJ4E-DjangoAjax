console.log('Msg js Linked')

function UpdateMsg(){
  $.ajax({
    type : "GET",
    url: "/get-msg/",
    success: function(response){
      console.log(response)
      for (var key in response.obj){
        document.getElementById('root').innerHTML += `<li>${response.obj[key].sender_id} : ${response.obj[key].text}</li>`
      }
    },
    error: function(){
      alert('Error in fetching data')
    }
  })
}
UpdateMsg()
