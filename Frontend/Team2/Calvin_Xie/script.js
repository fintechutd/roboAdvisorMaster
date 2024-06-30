function displayInput() {
    var userInput = document.getElementById('user_input').value;
    var displayArea = document.getElementById('display_area');
    displayArea.innerHTML = "<p>Your input: " + userInput + "</p>";
  }
  
var submitAnswer = function(){
  var radios = document.getElementById("choice");
  var val = "";
  for(var i = 0, length = radios.length; i<length;++i)
  {
    if(radios[i].checked)
    {
      val = radios[i].value;
      document.getElementById("display_area").innerHTML = "Correct";
      break;
    }
  }
  if(val == "")
  {
    document.getElementById.innerHTML = "Please choose an answer";
  }
};