$(document).ready(function () {
    $('.form').on('submit',function(e){
        e.preventDefault();

        var data = new FormData($('.form')[0]);
        $.ajax({
            xhr: function(){
                var xhr = new window.XMLHttpRequest();
                xhr.upload.addEventListener('progress',(e)=>{
                    console.log((e.loaded / e.total)*100);
                });
                return xhr;
            },
            type: "POST",
            url: "/submit",
            data: data,
            processData:false,
            contentType:false,
            success: function (response) {
                console.log(response);
            }
        });
    });
});