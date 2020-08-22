//Boostrap toasts
$('.toast').toast('show');

//Delete confirmation poopup for admin removing products
const deleteButton = $('#delete-button');
const deletePopup = $('.overlay-delete');
const popupText = $('#delete-popup');  

deleteButton.click(function(){
    deletePopup.show();
    deletePopup.addClass('overlay-show');
    popupText.show();
    return false;
});

deletePopup.click(function(){
    deletePopup.hide();
    deletePopup.removeClass('overlay-show');
    popupText.hide();
});