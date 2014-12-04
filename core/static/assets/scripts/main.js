
var shortener = {

    el: {
        input: $('input#url'),
        btn  : $('button#short')
    },

    init: function() {
       shortener.el.input.on('keypress', shortener.shortenit);
       shortener.el.btn.on('click', shortener.shortenit);
    },

    shortenit: function (e) {

        e.preventDefault();

        var url = shortener.el.input.val();

        $.get('/shortenit/', { 'url' :  url }, function(data) {
            console.log(data);
        });
    }
};

$(function() {
    shortener.init();
});
