
var fn = function(){
  var $btn = $("#btn");
  var $inputUsername = $("#username");
  var $password = $("#password");

  $btn.click(function(){
    $.ajax({
      "type": "POST",
      "url": "/api/login",
      "contentType": 'application/json;',
      "data": JSON.stringify({
        "name":$inputUsername.val(),
        "password":$password.val()
      }),
      "success": function (data) {

          if (data.code == 200){
            window.location.href = "/static/views/index.html"
            $.cookie("id",data.data[1])
            $.cookie("name",$inputUsername.val())
            $.cookie("type",data.data[2])
          }else{
            alert("账户不存在或密码错误")
          }
      }
    })
  })

  $("#register").click(function (){
    window.location.href = "regist.html"
  })
};
fn();