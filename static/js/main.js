
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

});


function toggleSub(t) {
    $(t).parent().toggleClass("open");
}

function addArticles(data) {
    $('.recent-articles').append(data);
}

function moreArticles() {
    var page = parseInt($('#load').attr('data-page'));
    $('#load').attr('data-page', page + 1);
    var category = $('#load').attr('data-category');
    if (category) {
        var articles = $.get("/api/article_list/" + category + '/' + page, function(data) { addArticles(data); }).fail(function() {
                $('#load').hide();
            });
    } else {
        var articles = $.get("/api/article_list/" + page, function(data) { addArticles(data); }).fail(function() {
                $('#load').hide();
            });
    }
}
