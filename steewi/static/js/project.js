$('#voteForm').on('submit', (function(event){
    event.preventDefault();
    like(this);
 }));

function like(form) {
    url = $(form).attr('action');
    formData = $(form).serializeArray();
    $.ajax({
        url: url,
        type: 'POST',
        data: formData,

        success: function(jsonResp) {
            if (jsonResp['result'] == 'ok') {
                likeScore = $('#likeScore')
                current_score = parseInt(likeScore.html(), 10);
                likeScore.html("<strong>" + (current_score+1) + "</strong> (you liked)");
                $(form).hide();
                showMessage('success', 'Thank You!')}
            else{showMessage('danger', 'Sorry, something went wrong')}
        },
        error: function(xhr,errmsg,err) {
            showMessage('danger', ("Your vote hasn't been submitted due to " + xhr.status +" "+ xhr.statusText))
        }
    });
    }

function showMessage(level, msg){
    $('#content-container').prepend(('<div class="alert alert-'+level+' alert-dismissible"> <button type="button" class="close" data-dismiss="alert" aria-label="Close"> <span aria-hidden="true">&times;</span> </button>' + msg +'</div>'));
    $(".alert").delay(3000).fadeOut(500)
}

$(document).ready(function(){
    $(".alert").delay(3000).fadeOut(500)
})
/*
Formatting hack to get around crispy-forms unfortunate hardcoding
in helpers.FormHelper:

    if template_pack == 'bootstrap4':
        grid_colum_matcher = re.compile('\w*col-(xs|sm|md|lg|xl)-\d+\w*')
        using_grid_layout = (grid_colum_matcher.match(self.label_class) or
                             grid_colum_matcher.match(self.field_class))
        if using_grid_layout:
            items['using_grid_layout'] = True

Issues with the above approach:

1. Fragile: Assumes Bootstrap 4's API doesn't change (it does)
2. Unforgiving: Doesn't allow for any variation in template design
3. Really Unforgiving: No way to override this behavior
4. Undocumented: No mention in the documentation, or it's too hard for me to find
*/
$('.form-group').removeClass('row');
