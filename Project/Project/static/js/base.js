$(document).ready(function() {
    $("#messages").delay(2000).hide("slow");




    /************start of login.html*********************/
    $("#id_username").addClass("form-control").attr("placeholder","用戶名");
    $("#id_password").addClass("form-control").attr("placeholder","密碼");
    /************end of login.html*********************/


    /************start of signup.html*********************/
    $("#id_name").addClass("form-control").attr("placeholder","姓名");
    $("#id_gender").addClass("form-control");
    $("#id_email").addClass("form-control").attr("placeholder","E-mail");
    $("#id_id_card_num").addClass("form-control").attr("placeholder","身份證字號");
    $("#id_address").addClass("form-control").attr("placeholder","地址");
    $("#id_mobile").addClass("form-control").attr("placeholder","手機號碼");
    $("#id_home_tel").addClass("form-control").attr("placeholder","家庭電話");
    $("#id_facebook").addClass("form-control").attr("placeholder","Facebook");
    $("#id_line").addClass("form-control").attr("placeholder","Line ID");
    $("#id_profile").addClass("form-control").attr("placeholder","填寫個人自述");
    $("#id_photo").addClass("form-control");
    $("#id_password1").addClass("form-control").attr("placeholder","填寫密碼");
    $("#id_password2").addClass("form-control").attr("placeholder","確認密碼");
    /************end of signup.html*********************/


    /************start of post_a_pet.html*********************/
    $(".post-pet-form").find('select').addClass("form-control");
    $("#id_pet_name").addClass("form-control").attr("placeholder","請填寫寵物名字");
    $("#id_breed").addClass("form-control").attr("placeholder","請填寫品種");
    $("#id_content").addClass("form-control").attr("placeholder","請填寫寵物的介紹");
    /************end of post_a_pet.html*********************/
});