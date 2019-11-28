
/* Highlight */
$( document ).ready(function() {
    hljs.initHighlightingOnLoad();
    $('table').addClass('table table-striped table-hover');
});


$('body').scrollspy({
    target: '.bs-sidebar',
});


/* Prevent disabled links from causing a page reload */
$("li.disabled a").click(function() {
    event.preventDefault();
});

// 给markdown图片添加链接
$(document).ready(function() {
    var n = 1;
    $("p img").each(function() {
        // 让图片不以图集存在
        // n++;
        // var strA = "<a href='" + this.src + "' data-lightbox='xxoo-" + n + "' data-title='" + this.alt + "'></a>";
        var strA = "<a href='" + this.src + "' data-lightbox='xxoo' data-title='" + this.alt + "'></a>";
        $(this).wrapAll(strA);
    });
});
