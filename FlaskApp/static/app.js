$(document).ready( function() {

  $( "#testBtn" ).click(function() {
    console.log("Test button clicked");
    $.ajax({
      type : "POST",
      url : "/test",
      data : { param : "Did you get it?"}
    }).done(function(result){
      console.log(result);
    });
  });

  $( ".colors" ).click(function(){
    var id = $(this).attr('id');
    console.log("Click on " + id + " button.");
    $.ajax({
      type : "POST",
      url : "/colourSound",
      data : { buttonColour : id}
    }).done(function(result){
      console.log("Response: " + result);
      console.log("Played sound for: " + id + " button.");
    });
  });

  var input = $("#fileName").parents('.input-group').find(':text');
  input.val(""); // clears the file name upon reload

  console.log("Ready and waiting!");

  $(document).on('change', ':file', function() {
    var input = $(this),
    numFiles = input.get(0).files ? input.get(0).files.length : 1,
    label = input.val();//.replace(/\\/g, '/').replace(/.*\//, '');
    console.log(numFiles);
    console.log(label);
    console.log(input);
    input.trigger('fileselect', [numFiles, label]);
  });

  $(':file').on('fileselect', function(event, numFiles, label) {

    console.log("FIRED!");

    var input = $(this).parents('.input-group').find(':text'),
    log = numFiles > 1 ? numFiles + ' files selected' : label;

    if( input.length ) {
      input.val(log);
    } else {
      if( log ) alert(log);
    }

  });

});

function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
      $('#myImage')
      .attr('src', e.target.result)
    };

    reader.readAsDataURL(input.files[0]);
  }
}
