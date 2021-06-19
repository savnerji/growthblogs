

function password_check() {
    $('#msg2').hide();
    console.log('working ',)
    var confirm = $('#password2').val();
    var original = $('#password').val();
    if (confirm.length > original.length) {

        $('#msg2').text("Password did not matched !");
        $('#msg2').show();
        return true;
    }
    for (let i = 0; i < confirm.length; i++) {
        if (confirm[i] != original[i]) {
            $('#msg2').text("Password did not matched !");
            $('#msg2').show();
            return true;
        }
    }

}



$("#loginbtn").on("click", function (event) {
    event.preventDefault();
    var email = $('#login_email').val();
    var password = $('#login_password').val();

    $.ajax({
        type: "POST",
        url: '/login',
        data: {
            'email': email,
            'password': password,
            csrfmiddlewaretoken: $('meta[name="_token"]').attr('content')
        },
        beforeSend: function () {
            $("#loading").show();
        },
        success: function (result) {
            if (result == 0) {
                window.location.reload();
            }
            else {
                $('#incorrect').text("Invalid login credentials!");
                $('#incorrect').show();

                setTimeout(function () {
                    $('#incorrect').hide();
                }, 3000);

            }
        },
        complete: function (data) {
            $("#loading").hide();
        }
    });

});



$("#submitbtn").on("click", function (event) {
    event.preventDefault();

    var username = $("#username").val();
    var email = $("#inputEmail").val();
    var password = $("#password").val();

    $.ajax({
        type: "POST",
        url: '/signup',
        data: {
            'username': username,
            'email': email,
            'password': password,
            csrfmiddlewaretoken: $('meta[name="_token"]').attr('content')
        },
        beforeSend: function () {
            $("#loading").show();
        },
        success: function (result) {
            if (result == 0) {
                $('#modalbuttons').hide();
                $('#frm1').hide();
                $('#frm2').show();
                $('#panel').innerText = 'LOG IN';
            }
            else if (result == 1) {

                $('#msg').text("Invalid e-mail address!");
                $('#msg').show();
                setTimeout(function () {
                    $('#msg').hide();
                }, 3000);
            }
            else if (result == 2) {
                $('#msg').text("Email already taken!");
                $('#msg').show();

                setTimeout(function () {
                    $('#msg').hide();
                }, 3000);
            }
            else {
                alert(result);
            }
        },
        complete: function (data) {
            $("#loading").hide();
        }
    });

});
