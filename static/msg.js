console.log('Msg js Linked');

function UpdateMsg() {
  $.ajax({
    type: "GET",
    url: "/get-msg/",
    success: function(response) {
      console.log(response);

      // Create a document fragment to build the new content
      var fragment = document.createDocumentFragment();

      for (var key in response.obj) {
        var listItem = document.createElement('li');
        listItem.textContent = `${response.obj[key].sender} : ${response.obj[key].text}`;
        fragment.appendChild(listItem);
      }

      // Clear the existing content and append the new content
      var rootElement = document.getElementById('root');
      rootElement.innerHTML = '';
      rootElement.appendChild(fragment);
    },
    error: function() {
      alert('Error in fetching data');
    }
  });
}

function MainCall() {
  UpdateMsg();
}

setInterval(MainCall, 200);
