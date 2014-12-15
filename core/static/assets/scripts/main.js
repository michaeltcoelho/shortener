
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
            $.get('/shorten/', {
                    'url' :  url
                  }, function(data) {

                  shortener.el.input.val("");

                  if (data.error) {
                    toastr.error(data.error.url, 'Algo deu errado! :(');
                  }
                  else {
                    shortener.el.content.html(shortener.html(data));

                    if(data.created == true)
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
                '<a target="_blank" href="' + d.shortened_url + '">' + d.shortened_url + '</a>' +
            '</div>' +
        '</div>');
    },

    row: function (link) {
        return $(
        '<tr>' +
            '<td data-url="' + link.url + '" class="text-left"><a href="' + link.url + '" class="link" target="_blank">' + link.url + '</a></td>' +
            '<td class="text-left"><a href="' + link.shortened_url + '" class="link" target="_blank">' + link.shortened_url + '</a></td>' +
            '<td class="text-align">' + link.submitted + '</td>' +
            '<td class="text-center">' + link.visits + '</td>' +
        '</tr>');
    }
};

$(function() {
    shortener.init();
});
