var shortener={el:{input:$("input#url"),btn:$("button#short"),content:$("#shortened"),table:$("#link-table tbody")},init:function(){shortener.el.btn.on("click",shortener.shorten),shortener.el.input.on("keyup",function(){shortener.el.input.removeClass("field-error")})},shorten:function(t){t.preventDefault();var e=shortener.el.input.val();e?$.get("/shorten/",{url:e},function(t){t.error?toastr.error(t.error.url,"Informação incorreta..."):(shortener.el.content.html(shortener.html(t)),shortener.el.table.append(shortener.row(t)))}):shortener.el.input.addClass("field-error").focus()},html:function(t){return $('<div id="url-shortened"><div class="url"><span>Copie sua url encurtada: </span><a href="'+t.shortened_url+'">'+t.shortened_url+"</a></div></div>")},row:function(t){return $('<tr><td class="text-left"><a href="'+t.url+'" target="_blank" class="link">'+t.url+'</a></td><td class="text-align">'+t.submitted+'</td><td class="text-left"><a href="'+t.shortened_url+'" class="link">'+t.shortened_url+'</a></td><td class="text-center">'+t.visits+"</td></tr>")}};$(function(){shortener.init()});