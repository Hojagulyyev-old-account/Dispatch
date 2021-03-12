$(document).ready(function(){
  var x = $("#username").on("keyup", function(){
    const i = x.val();
    var z = $('.secret').val();
    if (i === z){
      $("#modi").show();
    }else{
      $("#modi").hide();
    }
  });

  function ChangePlaceholder(e) {
    if (e === 2){
      $("#pswd").attr("placeholder", "Junior Password")
    }else if (e === 1){
      $("#pswd").attr("placeholder", "Confirm Password")
    }else{
      $("#pswd").attr("placeholder", "Moderator Password")
    }
  }

  $(".junior").each(function(arg1, arg2){
      // console.log(arg1)
      // console.log(arg2)
      $(this).on('click', function(){
      if ($(this).val() === 'junior'){
        ChangePlaceholder(2);
      }else if($(this).val() === 'user'){
        ChangePlaceholder(1);
      }else{
        ChangePlaceholder(3);
      }
    });
  });
});
