$(document).ready(function(){

  const button = $('.owez-js-btn');
  button.on('click', function(){
    console.log('Works')
    $(".error-msg").fadeOut(1000);
  });

  var x = $("#username").on("keyup", function(){
    const i = x.val();
    var z = $('.secret').val();
    if (i === z){
      $("#modi").show();
    }else{
      $("#modi").hide();
    }
  });

  $('.post_body').each(function(index){
      var cls = $.trim($(this).text());
      var parts = cls.split(" ");
      var postEl = $(this);
      // const tgs = $(".hashtags")
      // $.each(tgs, function(i, e){
      //   console.log(i)
      //   console.log(e)
      // })
      $.each(parts, function(k, v){
        if (v.charAt(0) == '#'){
          // v.css('color', 'red')
          // var link = document.createElement('a');
          // $(link).attr('href', '/')
          // link.append(v)
          // console.log(link)
          // console.log(postEl.html());
          var clean_hash = v.substring(1)
          var lower = clean_hash.toLowerCase();
          postEl.html(postEl.html().replaceAll(v,
              `<a href="/hashtag/${lower}">${v}</a>`
          ));

        }

      });

  });

  // $('.post_body a').on('click', function(e) {
  //     console.log('clicked');
  //       // e.preventDefault();
  //     $.get($(this).data('href'), function(data) {
  //       arr = JSON.parse(data);
  //       // console.log(arr);
  //
  //       Object.keys(arr).forEach(key => {
  //         console.log( arr[key]['fields']['body']);
  //       });
  //
  //     });
  // });



  var input = $("#inputik").on('click', function(){
    if (input.css('color') === 'rgb(245, 31, 17)'){
      input.css('color', 'black')
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
