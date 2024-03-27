console.log("register log");
var GOTP =""

$("#btnOTP").on('click',function() {
    var email = $("#email").val();
    var curl = window.location.url;
    if (email == "" || email == undefined)
    {
        $("#email").focus();
        return false
    }

    data = {"email":email}
    GOTP=""
    console.log("Data==>",data)
    $.ajax({
        url:"http://127.0.0.1:8000/otp/",
        type:"POST",
        data: data,
        dataType:"json",
        beforesend: function()
        {

        },

        success: function(response)
        {
            console.log("success :",response);
            GOTP = response.otp;
            
        },

        error: function(error)
        {
            console.log("error:",error);
        }
        
    });
});


function submitRegister()
{
    var fullName = $("#fullName").val();
    var email = $("#email").val();
    var contact = $("#contact").val();
    var age = $("#age").val();
    var address = $("#address").val();

    var academicLevel = $("#academicLevel").val();
    var university = $("#university").val();
    var fieldStudy = $("#fieldStudy").val();
    var studyDestination = $("#studyDestination").val();
    var enrollment = $("#enrollment").val();
    var languageProficiency = $("#languageProficiency").val();

    var userOTP = $("#UOTP").val();
    
    if(fullName =="" || fullName==undefined)
    {
        $("#fullName").focus();
        return false;
    }
    if(email =="" || email==undefined)
    {
        $("#email").focus();
        return false;
    }
    if(contact =="" || contact==undefined)
    {
        $("#contact").focus();
        return false;
    }
    if(age =="" || age==undefined)
    {
        $("#age").focus();
        return false;
    }

    if(address =="" || address==undefined)
    {
        $("#address").focus();
        return false;
    }
    if(academicLevel =="" || academicLevel==undefined)
    {
        $("#academicLevel").focus();
        return false;
    }
    if(university =="" || university==undefined)
    {
        $("#university").focus();
        return false;
    }
    if(fieldStudy =="" || fieldStudy==undefined)
    {
        $("#fieldStudy").focus();
        return false;
    }
    if(studyDestination =="" || studyDestination==undefined)
    {
        $("#studyDestination").focus();
        return false;
    }
    if(enrollment =="" || enrollment==undefined)
    {
        $("#enrollment").focus();
        return false;
    }
    if(languageProficiency =="" || languageProficiency==undefined)
    {
        $("#languageProficiency").focus();
        return false;
    }

    console.log("USer otp:",userOTP, "GLOBAL OTP:",GOTP);
    if(userOTP =="" || userOTP==undefined || userOTP != GOTP)
    {
        $("#UOTP").focus();
        $("#errorOTP").removeClass("d-none");
        return false;
    }
    else
    {
        $("#errorOTP").addClass("d-none");
    }

    $("#registerForm").submit();

}