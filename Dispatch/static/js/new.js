$(document).ready(function(){

  // LIKE  //  DISLIKE //  SYSTEM

  

  // LIKE  //  DISLIKE //  SYSTEM


  // Jquery Search operation
  // $('.mh-form').on('submit', function(e){
  //   e.preventDefault();
  //   console.log($('this'))
  // });
  const postbtn = $('#createpost').hide();
  const textarea = $('#textarea');
  // console.log(textarea)
  $(textarea).keyup(function(){
    const space = $(this).val().split(' ').length - 1;
    const chars = $(this).val().length

    var ln = chars - space
    // var spaces =
    if (ln > 40){
      postbtn.show();
    }else{
      postbtn.hide();
    }
  });


  $('.delete').on('click', function(e){

    var id = this.id;
    var href = this.href;
    e.preventDefault();

    $.ajax({
      url:href,
      data: {},
    });

    $("#post"+id).fadeOut(1000)
  });

  var not = $('.jquerysearch').val()
  var not_form = $('#not')
  var cform = $.trim(not_form)
  // var not = not_form.find($('.jquerysearch')).val()
  $('.jquerysearch').keyup(function(){

  var dInput = $(this).val()
  // console.log(dInput)
  var cln = $('.post_body').text();
  if (dInput !== ''){
    $('.jqueryposts').each(function(e,v){
      var ye = $(v).find('.post_body').text()
      var yes = $.trim(ye)

      var real = ($("ye:contains('" + dInput + "')"));
      // console.log(real)
      // $(yes).each(function(n,m){
      //   if (m.charAt(0) == '#'){
      //     console.log('yes#')
      //   }
        // console.log(m)
      });

    // $(".jqueryposts").hide();

    // console.log(real)
    // $(real).each(function(e,v){
    //
    //   var cld = $.trim($(this).text());
    //   var prts = cld.split(" ");
    //   var real_p = $(this)
    //   $.each(prts, function(q,pq){
    //     if (pq === dInput){
    //       console.log(pq)
    //
    //         // real_p.html(real_p.html().replaceAll(p,
    //         // `<span style='background-color:#f9f591'>${p}</span>`
    //       ));
    //     }
    //   });
    //
    // });
  }


  // console.log(ll)
  // $('.post_body').each(function(e, v){
  //   var post_text = $(v).text()
  //   var cln = $.trim(post_text)
  //   var spl = cln.split(" ");
  //   $(spl).each(function(e, v){
  //       if (dInput === v){
  //         // console.log(v)
  //       }
  //       if ($('v:contains("'+dInput+'")')){
  //         console.log(dInput)
  //       }
  //     });
  //   });
});


});
