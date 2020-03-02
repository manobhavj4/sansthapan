$(document).ready(function(){
// Contact Form Handler
var contactForm = $(".contact-form")
var contactFormMethod = contactForm.attr("method")
var contactFormEndpoint = contactForm.attr("action") // /abc/

function displaySubmitting(submitBtn,defaultText, doSubmit){
if(doSubmit){
  submitBtn.addClass("disabled")
  submitBtn.html("<i class='fa fa-spin fa-spinner'></i> Sending...")
} else{
  submitBtn.removeClass("disabled")
  submitBtn.html(defaultText)
}
}

contactForm.submit(function(event){ 
event.preventDefault()

var contactFormSubmitBtn = contactForm.find("[type='submit']")
var contactFormSubmitBtntxt = contactFormSubmitBtn.text()

var contactFormData = contactForm.serialize()
var thisForm = $(this)
displaySubmitting(contactFormSubmitBtn,"",true)
$.ajax({
  method: contactFormMethod,
  url: contactFormEndpoint,
  data: contactFormData,
  success: function(data){
    contactForm[0].reset()
    
    setTimeout(function(){
      $.alert({title: "Success!!!", content: data.message, theme: "modern",}) 
    }, 1500)

    setTimeout(function(){
      displaySubmitting(contactFormSubmitBtn,contactFormSubmitBtntxt,false)
    }, 1600)
  },
  error: function(error){
    console.log(error.responseJSON)

    var jsonData = error.responseJSON
    var msg = ""

    $.each(jsonData, function(key, value){
      msg += key + ": " + value[0].message + "<br/>"
    })

    setTimeout(function(){
      $.alert({title: "Oops!", content: msg, theme: "modern",})  
    }, 500)

    setTimeout(function(){
      displaySubmitting(contactFormSubmitBtn,contactFormSubmitBtntxt,false)
    }, 600)

  }
})
})

})
