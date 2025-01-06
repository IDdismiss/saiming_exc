// 实现闪现消息,定时消失
var message = document.getElementById("message");
var timer = window.setTimeout(function(){
    message.remove();
}, 3000)
