$(document).ready(function(){

  var enableSubmit = function(e){
    $(e).removeAttr('disabled');
  }

  $('.like-form').on('submit', function(e){
    e.preventDefault();

    const post_id = $(this).find('.iam').attr('value')
    const url = $(this).attr('action');
    // console.log(url)

    const cssLike = $(`#likes${post_id}`)

    let res;
    const likes = $(`.like-count${post_id}`).text()
    const intlike = parseInt(likes)

    $.ajax({
      type:'POST',
      url:url,
      data:{
        'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
        'post_id':post_id,
      },
      success:function(response){
        var tgg = response['like']
        console.log(response['x'])
        // console.log(tgg)
        if (tgg === 'liked'){
          res = intlike + 1
          $(cssLike).css('color','#f55442')
          $(`.disobtn${post_id}`).attr('disabled', true);
          setTimeout(function() { enableSubmit($(`.disobtn${post_id}`))}, 500)
        }else{
          res = intlike - 1
          $(cssLike).css('color','#adadfd')
        }
        $(`#span${post_id}`).text(res)
        // $(`#likes${}`)
      },
      error:function(response){
        console.log('error')
      }
    });
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

          function endsWithAny(suffixes, string) {
              return suffixes.some(function (suffix) {
                  return string.endsWith(suffix);
              });
          }
          var wate;

          // v.css('color', 'red')
          // var link = document.createElement('a');
          // $(link).attr('href', '/')
          // link.append(v)
          // console.log(link)
          // console.log(postEl.html());
          var clean_hash = v.substring(1)
          var n = endsWithAny([".", "!", "?", ","], clean_hash);
            if (n === true){
              var clean_hash = clean_hash.slice(0, -1);
              // console.log(clean_hash)
            }
          var lower = clean_hash.toLowerCase();
          postEl.html(postEl.html().replaceAll(v,
              `<a href="/hashtag/${lower}"> ${v} </a>`
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
