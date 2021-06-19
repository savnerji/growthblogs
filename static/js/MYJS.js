

                                $(document).ready(function () {


                                    let status = false;

                                    $('#login').click(function () {

                                        $('#panel').text("Log In");
                                        $('#frm1').hide();
                                        $('#frm2').show();
                                        status = true;

                                    })

                                    $('#signup').click(function () {

                                        $('#panel').text("sIGN uP");
                                        $('#frm2').hide();
                                        $('#frm1').show();
                                        status = true;

                                    })

                                })


       