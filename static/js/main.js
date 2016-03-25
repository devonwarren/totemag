
$(document).ready(function() {
   
    if ($("#side-ad").length) {
        var $sdiv = $("#side-ad");
        var top = $("#side-ad").position().top;
        var height = $('#side-ad img').height();

        if ($(window).width() < 600) {
            $sdiv.hide();
        } else {
            $(window).scroll(function() {
                var footer = $("#footer").position().top;
                var scroll = $(window).scrollTop();
                if (scroll > top && scroll < (footer - height - 60)) {
                    $sdiv.css('margin-top', scroll - top + "px");
                }
            });
        }
    }  

    $( "#subscription" ).remodal();

     $( "#subscribe" ).click(function() {
        $( "#subscription" ).remodal();
     });

     $("#navOpen").click(function() {
       $("body").toggleClass("sidebarOpen");
     });

     $("#shadow").click(function() {
       $("body").removeClass("sidebarOpen");
     });
    
     $('#goto_bazaar').on('change', function() {
        if (this.value != '') {
            location.href = "#shop-" + this.value;
        }
     });


});


function toggleSub(t) {
    $(t).parent().toggleClass("open");
}
