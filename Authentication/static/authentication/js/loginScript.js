$(document).ready(function(){
    $('#submit_button').click(function(){
        if($('#id_email').val().length !== 0 && $('#id_password').val().length !== 0){
            $.ajax({
                url: temp,
                type: 'POST',
                data: {
                    'csrfmiddlewaretoken': csrf,
                    'email': $('#id_email').val(),
                    'password': $('#id_password').val()
                },
                success: function(data){
                    if (data !== 'User Not Registered'){
                        get_data();
                    }
                    else{
                        swal({
                            title: 'Invalid Input',
                            text: data,
                            icon: 'warning',
                            button: 'ok'
                        });
                    }
                }
            });
        }
        else{
            swal({
                title: 'Invalid Input',
                text: 'The Fields Cannot Be Empty!',
                icon: 'error',
                button: 'ok'
            });
        }
    });
});

function get_data(){
    $.ajax({
        url: jsonUrl,
        type: "GET",
        dataType: "json",
        success: function(data){
            if (data.gender === "LK"){
                $('#card_image').attr('src', manUrl);
            }
            else{
                $('#card_image').attr('src', womanUrl);
            }
            $('#card_title').html('Welcome Back');
            $('#form-login').remove();
            $('#card_body').append(
                "<div class = 'mb-3'>"+
                    "<h3>"+ data.first_name + " " + data.last_name +"</h3>" +
                "</div>"
            );
            setTimeout(function(){
                window.location.href = redirectUrl;
            }, 3000);
        }
    });
}