
var shortener = {

    el: {
      input  : $('input#url'),
      btn    : $('button#short'),
      content: $('#shortened'),
      table  : $('#link-table tbody')
    },

    init: function () {
        shortener.el.btn.on('click', shortener.shorten);
        shortener.el.input.on('keyup', function() {
            shortener.el.input.removeClass('field-error');
        });
    },

    shorten: function (e)
    {
        e.preventDefault();

        var url = shortener.el.input.val();

        if (url)
        {
            $.get('/shorten/',{ 'url' :  url }, function(data) {
                    if (data.error) {
                        toastr.error(data.error.url, 'Informação incorreta...');
                    }else{
                        shortener.el.content.html(shortener.html(data));
                        shortener.el.table.append(shortener.row(data));
                    }
                }
            );
        }
        else {
            shortener.el.input.addClass('field-error').focus();
        }
    },

    html: function(d) {
        return $(
        '<div id="url-shortened">' +
            '<div class="url">' +
                '<span>Copie sua url encurtada: </span>' +
                '<a href="' + d.shortened_url + '">' + d.shortened_url + '</a>' +
            '</div>' +
        '</div>');
    },

    row: function (link) {
        return $(
        '<tr>' +
            '<td class="text-left"><a href="' + link.url + '" target="_blank" class="link">' + link.url + '</a></td>' +
            '<td class="text-align">' + link.submitted + '</td>' +
            '<td class="text-left"><a href="' + link.shortened_url + '" class="link">' + link.shortened_url + '</a></td>' +
            '<td class="text-center">' + link.visits + '</td>' +
        '</tr>');
    }
};

$(function() {
    shortener.init();
});
