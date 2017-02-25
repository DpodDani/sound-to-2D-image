$(document).ready( function() {

  var hilbertCurve = [00, 01, 11, 10, 20, 30, 31, 21, 22, 32, 33, 23, 13, 12, 02, 03];

  var playAnimation = false;

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

  /* PRODUCTION FUNCTIONS */

  var drawHilbertCurve = function (index) {
    console.log("Outside: " + index);
    if (playAnimation) {
      var tCoord = (index < 16) ? hilbertCurve[index].toString() : "03";
      index++;
      var coord = (tCoord.length == 1) ? "0" + tCoord : tCoord;
      //console.log("#" + coord);
      $( "#" + coord ).css("background", "red");
      $( "#" + coord ).html(index);

      if (index <= 16){
        // console.log("Indisde: " + index);
        setTimeout (function() { drawHilbertCurve(index)}, 1000);
      } else {
        setTimeout (function() { drawHilbertCurve(0)}, 1000);
        $( ".musicBox" ).css("background-color", "grey");
        $( ".musicBox" ).html("");
      }
    }
  }

  $( "#viewSwitch" ).click(function() {
    console.log($("#myImage").css("display"));
    if ($("#myImage").css("display") != "none"){
      $("#myImage").css("display", "none");
      $('#myTable').css("display", "table");
      playAnimation = true;
      drawHilbertCurve(0);
    } else {
      $("#myImage").css("display", "inline");
      $('#myTable').css("display", "none");
      playAnimation = false;
    }
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
