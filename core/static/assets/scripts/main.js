
var shortener = {

    el: {
        input: $('input#url'),
        btn  : $('button#short')
    },

    init: function() {
       shortener.el.btn.on('click', shortener.short);
       shortener.el.input.on('keyup', function() {
            shortener.el.input.removeClass('field-error')
       });
    },

    short: function (e) {

        e.preventDefault();

        var url = shortener.el.input.val();

        if (url)
        {
            $.get(
                '/shortenit/',
                { 'url' :  url },
                function(data)
                {
                    console.log(data);
                }
            );
        }
        else {
            shortener.el.input.addClass('field-error').focus();
        }
    },
    html: function() {
        return $('');
    }
};

$(function() {
    shortener.init();
});
