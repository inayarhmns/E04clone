$(document).ready(function(){
    $('#button1').click(function(){
        $.ajax({
            url: temp,
            type: "POST",
            data: {
                'csrfmiddlewaretoken': csrf,
                'username': $('#id_username').val(),
                'first_name': $('#id_first_name').val(),
                'last_name': $('#id_last_name').val(),
                'email':$('#id_email').val(),
                'password1':$('#id_password1').val(),
                'password2':$('#id_password2').val(),
                'jenis_kelamin':$('#id_jenis_kelamin').val(),
                'kontak':$('#id_kontak').val(),
                'alamat':$('#id_alamat').val()
            },
            success: function(data){
                if (data === "Account has successfully created !"){
                    swal({
                        title: 'Success',
                        text: data,
                        icon: 'success',
                        button: 'ok'
                    }).then(function(isConfirm){
                        if (isConfirm){
                            window.location.href = redirectUrl;
                        }
                    });   
                }
                else{
                    swal({
                        title: 'Invalid Input',
                        text: data,
                        icon: 'error',
                        button: 'ok'
                    });
                }
            }
        });
    });
});